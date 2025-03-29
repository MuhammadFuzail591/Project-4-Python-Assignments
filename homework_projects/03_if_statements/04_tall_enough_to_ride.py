# Extra Challenge
# def tall_enough_extension():
#    height : float = 0
#    while height!=50:
#       height_input : float = float(input("What is Your height..?"))
   
#    return height


def main():

   user_height : float = float(input("What's Your Height..? "))
   
   if(user_height>=50):
      print("You're tall enough to ride!")
   else:
      print("You're not tall enough to ride, but maybe next year!") 

if __name__ == '__main__':
    main()