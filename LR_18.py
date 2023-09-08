from LR_17 import *


class OrderDatabase(object):
    def __init__(self):
        self.filename = 'orders.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()


    price = property(lambda self: self.database[self.index].price)
    count = property(lambda self: self.database[self.index].count)
    name_product = property(lambda self: self.database[self.index].name_product)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_order(self, name_product, price, count):
        za = Order(0, '', '', name_product, count, price)
        if za.number in self.database:
            za.number = len(self.database) + 1
        self.database[za.number] = za
        self.save_database()

    def get_order_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_order(self, number):
        del self.database[number]
        self.save_database()

    def change_count(self, number, count):
        ord = self.get_order_by_number(number)
        if not ord:
            raise ValueError('value does not exist')
        ord.count = count
        self.save_database()


class ProviderDatabase(object):
    def __init__(self):
        self.filename = 'orders12.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()


    name = property(lambda self: self.database[self.index].name)
    kind = property(lambda self: self.database[self.index].kind)
    country = property(lambda self: self.database[self.index].country)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_provider(self, name, kind, country):
        pr = Provider(name, kind, country, '', '')
        if pr.number in self.database:
            pr.number = len(self.database) + 1
        self.database[pr.number] = pr
        self.save_database()

    def get_provider_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_provider(self, number):
        del self.database[number]
        self.save_database()

    def change_country(self, number, country):
        pr = self.get_provider_by_number(number)
        if not pr:
            raise ValueError('value does not exist')
        pr.country = country
        self.save_database()


class TradeOrganizationDatabase(object):
    def __init__(self):
        self.filename = 'orders13.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()


    name = property(lambda self: self.database[self.index].name)
    name_director = property(lambda self: self.database[self.index].name_director)
    tax_number = property(lambda self: self.database[self.index].tax_number)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_to(self, name, name_director, tax_number):
        to = TradeOrganization(name, '', name_director, tax_number)
        if to.number in self.database:
            to.number = len(self.database) + 1
        self.database[to.number] = to
        self.save_database()

    def get_to_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_to(self, number):
        del self.database[number]
        self.save_database()

    def change_tax_number(self, number, tax_number):
        to = self.get_to_by_number(number)
        if not to:
            raise ValueError('value does not exist')
        to.tax_number = tax_number
        self.save_database()


class PointOfSaleDatabase(object):
    def __init__(self):
        self.filename = 'orders14.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    name = property(lambda self: self.database[self.index].name)
    kind = property(lambda self: self.database[self.index].kind)
    trade_organization = property(lambda self: self.database[self.index].trade_organization)
    address = property(lambda self: self.database[self.index].address)
    name_lead = property(lambda self: self.database[self.index].name_lead)


    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_pof(self, name, kind, trade_organization, name_lead):
        pof = PointOfSale(name, kind, trade_organization, '', name_lead)
        if pof.number in self.database:
            pof.number = len(self.database) + 1
        self.database[pof.number] = pof
        self.save_database()

    def get_pof_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_pof(self, number):
        del self.database[number]
        self.save_database()

    def change_name(self, number, name):
        pof = self.get_pof_by_number(number)
        if not pof:
            raise ValueError('value does not exist')
        pof.name = name
        self.save_database()


class SellerDatabase(object):
    def __init__(self):
        self.filename = 'orders15.pkl'
        self.database = {}
        self.index = 0
        try:
            self.open_database()
        except:
            self.save_database()

    last_name = property(lambda self: self.database[self.index].last_name)
    first_name = property(lambda self: self.database[self.index].first_name)
    point_of_sale = property(lambda self: self.database[self.index].point_of_sale)
    city = property(lambda self: self.database[self.index].city)

    def __iter__(self):
        for item in self.database:
            yield self.database[item]

    def next(self):
        if self.index == len(self.database):
            raise StopIteration
        self.index = self.index + 1
        return self.database[self.index]

    def prev(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.database[self.index]

    def open_database(self):
        with open(self.filename, 'rb') as f:
            self.database = pickle.load(f)
        f.closed

    def save_database(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.database, f)
        f.closed

    def add_s(self, last_name, first_name, point_of_sale, city):
        s = Seller(last_name, first_name, '',  point_of_sale, '', '', '', '', city)
        if s.number in self.database:
            s.number = len(self.database) + 1
        self.database[s.number] = s
        self.save_database()

    def get_s_by_number(self, number):
        if number not in self.database:
            return None
        return self.database[number]

    def delete_s(self, number):
        del self.database[number]
        self.save_database()

    def change_city(self, number, city):
        s = self.get_s_by_number(number)
        if not s:
            raise ValueError('value does not exist')
        s.city = city
        self.save_database()


if __name__ == '__main__':
    pass
