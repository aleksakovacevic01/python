uslov = ("Izaberi jednu od sledecih naredbi:(0)izlaz, (1)dodaj novu belesku,  (2)procitaj belesku,  (3)promeni belesku, (4)ibrisi")
print(uslov)
l = []
while True:
    messaqe = input("Izaberite jednu od narebni: ")
    if messaqe == '0':
        break
    elif messaqe == '1':
        while True:
            m = {}
            k = input("Unesi naslov: ")
            if k == '1':
                break
            v = input("Unesi novu belesku: ")
            t = input("Unesi prioritet: ")
            if k not in m:
                m[k] = [v]
                m[k].append(t)
            else:
                m[k].append(v)
                m[k].append(t)


            l.append(m)
            print(m)

    elif messaqe == '2':
       print(l)

    elif messaqe == '3':
        print(l)
        rec = input("Unesi rec koju zelis promeniti: ")
        if rec not in m:
            print("Greska")
            continue 
        c = m[rec]
        print(c)
        print("Broj reci" + str(len(c)))
        i = int(input("Unesi broj reci koju zelis promeniti: "))
        w = input("Unesi novu rec: ")
        c[i] = w
        m[rec] = c

    elif messaqe == '4':
        rec = input("Unesi rec koju zelis obrisati: ")
        if rec in m:
            del m[rec]
            print("Uspesno ste izbrisali")

        else:
            print("Greska")