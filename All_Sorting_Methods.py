class SortingMethods : 
    def __init__(self):
        pass

    #All Sorting Methods are explained in individual Notebooks 

    # HEAP SORT 

    def swap(self ,lst , i , j):
        lst[i],lst[j] = lst[j],lst[i]

    def siftDown(self ,lst,i,upper):
        while True :
            l,r = i*2+1 , i*2+2
            if max(l,r)<upper :
                if max(lst[l],lst[r]) < lst[i] : break
                elif lst[r] > lst[l]:
                    self.swap(lst,r,i)
                    i=r
                else :
                    self.swap(lst,l,i)
                    i=l

            elif l<upper :
                if lst[l]>lst[i] :
                    self.swap(lst,i,l)
                    i=l
                else :
                    break
            

            else : break


    def heapSort(self ,lst):
        for i in range((len(lst)-2)//2,-1,-1) :
            self.siftDown(lst,i,len(lst))

        for j in range(len(lst)-1,0,-1):
            self.swap(lst,0,j)
            self.siftDown(lst,0,j)


#        MERGE SORT
    
    def MergeSort(self,data):
        if len(data)>1 :
            middle = len(data)//2
            left = data[:middle]
            right=data[middle:]

            self.MergeSort(right)
            self.MergeSort(left )
            

            i=j=k=0

            while i< len(left) and j <len(right) :
                if left[i]<right[j] :
                    data[k]=left[i]
                    i=i+1
                    k=k+1
                else :
                    data[k]=right[j]
                    j=j+1
                    k=k+1
            
            while i< len(left) :
                data[k] = left[i]
                k=k+1
                i=i+1
            
            while j< len(right) :
                data[k] = right[j]
                k=k+1
                j=j+1


#                                             QUICK SORT
#                 here i use the QuickSort with Functional/Non-In-Place Approach   there are other versions or options available see the notebook of QuickSort to learn more


    def QuickSort(self ,arr) : 
        if len(arr)<=1 :
            return arr
        else :
            pivot = arr[len(arr)//2]
            middle = [x for x in arr if x==pivot]
            left = [x for x in arr if x < pivot ]
            right = [x for x in arr if x> pivot]

            return self.QuickSort(left)+ middle + self.QuickSort(right)
        

    #                                    RADIX SORT
    
    def counting_sort(self , arr,exp):
        n = len(arr)
        output = [0]*n
        count = [0]*10

        for i in range(n) : 
            index = (arr[i]//exp) % 10
            count[index] = count[index]+1

        for i in range(1,10) :
            count[i] = count[i]+ count[i-1]

        for i in range(n-1 , -1, -1) :#stability
            index = (arr[i]//exp) % 10
            output[count[index]-1] = arr[i]
            count[index] = count[index] -1

        for i in range(n):
            arr[i] = output[i]

            

    def Radix_sort(self,arr):
        maxi = max(arr)
        exp = 1
        while (maxi // exp) > 0:
            self.counting_sort(arr,exp)
            exp = exp*10

    
#                 SHELL SORT
        
    def shell_sort(self,arr):
        n = len(arr)
        gap = n // 2  
        
        while gap > 0:
           
            for i in range(gap, n):
                temp = arr[i]
                j = i

                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp
            gap //= 2

        





    
