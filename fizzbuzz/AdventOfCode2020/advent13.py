from functools import reduce


input_lines ='''1000104
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17'''.splitlines()

test = '''10
7,13,x,x,59,x,31,19'''.splitlines()
original_timestamp = int(input_lines[0])
busses = list(map(int, filter(lambda  x: x.isnumeric(), input_lines[1].split(','))))
new_bus_list = input_lines[1].split(',')


def question1(original_timestamp):
    timestamp = original_timestamp
    while True:
        for bus in busses:
            if timestamp % bus == 0:
                return (bus * (timestamp - original_timestamp))

        timestamp += 1    

print(question1(original_timestamp))

def question2(bus_list):
    def chinese_remainder(bus_list):
        busses = [a[0] for a in bus_list]
        sum = 0
        prod = reduce(lambda a, b: a*b, busses)
        for n_i, a_i in bus_list:
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod
 
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1: return 1
        while a > 1:
            q = a // b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0: x1 += b0
        return x1

    print('Question2')
    
    busses = [(int(bus), - number) for number, bus in enumerate(bus_list) if bus.isnumeric()]
    result = chinese_remainder(busses)
    return result

print(question2(new_bus_list))