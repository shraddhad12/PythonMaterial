import heapq

class Heap:

    def __init__(self, size):
        self.customeList = (size+1) * [None]
        self.heap_size = 0
        self.max_size = size+1

    def create_heap(self):
        new_heap = Heap(size=10) # --- time complexity O(1)
        print(new_heap.customeList, new_heap.heap_size, new_heap.max_size) # --- time complexity O(1), space complexity O(N)


    def peakOf_Heap(self):
        if not self:
            return
        else:
            self.customeList[1]  # --- time complexity O(1), space complexity O(1)

    def sizeOfHeap(self):
        if not self:
            return
        else:
            return self.heap_size #---------------------TC O(1) SC O(1)

    def levelOrderTraversal(self):
        if not self:
            return
        else:
            for i in range(1, self.heap_size+1): # ---------------TC O(N) SC O(1)
                print(self.customeList[i], end = " ")

    def heepifyTreeInsert(self, index, heapType):
        if index <= 1:
            return
        parentIndex = int(index/2)
        if heapType == "Min":
            if self.customeList[index] < self.customeList[parentIndex]:
                self.customeList[index], self.customeList[parentIndex] = self.customeList[parentIndex], self.customeList[index]
            self.heepifyTreeInsert(parentIndex, heapType)  # ------------------------------------------TC O(logn N) SC O(logn N)
        elif heapType == "Max":
            if self.customeList[index] > self.customeList[parentIndex]:
                self.customeList[index], self.customeList[parentIndex] = self.customeList[parentIndex], self.customeList[index]
            self.heepifyTreeInsert(parentIndex, heapType)   # ------------------------------------------TC O(logn N) SC O(logn N)

    
    def insertNode(self, value, heapType):
        if (self.heap_size + 1) == self.max_size:
            return "Heap is full"
        self.customeList[self.heap_size+1] = value
        self.heap_size += 1
        self.heepifyTreeInsert(self.heap_size, heapType)  # ------------------------------------------TC O(logn N) SC O(logn N)
        return "The value has been inserted"



new_heap = Heap(10)


new_heap.insertNode(4, "Min")
new_heap.insertNode(5, "Min")
new_heap.insertNode(2, "Min")
new_heap.insertNode(1, "Min")
new_heap.levelOrderTraversal()
