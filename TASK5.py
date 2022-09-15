
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def sign_change (array):
    result_array=[]
    for i in range (len(array)):
        result_array.append(-1*array[i])
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
#print(list)