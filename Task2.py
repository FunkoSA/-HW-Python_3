
def multiplication_first_last (array):
    """Функция нахождения суммы значений нечетных елементов списка"""
    if len(array)%2 == 0:
        size = int(len(array)/2)
    else:
        size = int(len(array)/2 + 0.5)
    array_m = []
    for i in range (1,(size+1)):
        array_m.append(array[i-1]*array[-i])
    return array_m
spisok = [2, 3, 4, 5, 6] 
print(multiplication_first_last(spisok))


