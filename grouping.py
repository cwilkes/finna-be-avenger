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
    for customer_id, order in group_orders_to_customer(input_file).items():
        print customer_id, order
