'''
rock = 1
paper = 0
scissor = -1
'''
import random
computer = random.choice([0,1,-1])
youint= input("Enter your choice :")
youdict ={ 'scissor':-1, 'rock':1, 'paper':0 }
reversedict={ -1 :'scissor', 1:'rock', 0:'paper' }
you = youdict[youint]
print(f"you chose {youint} \n computer chose {reversedict[computer]}")
if(computer == you):
        print('draw')
elif(you ==1 and computer ==-1):
    print('You Win')
elif(you==1 and computer ==0):
        print('You Lose')
elif(you ==0 and computer ==1):
          print('You Win')
elif(you ==0 and computer==-1):
           print('You Lose')
elif(you ==-1 and computer ==0):
            print('You Win')
elif(you ==-1 and computer ==1):
            print('You Lose')
else:
        print("Something went wrong")
