
input_numbers = [16,1,0,18,12,14,19]
i1 = [0,3,6]

spoken = dict()

def speak(numbers):
    previous = -1
    for i, number in enumerate(numbers):
        spoken.update({previous: i})      
        yield number
        previous = number

    for i in range(len(numbers), 30_000_000):
        val = spoken.get(previous, 0)
        spoken.update({previous: i})

        if val == 0:
            yield 0
            previous = 0
        else:
            value = i - val
            yield value
            previous = value
        

yielder = speak(input_numbers)

for i, value in enumerate(yielder):
    if i % 100000 == 0:
        print(i, value)

print(spoken)





