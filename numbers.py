
#Ask the user to enter three different integers.
print ("This programs needs the user to input 3 values \n")

num1 = input("please enter the 1st number: \n")
num2 = input("please enter the 2nd number: \n")
num3 = input("please enter the 3rd number: \n")

#print The sum of all the numbers
sum = float(num1) + float(num2) + float(num3)
print (f"the sum of the 3 numbers is {sum}")

#Print The first number minus the second numb
diff =float(num1) - float(num2)
print (f"first number minus second number is {diff}")

#The third number multiplied by the first numb
mult =float(num3) * float(num1)
print (f"third number multiplied by first number is {mult}")


#The sum of all three numbers divided by the third number
divided = float(sum) / float (num3)
print (f"sum of 3 numbers divided by third number is {divided}")
