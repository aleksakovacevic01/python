text = """ Chose one optios:
1) Create
2) Read
3) Quit
4) Delete
5) Update
"""

mapa = {}
while True:
    option = input("Input: ")
    if option == '1':
        k = input("Word: ")
        v = input("Meaning: ")
        if k not in mapa:
            mapa[k] = [v]

        else:
            mapa[k].append(v)

    elif option == '2':
        print(mapa)
    elif option == '3':
        print('quit')
        quit()
    elif option == '4':
        rec = input("Input: ")
        if rec in mapa:
            del mapa[rec]
            print("Successfully"+ rec)
        elif rec in mapa:
            del mapa[rec]
    elif option == '5':
        rec = input("Input: ")
        if rec not in mapa:
            print("ERROR")
            continue
        c = mapa[rec]
        print(c)
        for i, e in enumerate(c):
            print(str(i) + ": " + e)
        i = int(input("Enter index to be deleted: "))
        w = input("Enter new value: ")
        c[i] = w
        mapa[rec] = c


