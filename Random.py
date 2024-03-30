import random
# Here we edit the desired size of the matrix:
size = 20
# Random matrix
matrix = [[random.randint(1, 100) for j in range(size)] for i in range(size)]
#Result printed in desired format for greedy.py program:




with open('instance.txt', 'w') as file:
  print(size)
  file.write(str(size) + "\n")
  for y in matrix:
#    print(" ".join(str(x) for x in y))
    file.write(" ".join(str(x) for x in y) + "\n")
