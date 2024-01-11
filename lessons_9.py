# file=open('text.txt')
# file=open('text.txt','w')
# file=open('text.txt','r+t')

# try:
#     file=open('text.txt')
#     read = file.read ()
#     print (read)
#     file.close()
# finally:
#     file.close()
    
# with open ("text.txt") as filik:
#     rider = filik.read()
#     print (rider)
    
# with open ("text.txt",'w') as filik:
#      filik.write ("gggggg")
#      rider = filik.read()
#      print (rider)
# import os
# print(os.rename())



#Домашнее задание №1
#   Напишите функцию, которая будет открывать заранее созданный тхт файл и выводить 
#   содержимое на экран (тхт файл необходимо создать и наполнить самостоятельно).
def read_file():
    file=open('text.txt')
    read = file.read ()
    print (read)
    file.close()
read_file()

#Домашенее задание №2
# Напишите функцию, 
# которая будет выводить информацию о всех файлах и подкаталогах в произвольной папке на вашем ПК.

def dir_ps():
    import os
    dir_pc= os.listdir()
    print(dir_pc)

dir_ps ()

#Домашенее задание №3
# Написать функцию, которая будет открывать файл №1 
# находить в нем целые числа и записывать их в файл №2 (файл №1 создать самостоятельно).

with open ("text.txt","r") as filik:
    rider = filik.read()
    print (rider)
with open ("text2.txt",'w') as filik2:
    rider1 = rider.split()
    for  i in rider1:
        if i.isdigit():
            i=filik2.write(i + '\n')
with open ("text2.txt","r") as filik:
    rider = filik.read()
    print (rider)