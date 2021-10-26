from os import sep


def dec_to_bin(x, bits=5):
    x_int = int(x)
    x_frac = abs(x - x_int)


    if x_frac == 0:
        return dec_to_bin_int(x_int)

    return (dec_to_bin_int(x_int) + '.' + dec_to_bin_frac(x_frac, bits))


def bin_to_dec(x):
    x_split = x.split('.')

    if len(x_split) == 1:
        return bin_to_dec_int(x_split[0])
    
    if x_split[0][0] == '-':
        return -1 * (abs(bin_to_dec_int(x_split[0])) + bin_to_dec_frac(x_split[1]))

    return bin_to_dec_int(x_split[0]) + bin_to_dec_frac(x_split[1])


def dec_to_bin_int(x):
    output = []
    if x == 0:
        return [0]
    elif x < 0:
        output.append('-')
        x = x * (-1)

    while x != 0:
        output.append(x%2)
        x = x//2

    output.reverse()

    output_str = ''

    if output[-1] == '-':
        output_str = output.pop()

    for c in output:
        output_str += str(c)

    return output_str


def bin_to_dec_int(x):
    negative = 1
    if x[0] == '-':
        x = x[1:]
        negative = -1

    output = 0
    for i in range(len(x)):
        output += int(x[i]) * 2 ** (len(x)-i-1)

    output *= negative

    return output


def bin_to_dec_frac(x):
    output = 0
    for i in range(len(x)):
        output += int(x[i]) * 2 ** (-1 - i)
    
    return output


def dec_to_bin_frac(x, bits=5):
    assert x < 1
    
    output = ''
    while bits > 0:
        x *= 2
        if x >= 1:
            x -= 1
            output += '1'
        else:
            output += '0'

        bits -= 1
    return output


def bin_to_u2(x):
    if x[0] == '-':
        x = inversion('0' + x[1:])
        
        return bin_add_one_lsb(x)
    
    return '0' + x

def bin_to_u1(x):
    if x[0] == '-':
        return inversion(x[1:])

    return '0' + x

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


def u2_to_dec(x):
    x_split = x.split('.')

    try:
        return -1 * 2 ** (len(x_split[0]) - 1) + bin_to_dec_int(x_split[0][1:]) + bin_to_dec_frac(x_split[1])
    except IndexError:
        return -1 * 2 ** (len(x_split[0]) - 1) + bin_to_dec_int(x_split[0][1:])