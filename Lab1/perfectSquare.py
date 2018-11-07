def sqrt(number):
    i = 0;
    while (i * i < number):
        i += 1
    return i

number = input("Introduce number: ")
number = int(number)
if (sqrt(number) * sqrt(number) == number):
    print("Perfect square")
else:
    print("Not an perfect square")        
