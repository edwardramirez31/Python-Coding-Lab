#Funciones para el reto 2
#Solo es ejecutar el archivo python reto2.py para que muestre todas las salidas a la vez. La única que no se muestra es la de Fibonacci para no truncar la ejecución.
import random
import re

def findMultiples(init, end):
    multiples = []
    for i in range(init, end):
        if i % 5 == 0 or i % 7 == 0:
            multiples.append(i)
    return multiples

findMultiples()

#Ingresa string y debo saber si lleva F O C, si no detecta niguno decir que esta mal el formato
def convertTemp(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9

convertTemp()

def getRandom(init, end):
    return random.randint(init, end)

getRandom()

def checkRandomNumber():

    print('Ingresa un numero entre 1 y 9')
    num = int(input())
    num_rand = getRandom(1, 9)

    if num == num_rand:
        print('Felicidades, acertaste')
    else:
        print('Intentalo de nuevo')
        checkRandomNumber()

checkRandomNumber()

def getPatron():

    for i in range(5):

        if ( (i >= 4) and (i <= 5) ):

            for j in range(i):
                print('* ', end='')
            print()

            for j in range(i):
                print('* ', end='')
            print()

        else:

            for j in range(i):
                print('* ', end='')
            print()


    for i in range(4, 0, -1):
        for j in range(i):
            print('* ', end='')
        print()

getPatron()

def inverteString(string):
    return string[::-1]

inverteString()

def getWordToInverte():
    word = input('Ingresa una palabra: ')
    print(inverteString(word))

getWordToInverte()

def countParNumbers(list):
    count_par = 0
    count_impar = 0
    for i in list:
        if i % 2 == 0:
            count_par += 1
        else:
            count_impar += 1
    print('Hay {} numeros pares y {} numeros impares'.format(count_par, count_impar))

countParNumbers([1,2,3,4,5,6,7,8,9])

def skipNumber():

    for i in range(7):
        if ( (i != 3) and (i != 6) ):
            print(i)

skipNumber()

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Lo dejo comentado para que no trunque la ejecucion de las demas funciones
#for x in range(50):
#    print(str(x)+' '+ str(fibonacci(x)))

def fizzbuzz():

    for i in range(50):

        if ( (i % 3 == 0) and (i % 5 == 0) ):
            print('FizzBuzz')
        if i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

fizzbuzz()

def bintoint():

    str_list = '0100,0011,1010,1001,1100,1001'
    list = str_list.split(',')

    for i in list:
        if (int(i, 2) % 5 == 0):
            print('{}'.format(i), end=', ')

bintoint()

def countLettersAndDigits(string):

    count_letters = 0
    count_digits = 0

    for i in string:
        if i.isalpha():
            count_letters += 1
        elif i.isdigit():
            count_digits += 1

    print('Hay {} letras y {} digitos'.format(count_letters, count_digits))

countLettersAndDigits()

def validatePassword(password):

    if not re.search('[0-9]', password):
        print("La contraseña debe contener al menos un número")
    elif not re.search('[a-z]', password):
        print("La contraseña debe contener al menos 1 letra minuscula")
    elif not re.search('[A-Z]', password):
        print("La contraseña debe contener al menos 1 letra mayuscula")
    elif len(password) < 6:
        print("La contraseña debe tener al menos 6 caracteres")
    elif len(password) > 16:
        print("La contraseña debe tener menos de 16 caracteres")
    else:
        print("La contraseña es valida")

validatePassword()

def tableMultiples(mult):

    for i in range(1, 11):
        print('{} x {} = {}'.format(i, mult, i*mult))

tableMultiples(2)

def nbTest():
    nb1 = int(input("Enter nb1:"))
    nb2 = int(input("Enter nb2:"))
    nb3 = int(input("Enter nb3:"))

    if nb1 > nb2:
        nb1 = nb3 * 2
    else:
        nb1 = nb1 + 1
        if nb2 > nb3:
            nb1 = nb1 + nb3 * 3
        else:
            nb1 = 0
            nb3 = nb3 * 2 + nb2

    print(nb1, nb2, nb3)

nbTest()