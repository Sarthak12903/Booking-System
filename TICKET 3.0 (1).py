import random
print("_________________________________________________________________________Book The Show_____________________________________________________________________")
print()
print()
z=str(input("ENTER NAME:"))
while True:
    c=input("ENTER MOBILE NUMBER:")
    if len(c)<10 or len(c)>10:
        print("Write correct phone number.")
        continue
    else:
        break
    
        
print()
s=["hindi","english","malyalam","telugu","tamil","kannada"]

while True:
    o=str(input("Language:"))
    o=o.lower()
    o=o.lstrip()
    
    if o==s[0]:
        print("""Now Showing:
              1.Jersey 
              2.RRR(HINDI)
              3.Spider-Man : No Way Home(Hindi)
              4.83
              5.Pushpa: The Rise (Hindi)
              6.Antim
              7.K.G.F Chapter-02 (Hindi)""")
    
        break
    elif o==s[1]:
        print("""Now Showing:
              1.The Call
              2.Conjuring 3
              3.Spiderman: No Way Home
              4.Stowaway
              5.Venom : Let their be Carnage
              6.The Imitation Game
              7.Top Gun 2""")
    
        
        break
    elif o==s[3]:
        print("""Now Showing:
              1.Pushpa: The Rise
              2.Master(Telugu)
              3.Ranarangam
              4.83 (Telugu)
              5.Aswathama
              6.K.G.F Chapter-02(Telugu)
              7.Agent Sai Srinivas Athreya""")
    
        
        break
    elif o==s[2]:
        print("""Now Showing:
              1.Valiyaperunnal
              2.Master(Malyalam)
              3.Pushpa: The Rise(Malyalam)
              4.Malik
              5.One
              6.Ranam""")
    
      
        break
    elif o==s[4]:
        print("""Now Showing:
              1.Sorarai pottru
              2.Asuran
              3.Master
              4.Pushpa: The Rise( Tamil)
              5.Andhagharram
              6.Psyco
              7.Jai bhim""")
    
        
        break
    elif o==s[5]:
        print("""Now Showing:
              1.K.G.F Chapter-02
              2.Pogaru
              3.Master(Kannada)
              4.Gentleman
              5.Pailwan
              6.Pushpa:The Rise (Kannada)""")
    
        break
    else:
        print("Not available")
        input("PRESS ENTER")
    continue
y=input("MOVIE NAME:")
print()
print("Theater's Name:")
print('\t',"""      1. PVR:Phoenix Market City, Pune
                  '04:40 PM'  '06:00 PM'  '07:05 PM'
                  '09:40 PM'   '10:45 PM'
               2. Bollywood Multiplex: Kharadi
                  '02:00 PM'  '03:15 PM'  '06:30 PM'
                  '07:15 PM'  '09:45 PM'  '10:15 PM'
               3. Cinepolis:Seasons Mall, Pune
                  '02:35 PM'  '04:00 PM'  '06:10 PM'
                  '07:35 PM'  '09:45 PM'  '10:30 PM'
               4.INOX:Amanora Town Centre, Hadapsar
                  '03:00 PM'  '06:45 PM'  '09:00 PM'
                  '10:30 PM'""")
print()
gb=input("ENTER THEATER NAME/NUMBER:")
while True:
    if gb in "1. PVR:Phoenix Market City, Pune":
        print("""Chose your show timing:
                '04:40 PM'  '06:00 PM'  '07:05 PM'
                '9:40 PM'   '10:45 PM'""")
        time_1=input("Enter show timing:")
        
        break
    elif gb in "2. Bollywood Multiplex: Kharadi":
        print("""Chose your show timing:
                 '02:00 PM'  '03:15 PM'  '06:30 PM'
                 '07:15 PM'  '09:45 PM'  '10:15 PM'""")
        time_1=input("Enter show timing:")
        
        break
    elif gb in "3. Cinepolis:Seasons Mall, Pune":
        print("""Chose your show timing:
                 '02:35 PM'  '04:00 PM'  '06:10 PM'
                 '07:35 PM'  '09:45 PM'  '10:30 PM'""")
        time_1=input("Enter show timing:")
        
        break
    elif gb in "4.INOX:Amanora Town Centre, Hadapsar":
        print("""Chose your show timing:
                 '03:00 PM'  '06:45 PM'  '09:00 PM'
                 '10:30 PM'""")
        time_1=input("Enter show timing:")
        break
    else:
        print("ERROR")
        continue
    

    

