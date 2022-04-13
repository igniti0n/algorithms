import math
import quick_sort

def insertionSort(array):
        if len(array) == 1:
            return array
        i = 1
        while i < len(array):
            print(array)
            if array[i] < array[i-1]:
                j = i
                print("At:", array[i])
                for j in reversed(range(i)):
                    if array[j] < array[j-1]:
                        print("switching: ", array[j], " :: ", array[j-1])
                        temp = array[j]
                        array[j] = array[j-1]
                        array[j-1] = temp
                    else:
                        break
            i += 1
        return array
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [8, 5, 3, 9, 2, 1, 4, 10]
    quick_sort.quickSort(array)
    print(array)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
