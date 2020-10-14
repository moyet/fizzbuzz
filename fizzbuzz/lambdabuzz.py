fizz = lambda i : "Fizz" if i % 3 == 0  else ""
buzz = lambda i : "Buzz" if i % 5 == 0 else ""

def lambdabuzz():
    for i in range(1,101):
        output = ""
        output += fizz(i) + buzz(i)
        if not output:
            output = str(i)
        print(output)


if __name__ == "__main__":
    lambdabuzz()