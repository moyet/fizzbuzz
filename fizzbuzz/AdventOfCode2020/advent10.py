from functools  import cache

inputstrengt = '''8
131
91
35
47
116
105
121
56
62
94
72
13
82
156
102
12
59
31
138
46
120
7
127
126
111
2
123
22
69
18
157
75
149
88
81
23
98
132
1
63
142
37
133
61
112
122
128
155
145
139
66
42
134
24
60
9
28
17
29
101
148
96
68
25
19
6
67
113
55
40
135
97
79
48
159
14
43
86
36
41
85
87
119
30
108
80
152
158
151
32
78
150
95
3
52
49'''

i2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

smalllist = '''16
10
15
5
1
11
7
19
6
12
4'''

inputlist = list(map(int, inputstrengt.split('\n')))
inputlist.sort()

inputlist.append(inputlist[-1]+3)

previous = 0
ones = 0
twos = 0
threes = 0

for i in inputlist:
    if i - previous == 1:
        ones +=1
    elif i - previous == 2:
        twos += 1
    elif i - previous == 3:
        threes += 1
    previous = i

#print(ones, twos, threes)
#print(ones * threes)

endvalue = inputlist[-1]

inputlist = [0] + inputlist


@cache
def count_the_ways(current_value):
    if current_value == endvalue:
        return 1

    index = inputlist.index(current_value)

    returnvalue = 0

    slice_of_life = inputlist[index+1:index+4]
    for v in slice_of_life:
        if v - current_value <= 3:
            result = count_the_ways(v)
            returnvalue += result
    
    return returnvalue


result = count_the_ways(inputlist[0])

print(result)
