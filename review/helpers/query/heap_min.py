class HeapMin:

    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)


    def heapify(self, index):
        #print(index)
        n = self.size
        if index > (n/2-1) or index<0:
            return

        left_i = 2*index + 1
        right_i = 2*index + 2

        if right_i >=n:
            if self.arr[left_i] < self.arr[index]:
                temp = self.arr[left_i]
                self.arr[left_i] = self.arr[index]
                self.arr[index] = temp
        else:
            if self.arr[index] > self.arr[left_i] or self.arr[index] > self.arr[right_i]:
                #print('ghussa', left_i, right_i, index)
                min_i = left_i
                if self.arr[left_i] > self.arr[right_i]:
                    #print('ghussa', right_i)
                    min_i = right_i
                #print('max_i', max_i)
                temp = self.arr[min_i]
                self.arr[min_i] = self.arr[index]
                self.arr[index] = temp
                self.heapify(min_i)

    def sort(self):
        if self.size==1:
            return
        temp = self.arr[self.size - 1]
        self.arr[self.size - 1] = self.arr[0]
        self.arr[0] = temp
        self.size-=1
        self.heapify(0)
        self.sort()

    def insert(self, val):
        self.arr.append(val)
        self.size+=1
        par = int(int(self.size-2)/2)
        index = self.size - 1

        while(index!=0):
            #print(self.size, par,index)
            if self.arr[par] > self.arr[index]:
                temp = self.arr[par]
                self.arr[par] = self.arr[index]
                self.arr[index] = temp
            temp = index
            index = par
            par = int(int(temp - 1)/2)

    def pop_min(self):
        min_val = self.arr[0]
        self.arr[0]=self.arr[self.size-1]
        self.arr = self.arr[:-1]
        self.size-=1
        self.heapify(0)
        return min_val

    def peek(self):
        return self.arr[0]