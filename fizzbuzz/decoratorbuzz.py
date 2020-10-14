import functools

def fizzbuzz(func):
    """I'm a decorator"""
    @functools.wraps(func)
    def fizzbuzz(*args, **kwargs):
        first_arg = args[0]
        output = ''        
        if first_arg % 3 == 0:
            output += "Fizz"

        if first_arg % 5 == 0:
            output += "Buzz"
        if not output:
            output = first_arg
        func(output, **kwargs)
    return fizzbuzz


@fizzbuzz
def my_print(i):
    print(i)


def decoratorbuzz():
    for i in range(1, 101):
        my_print(i)


if __name__ == "__main__":
    decoratorbuzz()
