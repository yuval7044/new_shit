import requests
import re

def Challenge_1(string):
    for letter in string:
        if ord(letter) >= 97 and ord(letter) <= 120:
            new_letter = ord(letter) + 2
            print (chr(new_letter), end ="")
        elif ord(letter) == 121:
            print("a", end ="")
        elif ord(letter) == 122:
            print("b", end ="")
        elif ord(letter) == 32:
            print (" ", end ="")

def Challenge_2(Gbrish):
    for letter in Gbrish:
        if ord(letter) >= 97 and ord(letter) <= 122:
            print (letter, end="")

def Big_letter(letter):
    return letter >= 'A' and letter <= 'Z'

def small_letter(letter):
    return letter >= 'a' and letter <= 'z'

def Challenge_3(Big_string):
    for letter in range(len(Big_string)):
        if small_letter(Big_string[letter]):
            if Big_letter(Big_string[letter + 1]):
                if Big_letter(Big_string[letter + 2]):
                    if Big_letter(Big_string[letter + 3]):
                        if small_letter(Big_string[letter + 4]):
                            if Big_letter(Big_string[letter + 5]):
                                if Big_letter(Big_string[letter + 6]):
                                    if Big_letter(Big_string[letter + 7]):
                                        if small_letter(Big_string[letter + 8]):
                                            print(Big_string[letter + 4], end="")

def numbers_link(link):
    string = ''
    bla = requests.get(link)
    working = re.findall("^and the next nothing is", bla.text)
    if working:
        print("yes")
        for letter in bla.text:
            if letter >= '0' and letter <= '9':
                string = string[0:] + letter
    else:
        print("No")
    return string
link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=93781"
new_code = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
new_thing = numbers_link(link)
for number in range(10):
    new_link = str(new_code) + str(new_thing)
    link = new_link
    new_thing = numbers_link(link)
    print (new_thing)


