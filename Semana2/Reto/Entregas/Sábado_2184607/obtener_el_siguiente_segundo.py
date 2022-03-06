from datetime import datetime, timedelta

user_input = input("Ingrese el tiempo (ejemplo 14h12m14s)\n")
date = datetime.strptime(user_input, "%Hh%Mm%Ss")
date2 = date + timedelta(seconds=1)
print(date2.strftime('%Hh%Mm%Ss'))
