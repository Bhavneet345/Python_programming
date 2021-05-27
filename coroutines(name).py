def letter():
    import time
    time.sleep(4)
    l1=[]
    names=[]
    with open("letter.txt") as l:
        for letters in l:
            l1.append(letters)
        for line in l1:
            for name in line.split():
                names.append(name)
    while True:
        naam = (yield)
        if naam in names:
            print(f"Avaliable in letter {l1.index(line)+1}")
        else:
            print("not available")

search=letter()
print("Starting")
next(search)
naam = input("Enter name-")
search.send(naam)
naam =  input("Enter name-")
search.send(naam)
search.close()
