n = 5

def pascTri(numRows):
    # Need to create an array containing numRows # of arrays containing all ones
    tri = [[1]*(i+1) for i in range(numRows)] # [x]*y syntax : https://intellipaat.com/community/63426/how-to-create-a-zero-matrix-without-using-numpy
    # Adding up the two upper numbers to get the lower number (starting at third array bc first two are only ones)
    for i, n in enumerate(tri[2:]): #https://www.quora.com/Why-can%E2%80%99t-you-modify-lists-through-for-in-loops-in-Python#:~:text=You%20can't%20use%20for,like%20without%20affecting%20the%20list.
        # enumerate() function creates a tuple of the index and value
        for j in range(len(n)-2):
            # Current element of array = sum of above array's two elements that "border" it
            n[j+1] = tri[i+1][j] + tri[i+1][j+1]
    return tri
print(pascTri(n))
