import random
from search import *
from merge_sort import *

#This main function will be where I test code from Question 1
#the functions of merge_sort, linear_search, and binary_search are imported up top
def main():
    print("Question 1:")
    #this section of code will be repeated 3 times with size of S
    #being n = 1000, 5000, and 10000 for the cases
    print("S of size 1000:")
    print("k in S:")
    #creates a list of size n, in this case 1000 with the range of the values
    #being 1 to 99
    S1000 = [random.randrange(1, 99, 1) for i in range(1000)]
    #the value that is in the list that we want to find
    k = 77
    #prints that value is found and how many times loop has gone to show complexity
    print("Linear Search: ",linear_search(S1000,k))
    print("Binary Search: ",binary_search(merge_sort(S1000),k))
    print("k not in S:")
    #the value that is not in the list
    k = 101
    print("Linear Search: ", linear_search(S1000, k))
    print("Binary Search: ", binary_search(merge_sort(S1000), k))
    print("------------------------------------------------------------")


    print("S of size 5000:")
    print("k in S:")
    S5000 = [random.randrange(1, 99, 1) for i in range(5000)]
    k = 77
    print("Linear Search: ", linear_search(S5000, k))
    print("Binary Search: ", binary_search(merge_sort(S5000), k))
    print("k not in S:")
    k = 101
    print("Linear Search: ", linear_search(S5000, k))
    print("Binary Search: ", binary_search(merge_sort(S5000), k))
    print("------------------------------------------------------------")

    print("S of size 1000:")
    print("k in S:")
    S10k = [random.randrange(1, 99, 1) for i in range(10000)]
    k = 77
    print("Linear Search: ", linear_search(S10k, k))
    print("Binary Search: ", binary_search(merge_sort(S10k), k))
    print("k not in S:")
    k = 101
    print("Linear Search: ", linear_search(S10k, k))
    print("Binary Search: ", binary_search(merge_sort(S10k), k))
    print("------------------------------------------------------------")
#main function is ran here
main()
