import functools

def something(funktion):
    def fizzbuzz(func):
        """I'm a decorator"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            first_arg = args[0]
            second_arg = args[1]
            output = second_arg
            if isinstance(output, int):
                output = funktion(first_arg)
            else:
                output += str(funktion(first_arg))

            if not output:
                output = first_arg
            func(first_arg, output, **kwargs)
        return wrapper
    return fizzbuzz


@something(lambda a  : "Fizz" if a % 3 == 0  else "")
@something(lambda a  : "Buzz" if a % 5 == 0  else "")
@something(lambda a  : "Bonanza" if a % 7 == 0  else "")
def my_print(just_a_number, output):
    print(output)


def decoratorbuzz():
    for i in range(1, 101):
        my_print(i, '')


if __name__ == "__main__":
    decoratorbuzz()
