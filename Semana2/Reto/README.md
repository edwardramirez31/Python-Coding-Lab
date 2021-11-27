## Coding time!

Algunos consejos para solucionar estos problemas

1. Recuerda que todo software tiene el fin de transformar datos de entrada en datos de salida. Define bien tus inputs y outputs

2. Diseñar el algoritmo en forma de pseudocódigo, dividiendo el problema en pasos pequeños y fáciles de manejar.

3. Traducir ese pseudocódigo a Python.
   - Realizarse preguntas es importante:
     - ¿Cómo obtengo input por parte del usuario?
     - ¿Cómo puedo separar un string "Hola Mundo" por espacios?
     - ¿Cómo puedo obtener una lista de números de 0 a 5?
4. En caso de que haya alguna parte del presudocódigo que no sepa hacer, escribir en Google: `¿Cómo hacer X cosa en Python?`
5. En última instancia, si ya agotó sus recursos y posibilidades, buscar ayuda con alguien (Siempre pueden escribirme). Resuelva los retos de desarrollo en el orden que quiera, lo importante es que vaya resolviendo poco a poco y así ir ganando confianza.

### Iterar y usar condiciones

Escribe un programa en Python para encontrar los números que son que son múltiplos de 5 y 7, entre 1500 y 2700 (ambos incluidos)

### Convertir temperatura

Escriba un programa Python para convertir temperaturas desde grados Celsius a Fahrenheit o al contrario, dependiendo del input del usuario.

> Nota: Si ingresa 35C, el programa debe saber que se debe convertir a Fahrenheit. Si se ingresa 100F, de igual forma, dentro del software se debe intuir la conversión a Celsius

### Adivina el número

Escriba un programa Python para adivinar un número generado aleatoriamente entre 1 y 9.

> Nota: Se le pide al usuario que ingrese un número. Si el usuario adivina mal, el mensaje ("Ingresa un número") vuelve a aparecer hasta que el dato ingresado sea el correcto, en caso de acertar, el usuario obtendrá un "¡Bien adivinado!" como output y el programa saldrá.

### Patrón de caracteres

Escriba un programa en Python para construir el siguiente patrón. (Pista: usar bucle for)

```
*
* *
* * *
* * * *
* * * *
* * * *
* * *
* *
*
```

### Invertir palabras

Escriba un programa Python que acepte una palabra del usuario y la invierta por medio de un bucle

### Pares e impares

Escriba un programa en Python para contar el número de números pares e impares de una serie de números.

> **Datos de entrada:** 1, 2, 3, 4, 5, 6, 7, 8, 9
> **Resultado esperado:**
> Número de números pares: 5
> Número de números impares: 4

### Omitir valores

Escriba un programa Python que imprima todos los números del 0 al 6 excepto el 3 y el 6.

> Resultado esperado: 0 1 2 4 5

### Fibonacci

Escriba un programa para obtener la serie de Fibonacci entre 0 y 50.

> **Nota:** La secuencia de Fibonacci es la serie de números:
> 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
> Por defecto, los dos primeros números son 0 y 1, luego, cada número se encuentra sumando los dos números anteriores.

### Hagamos Fizzbuzz

Escriba un programa que itere en los números enteros del 1 al 50. Para múltiplos de tres, imprima "Fizz" en lugar del número y para los múltiplos de cinco imprima "Buzz". Para números que son múltiplos de tres y cinco, imprima "FizzBuzz". Si ninguna condición se cumple, solo imprima el número.

> **Salida de muestra en consola:**
> fizzbuzz
> 1
> 2
> fizz
> 4
> buzz
> ...

### A contar números binarios

Escriba un programa Python que acepte una secuencia de números binarios de 4 dígitos separados por comas como entrada e imprima los números que son divisibles por 5 en una secuencia separada por comas.

> **Datos de muestra:** 0100,0011,1010,1001,1100,1001
> **Resultado esperado:** 1010
> **Pista:** 1010 en el sistema decimal es 10

### Obtener números y letras

Escriba un programa Python que acepte una cadena y calcule el número de dígitos y letras.

> **Entrada:** "Python 3.2"
> **Salida:** "las letras ingresadas fueron 6 y losdígitos 2"

### Software que valida contraseñas

Escriba un programa Python para verificar la validez de la contraseña ingresada por los usuarios acorde con las siguientes reglas:

- Al menos 1 letra entre `[a-z]` y 1 letra entre `[A-Z]`.
- Al menos 1 número entre `[0-9]`.
- Al menos 1 carácter de `[$ # @]`.
- Longitud mínima 6 caracteres.
- Longitud máxima de 16 caracteres.

### Patrones

- Escriba un programa en Python para imprimir el patrón alfabético 'E'

```
*****
*
*
****
*
*
*****

```

- Escriba un programa en Python para imprimir el patrón de Mario Bros, recibiendo como entrada la cantidad `n` de filas que se desean imprimir

```
   # #
  ## ##
 ### ###
#### ####
```

### Multiplicación con bucles

Escribir un programa que pide un numero al usuario y muestra su tabla de multiplicar (del 1 al 10)

### Obtener el siguiente segundo

Escribe un programa que solicite el tiempo en forma de tres datos (horas, minutos, segundos). El programa calcula y muestra el tiempo un segundo después. Deben manejarse las entradas incorrectas

> Esto no es tan simple como parece ... Mire los siguientes ejemplos:
>
> - 14h17m59s => 14h18m0s
> - 6h59m59s => 7h0m0s
> - 23h59m59s => 0h0m0s

### ¿Cuáles son los valores de las variables al ejecutar el siguiente código?

```python
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
```

Antes de ejecutarlo, trata de adivinar los valores finales de las variables `nb1`, `nb2` and `nb3` acorde con sus valores iniciales. Complete la siguiente tabla.

| Valores iniciales   | Valor final de `nb1` | Valor final de `nb2` | Valor final de `nb3` |
| ------------------- | -------------------- | -------------------- | -------------------- |
| `nb1=nb2=nb3=4`     |                      |                      |                      |
| `nb1=4,nb2=3,nb3=2` |                      |                      |                      |
| `nb1=2,nb2=4,nb3=0` |                      |                      |                      |
