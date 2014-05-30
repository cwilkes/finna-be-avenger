import models
from collections import defaultdict
import sys


def group_orders_to_customer(order_file, max_lines=sys.maxint):
    ret = defaultdict(list)
    count = 0
    for order in models.get_orders(open(order_file)):
        ret[order.customer_id].append(order)
        count += 1
        if count >= max_lines:
            break
    return ret


if __name__ == '__main__':
    input_file = sys.argv[1]
    if len(sys.argv) >= 3:
        max_lines = int(sys.argv[2])
    else:
        max_lines = sys.maxint
    cust_table = {}
    prod_table = {}
    for customer_id, order_list in group_orders_to_customer(input_file).items():
        for order in order_list:
            cust_table.setdefault(customer_id, set()).add(order.product_id)
            prod_table.setdefault(order.product_id, set()).add(customer_id)

    while True:
        cust_id = raw_input()
        if cust_id == '*':
            break
        print cust_id
        
        cust_id = int(cust_id)
        if not cust_id in cust_table:
            print "Customer ID not found"
            continue
                
        product_ids = cust_table[cust_id]
        #print product_ids

        other_cust = set()
        for p in product_ids:
            other_cust = other_cust.union(prod_table[p])
        #print other_cust

        other_prod = set()
        for c in other_cust:
            other_prod = other_prod.union(cust_table[c])

        suggested = other_prod - product_ids
        print suggested



