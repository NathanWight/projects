







import math
size = int(input("How many columns and rows do you want in your multiplication table? "))
size = size + 1

for row_num in range(1,size):
    for column_num in range(1, size):
      product = row_num * column_num
      print(f"{product:3}", end="")
    print("")
    
    
   