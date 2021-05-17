if __name__ == '__main__' :
    lista = []

    with open("recommendations.tsv", "r") as resFile:
        for line in resFile:
            artwork = str(line.split("\t")[0])
            if artwork not in lista:
                lista.append(artwork)
    
    i = len(lista)
    print("\n\nOVERALL\n"+str(i)+" artworks involved by recommendation\n")
