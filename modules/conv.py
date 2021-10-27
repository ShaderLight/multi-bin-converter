from math import modf


def from_dec_conv(x, to_base, bits=5):
    x_frac, x_int = modf(x)

    x_frac = abs(x_frac)

    if x_frac == 0.0:
        return from_dec_conv_int(x, to_base)
    
    return from_dec_conv_int(x_int, to_base) + '.' + from_dec_conv_frac(x_frac, to_base, bits)


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