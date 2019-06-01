# Recursive Pattern for finding if the list has a target sum out of list or not

"""
input is a list i.e. [3,5,7,8,9]
output :
        True if found
        False if not found

Assumptions: Patten is to have two branches and pass one element as height goes up

                                        ROOT
                                        |
                        -3|t=12					+3|t=9
                       | 						 | 
            -5|t=12      +5| t=7		-5| t=9		+5| t=4
        t=12 | t = 7	|				|			|			|
    -7 ....

"""        

def target_sum(list1):
    def helper(list1,i,t,m):
        print (m)
        if i == len(list1):
            if t == 0:
                return True
            else:
                return False
        
        return helper(list1,i+1,t,"LHS") or helper(list1,i+1,(t-list1[i]), "RHS")
    
    return helper(list1,0,12,"top")
    
print (target_sum([3,5,7,8,9]))
