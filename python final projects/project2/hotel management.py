from msilib.schema import ODBCAttribute
from select import select
import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="sHj@6378#jw",
  database="hotel_M" 
)
#print(mydb)
mycursor=mydb.cursor()
#hotel management
print("\t\tHOTEL MANAGEMENT\t\t")
print("\t\t*****************\t\t")
print("WELCOME ABC HOTEL")
print("***************")
#introduce our hotel 
print("since:2002-2022")
print("our management is 20 years old to running successfully with our love and support")
print("our management is too good for quality")
print("And  amount quantity will be variable for you")
print("**Take your seat sir/mam**")
print("**what do you want sir/mam**")
#menu card#BUY ONE GET ONE 
    #OFFERS:
print("________________________________________________________________")
print("***GRAND OPENING OFFER***")
print("***only for/- 17,18,19.9.22")
fr=["1.biriyani+biriyani","2.biriyani+chilly_65","3.biriyani+chilly_65+cooldrinks"]
print(fr)
user=int(input("enter your offer 1,2,or 3:"))
if user==1:
  print("enjoy your buy one get one offer")
elif user==2:
  print("receive your food and enjoy")
elif user==3:
  print("your combo offer")
  print("enjoy :)")  
else:
  print("not in offer")   
print("_________________________________________________________________")              
print("#MENU CARD#")
print("^^^^^^^^^^^")  
mycursor.execute("select * from customer")
result=mycursor.fetchall()
for i in result:
    print(i)
#for i in result:
    #print(i)    
    #choose the order
avaliables=["online_order","home_parsel","table_place"]
print(avaliables)
user=input("it is available:")
     #ONLINE ORDER
if user=="online_order":
  print("you can order this number:5154784")
  op=input("enter your address:")
  print("**you can choose your order please**")
  print("**With in one hour your order will delivered")
  list=["1.chicken_biriyani","2.mutton_biriyani","3.aloo_gobi_masala","4.pannerbuttermasala","5.pannercurry","6.malai_kofta","7.mutterpanner","8.mix_veg","9.kaju_curry","10.aloo_tomato"]
  print(list)
  order=(input("your order pls:"))
  if order=="chicken_biriyani":
    print(f"your order {order} in menu")
  elif order=="mutton_biriyani":
    print(f"your order {order} in menu")
  elif order=="aloo_gobi_masala":
    print(f"your order {order} in menu")
  elif order=="pannerbuttermasala":
    print(f"your order {order} in menu")
  elif order=="pannercurry":
    print(f"your order {order} in menu")
  elif order=="malai_kofta":
    print(f"your order {order} in menu")
  elif order=="mutterpanner":
        print(f"your order {order} in menu")
  elif order=="mix_veg":
        print(f"your order {order} in menu")
  elif order=="kaju_curry":
    print(f"your order {order} in menu")
  elif order=="aloo_tomato":
    print(f"your order {order} in menu")                
  else:
    print(f"your order {order} is not in menu") 
    #HOME PARSEL
elif user=="home_parsel":
  list=["1.chicken_biriyani","2.mutton_biriyani","3.aloo_gobi_masala","4.pannerbuttermasala","5.pannercurry","6.malai_kofta","7.mutterpanner","8.mix_veg","9.kaju_curry","10.aloo_tomato"]
  print(list)
  da=input("choose menu list:")
  if da=="chicken_biriyani":
    print(f"your order {da} in menu")
  elif da=="mutton_biriyani":
    print(f"your order {da} in menu")
  elif da=="aloo_gobi_masala":
    print(f"your order {da} in menu")
  elif da=="pannerbuttermasala":
    print(f"your order {da} in menu")
  elif da=="pannercurry":
    print(f"your order {da} in menu")
  elif da=="malai_kofta":
    print(f"your order {da} in menu")
  elif da=="mutterpanner":
    print(f"your order {da} in menu")
  elif da=="mix_veg":
    print(f"your order {da} in menu")
  elif da=="kaju_curry":
    print(f"your order {da} in menu")
  elif da=="aloo_tomato":
    print(f"your order {da} in menu") 
  else:
    print("not in menu")  
    sd=input("how many parsel you want:")
    print("receive your parsel")
     #TABLE PLACE   
elif user=="table_place":
      list=["1.chicken_biriyani","2.mutton_biriyani","3.aloo_gobi_masala","4.pannerbuttermasala","5.pannercurry","6.malai_kofta","7.mutterpanner","8.mix_veg","9.kaju_curry","10.aloo_tomato"]
      print(list)    
      order=input("your order pls:").lower()
      if order=="chicken_biriyani":
        print(f"your order {order} in menu")
      elif order=="mutton_biriyani":
        print(f"your order {order} in menu")
      elif order=="aloo_gobi_masala":
        print(f"your order {order} in menu")
      elif order=="pannerbuttermasala":
        print(f"your order {order} in menu")
      elif order=="pannercurry":
        print(f"your order {order} in menu")
      elif order=="malai_kofta":
        print(f"your order {order} in menu")
      elif order=="mutterpanner":
        print(f"your order {order} in menu")
      elif order=="mix_veg":
        print(f"your order {order} in menu")
      elif order=="kaju_curry":
        print(f"your order {order} in menu")
      elif order=="aloo_tomato":
        print(f"your order {order} in menu")   
      else:
        print(f"your order {order} is not in menu")
      print("if you want any other item mam/sir")
      de=input("enter your ans:")        
      if de=="yes":
          print("sure sir/mam you can order again")
      else:
          print("thank you for visiting mam/sir")                            
print("_____________________________________________________________________")
    #customer feed back
print("you can give the feed back in 5star rating")
print("******************************************")
print("\t\t* * * * *\t\t")
fe=input(" ENTER YOUR FEED BACK:")
print("Thank you for your feed back")
print("**** AND THANK YOU FOR VISTING OUR HOTEL*****")