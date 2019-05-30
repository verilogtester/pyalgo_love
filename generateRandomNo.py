# Random number generation between 1 to 50 
import random
 
randintl = []
 
while (len(randintl)) != 50:
  rnum = random.randint(1,50)
  if rnum not in randintl:
    randintl.append(rnum)
print (randintl)
