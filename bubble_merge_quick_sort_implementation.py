def bubblesort(dataset):
    for i in range(len(dataset)-1,0,-1):
        for idx in range(i):
            if dataset[idx] > dataset[idx+1]:
                dataset[idx],dataset[idx+1] = dataset[idx+1], dataset[idx]
 
def mergesort(dataset):
    if len(dataset) > 1: #breakdown the array in to single element
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        
        # recursion to break the array 
        mergesort(leftarr)
        mergesort(rightarr)
        
        #index the array
        i=0 # index the left array
        j=0 # index the right array 
        k=0 # index the merged array
        
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1
            
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
 
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1
 
def quicksort(dataset, first, last):
    if first < last: 
        pivotindex = partition(dataset, first, last) #calculate the split point
        #sort the two partiion
        quicksort(dataset, first, pivotindex-1)
        quicksort(dataset, pivotindex+1, last)
        
def partition(dataset, first, last):
    pivotvalue = dataset[first] # chose the first item as pivot element
    lower = first + 1 	# establish the lower index
    upper = last		# establish the upper index
    done = False
    while not done:
        while lower <= upper and dataset[lower] <= pivotvalue:
            lower += 1 #advance the lower index
        while dataset[upper] >= pivotvalue and upper >= lower:
            upper -= 1 #advance the upper index   
        if upper < lower: #if two index crosses, found the split point
            done = True
        else: #exchange the upper and lower index values
            dataset[lower],dataset[upper] = dataset[upper], dataset[lower]
    
    dataset[first],dataset[upper] = dataset[upper], dataset[first] #exchange the pivot vaule
    return upper
 
def main():
    dataset = [23, 8, 16, 90, 2, 1, 92, 20]     
    print ("BUBBLE SORT")
    print ("Orignal dataset", dataset)
    bubblesort(dataset)
    print ("Results :",dataset)
    
    dataset = [23, 8, 16, 90, 2, 1, 92, 20]
    print ("MERGE SORT")
    print ("Orignal dataset", dataset)
    mergesort(dataset)
    print ("Results :",dataset)
    
    dataset = [23, 8, 16, 90, 2, 1, 92, 20]
    print ("QUICK SORT")
    print ("Orignal dataset", dataset)
    quicksort(dataset,0,len(dataset)-1)
    print ("Results :",dataset)
 
if __name__ == "__main__":
    main()
