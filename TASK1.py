
def summ_elements (array):
    """Функция нахождения суммы значений нечетных елементов списка"""
    result = 0
    for i in range (1,len(array),2):
        result+=array[i]
    return result
spisok = [2, 3, 5, 9, 3]
print (summ_elements(spisok))
