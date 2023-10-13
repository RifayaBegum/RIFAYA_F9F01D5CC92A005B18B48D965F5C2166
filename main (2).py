''' implement a class called player that represents a cricket player.the player class should have a 
method called play() which prints "the player is playing cricket". Derive two classes,Batsman and 
Bowler from the player class.Override the play() method in each derived class to print"The batsman 
is batting" and "the bowler is bowling", respectively. writ a program to create objects of both the 
batsman and bowler classes and call the play() method for each object.'''


# Define the base class player
class Player:
  def play(self):
    print(" The player is playing cricket.")
    
# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting. ")

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling. ")
      
# Create objects of Batsman and Bowler classes
batsman = Batsman() 
bowler = Bowler() 

# Call the play() method for each object
batsman.play() 
bowler.play() 