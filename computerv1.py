import re

def sqrt(nb):
    return nb ** 0.5

regex = '^(([-+]\s?)?\d*(\.?\d+)?\s?\*\s?(X\s?(\^\s?[+]?\d+))\s?)+=\s?(0|((([-+]\s)?\d*(\.?\d+)?\s?\*\s?(X\s?(\^\s?[+]?\d+))\s?)+))'
st = "-33 * X ^ 2 + 5 * X ^ 1 + 1 * X ^ 0 = 0"
x = re.search(regex, st)

if x == None:
    exit("Error")
st = st.replace(" ", "").lower()

data = []
n = len(st)
i = 0
sign = 1
while i < n:
    coef = ''
    if st[i] == '=':
        i += 1
        sign = -1
    while i < n and st[i] != '*':
        coef += st[i]
        i += 1
    i += 3
    if i >= n:
        break
    power = int(st[i])
    s1 = {
    'coef': sign * float(coef),
    'power': power
    }
    data.append(s1)
    i += 1

n = len(data)
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

n = len(data)
i = 0

while i < n - 1:
    j = i + 1
    while j < n:
        if data[i]['power'] < data[j]['power']:
            c = data[i]
            data[i] = data[j]
            data[j] = c
        j += 1
    i += 1

test = 'Reduced form: '
n = len(data)
i = 0

data1 = data[::-1]
while i < n:
    coef = str(data1[i]['coef'])
    power = str(data1[i]['power'])
    test = test + coef + ' * X ^ ' + power
    if i != n - 1:
        test += ' + '
    i += 1
    if i == n:
        test += ' = 0'
print(test)

degree = data[0]['power']
print("Polynomial degree:", degree)
if degree > 2:
    print("The polynomial degree is strictly greater than 2, I can't solve.")
elif degree == 2:
    a = data[0]['coef']
    b = data[1]['coef']
    c = data[2]['coef']

    delta = b * b - 4 * a * c

    if delta == 0:
        x0 = -b / 2 * a
        print("x0 = ", x0)
    elif delta > 0 :
        x1 = -b - sqrt(delta) / 2 * a
        x2 = -b + sqrt(delta) / 2 * a
        print("Discriminant is strictly positive, the two solutions are:")
        print( x1)
        print(x2)
    if delta < 0:
        delta = -delta
        z1r = -b / 2 * a
        z1i = sqrt(delta) / 2 * a
        print("Discriminant is strictly negative, the equation have two solution in C:")
        print(str(z1r) + " - i * " + str(z1i))
        print(str(z1r) + " + i * " + str(z1i))
elif degree == 1:
    x = -1 * data[1]['coef'] /  data[0]['coef']
elif degree == 0 and len(data) == 1:
    if data[0]['coef'] != 0:
        print("The equation has no solution.")
    else:
        print("Each real number is a solution")
