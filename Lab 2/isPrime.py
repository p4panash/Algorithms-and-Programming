def Read():
    return int(input("Introduce n: "))

def sqrt(number):
    i = 1
    while i * i < number :
        i += 1
    if i * i == number :
        return i
    return i - 1

def IsPrime(number):
    if number < 2 :
        return False
    for i in range(2, sqrt(number) + 1) :
        if number % i == 0 :
            return False
    return True

def main():
    number = Read()
    if IsPrime(number) :
        print("Is prime !")
    else :
        print("Is not prime !")

main()