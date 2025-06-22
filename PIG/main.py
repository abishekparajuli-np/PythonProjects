import random
max_score=100
class PIG:

    def __init__(self,player_names):
        self.names=player_names
        self.current_score=0
        self.total=[0 for _ in range(len(player_names))]
        self.indx=0

    
    def roll(self):
        return random.randint(1,6)
    
    def switch_turns(self):
        self.indx=(self.indx+1) % len(self.names)
        print("{} turn has sarted with total score= {} ".format(self.names[self.indx],self.total[self.indx]))
        self.play()


    def hold(self):
            self.total[self.indx]+=self.current_score
            print("{} has just ended his turn with score this round {} and total score {} ".format(self.names[self.indx],self.current_score,self.total[self.indx]))
            if self.total[self.indx]>=max_score:
                print("{} has won the game with Total Points={}".format(self.names[self.indx],self.total[self.indx]))
                exit()
            else:
                self.switch_turns()

    
    def play(self):
        self.current_score=0
        while True:
            _choice=input("{}, Do you want to roll or hold(roll/hold): ".format(self.names[self.indx])).lower().strip()
            if _choice == 'roll':
               num= self.roll()
               if num == 1:
                   print("Opps {} Rolled 1 your current score for the round is zero".format(self.names[self.indx]))
                   self.current_score=0
                   self.switch_turns()
               else:
                   self.current_score+=num
                   print("{} rolled {} .Round Total={}".format(self.names[self.indx],num,self.current_score))
            else:
                self.hold()
    


while True:
    try:
        players=int(input("Enter Number Of Players greater than 2: "))

        if players<2:
            print("Player must be more than 1")
            continue
        else:
            break

    except ValueError:
        print("Invalid Input")

player_names=[]
for value in range(players):
    name=input('Enter Player {} Name: '.format(value+1)).strip()
    player_names.append(name)

game=PIG(player_names)
game.play()



    







    