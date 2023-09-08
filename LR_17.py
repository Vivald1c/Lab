from LR_15_1 import InvalidPriceError
from LR_15_1 import InvalidNameError
from datetime import datetime
from functools import wraps
import time
import pickle


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:.6f} seconds to complete')
        return result
    return wrapper


def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f'{func.__name__} has been called {wrapper.count} times')
        return result
    wrapper.count = 0
    return wrapper


_next = 0

def _next_number():
    global _next
    _next += 1
    return _next


class TradeOrganization:
    """
    Класс TradeOrganization предоставляет описание
    названия торговой организации, адреса, ФИО директора, налогового номера
    """
    def __init__(self, name='', address='', name_director='', tax_number=0):
        self.__name = name
        self.__address = address
        self.__name_director = name_director
        self.__tax_number = tax_number
        self.number = _next_number()

    def __name_trade_organization(self):
        """ Метод name_trade_organization выводит название торговой точки """
        print('Название торговой компании: ' + self.__name)

    def __change_tax_number(self, tax_number=0):
        """ Метод change_tax_number изменяет налоговый номер на указанный """
        self.__tax_number = tax_number

    @staticmethod
    def __serialize(data):
        """ Метод серилизирует полученные данные """
        with open('inf_TO.pkl', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def __deserialize():
        """ Метод десериализирует данные """
        with open('inf_TO.pkl', 'rb') as f:
            data = pickle.load(f)
        return data

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        return 'Deleted'

    @property
    def name(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name

    @name.setter
    def name(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__name = value

    @property
    def address(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__address

    @address.setter
    def address(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__address = value

    @property
    def name_director(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name_director

    @name_director.setter
    def name_director(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__name_director = value

    @property
    def tax_number(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__tax_number

    @tax_number.setter
    def tax_number(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__tax_number = value


class PointOfSale:
    """
    Класс PointOfSale представляет описание названия торговой точки, типа
(универмаги, магазины, киоски, лотки и т.д.), торговой организации, адреса,
ФИО заведующего
    """
    def __init__(self, name, kind, trade_organization, address, name_lead):
        self.__name = name
        self.__kind = kind
        self.__trade_organization = trade_organization
        self.__address = address
        self.__name_lead = name_lead
        self.number = _next_number()

    def __type_point_of_sell(self):
        """ Метод type_point_of_sell выводит тип торговой точки """
        print('Тип торговой точки: ' + self.__kind)

    def __change_name(self, name=''):
        """ Метод change_name изменяет название торговой точки """
        self.__name = name

    @staticmethod
    def __serialize(data):
        """ Метод серилизирует полученные данные """
        with open('inf_TO.pkl', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def __deserialize():
        """ Метод десериализирует данные """
        with open('inf_TO.pkl', 'rb') as f:
            data = pickle.load(f)
        return data

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        return 'Deleted'

    @property
    def name(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name

    @name.setter
    def name(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__name = value

    @property
    def kind(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__kind

    @kind.setter
    def kind(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__kind = value

    @property
    def trade_organization(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__trade_organization

    @trade_organization.setter
    def trade_organization(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__trade_organization = value

    @property
    def address(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__address

    @address.setter
    def address(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__address = value

    @property
    def name_lead(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name_lead

    @name_lead.setter
    def name_lead(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__name_lead = value


class PersonalInfoSeller:
    """
        Класс PersonalInfoSeller представляет описание фамилии, имени, отчества продавца
    """
    def __init__(self, last_name, first_name, patronymic):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic


class Seller:
    """
    Класс Seller представляет описание фамилии, имени, отчества, торговой точки, должности, года рождения, пола, адреса
проживания, города
    """
    def __init__(self, last_name, first_name, patronymic, point_of_sale, position, year_of_birth, gender,
                 address_of_registration, city):
        #self.personal_info = PersonalInfoSeller(last_name, first_name, patronymic)
        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__point_of_sale = point_of_sale
        self.__position = position
        self.__year_of_birth = year_of_birth
        self.__gender = gender
        self.__address_of_registration = address_of_registration
        self.__city = city
        self.number = _next_number()

    '''def __str__(self):
        return 'last_name: {0}, first_name: {1}, patronymic: {2}'.format(self.personal_info.last_name,
                self.personal_info.first_name, self.personal_info.patronymic)'''

    def __name_of_point_of_sale(self):
        """ Метод name_of_point_of_sale выводит название торговой точки """
        print("Название торговой точки: " + self.__point_of_sale)

    def __change_position(self, position=''):
        """ Метод change_position изменяет должность """
        self.__position = position

    @staticmethod
    def __serialize(data):
        """ Метод серилизирует полученные данные """
        with open('inf_TO.pkl', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def __deserialize():
        """ Метод десериализирует данные """
        with open('inf_TO.pkl', 'rb') as f:
            data = pickle.load(f)
        return data

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        return 'Deleted'

    @property
    def last_name(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__last_name = value

    @property
    def first_name(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__first_name = value

    @property
    def patronymic(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__patronymic = value

    @property
    def point_of_sale(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__point_of_sale

    @point_of_sale.setter
    def point_of_sale(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__point_of_sale = value

    @property
    def position(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__position

    @position.setter
    def position(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__position = value

    @property
    def year_of_birth(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__year_of_birth

    @year_of_birth.setter
    def year_of_birth(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__year_of_birth = value

    @property
    def gender(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__gender = value

    @property
    def address_of_registration(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__address_of_registration

    @address_of_registration.setter
    def address_of_registration(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__address_of_registration = value

    @property
    def city(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__city

    @city.setter
    def city(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__city = value


class Provider:
    """
    Класс Provider представляет описание названия поставщика, типа деятельности, страны, города, адреса
    """
    def __init__(self, name='', kind='', country='', city='', address=''):
        self.__name = name
        self.__kind = kind
        self.__country = country
        self.__city = city
        self.__address = address
        self.number = _next_number()

    def __name_type_activity(self):
        """ Метод name_type_activity выводит тип деятельности """
        print('Тип деятельности ' + self.__kind)

    def __change_city(self, city=''):
        """ Метод change_city изменяет город """
        self.__city = city

    def display_info(self): #######################################################################################################################
        print(f"Поставщик: {self.__name}")
        print(f"Тип деятельности: {self.__kind}")
        print(f"Страна: {self.__country}")
        print(f"Город: {self.__city}")
        print(f"Адрес: {self.__address}")
    
    @staticmethod
    def __serialize(data):
        """ Метод серилизирует полученные данные """
        with open('inf_TO.pkl', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def __deserialize():
        """ Метод десериализирует данные """
        with open('inf_TO.pkl', 'rb') as f:
            data = pickle.load(f)
        return data

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        return 'Deleted'

    @property
    def name(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name

    @name.setter
    def name(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__name = value

    @property
    def kind(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__kind

    @kind.setter
    def kind(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__kind = value

    @property
    def country(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__country

    @country.setter
    def country(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__country = value

    @property
    def address(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__address

    @address.setter
    def address(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__address = value

    @property
    def city(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__city

    @city.setter
    def city(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__city = value


class Order:
    """
    Класс Order представляет описание даты заказа, торговой точки, поставщика, названия товара, кол-ва, цены
    """
    def __init__(self, date=datetime.today(), point_of_sale='', provider='', name_product='', count=0, price=0):
        self.__date = date
        self.__point_of_sale = point_of_sale
        self.__provider = provider
        self.__name_product = name_product
        self.__count = count
        self.__price = price
        self.__queue = []
        self.number = _next_number()

    def __change(self, amount):
        """ Метод change прибавляет указанное значение к количеству товара """
        self.__count += amount
        self.__queue.append(Transactions(amount))
        return amount

    @timeit
    @countcall
    def prices(self):
        """ Метод prices рассчитывает стоимость одного товара """
        return self.__count // self.__price

    def __get_transaction(self):
        """ Метод get_transaction возвращает дату и количество товара """
        for i in range(len(self.__queue)):
            item = self.__queue.pop(0)
            print('when {0} : count {1} '.format(self.__date, self.__count))

    def __add__(self, val):
        """ Сложение """
        self.__price += val

    def __sub__(self, val):
        """ Вычитание """
        self.__price -= val

    def __mul__(self, val):
        """ Умножение """
        self.__price *= val

    def __truediv__(self, val):
        """ Деление """
        self.__price /= val

    @staticmethod
    def serialize(data):
        """ Метод серилизирует полученные данные """
        with open('inf_TO.pkl', 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def __deserialize():
        """ Метод десериализирует данные """
        with open('inf_TO.pkl', 'rb') as f:
            data = pickle.load(f)
        return data

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        return 'Deleted'

    @property
    def price(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__price

    @price.setter
    def price(self, value):
        """ свойство для предоставления доступа к атрибуту """
        if value < 0:
            raise InvalidPriceError(value)
        else:
            self.__price = value

    @property
    def name_product(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__name_product

    @name_product.setter
    def name_product(self, val):
        """ свойство для предоставления доступа к атрибуту """
        if val is not (str()):
            raise InvalidNameError(val)
        else:
            self.__name_product = val

    @property
    def date(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__date

    @date.setter
    def date(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__date = value

    @property
    def point_of_sale(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__point_of_sale

    @point_of_sale.setter
    def point_of_sale(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__point_of_sale = value

    @property
    def provider(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__provider

    @provider.setter
    def provider(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__provider = value

    @property
    def count(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__count

    @count.setter
    def count(self, value):
        """ свойство для предоставления доступа к атрибуту """
        self.__count = value


class Transactions:
    """
    Класс Transactions, который описывает дату и количество товара
    """
    def __init__(self, amount):
        self.__when = datetime.today()
        self.__amount = amount

    def __add__(self, val):
        """ Сложение """
        self.__amount += val

    def __sub__(self, val):
        """ Вычитание """
        self.__amount -= val

    def __mul__(self, val):
        """ Умножение """
        self.__amount *= val

    def __truediv__(self, val):
        """ Деление """
        self.__amount /= val

    def __del__(self):
        """ Метод, который вызывается при уничтожении объекта """
        with open('transaction.txt', 'a') as f:
            f.write('when {0} : amount {1} \n'.format(self.__when, self.__amount))

    @property
    def when(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__when

    @property
    def amount(self):
        """ свойство для предоставления доступа к атрибуту """
        return self.__amount


if __name__ == '__main__':
    order = Order(datetime.today(), 'Moscow', 'Tasty Milk', 'Молоко', 100000, 2684)
    order.prices()
    order.prices()
