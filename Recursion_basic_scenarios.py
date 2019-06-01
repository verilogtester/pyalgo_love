# Recursive Pattern for Sum()
## Base case (aka breaking condition)
## Generic Case L[i] + Sum_list(L[i-1])

print ('### Recursion passing index - Sum of list)###')

def sum_list(list1):
    def helper(list1,i):
        if len(list1) == i: # base case (breaking condition)
            return 0
        else:
            return list1[i] + helper(list1,i+1) # Generic case function
    return helper(list1,0)

list1 = [1,3,5]
print (sum_list(list1))

print ('\t ### END ###\n\n')

print ('### Recursion passing list - Reverse string)###')
# base case (aka breaking condition) - if len(str) is 0 then return ''
# generic case - f(s[1:]) + s[0]

def reverse_str(stlist):
    def helper(stlist):
        if len(stlist) == 0: # base case (breaking condition )
            return ""
        return helper(stlist[1:]) + stlist[0] # generic case function 
    return helper(stlist)

string1 = "arbind rohilla"
print ("Input string: ", string1)
print ("output string:", reverse_str([c for c in string1]))

print ('\t ### END ###\n\n')

print ('### input = abcde, output = deabc)###')
# use reverse function wrote above to do this operation

k = 2 # define circular rotation here 
print ('defined circular rotation: {}'.format(k))
string1 = "abcde"
print ("Input string: ", string1)
s1 = reverse_str("abcde")
s2 = reverse_str(s1[:k]) + reverse_str(s1[k:])
print ("output string: ",s2)

print ('\t ### END ###')
