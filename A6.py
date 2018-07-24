#Importing NumPy as np
import numpy as np

#Function that takes an input vector and a boolean argument to constuct Vandermonde matrix

def ATV_mat(vect,increasing):
    N = len(vect)
    if increasing.upper() == 'FALSE':#if the increasing is False

        #the powers decrease from left to right
        van_mat = np.column_stack([vect**(N-1-i) for i in range(N)])

    else:#if the increasing is True

        #the powers increase from left to right
        van_mat = np.column_stack([vect**(i) for i in range(N)])

    return van_mat

x = np.array([1,2,3,4,5])
y = 'true'
print(ATV_mat(x,y))
