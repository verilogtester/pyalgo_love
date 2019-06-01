#Patten 2 - to generate sub set using recursion
# divide the problem into subproblem with the base case and generic case
# base case, if list is empty return emptly list
# generic case, f(list[1:]) + list[0])  

def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])
    print (x)

    return x + [[l[0]] + y for y in x]

print (subs(["a","b"]))
