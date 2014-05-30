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
    for c, o in cust_table.items():
        print c, len(o)
    for p, c in prod_table.items():
        print p, len(c)
