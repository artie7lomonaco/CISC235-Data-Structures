from AVLTreeMap_fix import *
from WebPageIndex import *
from WebpagePriorityQueue import *
import os


# readfiles code, reads the files in "data" directory
# adds wpi to a list and returns it
def readFiles(path):
    dirList = os.listdir(path)
    result = []
    for i in dirList:
        pageString = path + "/" + i
        result.append(WebPageIndex(pageString))
    return result

#main function where test takes place
def main():
    path = "data"
    my_file = open("queries.txt", "r")
    values = my_file.read().lower()
    my_file.close()
    files = readFiles(path)

    # create list of queries to go through
    with open('queries.txt', 'r') as f:
        listl = []
        for line in f:
            strip_lines = line.strip()
            listli = strip_lines
            # print(listli)
            m = listl.append(listli)
    arr = listl
    # goes through list of queries and prints out the list
    for i in arr:
        print(i)
        test = WebpagePriorityQueue(files, i)
        test.printQ()


main()