print()


print("\_______________________________________________________________________________SCREEN__________________________________________________________________/")

for a in range(10):
    for b in range(1,10):
        print("\t",a,b,"◻◻",end="")
    print()
    print()



    
print("(MAX. Two booking available)")
print("""EXAMPLE: 01 ◻◻
      Seat number: 01.A--->01 ▧◻
      OR Seat number: 01.A,01.B--->01 ▧▧""")
print()
print("""NOTICE: Seat number: 10,20,30,40,50,60,70,80,90,100 slot is open only in case of Housefull""")
print()
print()

while True:
    m=int(input("Number of seats:"))
    if m<0:
        print("Please select the seat")
    elif m>2:
        print("You can't select more than 2 seats")
        
    elif 0<m<3:
        input("PRESS_ENTER")
        break
    else:
        print("Type again")
        continue
        
d=input("SEAT NUMBER:")


print("\__________________________________________________________________________________SCREEN_______________________________________________________________________/")

for j in range(10):
    for l in range(1,10):
        string="◻◻"
        if d=="01.A":
            if j==0:
                if l==1:
                    string="▧◻"
                    
            print("\t",j,l,string,end="")
        
        elif d=="01.B":
            if j==0:
                if l==1:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="01.A,01.B":
            if j==0:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="02.A":
            if j==0:
                if l==2:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="02.B":
            if j==0:
                if l==2:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="02.A,02.B":
            if j==0:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="03.A":
            if j==0:
                if l==3:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="03.B":
            if j==0:
                if l==3:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="03.A,03.B":
            if j==0:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="04.A":
            if j==0:
                if l==4:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="04.B":
            if j==0:
                if l==4:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="04.A,04.B":
            if j==0:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="05.A":
            if j==0:
                if l==5:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="05.B":
            if j==0:
                if l==5:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="05.A,05.B":
            if j==0:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="06.A":
            if j==0:
                if l==6:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="06.B":
            if j==0:
                if l==6:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="06.A,06.B":
            if j==0:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="07.A":
            if j==0:
                if l==7:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="07.B":
            if j==0:
                if l==7:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="07.A,07.B":
            if j==0:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="08.A":
            if j==0:
                if l==8:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="08.B":
            if j==0:
                if l==8:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="08.A,08.B":
            if j==0:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="09.A":
            if j==0:
                if l==9:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="09.A,09.B":
            if j==0:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="09.B":
            if j==0:
                if l==9:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="11.A":
            if j==1:
                if l==1:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="11.B":
            if j==1:
                if l==1:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="11.A,11.B":
            if j==1:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="12.A":
            if j==1:
                if l==2:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="12.B":
            if j==1:
                if l==2:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="12.A,12.B":
            if j==1:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="13.A":
            if j==1:
                if l==3:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="13.B":
            if j==1:
                if l==3:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="13.A,13.B":
            if j==1:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="14.A":
            if j==1:
                if l==4:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="14.B":
            if j==1:
                if l==4:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="14.A,14.B":
            if j==1:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="15.A":
            if j==1:
                if l==5:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="15.B":
            if j==1:
                if l==5:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="15.A,15.B":
            if j==1:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="16.A":
            if j==1:
                if l==6:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="16.B":
            if j==1:
                if l==6:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="16.A,16.B":
            if j==1:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="17.A":
            if j==1:
                if l==7:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="17.B":
            if j==1:
                if l==7:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="17.A,17.B":
            if j==1:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="18.A":
            if j==1:
                if l==8:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="18.B":
            if j==1:
                if l==8:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="18.A,18.B":
            if j==1:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="19.A":
            if j==1:
                if l==9:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="19.B":
            if j==1:
                if l==9:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="19.A,19.B":
            if j==1:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="21.A":
            if j==2:
                if l==1:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="21.B":
            if j==2:
                if l==1:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="21.A,21.B":
            if j==2:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="22.A":
            if j==2:
                if l==2:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="22.B":
            if j==2:
                if l==2:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="22.A,22.B":
            if j==2:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="23.A":
            if j==2:
                if l==3:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="23.B":
            if j==2:
                if l==3:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="23.A,23.B":
            if j==2:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="24.A":
            if j==2:
                if l==4:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="24.B":
            if j==2:
                if l==4:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="24.A,24.B":
            if j==2:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="25.A":
            if j==2:
                if l==5:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="25.B":
            if j==2:
                if l==5:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="25.A,25.B":
            if j==2:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="26.A":
            if j==2:
                if l==6:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="26.B":
            if j==2:
                if l==6:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="26.A,26.B":
            if j==2:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="27.A":
            if j==2:
                if l==7:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="27.B":
            if j==2:
                if l==7:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="27.A,27.B":
            if j==2:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="28.A":
            if j==2:
                if l==8:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="28.B":
            if j==2:
                if l==8:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="28.A,28.B":
            if j==2:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="29.A":
            if j==2:
                if l==9:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="29.B":
            if j==2:
                if l==9:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="29.A,29.B":
            if j==2:
                if l==9:
                    string='▧▧'
            print("\t",j,l,string,end="")
        elif d=="31.A":
            if j==3:
                if l==1:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="31.B":
            if j==3:
                if l==1:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="31.A,31.B":
            if j==3:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="32.A":
            if j==3:
                if l==2:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="32.B":
            if j==3:
                if l==2:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="32.A,32.B":
            if j==3:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="33.A":
            if j==3:
                if l==3:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="33.B":
            if j==3:
                if l==3:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="33.A,33.B":
            if j==3:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="34.A":
            if j==3:
                if l==4:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="34.B":
            if j==3:
                if l==4:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="34.A,34.B":
            if j==3:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="35.A":
            if j==3:
                if l==5:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="35.B":
            if j==3:
                if l==5:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="35.A,35.B":
            if j==3:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="36.A":
            if j==3:
                if l==6:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="36.B":
            if j==3:
                if l==6:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="36.A,36.B":
            if j==3:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="37.A":
            if j==3:
                if l==7:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="37.B":
            if j==3:
                if l==7:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="37.A,37.B":
            if j==3:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="38.A":
            if j==3:
                if l==8:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="38.B":
            if j==3:
                if l==8:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="38.A,38.B":
            if j==3:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="39.A":
            if j==3:
                if l==9:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="39.B":
            if j==3:
                if l==9:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="39.A,39.B":
            if j==3:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="41.A":
            if j==4:
                if l==1:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="41.B":
            if j==4:
                if l==1:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="41.A,41.B":
            if j==4:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="42.A":
            if j==4:
                if l==2:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="42.B":
            if j==4:
                if l==2:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="42.A,42.B":
            if j==4:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="43.A":
            if j==4:
                if l==3:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="43.B":
            if j==4:
                if l==3:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="43.A,43.B":
            if j==4:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="44.A":
            if j==4:
                if l==4:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="44.B":
            if j==4:
                if l==4:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="44.A,44.B":
            if j==4:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="45.A":
            if j==4:
                if l==5:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="45.B":
            if j==4:
                if l==5:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="45.A,45.B":
            if j==4:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="46.A":
            if j==4:
                if l==6:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="46.B":
            if j==4:
                if l==6:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="46.A,46.B":
            if j==4:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="47.A":
            if j==4:
                if l==7:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="47.B":
            if j==4:
                if l==7:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="47.A,47.B":
            if j==4:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="48.A":
            if j==4:
                if l==8:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="48.B":
            if j==4:
                if l==8:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="48.A,48.B":
            if j==4:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="49.A":
            if j==4:
                if l==9:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="49.B":
            if j==4:
                if l==9:
                    string="◻▧"
            print("\t",j,l,string,end="")
        elif d=="49.A,49.B":
            if j==4:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="51.A":
            if j==5:
                if l==1:
                    string="▧◻"
            print("\t",j,l,string,end="")
        elif d=="51.B":
            if j==5:
                if l==1:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="51.A,51.B":
            if j==5:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="52.A":
            if j==5:
                if l==2:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="52.B":
            if j==5:
                if l==2:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="52.A,52.B":
            if j==5:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="53.A":
            if j==5:
                if l==3:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="53.B":
            if j==5:
                if l==3:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="53.A,53.B":
            if j==5:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="54.A":
            if j==5:
                if l==4:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="54.B":
            if j==5:
                if l==4:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="54.A,54.B":
            if j==5:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="55.A":
            if j==5:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="55.B":
            if j==5:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="55.A,55.B":
            if j==5:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="56.A":
            if j==5:
                if l==6:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="56.B":
            if j==5:
                if l==6:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="56.A,56.B":
            if j==5:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="57.A":
            if j==5:
                if l==7:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="57.B":
            if j==5:
                if l==7:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="57.A,57.B":
            if j==5:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="58.A":
            if j==5:
                if l==8:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="58.B":
            if j==5:
                if l==8:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="58.A,58.B":
            if j==5:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="59.A":
            if j==5:
                if l==9:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="59.B":
            if j==5:
                if l==9:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="61.A":
            if j==6:
                if l==1:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="59.A,59.B":
            if j==5:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="61.B":
            if j==6:
                if l==1:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="61.A,61.B":
            if j==6:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="62.A":
            if j==6:
                if l==2:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="62.B":
            if j==6:
                if l==2:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="62.A,62.B":
            if j==6:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="63.A,63.B":
            if j==6:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="63.A":
            if j==6:
                if l==3:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="63.B":
            if j==6:
                if l==3:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="64.A":
            if j==6:
                if l==4:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="64.B":
            if j==6:
                if l==4:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="64.A,64.B":
            if j==6:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="65.A":
            if j==6:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="65.B":
            if j==6:
                if l==5:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="65.A,65.B":
            if j==6:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="66.A":
            if j==6:
                if l==6:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="66.B":
            if j==6:
                if l==6:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="66.A,66.B":
            if j==6:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="67.A":
            if j==6:
                if l==7:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="67.B":
            if j==6:
                if l==7:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="67.A,67.B":
            if j==6:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="68.A":
            if j==6:
                if l==8:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="68.B":
            if j==6:
                if l==8:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="68.A,68.B":
            if j==6:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="69.A":
            if j==6:
                if l==9:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="69.B":
            if j==6:
                if l==9:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="69.A,69.B":
            if j==6:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="71.A":
            if j==7:
                if l==1:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="71.B":
            if j==7:
                if l==1:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="71.A,71.B":
            if j==7:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="72.A":
            if j==7:
                if l==2:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="72.B":
            if j==7:
                if l==2:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="72.A,72.B":
            if j==7:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="73.A":
            if j==7:
                if l==3:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="73.B":
            if j==7:
                if l==3:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="73.A,73.B":
            if j==7:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="74.A":
            if j==7:
                if l==4:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="74.B":
            if j==7:
                if l==4:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="74.A,74.B":
            if j==7:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="75.A":
            if j==7:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="75.B":
            if j==7:
                if l==5:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="75.A,75.B":
            if j==7:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="76.A":
            if j==7:
                if l==6:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="76.B":
            if j==7:
                if l==6:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="76.A,76.B":
            if j==7:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="77.A":
            if j==7:
                if l==7:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="77.B":
            if j==7:
                if l==7:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="77.A,77.B":
            if j==7:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="78.A":
            if j==7:
                if l==8:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="78.B":
            if j==7:
                if l==8:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="78.A,78.B":
            if j==7:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="79.A":
            if j==7:
                if l==9:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="79.B":
            if j==7:
                if l==9:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="79.A,79.B":
            if j==7:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="81.A":
            if j==8:
                if l==1:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="81.B":
            if j==8:
                if l==1:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="81.A,81.B":
            if j==8:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="82.A":
            if j==8:
                if l==2:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="82.B":
            if j==8:
                if l==2:
                    sring="□▧"
            print("\t",j,l,string,end="")
        elif d=="82.A,82.B":
            if j==8:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="83.A":
            if j==8:
                if l==3:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="83.B":
            if j==8:
                if l==3:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="83.A,83.B":
            if j==8:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="84.A":
            if j==8:
                if l==4:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="84.B":
            if j==8:
                if l==4:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="84.A,84.B":
            if j==8:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="85.A":
            if j==8:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="85.B":
            if j==8:
                if l==5:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="85.A,85.B":
            if j==8:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="86.A":
            if j==8:
                if l==6:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="86.B":
            if j==8:
                if l==6:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="86.A,86.B":
            if j==8:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="87.A":
            if j==8:
                if l==7:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="87.B":
            if j==8:
                if l==7:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="87.A,87.B":
            if j==8:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="88.A":
            if j==8:
                if l==8:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="88.B":
            if j==8:
                if l==8:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="88.A,88.B":
            if j==8:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="89.A":
            if j==8:
                if l==9:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="89.B":
            if j==8:
                if l==9:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="89.A,89.B":
            if j==8:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="91.A":
            if j==9:
                if l==1:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="91.B":
            if j==9:
                if l==1:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="91.A,91.B":
            if j==9:
                if l==1:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="92.A":
            if j==9:
                if l==2:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="92.B":
            if j==9:
                if l==2:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="92.A,92.B":
            if j==9:
                if l==2:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="93.A":
            if j==9:
                if l==3:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="93.B":
            if j==9:
                if l==3:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="93.A,93.B":
            if j==9:
                if l==3:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="94.A":
            if j==9:
                if l==4:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="94.B":
            if j==9:
                if l==4:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="94.A,94.B":
            if j==9:
                if l==4:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="95.A":
            if j==9:
                if l==5:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="95.B":
            if j==9:
                if l==5:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="95.A,95.B":
            if j==9:
                if l==5:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="96.A":
            if j==9:
                if l==6:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="96.B":
            if j==9:
                if l==6:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="96.A,96.B":
            if j==9:
                if l==6:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="97.A":
            if j==9:
                if l==7:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="97.B":
            if j==9:
                if l==7:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="97.A,97.B":
            if j==9:
                if l==7:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="98.A":
            if j==9:
                if l==8:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="98.B":
            if j==9:
                if l==8:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="98.A,98.B":
            if j==9:
                if l==8:
                    string="▧▧"
            print("\t",j,l,string,end="")
        elif d=="99.A":
            if j==9:
                if l==9:
                    string="▧□"
            print("\t",j,l,string,end="")
        elif d=="99.B":
            if j==9:
                if l==9:
                    string="□▧"
            print("\t",j,l,string,end="")
        elif d=="99.A,99.B":
            if j==9:
                if l==9:
                    string="▧▧"
            print("\t",j,l,string,end="")
        else:
            print("NOT AVAILABLE.......")
