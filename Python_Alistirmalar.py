text = "The goal is to turn data into information, and information into insight"
text.upper().split()

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0]
lst[10]
new_lst = lst[0:4]
lst.pop(8)
lst.append("R")
lst.insert(8, "N")

dict = {'Christian': ["Amerika", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
dict.keys()
dict.values()
dict["Daisy"] = ["England", 13]
dict["Ahmet"] = ["Turkey", 24]
dict.pop("Antonio")

l = [2, 13, 18, 93, 22]


def func(list):
    tek = []
    cift = []

    for i in list:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return tek, cift


tek, cift = func(l)

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i in enumerate(ogrenciler, 1):
    if i[0]<=3:
        print(f"Mühendislik Fakültesi  {i[0]} . ogrenci : {i[1]}")

    else:
        print(f"Tıp Fakültesi  {i[0]-3} . ogrenci : {i[1]}")



ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
a = list(zip(ders_kodu,kredi,kontenjan))
for i in a:
    print(f"Kredisi {i[1]} olan {i[0]} kodlu dersin kontenjanı {i[2]} kişidir.")

kume1 = set(["data","python",])
kume2 = set(["data","function","qcut","lambda","python","miuul"])
kume1.issuperset(kume2)
kume2-kume1
kume2.difference(kume1)
kume2.intersection(kume1)
