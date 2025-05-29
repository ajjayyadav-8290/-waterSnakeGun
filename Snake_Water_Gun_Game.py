 
#'''               SNAKE WATER GUN  Game           ''' 

import random
Computer = random.choice([1, -1, 0])
youstr = input("Enter your choice : ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"s",-1:"w",0:"g"}
you = youDict[youstr]
print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[Computer]}")
if(Computer == you):
    print("Its a draw")
else:
    if(Computer==1 and you== 0):
        print('''you win \n\n"!..."Thanks for play"...!"''' )
    elif(Computer==1 and you== -1):
        print('''you lose \n\n"!..."Thanks for play"...!" ''' )
    elif(Computer==-1 and you==0):
        print('''you lose \n\n"!..."Thanks for play"...!" ''' )
    elif(Computer==-1 and you==1):
        print('''you win \n\n"!...Thanks for play"..."!''' )
    elif(Computer==0 and you==1):
        print('''you lose \n\n"!..."Thanks for play"...!" ''' )
    elif(Computer==0 and you==-1):
        print('''you win \ns
              "!..."Thanks for play"...!" ''' )
    elif(""):
        print("something went wrong...!")
 

 

                           
