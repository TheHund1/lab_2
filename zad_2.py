
def zad_2a(five_names_list):
    for i in five_names_list:
        print(i)
def zad_2bV1(five_numbers_list):
    for i in range(len(five_numbers_list)):
        five_numbers_list[i] = five_numbers_list[i]*2
    print(five_numbers_list)
def zad_2bV2(five_numbers_list):
    five_numbers_list = [number * 2 for number in five_numbers_list]
    print(five_numbers_list)
def zad_2c(c):
    for i in c:
        if(i%2 == 0):
            print(i)
def zad_2d(d):
    isEverySecond = True
    for i in d:
        if(isEverySecond):
            print(i)
            isEverySecond = False
        else: isEverySecond = True
a = [item for item in range(0, 10)]
zad_2d(a)
print()