while True:
    num = int(input("Enter a number to check if it is prime or not :"))
    for j in range(2,num):
        if num%j == 0:
            print("Not a prime")
            break
    else:
        print("Prime")