
def mapbang(i):
    out = ''
    if i % 3 == 0:
        out += 'Fizz'
    if i % 5 == 0:
        out +=  "Bang"
    if not out:
        out = str(i)

    return out


def main():
    my_list = map(mapbang, range(1, 101))
    for i in my_list:
        print(i)

if __name__ == "__main__":
    main()
