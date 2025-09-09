def matrix_bsearch(matrix,in_which_row,target):
    l = 0
    r = len(matrix[in_which_row])-1

    while l <= r:
        mid = (l+r)//2
        if matrix[in_which_row][mid]==target:
            return True
        elif matrix[in_which_row][mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False
def find_row(matrix,target):
    l = 0
    r = len(matrix)-1
    while l<=r:
        mid = (l+r)//2
        if target > matrix[mid][-1]:
            l = mid + 1
        else:
            r = mid - 1
    return l
def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 7
    if target > matrix[-1][-1]:
        print(False)
        return
    #last_column = []
    #for i in range(len(matrix)): #row in matrix
        #last_column.append(matrix[i][-1])
    
    in_which_row = find_row(matrix,target)
    print(in_which_row)
    

    found = matrix_bsearch(matrix,in_which_row,target)
    print(found)
main()

