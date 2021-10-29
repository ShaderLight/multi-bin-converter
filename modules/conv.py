from math import modf


def from_dec_conv(x, to_base, bits=5):
    x_frac, x_int = modf(x)

    x_frac = abs(x_frac)

    if x_frac == 0.0:
        return from_dec_conv_int(x, to_base)
    
    return from_dec_conv_int(x_int, to_base) + '.' + from_dec_conv_frac(x_frac, to_base, bits)


def to_dec_conv(x, from_base):
    negative = 1
    if x[0] == '-':
        negative = -1
        try:
            x_splitted = x.split('.')
            print(x_splitted)
            x_int, x_frac = x_splitted[0][1:], x_splitted[1]
        except IndexError:
            x_int = x[1:]
    else:
        try:
            x_int, x_frac = x.split('.')
        except ValueError:
            x_int = x

    try:
        return negative * (to_dec_conv_int(x_int, from_base) + to_dec_conv_frac(x_frac, from_base))
    except UnboundLocalError:
        return negative * (to_dec_conv_int(x_int, from_base))


def to_dec_conv_int(x, from_base):
    output = 0

    x = detranslate_values(x)
    for i in range(len(x)):
        output += int(x[i]) * from_base ** (len(x)-i-1)

    return output


def to_dec_conv_frac(x, from_base):
    output = 0

    x = detranslate_values(x)
    for i in range(len(x)):
        output += int(x[i]) * from_base ** (-1 - i)
    
    return output


def from_dec_conv_int(x, to_base):
    output = []

    x = int(x)
    if x == 0:
        return '0'
    elif x < 0:
        output.append('-')
        x = x * (-1)

    while x != 0:
        output.append(x % to_base)
        x = x // to_base

    output.reverse()
    output = translate_values(output)

    output_str = ''

    if output[-1] == '-':
        output_str = output.pop()

    for c in output:
        output_str += str(c)

    return output_str


def from_dec_conv_frac(x, to_base, bits=5):
    assert x < 1
    
    output = []
    while bits > 0:
        x *= to_base
        int_part = int(modf(x)[1])
        x = modf(x)[0]

        if int_part >= 1:
            output.append(str(int_part))
        else:
            output.append('0')

        bits -= 1
    
    output = translate_values(output)
    output_str = ''
    for c in output:
        output_str += str(c)

    return output_str


def translate_values(x):
    LETTERS = ('A', 'B', 'C', 'D', 'E', 'F')
    for i in range(len(x)):
        try:
            element = int(x[i])
        except:
            continue

        if int(x[i]) >= 10:
            x[i] = LETTERS[element - 10]

    return x


def detranslate_values(x):
    LETTERS = ('A', 'B', 'C', 'D', 'E', 'F')
    output = []

    for c in x:
        try:
            output.append(int(c))
        except ValueError:
            if c in LETTERS:
                output.append(LETTERS.index(c) + 10)
            else:
                output.append(c)
    
    return output