
def fib(n):
    '''Форирование последовательности Фибоначи'''
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def sign_change (array):
    '''Смена знака в развернутом массиве и удаление последнего элемента'''
    result_array=[]
    for i in range (len(array)):
        if i %2 == 0:
            result_array.append(-1*array[i])
        else:
            result_array.append(array[i])
    result_array.pop()
    return result_array
number = int(input('Введите индекс '))
list = []
for e in range(number+1):
    if e == 0:
        list.append(0)
    else:
        list.append(fib(e))
list1 = list.copy()
list.reverse()
list = sign_change(list)
print(list + list1)
