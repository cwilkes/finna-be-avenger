from collections import namedtuple

Campaign = namedtuple('Campaign', 'campaign_id, network, rate_metric, rate_amount, keyword, min_lat')
Click = namedtuple('Click', 'date, cookie, landing_page')
Chargeback = namedtuple('Chargeback', 'date, transaction_id, amount')
CityGeo = namedtuple('CityGeo', 'city, latitude, longitude')
Product = namedtuple('Product', 'product_area, product_id, amount')
Order = namedtuple('Order', 'date, transaction_id, customer_id, product_id, amount, latitude, longitude')
Impression = namedtuple('Impression', 'date, campaign_id, keyword, cookie')
Register = namedtuple('Register', 'date, cookie, customer_id, latitude, longitude')


def get_campaigns(reader):
    next(reader)
    for e in (_.strip().split() for _ in reader):
        yield Campaign(int(e[0]), e[1], e[2], float(e[3]), e[4], float(e[5]))


def get_clicks(reader):
    for e in (_.strip().split() for _ in reader):
        yield Click(e[0], e[1], e[2], int(e[3]))

