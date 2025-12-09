from All_Sorting_Methods import SortingMethods
import timeit
import copy

class Benchmarking:

    def __init__(self,lst):
        self.lst = lst
        self.sorter = SortingMethods()
        self.results = {}

    
    def benchmark_heap_sort(self):
        arr = copy.deepcopy(self.lst)
        time_taken = timeit.timeit(
            lambda: self.sorter.heapSort(arr),
            number=1
        )
        self.results['Heap Sort'] = time_taken

        return time_taken
    
    def benchmark_merge_sort(self):
        arr = copy.deepcopy(self.lst)
        time_taken = timeit.timeit(
            lambda: self.sorter.MergeSort(arr),
            number = 1
        )
        self.results['Merge Sort'] = time_taken
        return time_taken
    
    def benchmark_quick_sort(self):
        arr = copy.deepcopy(self.lst)
        time_taken=timeit.timeit(
            lambda: self.sorter.QuickSort(arr),
            number=1
        )
        self.results['Quick Sort'] = time_taken
        return time_taken
    
    def benchmark_radix_sort(self):
        arr = copy.deepcopy(self.lst)
        time_taken = timeit.timeit(
            lambda: self.sorter.Radix_sort(arr),
            number = 1
        )
        self.results['Radix Sort'] = time_taken
        return time_taken
    
    def benchmark_shell_sort(self):
        arr = copy.deepcopy(self.lst)
        time_taken = timeit.timeit(
            lambda: self.sorter.shell_sort(arr),
            number=1
        )
        self.results['Shell Sort'] = time_taken
        return time_taken
    
    def run_all_benchmarks(self):
        
        self.benchmark_heap_sort()
        self.benchmark_merge_sort()
        self.benchmark_quick_sort()
        self.benchmark_radix_sort()
        self.benchmark_shell_sort()

        print(self.results)

        return self.results
    
if __name__ == '__main__':
    print("here we gooo")
    k = Benchmarking([12,3,41,5,6,14,211,72,72,5, 34567,1,89,91,8,4,0,279,8,23,74,6])
    k.run_all_benchmarks()






    




