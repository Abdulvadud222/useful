
# password = input("Please input your password: ")
number = int(input("Enter a number to generate its multiplication table: ")) 
 
for i in range(1, 11): 
     
    row = "" 
 
    
    j = number
    product = i * 1
    product = i * j 
    
    row += f"{product:4}"  # Right-align each entry with width 4 
    
 
    print(row) 
