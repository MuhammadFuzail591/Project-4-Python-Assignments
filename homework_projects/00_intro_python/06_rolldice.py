import random


def dice_roll():
   dice1 : int = random.randint(1,6)
   dice2 : int = random.randint(1,6)
   return dice1, dice2

def main():
   print("------- ROLL DICE -------")
   
   dice1, dice2 = dice_roll()
   print(f"Dice 1: {dice1}")
   print(f"Dice 2: {dice2}")
   total = dice1 + dice2
   print(f"Total of two dice: {total}")
   


if __name__ == '__main__':
   main()
