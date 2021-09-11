from utils import display ,grid_values,grid_values2,eliminate,only_choice,reduce_puzzle, search

display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

# replace . with values that can fits in 
print("improvements of grid value version 2")
display(grid_values2('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

# Apply eliminates to eliminate values from peers  
print("implementation of eliminate functiom ")
display(eliminate(grid_values2('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))

display(only_choice(eliminate( only_choice(eliminate(eliminate( only_choice(eliminate( only_choice(grid_values2('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))))))))))
# it will display the answer 
# 4 8 3 |9 2 1 |6 5 7 
# 9 6 7 |3 4 5 |8 2 1 
# 2 5 1 |8 7 6 |4 9 3 
# ------+------+------
# 5 4 8 |1 3 2 |9 7 6 
# 7 2 9 |5 6 4 |1 3 8 
# 1 3 6 |7 9 8 |2 4 5 
# ------+------+------
# 3 7 2 |6 8 9 |5 1 4 
# 8 1 4 |2 5 3 |7 6 9 
# 6 9 5 |4 1 7 |3 8 2 

# lets make it more easy to do
display(reduce_puzzle(grid_values2('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))

# the harder one which require search solution 

print("hard wa")
display(reduce_puzzle(grid_values2('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))
display(search(grid_values2('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))