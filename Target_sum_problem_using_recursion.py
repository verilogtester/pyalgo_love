# Recursive Pattern for finding subset for the Target sum in a list. 

"""
input is a list i.e. [3,5,7,8,9]
output :
        [[5, 7], [3, 9]]
        

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
    def helper(list1,i,t,m,temp,out):
        #print (temp,m,list1)
        if i == len(list1):
            if t == 0:
                out.append(temp)
                return()
            return()
        
        helper(list1,i+1,t,"LHS",temp,out) 
        helper(list1,i+1,(t-list1[i]),"RHS",temp + [list1[i]],out)
    out = []
    helper(list1,0,12,"top",[],out)
    return out
    
print (target_sum([3,5,7,8,9]))            
            
        


