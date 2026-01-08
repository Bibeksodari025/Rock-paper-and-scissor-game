# Rock,paper and scissor game using python(random module)
import random

list = ["Rock","Paper","Scissor"]
# rock vs scissor -> rock
# rock vs paper -> paper
# paper vs scissor -> scissor

while True:
    ucount=0
    ccount=0
    uc=int(input('''
Game start:
1. yes
2.Exit | No       '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1.Rock
2.Paper
3.Scissor  '''))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor" 
            Cchoice=random.choice(list)
            if uchoice==Cchoice:
                print("computer value:",Cchoice)
                print("User value",uchoice)
                print("Game draw:") 
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Scissor" and Cchoice=="Paper") or (uchoice=="Paper"and Cchoice=="Rock"):
                print("computer value",Cchoice)
                print("User choice",uchoice)
                print("You win")
                ucount=ucount+1
            else:
                print("computer value",Cchoice)
                print("User value",Cchoice)
                ccount=ccount+1
            if(ucount==ccount):
                print("User count",ucount)
                print("computer count",ccount)
                print("Game is draw:")
            elif(ucount>ccount):
                print("User count:",ucount)
                print("computer count",ccount)
                print("You win:")
            else:
                print("User count:",ucount)
                print("computer count",ccount)
                print("Computer win:")                                  
    else:
        break
