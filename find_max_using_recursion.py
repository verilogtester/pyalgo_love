def find_max(dataset):
    if len(dataset) == 1:
        return dataset[0]
    
    op1 = dataset[0]
    op2 = find_max(dataset[1:])
    
    if op1 > op2:
        return op1
    else:
        return op2
       
def main():
    dataset = [23, 45, 232, 03, 45, 45, 38, 56]
    print(find_max(dataset))
    
 
if __name__ == "__main__":
    main()
