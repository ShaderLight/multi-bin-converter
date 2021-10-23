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