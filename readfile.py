from pickle import load
fk={}
fh=open('tickets.dat','rb')
try:
    while True:
        fk=pikle.load(fh)
        print(fk)
except:
    fh.close()
