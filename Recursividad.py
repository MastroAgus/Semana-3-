def potencia (base,exponente):
    #Calcula la potencia cuando resibe la base y su exponente 
    if exponente == 0:
        return 1
    else:
        return base * potencia (base, exponente - 1)
    
