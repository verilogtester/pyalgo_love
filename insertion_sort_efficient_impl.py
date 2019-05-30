# we reduced the numbers of swap operations and doing swap only when the right location is found for the number in the sort order.
def insertion_sort(dataset):
    for i in range(1, len(dataset)):
        curNum = dataset[i]
        for j in range(i-1,-1,-1):
            if dataset[j] > curNum:
                dataset[j+1] = dataset[j]
            else:
                dataset[j+1] = curNum
                break
            dataset[j] = curNum
                                  
def main():
    dataset = [8,64,18,88,1,90,12,47,9,25]
    print (dataset)
    insertion_sort(dataset)
    print (dataset)
    
 
if __name__ == "__main__":
    main()
