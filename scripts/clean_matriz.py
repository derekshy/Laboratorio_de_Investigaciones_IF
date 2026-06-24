with open("./scripts/matrices.txt", "r", encoding="utf-8") as file:

    content = file.readlines() #guarda el contenido del txt, y se puede iterar linea por linea

    ls = []
    #crea una lista de 30 listas, cada lista contiene la linea i-esima del txt
    for i in range(0,len(content),2):
        ls.append(list(content[i].split()))

    #elimina el x_ 
    for lista in range(len(ls)):
        ls[lista].pop(0)
        
    #cada lista, guarda todos los string del valor que le corresponda
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j] = ls[i][j][ls[i][j].find("=")+1:]
        
    #elimina la "," que habia en los strings, (los ultimos no tenian "," ojo)
    for i in range(len(ls)):
        for k in range(len(ls[i])):
            if "," in ls[i][k]:
                ls[i][k] = ls[i][k][:-1]

    #añade un 0, para el index que corresponda (por ejemplo, el enlace del primero con el primero es 0, y el 2 con el 2 y asi, todos esos son 0, asi que los añade)
    for i in range(len(ls)):
        ls[i].insert(i,0)
    #convierte todos los datos a enteros, los 0 ya lo eran de por si, los demas no
    for i in range(len(ls)):
        for k in range(len(ls[i])):
            ls[i][k] = int(ls[i][k])

    #imprime el resultado listo para pegar
    for i in range(len(ls)):
        print(ls[i], end="")
        if i != len(ls)-1:
            print(",")