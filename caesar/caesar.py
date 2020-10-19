import string


def caesar_code(input_string, key):
    key = key % 26 
    def encode(char, key):
        if char in string.ascii_letters:
            byte  = ord(char) + key
            # Not a ascii char anymore. Lets switch it down
            if chr(byte) not in string.ascii_letters:
                byte -= 26
            return(chr(byte))
        return char

    result = ''.join([encode(char, key) for char in input_string])
    return result


if __name__ == "__main__":
    print(caesar_code('Lille kat, lille kat, lille kat på vejen.', 12))

