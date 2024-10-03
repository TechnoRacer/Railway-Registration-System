from pickle import load,dump
import time
import random
import os
import TICKETS as tick
import train
def menu():
    print()
    print("WELCOME TO AKSHAYAN METRO".center(80))
    while True:
        print()
        print("="*80)
        print("\t\t\t\tRAILWAY")
        print()
        print("="*80)
        print()
        print("\t\t\t1.UPDATE TRAIN DETAILS.")
        print()
        print("\t\t\t2.TRAIN DETAILS.")
        print()
        print("\t\t\t3.RESERVATION OF TICKETS.")
        print()
        print("\t\t\t4.CANCELLATION OF TICKETS.")
        print()
        print("\t\t\t5.DISPLAY PNR STATUS.")
        print()
        print("\t\t\t6.QUIT.")
        print("**-office use........")
        ch=int(input("\t\t\tENTER YOUR CHOICE:"))
        os.system('cls')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tLOADING."),time.sleep(1)
        print("."),time.sleep(0.5)
        print("."),time.sleep(2)
        os.system('cls')
        if ch==1:
            j="password"
            r=input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\tENTER THE PASSWORD:")
            os.system('cls')
            if (j==r):
                x='y'
                while (x.lower()=='y'):
                    fout=open("trdetails.dat","ab")
                    traiin=train.getinput()
                    dump(traiin,fout)
                    fout.close()
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\tUPDATING TRAIN LIST PLEASE WAIT ..",time.sleep(1))
                    print(".",time.sleep(0.5))
                    print(".",time.sleep(2))
                    x=input("ADD MORE RECORDS(y OR n):")
                    os.system('cls')
                    continue
            elif(j!=r):
                print("\n\n\n\n\n")
                print("WRONG PASSWORD".center(80))
        elif ch==2:
            fin=open("trdetails.dat",'rb')
            if not fin:
                print("ERROR")
            else:
                try:
                    while True:
                        print("*"*80)
                        print("\t\t\t\tTRAIN DETAILS")
                        print("*"*80)
                        print()
                        train.output()
                        x=input("PRESS ENTER TO EXIT")
                        if x=="":
                            break
                        os.system('cls')
                except:
                    pass
        elif ch==3:
            print('='*80)
            print("\t\t\t\tRESERVATION OF TICKETS")
            print('='*80)
            print()
            tick.reservation()
        elif ch==4:
            print('='*80)
            print("\t\t\t\tCANCELLATION OF TICKETS")
            print()
            print('='*80)
            print()
            tick.cancellation()
        elif ch==5:
            print('='*80)
            print("PNR STATUS".center(80))
            print("="*80)
            print()
            tick.display()
        elif ch==6:
            input("PRESS ENTER TO GO TO TO BACK MENU ")
            os.system('cls')
            print("\t\t\t\t\n\n\n\n\n\tTHANKYOU....")
            print("\n\t\t\tDONE BY:-")
            print("\t\t\t\tAdithya,Jebas,Hari prasath and Sailesh")
            print("\t\t\t\tXII-B")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\tLOADING.."),time.sleep(1)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(2)
            os.system('cls')
            quit()
menu()
            
