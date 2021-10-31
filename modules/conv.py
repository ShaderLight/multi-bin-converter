from math import modf


# From base-10 to any base (up to 16)

def from_dec_conv(x, to_base, bits=5):
    x_frac, x_int = modf(x)

    x_frac = abs(x_frac)


    if x_frac == 0.0:
        if to_base == 'u2':
            return bin_to_u2(from_dec_conv_int(x, 2))
        elif to_base == 'u1':
            return bin_to_u1(from_dec_conv_int(x, 2))
        
        return from_dec_conv_int(x, to_base)
    
    if to_base == 'u2':
        return bin_to_u2(from_dec_conv_int(x_int, 2) + '.' + from_dec_conv_frac(x_frac, 2, bits))
    elif to_base == 'u1':
        return bin_to_u1(from_dec_conv_int(x_int, 2) + '.' + from_dec_conv_frac(x_frac, 2, bits))

    return from_dec_conv_int(x_int, to_base) + '.' + from_dec_conv_frac(x_frac, to_base, bits)


# From any base (up to 16) to base-10

def to_dec_conv(x, from_base):
    negative = 1
    if x[0] == '-':
        negative = -1
        try:
            x_splitted = x.split('.')
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


# From base-2 to u2 (two's complement)

def bin_to_u2(x):
    if x[0] == '-':
        if x[1] == '1':
            x = inversion('0' + x[1:])
        else:
            x = inversion(x[1:])

        return bin_add_one_lsb(x)
    
    if x[0] == '0':
        return x
    return '0' + x


# From base-2 to u1 (one's complement)

def bin_to_u1(x):
    if '.' in x:
        x = x.split('.')[0]
    if x[0] == '-':
        if x[1] == '1':
            return inversion('0' + x[1:])
        return inversion(x[1:])
    
    if x[0] == '0':
        return x
    
    return '0' + x


# From u2 (two's complement) function

def u2_to_dec(x):
    x_split = x.split('.')

    try:
        return -1 * 2 ** (len(x_split[0]) - 1) * int(x_split[0][0]) + to_dec_conv(x_split[0][1:], 2) + to_dec_conv(x_split[1], 2)
    except IndexError:
        return -1 * 2 ** (len(x_split[0]) - 1) * int(x_split[0][0]) + to_dec_conv(x_split[0][1:], 2)


# From u1 (one's comeplement) function

def u1_to_dec(x):
    x_split = x.split('.')

    try:
        return -1 * (2 ** (len(x_split[0]) - 1) - 1) * int(x_split[0][0]) + to_dec_conv(x_split[0][1:], 2) + to_dec_conv(x_split[1], 2)
    except IndexError:
        return -1 * (2 ** (len(x_split[0]) - 1) - 1) * int(x_split[0][0]) + to_dec_conv(x_split[0][1:], 2)


# --- Other functions ---
# Integral part converting

def to_dec_conv_int(x, from_base):
    output = 0

    x = detranslate_values(x)
    for i in range(len(x)):
        output += int(x[i]) * from_base ** (len(x)-i-1)

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


# Fractional part converting

def to_dec_conv_frac(x, from_base):
    output = 0

    x = detranslate_values(x)
    for i in range(len(x)):
        output += int(x[i]) * from_base ** (-1 - i)
    
    return output


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


# Translation for bases higher than 10

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


# Binary operations

def inversion(x):
    output = ''
    for i in range(len(x)):
        if x[i] == '0':
            output += '1'
        elif x[i] == '1':
            output += '0'
        else:
            output += x[i]

    return output


def bin_add_one_lsb(x):
    sep_index = ['.', x.find('.')]
    
    if sep_index[1] == -1:
        sep_index = [',', x.find(',')]

    for i in range(len(x)):
        if x[len(x) - i - 1] == '0':
            output = x[:len(x) - i - 1] + '1' + '0' * len(x[len(x) - i:])

            if sep_index[1] >= 0:
                output = output[:sep_index[1]] + sep_index[0] + output[sep_index[1] + 1:]

            return output

    raise OverflowError