import re
import sys

def sqrt(nb):
    return nb ** 0.5



if len(sys.argv) != 2:
    exit("ERROR")

st = sys.argv[1]
st = st.replace(" ", "")
regex = r"^(([-+])?((\d\.)?\d)?(\*?X(\^[+-]?(\d+))?)?)+=(([-+])?((\d\.)?\d)?(\*?X(\^[+-]?(\d+))?)?)+$"
x = re.search(regex, st)

if x == None:
    exit("Error")
if st[0] == '=':
    exit("ERROR")
if st[len(st) - 1] == '=':
    exit("ERROR")
st = st.replace(" ", "").lower()

data = []
n = len(st)
i = 0
otherSideSign = 1
sign = 1

while i < n:
    coef = ''
    power = '0'
    powSign = 1
    if st[i] == '-':
        sign = -1
        i += 1
    elif st[i] == '+':
        i += 1
    if st[i] == 'x':
        coef = 1
        power = 1
        i += 1
    else:
        coef = ''
        while i < n:
            if st[i] >= '0' and st[i] <= '9' or st[i] == '.':
                coef += st[i]
            else:
                if st[i] == 'x':
                    exit("ERROR")
                if st[i] == '*':
                    power = '1'
                    i += 2
                break
            i += 1
    if i < n and st[i] == '^':
        power = ''
        i += 1
        if st[i] == '-':
            powSign = -1
            i += 1
        if st[i] == '+':
            i += 1
        while i < n:
            if st[i] >= '0' and st[i] <= '9':
                power += st[i]
            else:
                break
            i += 1
    s1 = {
    'coef': sign * otherSideSign * float(coef),
    'power': powSign * int(power)
    }
    data.append(s1)
    if i < n:
        if st[i] == '=':
            otherSideSign = -1
            sign = 1
        elif st[i] == '-':
            sign = -1
        elif st[i] == '+':
            sign = 1
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
            j -= 1
        j += 1
    i += 1

n = len(data)
i = 0

while i < n:
    if data[i]['coef'] == 0:
        del data[i]
        n -= 1
        i -= 1
    i += 1

n = len(data)
i = 0


while i < n:
    if data[i]['power'] < 0:
        exit("ERROR")
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

if len(data) == 0:
    print("Reduced form: 0 = 0")
    print("Each real number is a solution")
    exit()

while i < n:
    coef = data1[i]['coef']
    power = data1[i]['power']
    powers = str(data1[i]['power'])
    if data[0]['coef'] < 0:
        test += '-'
    if coef > 0:
        coefs = str(data1[i]['coef'])
        if power > 1:
            test = test + coefs + ' * X ^ ' + powers
        elif power == 1:
            test = test + coefs + ' * X'
        elif power == 0:
            test = test + coefs
    elif coef < 0:
        coefs = str(data1[i]['coef'] * -1)
        if power > 1:
            test = test + coefs + ' * X ^ ' + powers
        elif power == 1:
            test = test + coefs + ' * X'
        elif power == 0:
            test = test + coefs
    if data1[i]['coef'] != 0 and i + 1 < n :
        if data1[i + 1]['coef'] < 0:
            test += ' - '
        elif data1[i + 1]['coef'] > 0:
            test += ' + '
    i += 1
    if i == n:
        test += ' = 0'
print(test)


degree = data[0]['power']
print("Polynomial degree:", degree)
if degree > 2:
    print("The polynomial degree is strictly greater than 2, I can't solve.")
if degree == 2:
    a = data[0]['coef']
    b = 0
    c = 0
    if len(data) == 3:
        a = data[0]['coef']
        b = data[1]['coef']
        c = data[2]['coef']
    elif len(data) == 2:
        if data[1]['power'] == 1:
            b = data[1]['coef']
            c = 0
        elif data[1]['power'] == 0:
            b = 0
            c = data[1]['coef']
    delta = b * b - (4 * a * c)
    if delta == 0:
        x0 = -b / (2 * a)
        print("x0 = ", x0)
    elif delta > 0 :
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("Discriminant is strictly positive, the two solutions are:")
        print( x1)
        print(x2)
    if delta < 0:
        delta = -delta
        z1r = -b / (2 * a)
        z1i = sqrt(delta) / (2 * a)
        print("Discriminant is strictly negative, the equation have two solution in C:")
        print(str(z1r) + " - i * " + str(z1i))
        print(str(z1r) + " + i * " + str(z1i))
elif degree == 1:
    if len(data) == 1:
        if data[0]['power'] == 1:
            print("The solution is:")
            exit('0')
    if data[0]['coef'] == 0:
        print("The equation has no solution.")
    else:
        x = -1 * data[1]['coef'] /  data[0]['coef']
        print("The solution is:")
        print(x)
elif degree == 0 and len(data) == 1:
    if data[0]['coef'] != 0:
        print("The equation has no solution.")
    else:
        print("Each real number is a solution")