NUMPAD = {
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GHI',
    '5': 'JKL',
    '6': 'MNO',
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '1': '1',
    '0': '0',
}


def phone_mnemonic(phone_number):
    len_number = len(phone_number)

    def print_all_words(index, string_so_far):
        # Base Case
        if index == len_number:
            print(string_so_far)
            return

        # General Case
        for char in NUMPAD[phone_number[index]]:
            temp = '{}{}'.format(string_so_far, char)
            print_all_words(index + 1, temp)
        return

    print_all_words(0, '')
