#MIT License
#
#Copyright (c) 2026 9arya
import random
import string
import base64
import sys
def main():
    try:
        LengthOfPassword = 0
        if len(sys.argv) < 2:
            LengthOfPassword += 30
        elif (sys.argv[1]).lower() == "google":
            LengthOfPassword += 100
        else:
            LengthOfPassword += int(sys.argv[1])
        mo=""
        for n in range(LengthOfPassword):
            d=random.choice(string.printable)
            mo+=mo.join(d)
        FirstResult="".join(mo)
        SecondResult = base64.z85encode(FirstResult.encode())
        LastResult=SecondResult.decode()
        print(LastResult[0:LengthOfPassword])
    except (KeyboardInterrupt, EOFError):
        return
if __name__=="__main__":
    main()
#this python script usefull for generate password
#how to use:
#python [NAME_SCRIPT_FILE] [PASSWORD_LENGTH]
#python [NAME_SCRIPT_FILE] [ACCOUNT_TYPE]
#for example:
#python passwd_gen.py 60