price=random.randrange(70,700)    
print()
print()
print()
if gb in "1. PVR:Phoenix Market City, Pune":
    print('\t',"____________________________")
    print('\t',"Almost There!!")
    print('\t',y.upper(),"________",m)
    print('\t',"PVR:Phoenix Market City, Pune","__",time_1)
    print('\t','TICKET PRICE:',price*m)
    print('\t','GST:',       (5/100)*price)
    print('\t','TOTAL PRICE:',(price*m)+((5/100)*price))
    print()
    print('\t','Proceed For Payement')
    print('\t',"____________________________")
    input("(PRESS_ENTER)")

elif gb in "2. Bollywood Multiplex: Kharadi":
    print('\t',"____________________________")
    print('\t',"Almost There!!")
    print('\t',y.upper(),"________",m)
    print('\t',"Bollywood Multiplex: Kharadi","__",time_1)
    print('\t','TICKET PRICE:',price*m)
    print('\t','GST:',       (5/100)*price)
    print('\t','TOTAL PRICE:',(price*m)+((5/100)*price))
    print()
    print('\t','Proceed For Payement')
    print('\t',"____________________________")
    input("(PRESS_ENTER)")
elif gb in "3. Cinepolis:Seasons Mall, Pune":
    print('\t',"____________________________")
    print('\t',"Almost There!!")
    print('\t',y.upper(),"________",m)
    print('\t',"Cinepolis:Seasons Mall, Pune","__",time_1)
    print('\t','TICKET PRICE:',price*m)
    print('\t','GST:',       (5/100)*price)
    print('\t','TOTAL PRICE:',(price*m)+((5/100)*price))
    print()
    print('\t','Proceed For Payement')
    print('\t',"____________________________")
    input("(PRESS_ENTER)")
