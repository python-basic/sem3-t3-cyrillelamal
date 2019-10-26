def rot13(initial_string, encode=True, bias=13):
    """Return en/de -coded string according to ecnode parameter"""
    new_string = ''

    for ch in initial_string:
        chr_num = ord(ch)
        chr_num = chr_num + bias if encode else chr_num - bias
        new_string += chr(chr_num)

    return new_string


def main():
    initial_string = input('Строка для шифрования: ')
    encoded_string = rot13(initial_string)
    print(f'Новая строка {encoded_string}')


if __name__ == '__main__':
    main()
