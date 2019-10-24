def cap():
    n = int(input('Enter your the capacity of array:'))
    return n


def inputArray(n):
    arr = []
    for x in range(n):
        print("Enter ele [", x, "]:")
        i = int(input(""))
        arr.append(i)
    return arr


def eleUnique(arr):
    arr_1 = []
    arr_1.append(arr[0])
    for i in arr:
        count = 0
        for j in arr_1:
            if i == j:
                count += 1
        if(count == 0):
            arr_1.append(i)
    return arr_1


def showTime(arr, arr_1):
    arr_2 = []
    for i in arr_1:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        arr_2.append(count)
    return arr_2


def endGame(arr_1, arr_2):
    arr_3 = []
    for i in range(len(arr_1)):
        if(arr_2[i] == 1):
            arr_3.append(arr_1[i])
    return arr_3


def main():
    n = cap()
    arr = inputArray(n)
    arr_1 = eleUnique(arr)
    arr_2 = showTime(arr, arr_1)
    arr_3 = endGame(arr_1, arr_2)
    print(arr_3)


main()
