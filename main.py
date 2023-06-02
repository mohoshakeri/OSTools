import readline
from rename import rename_all

print('Choose: ')
print('1. Rename All')
choose = int(input())

if choose == 1:
    path = input('Choose path: \n')
    dir_ch = bool(int(input("1 if dir rename 0 if no: \n")))
    file_ch = bool(int(input("1 if file rename 0 if no: \n")))
    start = input('Enter start str (opt)\n')
    rename_all(path,start,dir_ch,file_ch)
