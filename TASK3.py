
def array_prepare (array):
    """Функция подготовки массива дробных частей исходного массива"""
    prepared_array = []
    for i in range (len(array)):
        prepared_array.append(round(array[i]%1,4))
    return prepared_array
def diff_max_min (array_for_diff):
    """Функция нахождения разницы меджу максимальным и минимальным значением элементов массива"""
    min = array_for_diff[0]
    max = array_for_diff[0]
    for i in range (len(array_for_diff)):
        if min > array_for_diff[i]:
            min = array_for_diff[i]
        elif max < array_for_diff[i]:
            max = array_for_diff[i]
    difference = round(max - min,4)
    return difference

spisok = [1.1, 1.2, 3.1, 5.17, 10.02]
print(diff_max_min(array_prepare(spisok)))
spisok = [4.07, 5.1, 8.2444, 6.9844]
print(diff_max_min(array_prepare(spisok)))