import re
f1 = open('access.log','r')
s = []
ips = []
for line in f1.readlines():
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
    seti = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.', str(ip))
    for i in seti:
        if i in s:
            pass
        else:
            s.append(i)
    for i in ip:
        if i in ips:
            pass
        else:
            ips.append(i)
s.sort()
for x in s:
    print("Подсеть: ",x)
    for j in ips:
        if j.startswith(x):
            print(j)
