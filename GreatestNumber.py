numbers = [1,2,3,4,5,6,7,8] #declare the numbers you want
max = numbers[0] #lets assume the "0" index number to be the greatest
for num in numbers: #getting the items from the list
    if num > max: #checks if number is greater than max
        max = num #returns the value of the number greater than the maximum and sets the max to the number
else:
    print(max) #when the loop reaches the greatest number else statement prints it out