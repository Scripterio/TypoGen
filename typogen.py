#Takes a password, spits out possible typos
#It does not take into account possible "Shift"errors or CapLock disasters

password = raw_input("Enter password: ")
print password

list0 = "9op-"
list9 = "8io0"
list8 = "7ui9"
list7 = "6yu8"
list6 = "5ty7"
list5 = "4rt6"
list4 = "3er5"
list3 = "2we4"
list2 = "1qw3"
list1 = "`q2"
lista = "qwsz"
listb = "fghn v"
listc = "sdfv x"
listd = "werfvcxs"
liste = "234rfdsw"
listf = "ertgbvcd"
listg = "rtyhnbvf"
listh = "tyujmnbg"
listi = "789olkju"
listj = "yuik,mnh"
listk = "uiol.,mj"
listl = "iop;/.,k"
listm = "hjk, n"
listn = "ghjm b"
listo = "890p;lki"
listp = "90-[';lo"
listq = "12wsa"
listr = "345tgfde"
lists = "qwedcxza"
listt = "456yhgfr"
listu = "678ikjhy"
listv = "dfgb c"
listw = "123edsaq"
listx = "asdc z"
listy = "567ujhgt"
listz = "asx"

my_dict = {'0': list0,
           '9': list9,
           '8': list8,
           '7': list7,
           '6': list6,
           '5': list5,
           '4': list4,
           '3': list3,
           '2': list2,
           '1': list1,
           'a': lista,
           'b': listb,
           'c': listc,
           'd': listd,
           'e': liste,
           'f': listf,
           'g': listg,
           'h': listh,
           'i': listi,
           'j': listj,
           'k': listk,
           'l': listl,
           'm': listm,
           'n': listn,
           'o': listo,
           'p': listp,
           'q': listq,
           'r': listr,
           's': lists,
           't': listt,
           'u': listu,
           'v': listv,
           'w': listw,
           'x': listx,
           'y': listy,
           'z': listz}
x = 0
for c in password:

    typo = list(password)
    for e in my_dict[c]:

        typo[x] = e
        print ''.join(typo)
    x += 1
