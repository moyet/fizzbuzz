
def fizzbuzz():
    i = 1
    while True:
        output = ''
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0 :
            output += "Buzz"
        if not output:
            output = str(i)
        yield output
        i += 1


def main():
    for fb in fizzbuzz():
        if fb == '101': 
            break
        print(fb)
    

if __name__ == "__main__":
    main()
