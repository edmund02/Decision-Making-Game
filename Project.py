database=[    ['hong','1324'],['edmund','4242']   ]
ID=['hong','edmund']

def UserAuthentication():
    global File
    username=raw_input('Enter Username: ')
    pin=raw_input('Enter PIN code: ')
    Chances=2
    if [username,pin] in database:
        print 'Access granted'
    while [username,pin]not in database:
        print 'Invalid username and pin, please try again'
        username=raw_input('Enter Username: ')
        pin=raw_input('Enter PIN code: ')
        Chances=Chances-1
        if [username,pin]in database:
            print 'Access granted'
            PlayAgain = True
        if Chances<=0 and [username,pin]    not in database:
            print 'Bye'
            exit()
    if username == 'hong':
        File=ID[0]
    if username == 'edmund':
        File=ID[1]


def UserPreviousRecord():
    global CreateFile
    UserInput_Previous=raw_input("Did you play this before? (y/n): ")
    while (UserInput_Previous != "y" or UserInput_Previous != "n"):
        if UserInput_Previous == "y" or UserInput_Previous == "n":
            break
        else:
            print 'Please enter y or n'
            UserInput_Previous = raw_input("Do you want your Record? (y/n): ")
    if File==ID[0]:
        if UserInput_Previous == 'n':
            CreateFile = True
            my_file = open('ScoreBoard1.txt', 'w')
        if UserInput_Previous == 'y':
            CreateFile = False
    if File==ID[1]:
        if UserInput_Previous == 'n':
            CreateFile=True
            my_file = open('ScoreBoard2.txt', 'w')
        if UserInput_Previous == 'y':
            CreateFile = False

def CheckFile():
    global CreateFile
    if File==ID[0]:
        try:
            open('ScoreBoard1.txt', 'r')
        except IOError as e:
            print 'You lied.'
            CreateFile = True
            my_file = open('ScoreBoard1.txt', 'w')
    if File==ID[1]:
        try:
            open('ScoreBoard2.txt', 'r')
        except IOError as e:
            print 'You Lied.'
            CreateFile = True
            my_file = open('ScoreBoard2.txt', 'w')


def UserRecord():
    global SeeRecord
    UserInput_Record = raw_input("Do you want to see your Record? (y/n): ")
    while (UserInput_Record != "y" or UserInput_Record != "n"):
        if UserInput_Record == "y" or UserInput_Record == "n":
            break
        else:
            print 'Please enter y or n'
            UserInput_Record = raw_input("Do you want to see your Record? (y/n): ")
    if UserInput_Record == 'y':
        SeeRecord= True
    if UserInput_Record == 'n':
        SeeRecord= False
    if SeeRecord == True:
        OpenRecord()


def UserStart():
    global PlayGame
    UserInput_Start =raw_input("Do you want your Start? (y/n): ")
    while (UserInput_Start != "y" or UserInput_Start != "n"):
        if UserInput_Start == "y" or UserInput_Start == "n":
            break
        else:
            print 'Please enter y or n'
            UserInput_Start = raw_input("Do you want to Start? (y/n): ")
    if UserInput_Start == 'y':
        PlayGame=True
    if UserInput_Start == 'n':
        exit()


        
def UserPlayAgain(): 
    UserInput_Play = raw_input("Do you want to play again? (y/n): ")
    while (UserInput_Play != "y" or UserInput_Play != "n"):
        if UserInput_Play == "y" or UserInput_Play == "n":
            break
        else:
            print 'Please enter y or n'
            UserInput_Play = raw_input("Do you want to play again? (y/n): ")
    if UserInput_Play == 'y':
        PlayGame= True
    if UserInput_Play == 'n':
        PlayGame= False
    if PlayGame ==False:
        exit()


def UserSaveRecord():
    global SaveRecord
    UserInput_SaveRecord=raw_input("Do you want to save your Record? (y/n): ")
    while (UserInput_SaveRecord != "y" or UserInput_SaveRecord != "n"):
        if UserInput_SaveRecord == "y" or UserInput_SaveRecord == "n":
            break
        else:
            print 'Please enter y or n'
            UserInput_SaveRecord = raw_input("Do you want to save your Record? (y/n): ")
    if UserInput_SaveRecord == 'y':
        SaveRecord= True
    if UserInput_SaveRecord == 'n':
        SaveRecord= False
    if SaveRecord== True:
        record()


