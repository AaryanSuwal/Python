num = int(input("Input a number"))

if num <= 1:
    print("Not a prime number")
elif(num == 2 or num == 3):
    print("Is a prime number")
else:
    for i in range(2, num):
        if(num%i == 0):
            print("Not a prime number")
            break
    else:
        print("Prime Number")