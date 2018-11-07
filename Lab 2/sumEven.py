def Read():
    return int(input("Introduce n: "))

def SumofEvenNumbers(number) :
    sum = 0
    for i in range(2, number + 1, 2) :
        sum += i
    return sum

def main() :
    n = Read()
    print(SumofEvenNumbers(n))

main()