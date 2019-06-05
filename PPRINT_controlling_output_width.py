data = [ (i, { 'a':'A',
               'b':'B',
               'c':'C',
               'd':'D',
               'e':'E',
               'f':'F',
               'g':'G',
               'h':'H',
               })
         for i in range(3)
         ]

import pprint 

for d in data:
    for c in 'defgh':
        del d[1][c]

for width in [ 80, 20, 5 ]:
    print ('WIDTH =', width)
    pprint.pprint(data, width=width)
   
