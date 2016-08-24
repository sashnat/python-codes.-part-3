''' «Права доступа» "Permissions"
by Natalia Sashnikova.

В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. 
Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W,
чтение R,
запуск X.
В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. 
В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. 
Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. 
К одному и тому же файлу может быть применено любое колличество запросов.
Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет
возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.

на входе:
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog '''

list = []
list2 = []
n = int(input())
for line in range(n):
    line = input().split()
    line = ['read' if x=='R' else x for x in line]
    line = ['write' if x=='W' else x for x in line]
    line = ['execute' if x=='X' else x for x in line]
    list.append(line)
m = int(input())    
for l in range(m):
    l = input().split()
    l[0], l[1] = l[1], l[0]
    list2.append(l)
for j in range(m):
    for i in range(n):
        if list[i][0] == list2[j][0]:# первый элемент в строке
            if list2[j][1] in list[i][1:]: # от 2 до конца строки
                print('OK')
            if list2[j][1] not in list[i][1:]:
                print('Access denied')
