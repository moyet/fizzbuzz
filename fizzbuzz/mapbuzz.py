
def mapbuzz(i):
    out = ''
    if i % 3 == 0:
        out += 'Fizz'
    if i % 5 == 0:
        out += "Buzz"
    if not out:
        out = str(i)

    return out


def main():
    my_list = map(mapbuzz, range(1, 101))
    for i in my_list:
        print(i)

if __name__ == "__main__":
    main()
