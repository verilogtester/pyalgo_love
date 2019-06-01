# Recursive Pattern for generating subsets

## input pattern : "ab"
## output pattern : ["", "a", "b", "ab"]

#	Recursion tree will look like following for this pattern
#			"ab" [ROOT]
#					|
#			-a			 +a
#			|		      |
#		-b		+b	  -b	+b
# => 	""		"b"		"a"		"ab"
# This pattern is very common for many real time applications

# Assumptions:
# Base Case 
#	if len(str) == i:
#		#add temp to the out
#		return
# Generic Case
# helper(list,i+1, temp,append(list[i]),out) 	# this branch is for append
# helper(list,i+1,temp,out						# this branch is for not to append

# Here, passing string should be avoided, as 
# the string is immutable. better convert string into list, as list is mutable in python

def gen_subset(slist):
    def helper(slist,i,temp,out):
        print (temp)
        if len(slist) == i:
            out.append(temp)
            return()
        else:
            helper(slist,i+1,temp,out)
            # temp.append(slist[i]) 
                # we should not append the temp variable, because 
                # temp.append() modifies the temp variable in-place.
                # Instead we need to pass a copy of temp to the next recursion call. 
            helper(slist,i+1,temp + [slist[i]],out)
                        
    out = []
    helper(slist,0,[],out)
    return out

s = "ab"
print (gen_subset([c for c in s]))

# check below how list append and concatenation affect the value being passed
a = [1,2,3,4]
b = [5]

print (a + b)
a.append(b)
print (a)
