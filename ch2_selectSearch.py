def findBiggest(arr):
    biggest = arr[0]
    biggest_index = 0
    for i in range(len(arr)):
        if arr[i]>biggest:
            biggest = arr[i]
            biggest_index = i
    return biggest_index

def selectionSort(arr):
    new_arr=[]
    for i in range(len(arr)):
        new_arr.append(arr[findBiggest(arr)])
        arr.pop(findBiggest(arr))
    return new_arr

print(selectionSort([5,3,6,2,10]))