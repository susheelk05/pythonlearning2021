# write first 100 odd numbers 1 3 5 7 9.....



count = 0
for x in range(1,200):
    if x%2 == 1:
        print(x)
        count = count+1
        if count == 100:
            break
