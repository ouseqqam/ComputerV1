import math

str = "2 * X ^ 2 - 33 * X ^ 1 + 2 * X ^ 0 = 3 * X ^ 2"
str = str.replace(" ", "").lower()

data = []
n = len(str)
i = 0
while i < n:
    coef = ''
    if str[i] == '=':
        i += 1
    while i < n and str[i] != '*':
        coef += str[i]
        i += 1
    i += 3
    if i >= n:
        break
    power = int(str[i])
    s1 = {
    'coef': int(coef),
    'power': power
    }
    data.append(s1)
    i += 1
print(data)
n = len(data)
print(n)
i = 0

while i < n - 1:
    j = i + 1
    while j < n:
        if data[i]['power'] == data[j]['power']:
            data[i]['coef'] += data[j]['coef']
            del data[j]
            n -= 1
        j += 1
    i += 1

a = data[0]['coef']
b = data[1]['coef']
c = data[2]['coef']

delta = b * b - 4 * a * c

if delta = 0:
    x0 = -b / 2 * a
else if delta > 0 :
    x1 = -b - math.sqrt(delta) / 2 * a
    x2 = -b + math.sqrt(delta) / 2 * a

