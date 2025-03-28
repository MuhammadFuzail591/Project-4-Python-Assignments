import random

def dice_roll():
   dice1 : int = random.randint(1,6)
   dice2 : int = random.randint(1,6)
   print(f"Dice 1: {dice1} \n Dice 2: {dice2}")

def main():
   dice1 : int = 12

   print(f"Dice 1 in main before Function Call is {dice1}")
   dice_roll()
   dice_roll()
   dice_roll()
   print(f"Dice 1 in main is {dice1}")


if __name__ == '__main__':
   main()