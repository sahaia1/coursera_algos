'''
Problem # 29

Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''


def encode(string):
    if not string:
        return string
    count = 1
    encoded_string = []
    i = 1
    while i < len(string):
        while i < len(string) and string[i] == string[i - 1]:
            i += 1
            count += 1
        encoded_string.append('{}{}'.format(count, string[i - 1]))
        count = 1
        i += 1
    return ''.join(encoded_string)


def decode(string):
    if not string:
        return string
    decoded_string = []
    i = 0
    while i < len(string):
        num, char = int(string[i]), string[i + 1]
        for _ in range(num):
            decoded_string.append(char)
        i += 2
    return ''.join(decoded_string)