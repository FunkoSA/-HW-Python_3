import math
def multiplication_first_last (array):
    array_m = []
    for i in range (1,(math.ceil(len(array)/2)+1)):
        array_m.append(array[i-1]*array[-i])
    return array_m
spisok = [2, 3, 4, 5, 6] 
print(multiplication_first_last(spisok))

