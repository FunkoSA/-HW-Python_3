bin_number =[]
def dec_to_bin (number):
    if number > 0:
        bin_number.append(number%2)
        dec_to_bin(number//2)
    else:
        bin_number.reverse()
        
        return print(''.join(map(str,bin_number)))

n = int(input('Введите дестичное число дла перевода в двоичную систему: '))
print('Результат перевода:')
dec_to_bin(n)


