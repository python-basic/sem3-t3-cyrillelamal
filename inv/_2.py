import re


def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, по которой мы ищем: ")

    choice = None
    while choice != '4':

        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')
        print('3 - найти все вхождения подстроки')
        print('4 - для выхода')

        choice = input("Сделайте  выбор (1..4) ")

        if choice == '1':
            print(search_str(input_str, searchable_str))
        elif choice == '2':
            rep_str = input('Строка для замены: ')
            print(search_n_replace_str(input_str, rep_str, searchable_str))
        elif choice == '3':
            print(search_str(input_str, searchable_str, True))


def search_str(what="", where="", persist=False) -> list:
    idxs = []

    for match in re.finditer(what, where):
        idxs.append(match.start())
        if not persist:
            break

    return idxs


def search_n_replace_str(what="",  to_what="", where=""):
    return where.replace(what, to_what)


if __name__ == '__main__':
    main()
