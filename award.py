

#Ask the user to enter times for the 3 events in a triathlon.
print ("This programs needs the user to input 3 triathlon times in minutes \n")

swimming = input("please enter the swim time in minutes: \n")
cycling = input("please enter the cycling time in minutes: \n")
running = input("please enter the running time in minutes: \n")

#print The total triathlon time
sum = int(swimming) + int(cycling) + int(running)
print (f"the total time taken for the triathlon is {sum}")

# decide the awards to be granted based on the time divided into 4 categories
#if less than or equal to 100 minutes then grant honorary colors
if sum <=100 : 
    print ("You receive honorary colors")
#if less than or equal to 105 minutes and more than 100 
# then grant honorary half colors
elif sum <=105 :
    print ("You receive honorary half colors")
#if less than or equal to 110 minutes and more than 105 
# then grant honorary scroll
elif sum <=110 :
    print ("You receive honorary scroll")
#if more than 111 minutes no award is granted       
else:
    print ("your time was greater than 111 minutes, no award")