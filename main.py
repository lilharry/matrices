from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print "identity matrix"
identity = new_matrix()
ident(identity)
print_matrix(identity)

print "scalar multiplication (identity matrix * 5)"
scalar_mult(identity,5)
print_matrix(identity)

print "matrix multiplication of m1 and m2\n"
print "m1:"
m1 = new_matrix()
add_point(m1,1,1)
add_point(m1,2,2)
add_point(m1,3,3)
add_point(m1,4,4)
print_matrix(m1)
print "m2:"
m2 = new_matrix()
add_point(m2,0,0)
add_point(m2,1,1)
add_point(m2,2,2)
add_point(m2,3,3)
print_matrix(m2)
print "product:"
matrix_mult(m1,m2)
print_matrix(m2)
#---------------------------------------------------------

#image
for i in range(0,400,5):
	matrix = new_matrix()
	add_edge(matrix,250-i,25+i,0,475-i,250-i,0)
	add_edge(matrix,475-i,250-i,0,250+i,475-i,0)
	add_edge(matrix,250+i,475-i,0,25+i,250+i,0)
	add_edge(matrix,25+i,250+i,0,250-i,25+i,0)
	color = [random.randrange(255),random.randrange(255),random.randrange(255)]
	draw_lines( matrix, screen, color )




display(screen)
