solve1 = 0
solve2 = 0
from math import*   #libraries
import re 
print("Welcome to a quadratic solver! To solve, you need to enter your equation below in this format with proper spaces: ax + bx + c = 0 and variables must have a 1 beside them not just the variable itself")
print("Put a 0 if there if c is non existent")
while True:
   
    print("")
    quad = input("Enter your quadratic , it only works in this format: 5x^2 - 2x - 9 = 0 (you can change the 0 with any integer)> ")
    scan = quad.split()
   
    try:
            a = int(re.search(r'\d+', scan[0]).group())   #filter our integers for a from the input
            
            
           
            
            if scan[1] == "-":
                num1t = int(re.search(r'\d+', scan[2]).group())         #check for minus signs
                b = -num1t
            else:
                num1t = int(re.search(r'\d+', scan[2]).group())
                b = num1t
            variable = scan[2].replace(str(num1t),"")    
            num2t = int(scan[4])
            if scan[3] == "-":
                
                num2 = -num2t
               
            else:
                num2 = num2t
                
            if scan[6] != "0":
                temp = int(scan[6])
                c = int(num2) + (-temp)
                
                
            else:
                c = num2
           

            print("*" * 100)
            try:
                solve1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)            #solves with quadratic equation
               
            except:
                print("Solution 1 is undefined")            #attempting to divide by zero or an incorrect number is used
            try:
                
                solve2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
                
            except:
                print("Solution 2 is undefined")
            
            
            print(variable,"= ("+str(round(solve1,2))+","+str(round(solve2,2))+")")      #prints out the final answer
          

    except:
            print("You have entered the equation incorrectly")      #if an error occurs
