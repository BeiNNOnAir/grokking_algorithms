# 4.1 sum function
def sum_(lst):
    if len(lst)==1:
        return lst[-1]
    else:
        return lst.pop()+sum_(lst)
# test = sum_([3,4,5])
# print(test)

# 4.2 count function
def count_(lst):
    if len(lst)==1:
        return 1
    else:
        return 1+ count_(lst[1:])
# test = count_([3,4,5])
# print(test)

# 4.3 max function
def max_(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) ==2:
        if lst[0] >lst[1]:
            return lst[0]
        else:
            return lst[1]
    else:
        return max_([lst[0], max_(lst[1:])])
# test = max_([8,3,4,5])
# print(test)

def quicksort(lst):
    less = []
    greater = []
    if len(lst)<2:
        return lst
    else:
        pivot = lst[0]
        for i in lst[1:]:
            # here remember [1:], otherwise it is a dead loop
            if i <=pivot:
                less.append(i)
            else:
                greater.append(i)
        return quicksort(less)+[pivot]+quicksort(greater)
print(quicksort([4,6,3,5,2]))