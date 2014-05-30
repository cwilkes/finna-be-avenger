import sys
import models
import math


def compare_entries(entries, compare_func):
    for pos, entry1 in enumerate(entries):
        for entry2 in entries[pos+1:]:
            yield entry1, entry2, compare_func(entry1, entry2)


def compare_by_lat_long(e1, e2):
    return math.sqrt(math.pow(e1.latitude-e2.latitude, 2) + math.pow(e1.longitude-e2.longitude, 2))


def main(args):
    orders = list(models.get_orders(open(args[1])))
    for e1, e2, distance in compare_entries(orders, compare_by_lat_long):
        print e1, e2, distance


if __name__ == '__main__':
    main(sys.argv)