elif gb in "4.INOX:Amanora Town Centre, Hadapsar":
    print('\t',"____________________________")
    print('\t',"Almost There!!")
    print('\t',y.upper(),"________",m)
    print('\t',"INOX:Amanora Town Centre, Hadapsar","__",time_1)
    print('\t','TICKET PRICE:',price*m)
    print('\t','GST:',       (5/100)*price)
    print('\t','TOTAL PRICE:',(price*m)+((5/100)*price))
    print()
    print('\t','Proceed For Payement')
    print('\t',"____________________________")
    input("(PRESS_ENTER)")
else:
    print("________")
    print()
    print("Error...")
    print()
    print("________")
a = (price*m) + ((5/100)*price)

print()
print()
print("Proceed for payment.")
print()
b_n=input("BANK NAME:")
while True:
    c_n=input("CARD_NUMBER:")
    if c_n.isdigit():
        if len(c_n)==12:
            break       
    else:
        print("ERROR..")
        continue
               
import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user = "root", passwd = "sarthak12093", database = "management")
st = "insert into purchase_history2(Name, Movie, Language, Theater, Tickets, Bank, Amount)values('{}', '{}', '{}', '{}', {}, '{}', {})".format(z, y, o, gb, m, b_n, a)
cursor = mycon.cursor()
cursor.execute(st)
mycon.commit()


da=input('EXPIRY_DATE:')

while True:
    CVV=input("CVV:")
    if CVV.isdigit():
        if len(CVV)==3:
            print("Proceessing your details....")
        break
    
    else:
        print(" Wrong Card Number Or Cvv.")
print()
print("Your Ticket Has Been Booked...(^_^)")
print("Within Few Hour Your Ticket Would Be Sent To You.")
print()

ab = input("Would you like see your Purchase History?")
if ab == "yes" or "Yes":
    cursor = mycon.cursor()
    cursor.execute("select * from purchase_history2")
    data = cursor.fetchall()
    for row in data:
        print(row)
    print("ENJOY YOUR MOVIE....(^_^)")
else:
    print("ENJOY YOUR MOVIE....(^_^)")

import csv
myfile = open("Purchase History1.csv", "a")
stuwriter = csv.writer(myfile)
stuwriter.writerow([z, y, o, gb, m, b_n, a])
myfile.close()
