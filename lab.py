import numpy as np
mat=np.array([[1,2,3],[2,3,4],[5,6,7]])
for row in mat:
    for element in row:
        print(element,end=" ")
    print()
