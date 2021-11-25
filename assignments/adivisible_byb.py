
def div_ab(a,b):
    if a % b == 0:
        print("%s is divisible by %s" %(a,b))
    else:
        print("{0} is not divisible by {1}".format(a,b))

while True:

    x = int(input("enter a:"))
    y = int(input("enter b:"))
    div_ab(x,y)



