#fizzbuzz
n=0
while n<=50:
    if n%3 == 0 and n%5 ==0:
        print("FizzBuzz")
    if n%3 == 0 and n%5 !=0:
        print("Fizz")
    if n%5 == 0 and n%3 !=0:
        print("Buzz")
    elif n%3 != 0 and n%5 !=0:
        print(n)
    n += 1
print("Fin del programa")
