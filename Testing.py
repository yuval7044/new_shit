c = {"yuval": "21.213.124.1","gal": "1231245 123 21312"}
print(len(c))
names = c.keys()
sockets = c.values()
count = 1
for name in names:
    if name == "gal":
        print(count)
    else:
        count = count + 1

for nu