def checkio(first, second):
    first_bin = bin(first)[2:]
    second_bin = bin(second)[2:]
    and_table = [[str((int(bit_first, 2) and int(bit_second, 2))) for bit_first in second_bin] for bit_second in first_bin]
    or_table = [[str((int(bit_first, 2) or int(bit_second, 2))) for bit_first in second_bin] for bit_second in first_bin]  
    xor_table = [[str((int(bit_first, 2) ^ int(bit_second, 2))) for bit_first in second_bin] for bit_second in first_bin]
    and_sum = 0
    or_sum = 0
    xor_sum = 0
    for row in and_table:
        and_sum += int(''.join(row), 2)
    for row in or_table:
        or_sum += int(''.join(row), 2) 
    for row in xor_table:
        xor_sum += int(''.join(row), 2) 
    return and_sum + or_sum + xor_sum

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
