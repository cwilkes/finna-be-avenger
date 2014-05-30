import sys
import models


def compare_entries(entries, compare_func):
    for pos, entry1 in enumerate(entries):
        for entry2 in entries[entry1+1:]:
            yield entry1, entry2, compare_func(entry1, entry2)


if __name__ == '__init__':
    orders = list(models.get_orders(open(sys.argv[1])))
    for e1, e2, distance in compare_entries(orders):
        print e1, e2, distance