recordFunction=[]
def record():
    if File==ID[0]:
        if point<25:
            scores = "You had Played Bad Ending"
        elif point<=50:
            scores = "You had Played Semi-Bad Ending"
        elif point<=75:
            scores = "You had Played Semi-Good Ending"
        else :
            scores = "You had Played Good Ending"
        recordFunction.append(scores)
        ScoreBoard1 = open('ScoreBoard1.txt', 'a')
        ScoreBoard1.write(  scores + "\n")
        ScoreBoard1.close()
    if File==ID[1]:
        if point<25:
            scores = "You had Played Bad Ending"
        elif point<=50:
            scores = "You had Played Semi-Bad Ending"
        elif point<=75:
            scores = "You had Played Semi-Good Ending"
        else :
            scores = "You had Played Good Ending"
        recordFunction.append(scores)
        ScoreBoard2 = open('ScoreBoard2.txt', 'a')
        ScoreBoard2.write(scores + "\n")
        ScoreBoard2.close()



def OpenRecord():
    Record=[]
    if File==ID[0]:
        ReadNotePad=open('ScoreBoard1.txt','r')
        for line in ReadNotePad:
            Record.append(line)
        ReadNotePad.close
        NumPlayed=1
        ReadNotePad=open('ScoreBoard1.txt','r')
        for Play in range(0,len(Record)):
            List=ReadNotePad.readline()
            if NumPlayed==1:
                Text = "st"
            elif NumPlayed==2:
                Text = "nd"
            else:
                Text = "th"
            print List , "for the" , NumPlayed,Text ,"time"
            NumPlayed=NumPlayed+1
        ReadNotePad.close
        
    if File==ID[1]:
        ReadNotePad=open('ScoreBoard2.txt','r')
        Record=[]
        for line in ReadNotePad:
            Record.append(line)
        ReadNotePad.close
        NumPlayed=1
        ReadNotePad=open('ScoreBoard2.txt','r')
        for Play in range(0,len(Record)):
            List=ReadNotePad.readline()
            if NumPlayed==1:
                Text = "st"
            elif NumPlayed==2:
                Text = "nd"
            else:
                Text = "th"
            print List , "for the" , NumPlayed,Text ,"time"
            NumPlayed=NumPlayed+1
        ReadNotePad.close
    if len(Record)==0:
        print "There is No Record"


