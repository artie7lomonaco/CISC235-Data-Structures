# Linear search (Algorithm A):
# parameters are list and the target
# for loop that when True returns, loop breaks and function exited
# Otherwise returns false
def linear_search(arr, target):
    #count times loop runs
    count = 0
    #for loop that iterates through whole list
    #until target found, which returns value and exits function
    for i in arr:
        count=count+1
        if i == target:
            return True, count
    return False, count


# Binary Search (part of algorithm B):
#The parameters are the array and the targer
def binary_search(arr, x):
    #count of times loop runs
    count = 0
    upper_bound = len(arr) - 1
    lower_bound = 0
    mid = 0
    while lower_bound <= upper_bound:
        count = count + 1
        #mid changes every time depending on new upper or lower bounds
        mid = (upper_bound + lower_bound) // 2
        #if target less than mid, the mid becomes upper limit
        if x < arr[mid]:
            upper_bound = mid - 1
        #if target greater than mid, mid becomes lower bound
        elif x > arr[mid]:
            lower_bound = mid + 1
        #if mid is equal to target, returns true and loop count
        else:
            return True , count
    return False , count
