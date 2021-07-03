# Домашнее задание номер 2 из урока 4 "Основы языка Python"
# Текст задания: 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


from requests import get, utils


def sub_str(str_in, teg_name):
    before = str_in.find('<' + teg_name + '>') + len(teg_name) + 2
    after = str_in.find('</' + teg_name + '>')
    return str_in[before:after]


def currency_rates(*args):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    response.close()
    list_val = content.split("<Valute ID=")
    dict_val = {}
    for i in list_val[1:]:
        dict_val[sub_str(i, 'CharCode')] = f"{sub_str(i, 'Name')},{float(sub_str(i, 'Value').replace(',', '.')):.2f}"
    result = []
    for i in args:
        result.append(dict_val.get(i))
    return result


print(*currency_rates('USD'))
print(*currency_rates('EUR'))
print(*currency_rates('USD', 'EUR'))
print(*currency_rates('YYY'))