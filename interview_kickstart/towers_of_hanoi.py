def towers_of_hanoi(N):
    def move_discs(n, source, destination, aux):
        if n > 0:
            move_discs(n - 1, source, aux, destination)
            disc = source.pop()
            # print("moving {}th disc to destination".format(disc))
            destination.append(disc)
            move_discs(n - 1, aux, destination, source)
        return

    source = list(range(N))
    destination = []
    aux = []
    move_discs(N, source, destination, aux)
    return destination
