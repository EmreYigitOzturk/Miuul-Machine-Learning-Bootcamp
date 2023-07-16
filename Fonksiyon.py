def multi(a, b):
    """
    iki sayiyi carpar
    :param a: int,float
    :param b: int,float
    :return: int or float
    """
    print(a + b)


multi(5, 6)


def square(a):
    return a ** 2


square(2)

if 1 == 1:
    print("say hello :D")

a = input("bir metin giriniz: ")

def func(string):
    new_string = ""
    for i in range(len(string)):
        if(i % 2 == 0):
           new_string += string[i].upper()
        else:
            new_string += string[i]
    return new_string

print(func(a))


import seaborn as sns
a = sns.load_dataset("car_crashes")
a.columns = [column.upper() for column in a.columns ]

