class binaryS(object):
    def binarysearch(self, dataset, item):
        datasize = len(dataset) 
        loweridx = 0
        upperidx = datasize
        while loweridx < upperidx:
            mididx = (loweridx + upperidx) // 2
            if dataset[mididx] == item:
                return item
            if item > dataset[mididx]:
                loweridx = mididx +1
            else:
                upperidx = mididx -1
            
        if loweridx > upperidx:
            return None
  
def main():
    dataset = [1,2,3,4,5,6]
    obj = binaryS()
    print (dataset)
    print (obj.binarysearch(dataset,4))
 
if __name__ == '__main__':
    main()
