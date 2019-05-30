def insertion_sort(dataset):
    for i in range(1, len(dataset)):
        for j in range(i-1, 0, -1):
            print (dataset[j])
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
            else:
                break
    if dataset[0] > dataset[1]:
        temp = dataset[0]
        dataset[0] = dataset[1]
        dataset[1] = temp
 
def main():
    dataset = [12,64,47,9,25]
    print (dataset)
    insertion_sort(dataset)
    print (dataset)
    
 
if __name__ == "__main__":
    main()
