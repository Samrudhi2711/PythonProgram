'''The program takes the number and prints the number of digits in the number.'''
num=int(input("Enter the number ="))
count=0
while(num>0):
    count=count+1
    num=num//10
print("The number of digit in the number are :",count)
