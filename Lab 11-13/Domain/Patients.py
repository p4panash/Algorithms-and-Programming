from datetime import date


class Patients:

    def __init__(self, first_name, last_name, personal_numerical_code, disease):
        self.__disease = disease
        self.__personal_numerical_code = personal_numerical_code
        self.__last_name = last_name
        self.__first_name = first_name

    def setDisease(self, disease):
        self.__disease = disease

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def setPersonalNumericalCode(self, personal_numerical_code):
        self.__personal_numerical_code = personal_numerical_code

    def getDisease(self):
        return self.__disease

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getPersonalNumericalCode(self):
        return self.__personal_numerical_code

    def update(self, first_name, last_name, disease):
        self.__disease = disease
        self.__last_name = last_name
        self.__first_name = first_name

    def getAge(self):
        if self.__personal_numerical_code[0] == '1' or self.__personal_numerical_code[0] == '2':
            birthDate = date(1900 + int(self.__personal_numerical_code[1:3]), int(self.__personal_numerical_code[3:5]),
                             int(self.__personal_numerical_code[5:7]))
            return (date.today() - birthDate).days // 365
        elif self.__personal_numerical_code[0] == '3' or self.__personal_numerical_code[0] == '4':
            birthDate = date(1800 + int(self.__personal_numerical_code[1:3]), int(self.__personal_numerical_code[3:5]),
                             int(self.__personal_numerical_code[5:7]))
            return (date.today() - birthDate).days // 365
        elif self.__personal_numerical_code[0] == '5' or self.__personal_numerical_code[0] == '6':
            birthDate = date(2000 + int(self.__personal_numerical_code[1:3]), int(self.__personal_numerical_code[3:5]),
                             int(self.__personal_numerical_code[5:7]))
            return (date.today() - birthDate).days // 365

    def __str__(self):
        return (str(self.__first_name) + " " + str(self.__last_name) + " " + str(self.__personal_numerical_code) +
                " " + str(self.__disease))
