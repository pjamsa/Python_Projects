class Password: #new clas
    def __init__(self):
        self._PasswordVar = 2034 #single underscore = Protected Var

    def __init__(self):
        self.__PasswordVar = 5998 # double underscore = Private Var

Pin = Password()
Pin._PasswordVar = 9402 #changing protected Pin
print(Pin._PasswordVar)

Pin = Password()
Pin.__PasswordVar = 3902 # changing private pin
print(Pin.__PasswordVar)
