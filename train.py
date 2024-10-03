import os
import pickle
def __init__():
    trainno=0
    no_ofac1stclass=0
    no_ofac2ndclass=0
    no_ofac3rdclass=0
    no_ofsleeper=0
    totalseats=0
    trainname=''
    startingpt=''
    destination=''
def getinput():
    print("="*80)
    print("\t\t\tENTER THE TRAIN DETAILS")
    print()
    print("="*80)
    trainname=input("ENTER THE TRAIN NAME:").upper()
    print()
    trainno=int(input("ENTER THE TRAIN NUMBER:"))
    print()
    no_ofac1stclass=int(input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED:"))
    print()
    no_ofac2ndclass=int(input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED:"))
    print()
    no_ofac3rdclass=int(input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED:"))
    print()
    no_ofsleeper=int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED:"))
    print()
    startingpt=input("ENTER THE STARTING POINT:")
    print()
    destination=input("ENTER THE DESTINATION POINT:")
    trdetails={'trname':trainname,'trno':trainno,'no_ofac1stclass':no_ofac1stclass,'no_ofac2ndclass':no_ofac2ndclass,'no_ofac3rdclass':no_ofac3rdclass,'no_ofsleeper':no_ofsleeper,'startingpt':startingpt,'destination':destination}
    return trdetails
    os.system('cls')
def output():
    fh=open(r"trdetails.dat","rb")
    try:
        while True:
            tr=pickle.load(fh)
            print("="*80)
            print()
            print("THE ENTERED TRAIN NAME IS :",tr['trname'])
            print("THE TRAIN NUMBER ENTERED IS :",tr['trno'])
            print("STARTING POINT ENTERED IS:",tr['startingpt'])
            print("DESTINATION POINT ENTERED IS :",tr['destination'])
            print("NO_OF AC FIRST CLASS SEATS RESERVED ARE :",tr['no_ofac1stclass'])
            print("NO_OF AC SECOND CLASS SEATS RESERVED ARE :",tr['no_ofac2ndclass'])
            print("NO_OF AC THIRD CLASS SEATS RESERVED ARE :",tr['no_ofac3rdclass'])
            print("NO_OF SLEEPER CLASS SEATS RESERVED ARE:",tr['no_ofsleeper'])
            print()
            print("="*80)
    except:
        fh.close
def gettrainname():
    return (trainname)
def gettrainno():
    return (trainno)
def getno_ofac1stclass():
    return(no_ofac1stclass)
def getno_ofac2ndclass():
    return(no_ofac2ndclass)
def getno_ofac3rdclass():
    return(no_ofac3rdclass)
def getno_ofsleeper():
    return(no_ofsleeper)
def getstartingpt():
    return(startingpt)
def getdestination():
    return(destination)

    
