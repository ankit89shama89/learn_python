num = int(input("Enter the number to check: "))
check = range(2,(num -1))

if num > 2:
    for i in range(2,(num -1)):
        if num % i == 0:
            print(num, " is not a prime number")
            break
    else:
        print(num, " is a prime number")
elif num == 1:
    print(num, " is not a prime number")
elif num == 2:
    print(num, " is a prime number")


