from CircularQueue import *
def main():
    cq = circular_queue()
    print("Tests for the circle queue")
    print(cq.dequeue())
    print(cq.enqueue("a"))
    print(cq.enqueue("b"))
    print(cq.enqueue("c"))
    print(cq.enqueue("d"))
    print(cq.enqueue("e"))
    print(cq.enqueue("f"))
main()
