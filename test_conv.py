
import pytest

from modules.conv import*


def test_dec_to_bin():
    x = from_dec_conv(10, 2)
    assert x == '1010'

def test_dec_to_bin_frac():
    x = from_dec_conv(1234.75, 2)
    assert x == '10011010010.11000'


def test_dec_to_bin_negative():
    x = from_dec_conv(-1234, 2)
    assert x == '-10011010010'

def test_dec_to_bin_frac_negative():
    x = from_dec_conv(-1234.75, 2, bits=2)
    assert x == '-10011010010.11'

def test_bin_to_dec():
    x = to_dec_conv('1001', 2)
    assert x == 9

def test_bin_to_dec_frac():
    x = to_dec_conv('101.1', 2)
    assert x == 5.5

def test_bin_to_dec_negative():
    x = to_dec_conv('-111', 2)
    assert x == -7

def test_bin_to_dec_frac_negative():
    x = to_dec_conv('-111.01', 2)
    assert x == -7.25

def test_dec_to_oct():
    x = from_dec_conv(169, 8)
    assert x == '251'

def test_dec_to_oct_frac():
    x = from_dec_conv(169.125, 8, bits=1)
    assert x == '251.1'

def test_dec_to_oct_negative():
    x = from_dec_conv(-169, 8)
    assert x == '-251'

def test_dec_to_oct_frac_negative():
    x = from_dec_conv(-169.125, 8, bits=1)
    assert x == '-251.1'

def test_oct_to_dec():
    x = to_dec_conv('124', 8)
    assert x == 84

def test_oct_to_dec_frac():
    x = to_dec_conv('1.1', 8)
    assert x == 1.125

def test_oct_to_dec_negative():
    x = to_dec_conv('-124', 8)
    assert x == -84

def test_oct_to_dec_frac_negative():
    x = to_dec_conv('-124.2', 8)
    assert x == -84.25

def test_dec_to_hex():
    x = from_dec_conv(1249, 16)
    assert x == '4E1'

def test_dec_to_hex_frac():
    x = from_dec_conv(0.9375, 16, bits=1)
    assert x == '0.F'

def test_dec_to_hex_negative():
    x = from_dec_conv(-124, 16)
    assert x == '-7C'

def test_dec_to_hex_frac_negative():
    x = from_dec_conv(-124.9375, 16, bits=4)
    assert x == '-7C.F000'

def test_hex_to_dec():
    x = to_dec_conv('F', 16)
    assert x == 15

def test_hex_to_dec_frac():
    x = to_dec_conv('0.F', 16)
    assert x == 0.9375

def test_hex_to_dec_negative():
    x = to_dec_conv('-FF', 16)
    assert x == -255

def test_hex_to_dec_frac_negative():
    x = to_dec_conv('-FF.F', 16)
    assert x == -255.9375

def test_bin_to_u2():
    x = bin_to_u2('110001')
    assert x == '0110001'


def test_bin_to_u2_frac():
    x = bin_to_u2('110001.11')
    assert x == '0110001.11'


def test_bin_to_u2_negative():
    x = bin_to_u2('-11001')
    assert x == '100111'

def test_bin_to_u2_frac_negative():
    x = bin_to_u2('-1001.1')
    assert x == '10110.1'

def test_bin_to_u1():
    x = bin_to_u1('110001')
    assert x == '0110001'

def test_bin_to_u1_negative():
    x = bin_to_u1('-11001')
    assert x == '100110'

def test_u2_to_dec():
    x = u2_to_dec('0110')
    assert x == 6

def test_u1_to_dec():
    x = u1_to_dec('0110')
    assert x == 6