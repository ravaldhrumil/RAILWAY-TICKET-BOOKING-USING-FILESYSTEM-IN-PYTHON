import os
import time
class Railway:
    
    #init method for login and signup 
    def __init__(self):
        print("\n\t\t\tWELCOME")
        print("\n\tENTER [1] TO LOGIN\n\tENTER [2] TO SIGNUP")
        choice=int(input("\n\tENTER CHOICE:"))

        if choice==1:
            self.login()

        elif choice==2:
            self.signup()

        else:
            print("\n\n\t\tOPPS WRONG CHOICE ENTERED")
            time.sleep(1)
            self.__init__()

    
    #method for checking login credentials and if right than logging in
    def login(self):
        file=open("login_details",'r')
        l=file.readlines()
        self.usr=input("\n\tPLEASE ENTER YOUR USERNAME:")
        self.pas=input("\tPLEASE ENTER YOUR PASSWORD:")
        flag=0
        for i in range(len(l)):   #loop for checking credntials
            if i%2==0:
                if l[i]==self.usr+'\n' and l[i+1]==self.pas+'\n':
                    print("\n\t\tLOGIN SUCCESSFULL")
                    time.sleep(1)
                    flag+=1
                    self.menu()
        file.close()
        
        if flag==0:  #if wronf credentials entered
            print("\n\t\tOOPS WRONG PASWORD OR USENAME PLEASE TRY AGAIN!!!")
            time.sleep(1)
            self.__init__()

    #method for regesisrtraion of new member
    def signup(self):
        file=open("login_details",'r')
        l=file.readlines()
        usr=input("\n\tPLEASE ENTER NEW USERNAME:")
        flag=0
        for i in range(len(l)):   #loop to check if same username already exists or not
            if i%2==0:
                if l[i]==usr+'\n':   
                    print("\n\t\tTHIS USERNAME ALREADY EXIST!!")
                    time.sleep(1)
                    flag+=1
                    break
        file.close()

        file=open("login_details",'a+')

        if flag==0:
            pas=input("\tPLEASE ENTER PASSWORD:")
            file.write( usr + '\n')
            file.write( pas + '\n')
            print("\n\t\tUSER CREATED SUCCESSFULLY")
            time.sleep(1)
            file.close()


        self.__init__()


    #method to ask user for choice of what he wants to do
    def menu(self):
        print("\n\tENTER [1] TO BOOK TICKET\n\tENTER [2] TO CANCEL TICKET\n\tENTER [3] TO VIEW TICKET\n\tENTER [4] TO LOGOUT")
        choice=int(input('\n\tENTER CHOICE:'))

        if choice==1: #for new booking
            self.departure()

        elif choice==2: #for cancelling ticket
            exist=os.path.isfile(self.usr) #checking if ticket exist or not

            if exist==True:
                confirm=input("\n\tARE YOU SURE YOU WANT TO CANCEL YOUR TICKET(TYPE UES OR NO):").lower()
                if confirm=='yes':
                    os.remove(self.usr)
                    print("\n\n\tTICKET CANCELLED SUCCESSFULLY!!!")
                    time.sleep(2)
                else:
                    self.menu()

            else:
                print("\n\n\t\tYOU CURRENTLY HAVE NO TICKET BOOKED")
                time.sleep(1)
                self.menu()

        elif choice==3:  #for viewing ticket
            exist=os.path.isfile(self.usr)  #checking if ticket exist or not

            if exist==True:
                f=open(self.usr,'r')
                print('\n\n'+f.read())
                f.close()
                time.sleep(2)
                self.menu()

            else:
                print("\n\n\t\tYOU CURRENTLY HAVE NO TICKET BOOKED")
                time.sleep(1)
                self.menu()


            
        elif choice==4:
            print('\n\n\n\t\tTHANK YOU!!!!')
            time.sleep(4)
            exit(0)

        else:
            print("PLEASE ENTER CORRECT CHOICE!!")
            time.sleep(1)
            self.menu()



    #method for selecting departure station
    def departure(self):
        print('\n\n\tLIST OF BOARDING STATIONS\n\tAHMEDABAD\n\tVARANASI')
        self.board=input("\n\tENTER BOARDING STATION NAME:").lower()

        if self.board == 'ahmedabad' or self.board=='varanasi':
            self.arrival()
     
        else:
            print("\n\n\t\tSORRY NO TRAIN AVAILABLE FROM ",self.board.upper())
            time.sleep(1)
            self.departure()



    #method for selecting arrival station based on departure station input
    def arrival(self):
        if self.board=='ahmedabad':
            print('\n\n\tLIST OF TRAINS FROM AHMEDABAD\n\tMUMBAI\n\tSURAT')
            self.arrive=input("\n\tENTER THE DESTINATION NAME:").lower()

            if self.arrive=='mumbai' or self.arrive=='surat':
                 self.ticket()

            else:
                print("\n\n\t\tSORRY NO TRAIN AVAILABLE TO ",self.arrive.upper())
                time.sleep(1)
                self.arrival()


        if self.board=='varanasi':
            print('\n\n\tLIST OF TRAINS FROM VARANASI\n\tPRAYAGRAJ\n\tDELHI')
            self.arrive=input("\tENTER THE DESTINATION:").lower()

            if self.arrive=='prayagraj' or self.arrive=='delhi':
                self.ticket()

            else:
                print("\n\n\tSORRY NO TRAIN AVAILABLE TO ",self.arrive.upper())
                time.sleep(1)
                self.arrival()


     #method for taking input of passengers detail
    def ticket(self):
        file=open(self.usr,'a+')
        self.nop=int(input('\n\n\tENTER NUMBER OF PASSENGERS:'))
        for i in range(self.nop):
            self.name=input("\n\tPLEASE ENTER PASSENGER's NAME:").upper()
            file.write("PASSENGER's NAME: "+self.name+'\n')
            self.no=int(input("\tPLEASE ENTER PASSENGER's MOBILE NUMBER:"))
            file.write("PASSENGER's MOBILE NUMBER: "+str(self.no)+'\n')
            self.age=int(input("\tPLEASE ENTER PASSENGER's AGE:"))
            file.write("PASSENGER's AGE: "+str(self.age)+'\n')
            self.aadhar=int(input("\tPLEASE ENTER PASSENGER's AADHAR CARD NUMBER:"))
            file.write("PASSENGER's AADHAR NUMBER: "+str(self.aadhar)+'\n\n')


        file.write('\nFROM: '+self.board)
        file.write('\nTO: '+self.arrive)
        file.close()
        self.seat()


    # method for selecting train
    def seat(self):

        if self.board=='ahmedabad' and self.arrive=='mumbai':
            print('\n\n\tTHERE ARE FOLLOWING TRAINS AVAILABLE\n\tENTER [1] FOR VANDE BHARAT\n\tENTER [2] FOR MAHARAJA EXPRESS')
            ch3=int(input("\n\tPLEASE ENTER CHOICE:"))
            if ch3==1: #storing price of seat for seleted train
                self.seater=780
                self.ac1=2100
                self.ac2=1800
                self.ac3=1300
                

            elif ch3==2: 
                self.seater=1150 
                self.ac1=2800
                self.ac2=2185
                self.ac3=1760
               

            else:
                print("\n\n\tPLEASE ENTER CORRECT CHOICE!!")
                time.sleep(1)
                self.seat()

           


        if self.board=='ahmedabad' and self.arrive=='surat':
            print('\n\n\tTHERE ARE FOLLOWING TRAINS AVAILABLE\n\tENTER [1] FOR GARIB RATH\n\tENTER [2] FOR RANJITSINH EXPRESS')
            ch3=int(input("\tPLEASE ENTER CHOICE:"))

            
            if ch3==1: #for selected train
                self.seater=350
                self.ac1=1300
                self.ac2=1080
                self.ac3=960
            

            elif ch3==2: #for selected train
                self.seater=450
                self.ac1=1430
                self.ac2=1150
                self.ac3=1000
               

            else:
                print("\n\n\tPLEASE ENTER CORRECT CHOICE!!")
                time.sleep(1)
                self.seat()




        if self.board=='varanasi' and self.arrive=='prayagraj':
            print('\n\n\tTHERE ARE FOLLOWING TRAINS AVAILABLE\n\tENTER [1] FOR CHAURA CHAURI EXP\n\tENTER [2] FOR SWATANTRATA EXP')
            ch3=int(input("\tPLEASE ENTER CHOICE:"))

            
            if ch3==1: #for selected train
                self.seater=600
                self.ac1=1300
                self.ac2=1100
                self.ac3=900
               

            elif ch3==2: #for selected train
                self.seater=900
                self.ac1=2100
                self.ac2=1650
                self.ac3=1200
            

            else:
                print("\n\n\tPLEASE ENTER CORRECT CHOICE!!")
                time.sleep(1)
                self.seat()


           


        if self.board=='varanasi' and self.arrive=='delhi':
            print('\n\n\tTHERE ARE FOLLOWING TRAINS AVAILABLE\n\tENTER [1] FOR ATAL EXP\n\tENTER [2] FOR VANDE BHARAT')
            ch3=int(input("\tPLEASE ENTER CHOICE:"))
            
            if ch3==1: #for selected train
                self.seater=1200
                self.ac1=2400
                self.ac2=2100
                self.ac3=1600
                

            elif ch3==2: #for selected train
                self.seater=1360
                self.ac1=2470
                self.ac2=2200
                self.ac3=1790
                

            else:
                print("\n\n\tPLEASE ENTER CORRECT CHOICE!!")
                time.sleep(1)
                self.seat()

        self.time()
        

            
    #method for selecting time
    def time(self):
        print("\n\n\tPLEASE SELECT BOARDING TIME:\n\t[1] FOR 6:20 AM\n\t[2] FOR 5:50 PM")
        timech=int(input("\n\tENTER TIME CHOICE:"))
        if timech==1:
            self.boardtime='6:20 AM'
                
        elif timech==2:
            self.boardtime='5:50 PM'

        else:
            print("\n\n\tNO TRAIN AVAILABLE AT THIS TIME!!")
            time.sleep(1)
            self.time()

        self.seattype()


                

    #method for selecting seat type
    def seattype(self):

        while(True):
            print("\n\tENTER [1] FOR SEATER ($",self.seater,")\n\tENTER [2] FOR SLEPPER")
            ch1=int(input("\n\tPLEASE ENTER CHOICE:"))

            if ch1==1:
                break

            elif ch1==2: #if sleeper class is selected than to select tier
                
                while(True):
                    print("\n\n\tENTER [1] FOR 1AC ($",self.ac1,")\n\tENTER [2] FOR 2AC ($",self.ac2,")\n\tENTER [3] FOR 3AC ($",self.ac3,")")
                    ch2=int(input("\n\tPLEASE ENTER CHOICE:"))

                    if ch2== 1 or ch2==2 or ch2==3:
                        break
                    else:
                        print("\n\n\t\tPLEASE ENTER CORRECT SLEEPER CLASS CHOICE!!")
                        time.sleep(1)
                break


            else:
                print("\n\n\tPLEASE ENTER CORRECT SEAT CHOICE!!")
                time.sleep(1)


        f=open(self.usr,'a+')

        #adding seat and price information to file
        if ch1==1: #to add price in file
            f.write('\nPRICE PER TICKET  $'+str(self.seater))
            f.write('\nTOTAL PRICE  $')
            f.write(str(self.nop*self.seater))

        if ch1==2: #to add price in file
            if ch2==1:
                f.write('\nPRICE PER TICKET  $'+str(self.ac1))
                f.write('\nTOTAL PRICE  $')
                f.write(str(self.nop*self.ac1))
            if ch2==2:
                f.write('\nPRICE PER TICKET  $'+str(self.ac2))
                f.write('\nTOTAL PRICE  $')
                f.write(str(self.nop*self.ac2))
            if ch2==3:
                f.write('\nPRICE PER TICKET  $'+str(self.ac3))
                f.write('\nTOTAL PRICE  $')
                f.write(str(self.nop*self.ac3))
        



        f.write("\nBOARDING TIME IS: "+self.boardtime+'\n\n')
        f.close()
        print("\n\n\t\tTICKET BOOKED SUCCESSFULLY")
        time.sleep(2)
        self.menu()


r=Railway()