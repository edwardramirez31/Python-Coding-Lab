dato_tem = input("Escriba la temperatura (e.g., 100c, 34f): ")
li = len(dato_tem)
le = int(li)-1

tem = dato_tem[0:le]

if dato_tem.endswith("c"):
    fahrenheit = (int(tem)*  1.8 + 32)
    print ("{}c es equivalente a {}f".format(tem,fahrenheit))

if dato_tem.endswith("f"):
    cel = (int(tem) - 32) * 5/9;
    print ("{}f es equivalente a {}c".format(tem,cel))
    

