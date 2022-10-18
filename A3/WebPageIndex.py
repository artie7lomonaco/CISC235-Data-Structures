from AVLTreeMap_fix import *


class WebPageIndex:
    # initialization of the webPageIndex, requires a file
    # as input, then creates the data into a array based list
    def __init__(self, file):
        self.name = file
        my_file = open(file, "r")
        values = my_file.read().lower()
        data = values.split()
        my_file.close()
        arr = []
        self.hello = data
        for i in range(len(data)):
            if data[i] == data[0]:
                arr.append(i)
        self.tree = AVLtree(data[0], arr)
        passedIndexes = [data[0]]
        for i in range(len(data)):
            arr = []
            if data[i] not in passedIndexes:
                for k in range(len(data)):
                    if data[i] == data[k]:
                        arr.append(k)
                # print("value",data[i],", indexes:",arr)
                self.tree.put(data[i], arr)
                passedIndexes.append(data[i])

    # function that gets the name of wpi (for use in 1.3)
    def getName(self):
        return self.name

    # getCount function, parameters are string s,
    # goes through whole of the array of values,
    # whenn values equal to s, adds indexes of
    # values to indexHolder array list
    def getCount(self, s):
        if self.tree.search(s, self.tree.root):
            return int(len(self.tree.get(s)))
        else:
            return 0

    # getCount but for a list, which will be a string of mutliple
    # words that gets split, used for the next question (1.2) for
    # the cases with multiple word quieries
    def qGetCount(self, s):
        result = 0
        for i in s:
            result = result + self.getCount(i)
        return int(result)


# testing code
if __name__ == "__main__":
    # Testing for word graph
    test1 = WebPageIndex("data/doc4-stack.txt")
    test2 = WebPageIndex("data/doc9-hashtable.txt")
    print(test1.getCount('structure'))
    print(test1.qGetCount(["bing","an"]))
