import math


def print_matrix( matrix ):
    mat = ""
    for r in matrix:
        row = ""
        for c in r:
            row += str(c) + " "
        mat += row + "\n"
    print mat

def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

def scalar_mult( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c] * s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix(len(m1), len(m2[0]))
    for r in range(len(m1)):
        for c in range(len(m2[0])):
            #print "row = %d, col = %d" % (r,c)
            for x in range(len(m1[0])):
                m3[r][c] += m1[r][x] * m2[x][c]

    for r in range(len(m2)):
        for c in range(len(m2[r])):
            m2[r][c] = m3[r][c]




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
