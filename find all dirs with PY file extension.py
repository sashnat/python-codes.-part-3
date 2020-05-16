#Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".

import os
st = r'.\New Folder\\'
def out(x, y):
    l = set(d for d, dir, files in os.walk(x) for file in files if y in file)
    for i in sorted(list(l)):
        print(i.replace(st, ''))
m, n = st,".py"
out (m, n)
