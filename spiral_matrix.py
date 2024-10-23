def spiralOrder(matrix):
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        right_side, down, left_side, up = True, False, False, False

        count = 0
        output = []
        i = 0
        j = 0
        # change to m*n
        while(count < len(matrix)*len(matrix[0])):
            print(i,j)
            # print("top,bottom,left,right",top,bottom,left,right)
            output.append(matrix[i][j])
            count+=1
           
            if right_side:
                j+=1
                if j>right:
                    right_side, down, left_side, up = False, True, False, False
                    print("right_side, down, left_side, up", right_side, down, left_side, up)
                    j = right
                    top +=1
                    i+=1
            elif down:
                i+=1
                if i>bottom:
                    right_side, down, left_side, up = False, False, True, False
                    print("right_side, down, left_side, up", right_side, down, left_side, up)
                    right+=1
                    j-=1
                    i = bottom
            elif left_side:
                j-=1
                if j<left:
                    right_side, down, left_side, up = False, False, False, True
                    print("right_side, down, left_side, up", right_side, down, left_side, up)
                    bottom+=1
                    i-=1
                    j = left
            elif up:
                i-=1
                if i<top:
                    right_side, down, left_side, up = True, False, False, False
                    print("right_side, down, left_side, up", right_side, down, left_side, up)
                    top+=1
                    j+=1
                    i = top

                


            
matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralOrder(matrix)