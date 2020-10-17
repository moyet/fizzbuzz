from primes import primes

values = {
    3: "Fizz",
    5: "Buzz",
    7: "Bonanza",
}

def newbuzz(values, collection):
    for i in collection:
        output = ""
        for key in values:
            if i % key == 0:
                output += values[key]
        if not output:
            output = str(i)
        
        print(output)


if __name__ == "__main__":
    pri = primes()
    my_range = [next(pri) for i in range(1,101)]

    newbuzz(values, my_range)
