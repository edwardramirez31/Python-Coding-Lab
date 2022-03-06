import random
sorteo = (random.randint(1, 9))
print(sorteo)

while True:
    num = int(input("introduce un numero entre 1 y 9 "))
    if num == sorteo:
        print("felicidades, lo lograste")
        break
print ("hasta pronto")
