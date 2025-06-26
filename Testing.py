import subprocess
bla = {'yuval': 123123, 'gal' : 213123, 'harel': 1232132}
x = 0
namewanted = "harel"
for name in bla.keys():
    x = x + 1


bla = subprocess.getoutput("ping 8.8.8.8")
print(bla)