"""
Problem : permutation
input: "abc"
output 2! combinations : 
        ['a', 'b', 'c']
        ['a', 'c', 'b']
        ['b', 'a', 'c']
        ['b', 'c', 'a']
        ['c', 'b', 'a']
        ['c', 'a', 'b']

base case - if i == len(s)
generic case - multi branch per size till height size - 1

                ROOT
                  |
         abc	bac		cab
         |		   | 	   |
    abc	  acb  bac	bca cab	bab


In this case:
    Storage: O(n)
    Time : O(n!) - permutation computations 

#############################################
Complexity :
    Typical case Recursion
    -> Storage - linear with size - O(n)
    -> Time - O(2^0 + 2^1 + 2^2 + ...    ...2^n) = O(2^n)
    
    Recursion:
    -> Exhaustive search
    -> Very expensive
#############################################
"""

def permutation(list1):
    def helper(list1,i):
        if i == len(list1)-1:
            print (list1)
            return
        for j in range(i,len(list1)):
            list1[i],list1[j] = list1[j],list1[i]
            helper(list1,i+1)
            list1[i],list1[j] = list1[j],list1[i]
            
    helper(list1,0)

s = "abc"
permutation([c for c in s])


