def torres_de_hanoi(n, origen, destino, auxiliar):
    
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        # Mover n-1 discos de la torre origen a la torre auxiliar usando la torre destino como apoyo
        torres_de_hanoi(n - 1, origen, auxiliar, destino)
        # Mover el disco restante de la torre origen a la torre destino
        print(f"Mover disco {n} de {origen} a {destino}")
        # Mover los n-1 discos de la torre auxiliar a la torre destino usando la torre origen como apoyo
        torres_de_hanoi(n - 1, auxiliar, destino, origen)


