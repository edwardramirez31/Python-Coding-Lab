#Mario Bros
n= int(input("Ingrese el número de filas que desea obter: "))
for i in range (0,n+1):
    ecuacion= i*"#" + " " + i*"#"
    print("{:^20}".format(ecuacion))
