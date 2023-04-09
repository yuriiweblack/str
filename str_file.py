hi = "Hello, I'am" # help
hello = 'Hi, World!'
hello_hi = """\nHi, World!-Hi, World!
 Hi, World!-Hi, World!
 Hi, World!-Hi, World!"""
print(hi+hello+hello_hi)

alphabet = 'abcdefghijklmopqrstuvwxyz'
first_let = alphabet[::3]
print(first_let)
print(len(alphabet))

all_name = input("Input name: ")
print(id(all_name))
all_name_list = all_name.split(',')
print(all_name_list)
info_Dima = all_name_list[0]
info_Vlad = all_name_list[1]
info_Jena = all_name_list[2]
info_Max = all_name_list[3]
# print(info_Max , info_Jena)
address_D = 'Lisinka, 25'
address_V = 'Lisinka, 24'
address_J = 'Lisinka, 23'
addressM = 'Lisinka, 22'

print(f"{info_Dima} live on address {address_D}\n{info_Vlad} live on address {address_V} ")
