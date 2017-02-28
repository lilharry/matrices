from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_point(matrix,1,2)
add_point(matrix,1,4)
add_point(matrix,1,3)
add_point(matrix,1,5)
add_point(matrix,1,2)
print(matrix)

draw_lines( matrix, screen, color )
display(screen)
