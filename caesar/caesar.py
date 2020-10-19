import string


def caesar_code(input_string, key):
    def encode(char, key):
        if char in string.ascii_letters:
            byte  = ord(char) + key
            if chr(byte) not in string.ascii_letters:
                byte -= 26
            return(chr(byte))
        return char

    result = ''
    for char in input_string:
        result += encode(char, key)

    return result


if __name__ == "__main__":
    print(caesar_code('Lille kat, lille kat, lille kat på vejen.', 12))
