#usando continue
a = 0

while a < 10:
    a += 1
    if a == 5:#si esto pasa ignora el 5 y continua
        continue 
    print ("La variable llego al valor de", a)
print("fin")