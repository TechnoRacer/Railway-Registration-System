from pickle import load,dump
import time
import os
def __init__():
    no_ofac1stclass=0
    totaf=0
    no_ofac2ndclass=0
    no_ofac3rdclass=0
    no_ofsleeper=0
    no_oftickets=0
    name=''
    age=''
    resno=0
    status=''
def ret():
    return(resno)
def retname():
    return(name)
def display():
    f=0
    fin1=open("tickets.dat","rb")
    if not fin1:
        print("ERROR")
    else:
        print()
        n=int(input("ENTER PNR NUMBER:"))
        print("\n\n")
        print("FETCHING DATA ....".center(80))
        time.sleep(1)
        print()
        print("PLEASE WAIT...".center(80))
        time.sleep(1)
        os.system('cls')
    try:
        while True:
            tick=load(fin1)
        if (n==tick['resno']):
            f=1
            print("="*80)
            print("PNR STATUS".center(80))
            print("="*80)
            print()
            print("PASSENGER'S NAME:",tick['name'])
            print()
            print("PASSENGER'S AGE:",tick['age'])
            print()
            print("PNR NO:",tick['resno'])
            print()
            print("STATUS:",tick['status'])
            print()
            print("NO OF SEATS BOOKED:",tick['no_oftickets'])
            print()
    except:
        fin1.close()
        if (f==0):
            print()
            print("WRONG PNR NUMBER ....!!!!!!!")
            print()
def pending ():
    fin1=open("tickets.dat","rb")
    try:
        while True:
            tick=load(fin1)
            status="WAITING LIST"
            print("PNR NUMBER:",tick['resno'])
            print()
            time.sleep(1.2)
            print("STATUS=",tick['status'])
            print()
            print("NO OF SEATS BOOKED:",tick['no_oftickets'])
            print()
            if tick=={}:
                break
    except:
        fin1.close()
def confirmation():
    ststus = "CONFIRMED"
    print("PNR NUMBER:",tick['resno'])
    print()
    time.sleep(1.5)
    print("STATUS :",tick['status'])
    print()
def cancellation():
    z=0
    f=0
    fin=open("tickets.dat","rb")
    fout=open("temp.dat","ab")
    print()
    r=int(input("ENTER PNR NUMBER :"))
    try:
        while True :
            tick=load(fin)
            z=tick.ret()
        if z!=r:
            dump (tick,fout)
        elif z==r:
            f=1
    except:
        pass
        fin.close()
        fout.close()
        os.remove("tickets.dat")
        os.rename("temp.dat","tickets.dat")
        if f==0:
            print()
            print("NO SUCH RESERVATION NUMBER FOUND")
            print()
            time.sleep(2)
            os.system('cls')
        else:
            print()
            print("TICKET CANCELLED")
            print()
def reservation():
    trainno=int(input("WENTER THE TRAIN NUMBER:"))
    z=0
    f=0
    fin2=open("trdetails.dat",'rb')
    fin2.seek(0)
    if not fin2:
        print("ERROR")
    else:
        try:
            while True:
                tr=load(fin2)
                z=tr.gettrainno()
                n=tr.gettrainname()
                if (trainno==z):
                    print()
                    print("TRAIN NAME IS :",n)
                    f=1
                    print()
                    print("-"*80)
                    no_ofac1st=tr.getno_ofac1stclass()
                    no_ofac2nd=tr.getno_ofac2ndclass()
                    no_ofac3rd=tr.getno_ofac3rdclass()
                    no_ofsleeper=tr.getno_ofsleeper()
                    if(f==1):
                        fout1=open("tickets.dat","ab")
                        print()
                        name=input("ENTER THE PASSENGER'S NAME:")
                        print()
                        age=int(input("PASSENGER'S AGE:"))
                        print()
                        print("\t\t SELECT A CLASS YOU WOULD LIKE TO TRAVEL IN :-")
                        print("1.AC FIRST CLASS")
                        print()
                        print("2.AC SECOND CLASS")
                        print()
                        print("3.AC THIRD CLASS")
                        print()
                        print("4.SLEEPER CLASS")
                        print()
                        c=int(input("\t\t\tENTER YOUR CHOICE:"))
                        os.system('cls')
                        amt1=0
                        if (c==1):
                            no_oftickets=int(input("ENTER NO_OF FIRST CLASS AC SEATS TO BE BOOKED:"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=1000*no_oftickets
                                i=i+1
                                print()
                                print("PROCESSING..",time.sleep(0.5))
                                print(".",time.sleep(0.3))
                                print(".")
                                time.sleep(2)
                                os.system('cls')
                                print("TOTAL AMOUNT TO BE PAID=",amt1)
                                resno=random.randint(1000,2546)
                                x=no_ofac1st-totaf
                                print()
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick,fout1)
                                    break
                        elif(c==2):
                            no_ofticktes=int(input("ENTER NO_OF SECOND CLASS AC SEATS TO BE BOOKED :"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=900*no_oftickets
                                i=i+1
                                print()
                                print("PROCESSING..",time.sleeep(0.5))
                                print(".",time.sleep(0.3))
                                print('.',time.sleep(2))
                                os.system('cls')
                                print("TOTAL AMOUT TO BE PAID=",amt1)
                                resno=random.randint(1000,2546)
                                x=no_ofac2nd-totaf
                                print()
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick,fout1)
                                    break
                        elif(c==3):
                            no_oftickets=int(input("ENTER NO_OF THIRD CLASS AC SEATS TO BE BOOKED:"))
                            i=1
                            while(i<=no_oftickets):
                                totaf=totaf+1
                                amt1=800*no_oftickets
                                i=i+1
                                print()
                                print("PROCESSING..",time.sleep(0.5))
                                print(".",time.sleep(0.3))
                                print('.')
                                time.sleep(2)
                                os.system('cls')
                                print("TOTAL AMOUNT TO BE PAID=",amt1)
                                resno=random.randint(1000,2546)
                                x=no_ofac3rd-totaf
                                print()
                                if (x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick,fout1)
                                    break
                        elif(c==4):
                            no_oftickets=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE BOOKED :"))
                            i=1
                            while (i<=no_oftickets):
                                totaf=totaf+1
                                amt1=550*no_oftickets
                                i=i+1
                                print()
                                print("PROCESSING..",time.sleep(0.5))
                                print('.',time.sleep(0.3))
                                print('.')
                                time.sleep(2)
                                os.system('cls')
                                print("TOTAL AMOUNT TO BE PAID=",amt1)
                                resno=random.randint(1000,2546)
                                x=no_oftickets-totaf
                                print()
                                if(x>0):
                                    confirmation()
                                    dump(fout1)
                                    break
                                else:
                                    pending()
                                    dump(tick,fout1)
                                    break
        except:
            pass
            if(f==0):
                time.sleep(2)
                print("\n\n\n\n\n\n\t\t\t\tNO SUCH TRAINS FOUND!!")
                print()
                print()
                print()
                                
                                
