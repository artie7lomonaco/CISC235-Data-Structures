#Will be using merge sort to sort list since has complexity of O(nlogn) complexity
#First part to Algorithm B
#Splits list until list(s) contain only one element,
#using recursion splits them then merges them all
#and returns one sorted list
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        # Recursive call on each half of list
        #repeat this until len is 1
        merge_sort(left)
        merge_sort(right)
        # Two numbers that will be used to go through the halves
        i = 0
        j = 0
        # k will iterate over the whole list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left i half has been used
                my_list[k] = left[i]
                # Move the iterator i forward
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot of list with k
            k += 1
        # Go through remaining values that are left
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1
    return my_list