import random as r
def easypass(input):
    harflerkolay="1234567890"
    sifre="".join(r.sample(harflerkolay,input))
    return sifre

def medipass(input):
    harflerorta="abcdefghijklmnoprstuvyz1234567890"
    sifre="".join(r.sample(harflerorta,input))
    return sifre

def hardpass(input):
    harflerzor="abcdefghijklmnoprstuvyzwx1234567890ABCDEFGHIJKLMNOPRSTUVYZWX.,"
    sifre="".join(r.sample(harflerzor,input))
    return sifre

def impasibpass(input):
    harflerimkansiz = " abcdefghijklmnoprstuvyzwx1234567890ABCDEFGHIJKLMNOPRSTUVYZWX!'^+%&/()=?-_"
    sifre="".join(r.sample(harflerimkansiz,input))
    return sifre

print("Hi, Welcome to Password Creator \n Fistly, write length of password later choose password comlexty.")
passrange=int(input("Password length: "))
secim=int(input(" 1- Just numbers \n 2- lower letters and numbers \n 3- dot, lower/upper letters and numbers \n 4- specific characters, lower/upper letters and numbers \n 0- EXIT\n : "))
if secim== 1:
    print(easypass(passrange))
elif secim==2:
    print(medipass(passrange))
elif secim==3:
    print(hardpass(passrange))
elif secim==4:
    print(impasibpass(passrange))
elif secim==0:
    print("You Exited")