def story (a, b) :
    global point
    point=0
    print '--------------------------------------------------------------------------------'
    print "Here's the story begin..."
    print "You woke up late, it is about 7.30am in the morning. But your school starts at 7.00am. What to do?"
    print "a) Walk to school"
    print "b) Ride your bike to school (Forgot to pump the tyres)"
    print '--------------------------------------------------------------------------------'
    decision1=raw_input ("Please select your move (a/b): ")
    while (decision1!="a" and decision1!="b") :
        print "Invalid input, please re-enter your answer."
        decision1=raw_input ("Please select your move (a/b): ")
    if decision1=="a" :
        print "You start walking from your house. It is a long distance from your house to school. You start thinking what reason should explain to your teacher when you arrived in class and what punishment will you get from your teacher."
        print '--------------------------------------------------------------------------------'
        print "After 15 minutes of walking, u have arrived at the school gate but the gate was closed. The security guard near the gate is sleeping soundly hugging a teddy bear."
    if decision1=="b" :
        print "You immediately go and get the air pumper in your storeroom to pump your bike's tyres. While pumping the air to the tyres, you start thinking what reason should explain to your teacher when you arrived in class and what punishment will you get from your teacher."
        print '--------------------------------------------------------------------------------'
        print "After the tyres are fully pumped, you rush to school by riding your bike with high speed. In a short while, you have arrived at the school gate but the gate was closed. The security guard near the gate is sleeping soundly with a teddy bear on his hand."
    print "What to do?"
    print "a) Climb in illegally (You might get caught from climbing in)"
    print "b) Wake the guard by shouting (You might need a few minute to wake the guard)"
    print '--------------------------------------------------------------------------------'
    decision2=raw_input ("Please select your move (a/b): ")
    while (decision2!="a" and decision2!="b") :
        print "Invalid input, please re-enter your answer."
        decision2=raw_input ("Please select your move (a/b): ")
    if decision2=="a" :
        print "You are lucky, you sucessfully climb in and no ones caught you doing this."
    if decision2=="b" :
        print "You are lucky, the security guard woke up quickly after your first shouting."
    print '--------------------------------------------------------------------------------'
    print "You quickly run to your classroom. Teacher just started teaching when you arrived in class. Teacher ask for your reason why you are late fiercely and ready to punish you!"
    print "What to do?"
    print "a) Be honest (You might get a light punishment from your teacher)"
    print "b) Make up a reason (You might get a heavy punishment if you get caught by teacher that you are lying but you might avoid the punishment if your lie is convincing)"
    print '--------------------------------------------------------------------------------'
    decision3=raw_input ("Please select your move (a/b): ")
    while (decision3!="a" and decision3!="b") :
        print "Invalid input, please re-enter your answer."
        decision3=raw_input ("Please select your move (a/b): ")
    if decision3=="a" :
        point=point+25
        print "You received a light punishment which is standing during the first period since teacher knows that you are honest."
    if decision3=="b":
        print "You sucessfully avoided the punishment from your teacher because your lie is very convincing. But no matter how, you have a bad image in your friend's mind."
    print '--------------------------------------------------------------------------------'
    print "During class session, everyone are very concentrate on learning. Suddenly, fire alarm rang, you heard an announcement from your principal says:'EMERGENCY!EMERGENCY! Everyone, there are a bunch of zomb......' The principal did not finished his annoucement and was bitten by a zombie!"
    print "Whole class panic. What to do?"
    print "a) Run out of the class and try to survive by yourself (You might easily escape alone)"
    print "b) Stay and calm your classmate (You might help your clasmate but it is hard to escape with a group of people)"
    print '--------------------------------------------------------------------------------'
    decision4=raw_input ("Please select your move (a/b): ")
    while (decision4!="a" and decision4!="b") :
        print "Invalid input, please re-enter your answer."
        decision4=raw_input ("Please select your move (a/b): ")
    if decision4=="a" :
        print "You run to a nearest toilet to protect yourself by locking the door. While you are deciding for a further move, your classmate, John Cena who has been bullying you since first grade with a zombie chasing him into this toilet."
        print "What will you do?"
        print "a) Take the risk and help him out"
        print "b) Climb out through the window"
        print '--------------------------------------------------------------------------------'
        decision4a=raw_input ("Please select your move (a/b): ")
        while (decision4a!="a" and decision4a!="b") :
            print "Invalid input, please re-enter your answer."
            decision4a=raw_input ("Please select your move (a/b): ")
        if decision4a=="a" :
            point=point+25
            print "You and John Cena has killed the zombie by hitting the zombie with a mop and punch the zombie in the face"
            print "Suddenly, you heard there is voice shouting says that there is a safe house just at the backyard of the school. At the moment, John Cena request to follow you to the safe house because his leg was injured in the fight . But remember, he has always been bullying you since first grade."
            print "a) Leave John Cena and run toward the safe house by yourself"
            print "b) Forgive him and escape together"
            print '--------------------------------------------------------------------------------'
            decision4b=raw_input ("Please select your move (a/b): ")
            while (decision4b!="a" and decision4b!="b") :
                print "Invalid input, please re-enter your answer."
                decision4b=raw_input ("Please select your move (a/b): ")
            if decision4b=="a" :
                print "You just left John Cena alone because u cannot forgive what he did to u since first grade"
            if decision4b=="b" :
                point=point+25
                print "You forgive what he did in the past with kind-hearted and escape together."
        if decision4a=="b" :
            print "You just left John Cena with the zombie in the toilet."
            print "John Cena died from zombie"
            print '--------------------------------------------------------------------------------'
            print "You saw there is a safe house in the backyard and quickly run towards the safehouse. At the moment, you saw your teacher, Miss Elizabeth is pinning down by a zombie on the ground."
            print "What will you do?"
            print "a) Take the risk and help your teacher (The safe house might be full if you waste your time on helping her)"
            print "b) Ignore it and keep running (The zombie might chase you after attacking your teacher)"
            print '--------------------------------------------------------------------------------'
            decision4b=raw_input ("Please select your move (a/b): ")
            while (decision4b!="a" and decision4b!="b") :
                print "Invalid input, please re-enter your answer."
                decision4b=raw_input ("Please select your move (a/b): ")	
            if decision4b=="a" :
                point=point+25
                print "You decided to lend a hand to her and kill the zombie with a big stone."
            if decision4b=="b" :
                print "You freaked out to take the risk to help out. Your teacher is killed by the zombie"
    if decision4=="b" :
        point=point+25
        print "Everyone are very scare and shouting while suddenly, an annoying classmate of yours, Pheng who always screw up something in class decided to leave the class."
        print "What will you do?"
        print "a) Stop him, tell him we must work as a team and escape together"
        print "b) Ignore him and let him leave the class"
        print '--------------------------------------------------------------------------------'
        decision4a=raw_input ("Please select your move (a/b): ")
        while (decision4a!="a" and decision4a!="b") :
            print "Invalid input, please re-enter your answer."
            decision4a=raw_input ("Please select your move (a/b): ")	
        if decision4a=="a" :
            point=point+25
            print "You sucessfully persuade him to stay with the team."
            print '--------------------------------------------------------------------------------'
            print "Suddenly, a bunch of zombies rush in to attack us, and you remember there is a safe house at the backyard of the school."
            print "What will you do?"
            print "a) Run away and straight to the safe house because you are not confident in wining this fight"
            print "b) Take the risk and stay with your team to fight the zombies together"
            print '--------------------------------------------------------------------------------'
            decision4b=raw_input ("Please select your move (a/b): ")
            while (decision4b!="a" and decision4b!="b") :
                print "Invalid input, please re-enter your answer."
                decision4b=raw_input ("Please select your move (a/b): ")
            if decision4b=="a" :
                print "You decided to run away because you don't think that your classmate and you can take down all the zombies"
            if decision4b=="b" :
                point=point+25
                print "You decided to stay with the team and fight the zombies together."
        if decision4a=="b" :
            print "You just act like you do not know Pheng had ran out of the class."
            print '--------------------------------------------------------------------------------'
            print "Some other classmate also followed Pheng and ran out of the class. There are only few people left who stay back with you. Suddenly, there are a few of zombies are chasing Pheng's group. At the moment, you remember there is a safe house at the backyard of the school."
            print "What will you do?"
            print "a) Help Pheng's group to take down the zombies together"
            print "b) Leave Pheng's group and run to the safe house"	
            print '--------------------------------------------------------------------------------'
            decision4b=raw_input ("Please select your move (a/b): ")
            while (decision4b!="a" and decision4b!="b") :
                print "Invalid input, please re-enter your answer."
                decision4b=raw_input ("Please select your move (a/b): ")	
            if decision4b=="a" :
                point=point+25
                print "You can't just let your friend die from the zombie, so you decide to help Pheng's group to take down the zombie together."
            if decision4b=="b" :
                print "You do not want to help them because you do not want to take the risk."
    Bad = "When you are running towards the safe house, hundreds of zombies are chasing you to the safe house. In order to let you enter the safe house, they open the door and cause all the zombies to be able to rush into the safe house and killed everyone included you. In the end, everyone failed to escape from the zombies attack and died because of your selfishness."
    Semi_Bad ="When you are running towards the safe house, hundreds of zombies are chasing you to the safe house. You beg the people who are already in the safe house to open the door for you to enter. You straight rush into the safe house and kick those people out of the safe house and let the zombies change their target from you to them. At the end, your selfishness allowed you to survived but killed other people as a result."
    Semi_Good ="When you are running towards the safe house, hundreds of zombies are chasing you to the safe house. Because of your kind-hearted, you decided to sacrifices yourself by attracting te zombies to the other place. In the end , you died from the zombies attack but you have saved other people."
    Good="When you are running towards the safe house, hundreds of zombies are chasing you to the safe house. A lot of people come out from the safe house to help you and take down all the zombies. At the end, everyone survived from this zombies attack."
    if point<25 :
        Ending=Bad
    elif point<=50 :
        Ending=Semi_Bad
    elif point<=75 :
        Ending=Semi_Good
    else :
        Ending=Good
    print Ending   

    
UserAuthentication()
UserPreviousRecord()
CheckFile()
if CreateFile ==False:
    UserRecord()
UserStart()
while (PlayGame != False):
    story("a","b")
    UserSaveRecord()
    UserRecord()
    UserPlayAgain()
