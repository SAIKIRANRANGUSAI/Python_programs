import re

sai = input("pls enter your password:")

x = True
while x:
    if (len(sai)<6 or len(sai)<13):
        break
    elif not re.search("[A-Z]",sai):
        break
    elif not re.search("[a-z]",sai):
        break
    elif not re.search('[$@#]',sai):
        break
    elif re.search("\s",sai):
        break
    else:
        print("good")
        x = False
        break


if x:
    print("try again ")