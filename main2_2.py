first = int(input("enter the first number: "))
second = int(input("enter the second number: "))
third = int(input("enter the third number: "))
if first == second == third :
    print('3')
elif first == second or first == third or second == third :
    print('2')
else: print('0')
