# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix: list[list[int]]) -> list[int]:
        rstart = 0
        rend = len(matrix)-1
        cstart, cend = 0, len(matrix[0])-1

        output = []
        while(rstart <= rend and cstart<= cend):
            for col in range(cstart, cend+1):
                output.append(matrix[rstart][col])
            rstart = rstart + 1
            for row in range(rstart,rend+1):
                output.append(matrix[row][cend])
            cend = cend -1
            if rstart<=rend:
                for col in range(cend, cstart-1, -1):
                    output.append(matrix[rend][col])
                rend = rend - 1
            if cstart <= cend:
                for row in range(rend,rstart-1, -1):
                    output.append(matrix[row][cstart])
                cstart = cstart + 1
        return output

spiralOrder([[1]])

