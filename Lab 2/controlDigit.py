def Read():
    return int(input("Introduce n: "))

def ControlDigit(number):
    controlDigit = number
    while controlDigit > 9 :
        aux = controlDigit
        controlDigit = 0
        while aux != 0 :
            controlDigit += aux % 10
            aux = int(aux / 10)
    return controlDigit

def main():
    number = Read()
    print("The control digit of " + str(number) + " is " + str(ControlDigit(number)))

main()