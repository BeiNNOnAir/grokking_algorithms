def binary_search(lst,item):
    low = 0
    high = len(lst)-1
    while(low<=high):
        mid = round((low+high)/2)
        guess = lst[mid]
        if (guess>item):
            high = mid - 1
        elif (guess < item):
            low = mid+1
        else:
            return mid
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list,7))