def dec_to_bin(x):
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


def bin_to_dec(x):
    negative = 1
    if x[-1] == '-':
        x.pop()
        negative = -1

    output = 0
    for i in range(len(x)):
        output += x[i] * 2 ** (len(x)-i-1)

    output *= negative

    return output