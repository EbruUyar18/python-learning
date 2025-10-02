#continue-break-pass

new_list=[10,20,30,40,50,60]
for number in new_list:
    print(number)
    if number==20:
        print("20")
        break

for x in new_list:
    continue
    print("*_*")

for number in new_list:
    if number==40:
        continue
    print(number)

""" pass komutu daha cok kodu geliştirirken geri dönüp bakmak için döngülerde
    bloktan sonra yazılır."""
my_number=list()
for x in my_number:
    pass
