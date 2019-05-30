def insertion_sort(dataset):
    for i in range(1, len(dataset)):
        j = i - 1
        while dataset[j] > dataset[j+1] and j >= 0:
            temp = dataset[j]
            dataset[j] = dataset[j+1]
            dataset[j+1] = temp
            j -= 1
        
def main():
    dataset = [12,64,47,9,25]
    print (dataset)
    insertion_sort(dataset)
    print (dataset)
    
 
if __name__ == "__main__":
    main()
