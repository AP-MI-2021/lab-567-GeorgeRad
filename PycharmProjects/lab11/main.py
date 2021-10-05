def is_prime(n):
    '''
    Returneaza true daca n este prim
    :param n: intreg
    :return: True sau False
    '''
    if n == 2:
        return True
    elif n == 0 or n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3 , n // 2 + 1 , 2):
            if n % i == 0:
                return False
    return True

def get_product(n):
    '''
    Returneaza produsul numerelor din lista lst
    :param n: numar intreg
    :return: p
    '''
    lista = []
    p = 1
    for i in range(n):
        lista.append(int(input()))
    for i in range(n):
        p = p * lista[i]
    return p

def get_cmmdc_v1(x , y):
    '''
    Returneaza CMMDC a doua numere x si y folosind primul algoritm
    :param x: numar intreg
    :param y: numar intreg
    :return: x
    '''
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def get_cmmdc_v2(x , y):
    '''
    Returneaza CMMDC a doua numere x si y folosind al doilea algroitm
    :param x: numar intreg
    :param y: numar intreg
    :return: x
    '''
    while y != 0:
       r = x % y
       x = y
       y = r
    return x
assert is_prime(2) is True
assert is_prime(1) is False
assert is_prime(4) is False
assert is_prime(5) is True
assert get_cmmdc_v2(12 , 24) == 12
assert get_cmmdc_v1(12 , 24) == 12

def menu():
    print("1.Sa se stabileasca daca un numar n este prim sau nu")
    print("2.Sa se calculeze produsul a n numere naturale")
    print("3.Sa se calculeze CMMDC a 2 numere folosind primul algoritm")
    print("4.Sa se calculeze CMMDC a 2 numere folosind al doilea algoritm")

menu()
option = int(input("Introduceti optiunea dumneavoastra: "))

while option != 0:
    if option == 1:
        n = int(input("Introduceti numarul n = "))
        if is_prime(n) is True:
            print("Numarul este prim")
        else:
            print("Numarul introdus nu este prim")
    elif option == 2:
        n = int(input("Introduceti numarul elementelor n = "))
        print("Introduceti elementele multimii: ")
        print("Rezultatul inmultirii este: " , get_product(n))
    elif option == 3:
        a = int(input("a = "))
        b = int(input("b = "))
        print("CMMDC-ul lui a si b este: " , get_cmmdc_v1(a ,b))
    elif option == 4:
        a = int(input("a = "))
        b = int(input("b = "))
        print("CMMDC-ul lui a si b este:" , get_cmmdc_v2(a , b))
    elif option != 0:
        print()
        print("Ne pare rau dar optiunea introdusa nu exitsa")
        print("Va rugam introduceti o optiune existenta!")

    print()
    menu()
    option = int(input("Introduceti optiunea dumneavoastra: "))



