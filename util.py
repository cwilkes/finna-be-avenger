import sys
import models
import math
from grouping import group_orders_to_customer
import datetime


def get_closest_city(cities):
    def f(lat, lng):
        best_distance, best_city = sys.maxint, None
        for city in cities:
            my_distance = math.sqrt(math.pow(city.latitude-lat,2) + math.pow(city.longitude-lng, 2))
            if my_distance < best_distance:
                best_distance, best_city = my_distance, city
        return best_city
    return f


def compare_entries(entries, compare_func):
    for pos, entry1 in enumerate(entries):
        for entry2 in entries[pos+1:]:
            yield entry1, entry2, compare_func(entry1, entry2)


def compare_by_lat_long(e1, e2):
    return math.sqrt(math.pow(e1.latitude-e2.latitude, 2) + math.pow(e1.longitude-e2.longitude, 2))


def customer_cities(cities, orders_file):
    closest_city = get_closest_city(cities)
    for cust_id, orders in group_orders_to_customer(orders_file).items():
        cities = list()
        for order in orders:
            cities.append((order.date, models.LatLong(order.latitude, order.longitude), closest_city(order.latitude, order.longitude)))
        yield cust_id, sorted(cities, key=lambda _: datetime.datetime.strptime(_[0], '%Y-%m-%d'))


def main(args):
    #orders = list()
    #for e1, e2, distance in compare_entries(orders, compare_by_lat_long):
    #    print e1, e2, distance
    #cities = list(models.get_city(open(args[1])))
    #closest_city = get_closest_city(cities)
    #for order in models.get_orders(open(args[2])):
    #    print order, closest_city(order.latitude, order.longitude)
    cities = list(models.get_city(open(sys.argv[1])))
    for cust_id, cities in customer_cities(cities, sys.argv[2]):
        print cust_id, cities


if __name__ == '__main__':
    main(sys.argv)

