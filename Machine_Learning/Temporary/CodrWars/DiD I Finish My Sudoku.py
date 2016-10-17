#https://www.codewars.com/kata/did-i-finish-my-sudoku/train/python
import numpy as np

A=[[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]


A= np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [2, 3, 4, 5, 6, 7, 8, 9, 1],
             [3, 4, 5, 6, 7, 8, 9, 1, 2],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [5, 6, 7, 8, 9, 1, 2, 3, 4],
             [6, 7, 8, 9, 1, 2, 3, 4, 5],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [8, 9, 1, 2, 3, 4, 5, 6, 7],
             [9, 1, 2, 3, 4, 5, 6, 7, 8]])

#print (type(A))

#print (A[0:3,:3])
i=1
#print (A[i+0:i+3,:3])



def check_regions(board):
    for j in range(0,7):
        print ("printing when  J= {}".format(j))
        for i in range(0,7):
            print (A[j:i+j+3,:3])

check_regions(A)


def done_or_not(board): #board[i][j]
    A= sum([x for x in range(1,10)])
    print (A)
    sum_row=np.sum(board,axis=0)
    sum_column=np.sum(board,axis=1)
    if check_regions(board)==False:
        return 'Try again!'

    for i in range(9):
        if len(np.unique(board[i]))<9:
            return 'Try again!'
        if len(np.unique(board[i][:]))<9:
            return 'Try again!'



        if len(np.unique(sum_column))==1 and len(np.unique(sum_row))==1 :
            if sum_column[0]==A and sum_row[0]==A:
                return 'Finished'
            else :
                return 'Try again!'
        else:
             return  'Try again!'



#print (done_or_not(A))


# your solution here
  # ..
  # return 'Finished!'
  # ..
  # or return 'Try again!'