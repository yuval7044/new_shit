clients_dict = {"bla": "key", "bla1": "1"}

def dict_value(dict, addr): #print the place of speceific value in dict
    for value in enumerate(dict.keys()):
        if value == addr:
            print(value)
            return

def dict_keys(dict, client): #print the place of speceific key in dict
    for name in dict:
        if name == client:
            return len(client)


for value in enumerate(clients_dict.values()):
    if value == "key":
        print(value)