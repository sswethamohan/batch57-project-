from argparse import _MutuallyExclusiveGroup
import pandas as pd
import mysql.connector
import warnings
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="t_online" 
)
#print(mydb)
#mycursor=mydb.cursor()
def menu():
    print()
    print("\t\t\tTRAIN RESERVATION\t\t\t")
    print("\t\t\t******************\t\t\t")
    print("1. add new passenger details")
    print("2. show all from train details")
    print("3. show all from passenger table")
    print("4. show pnr no.")
    print("5. Reservation of ticket")
    print("6. Cancellation of Reservation")
menu() 

def add_passengers():
    warnings.filterwarnings('ignore')
    mycursor=mydb.cursor()
    list=[]
    name=input("ENTER NAME:")
    list.append(name)
    age=input("ENTER AGE:")
    list.append(age)
    train_no=input("ENTER TRAIN NO:")
    list.append(train_no)
    no_of_pass=input("ENTER NOO. OF PASENGERS:")
    list.append(no_of_pass)
    cls=input("ENTER CLASS:")
    list.append(cls)
    destination=input("ENTER DESTINATION:")
    list.append(destination)
    amount=input("ENTER FARE:")
    list.append(amount)
    status=input("ENTER STATUS:")
    list.append(status)
    rno=input("ENTER RNO:")
    list.append(rno)
    pas=(list)
    sql="insert into pass(name,age,train_no,no_of_pass,class,destination,amount,status,rno) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql,pas)
    mydb.commit()
    print('passenger record inserted')
    df=pd.read_sql("select * from pass",mydb)
    print(df)

def showtrainsdetails():
    warnings.filterwarnings('ignore')
    print("ALL TRAIN DETAILS")
    df=pd.read_sql("select * from train_detail",mydb)
    print(df)

def showpass():        
    warnings.filterwarnings('ignore')
    print("ALL PASSENGER DETAILS")
    df=pd.read_sql("select * from pass",mydb)
    print(df)

def disp_rno():
   warnings.filterwarnings('ignore')
   print("PNR STATUS WINDOW")
   a=float(input("enter train no.:"))
   qry="select name,status from pass where train_no=%s"%(a,)
   df=pd.read_sql(qry,mydb)
   print(df)

def ticketreservation():
    warnings.filterwarnings('ignore')
    print("WE HAVE THE FOLLOWING SEAT TYPESMFOR YOU")
    print("TNAME IS 1 FOR BANAGALORE_EXPRESS FROM DELHI")
    print()
    print("1. FIRST CLASS AC RS/-1000 PER PERSON")
    print("2. SECOND CLASS AC RS/-800 PER PERSON")
    print("1. THIRD CLASS AC RS/-500 PER PERSON")
    print("1. FOR SLEEPER RS/-400 PER PERSON")
    print()
    print("TNAME IS 2 FOR CHENNAI_EXPRESS FROM DELHI")
    print()
    print("1. FIRST CLASS AC RS/-2000 PER PERSON")
    print("2. SECOND CLASS AC RS/-1500 PER PERSON")
    print("1. THIRD CLASS AC RS/-500 PER PERSON")
    print("1. FOR SLEEPER RS/-400 PER PERSON")
    print()

    tname=input("*ENTER YOUR CHOICE OF TRAIN NAME PLEASE*:")
    print(tname)
    x=int(input("ENTER YOUR CHOICE OF TICKET PLEASE:"))
    n=int(input("HOW MANY TICKET YOU NEED:"))
    if(x==1):
        print("you have chosen first class ac ticket")
        s=1000*n
    elif(x==2):
        print("you have to choosen second class ac ticket")
        s=800*n
    elif(x==3):
        print("you have to choosen third class ac ticket")
        s=500*n    
    else:
        print("Invalid option") 
        print("please choose a train")
    print("your total ticket price is =",s,"\n")

def cancel():
    warnings.filterwarnings('ignore')
    print('before any changes in the status')
    df=pd.read_sql("select * from pass",mydb)
    print(df)
    mycursor=mydb.cursor()
    mycursor.execute("update pass set status='cancelled' where rno='21p1'")
    df=pd.read_sql("select * from pass",mydb)
    print(df)

opt=""
opt=int(input("enter your chioce:"))
if opt==1:
    add_passengers()
elif opt==2:
    showtrainsdetails()
elif opt==3:
    showpass()
elif opt==4:
    disp_rno()
elif opt==5:
    ticketreservation()
elif opt==6:
    cancel()    
else:
    print('invalid option')                                        
