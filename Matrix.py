import random
import operator
## MATRIX CLASS ASSIGNMENT

## TODO
## Implement a helper function to return the dot product of a 1 x n vector and
## an n x 1 vector - i.e. a row and a column.  They must be the same length,
## otherwise the function needs to exit without error.
# def dot( vec1, vec2 ):
#     if len(vec1) != len(vec2):
#         return 0
#     else:
#         dotty = 0
#         for i in vec1:
#             for j in vec2:
#                 dotty += vec1[i] + vec2[j]
#         return dotty







class Matrix(object):

    ## Initialize a Matrix object with an input matrix, stored as a list-of-lists.
    def __init__(self, matrix):
        self.matrix = matrix

        ## TODO
        ## Implement a class attribute to keep track of the matrix values.
        ## This attribute just stores the input data.  Be sure to check that
        ## 'matrix' is a list of lists before setting this value.
        ## REMINDER: set a class attribute by using 'self.attr_name = value'.
        ## TODO
        ## Implement class attributes to keep track of the number of rows and the
        ## number of columns.  You can use these to compare dimensions.

    ## TODO
    ## Implement helper function that returns the i-th row in the matrix.
    ## Should return a list of numbers (e.g. a 1 x m matrix).
    def get_row(self, i):
        return self.matrix[i]

    ## TODO
    ## Implement helper function that returns the j-th column in the matrix.
    ## Should return a list of lists, each of size 1 (e.g. an n x 1 matrix).
    def get_col( self, j ):
        return self.matrix[:][j]
        
         

    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the sum of self and other.
    def addm(self, other):
        #pseudocode :( 
        if len(self.get_row(0)) == len(other.get_row(0)) and len(self.get_col(0)) == len(other.get_col(0)):
            adding = []
            for i in self.matrix:
                for j in other.matrix:
                adding[i][j] = self.matrix[i] + other.matrix[j]
            return adding
        else:
            print("Doesn't work here!")
            return  
    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the difference of self and other.
    def subm(self, other):
        #pseudocode :( 
        if len(self.get_row(0)) == len(other.get_row(0)) and len(self.get_col(0)) == len(other.get_col(0)):
            subbing = []
            for i in self.matrix:
                for j in other.matrix:
                subbing[i][j] = self.matrix[i] + other.matrix[j]
            return subbing
        else:
            print("Doesn't work here!")
            return  
        
    ## TODO
    ## First, check whether other is a scalar or a matrix.
    ## If it is a scalar, return the product other * self.
    ## If it is a Matrix, return the matrix product of self
    ## and other.  This is to be accomplished by using the
    ## dot function defined above.
    # def multm( self, other ):
        
    ## TODO
    ## Return a Matrix that is the transpose of self.
    # def transposem( self ):

def main():
    # matrix_holder, matrix, current_row = [], [], []
    # rows = 0
    # cols = 0
    # rows = int(input("How many rows?"))
    # cols = int(input("How many columns?"))  

    # for i in range(rows):

    #     for j in range(cols):
    #         print("Input value for column ", j , " in row ", i )
    #         current_row.append(int(input("Enter: ")))
    m1 = Matrix([[1,2,3],
                [5,6,7],
                [7,8,9]])
    m1.get_row(0)
    print(m1.get_row(2))
    print(len(m1.get_col(1)))
    
    m2 = Matrix([[1,2,3],[5,6,7],[7,8,9]])

    m1.get_row(0)

            
    
    # if newmatrix >= 1:
    # for i in len(newmatrix):



    # newmatr

main()
