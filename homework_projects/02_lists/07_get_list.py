def get_list():
   new_list = []
   elem : str = input("Enter an element or Press Enter to stop..: ")
   while elem != "":
      new_list.append(elem)
      elem : str = input("Enter an element or Press Enter to stop..: ")

   return new_list

def main():
   final_list = get_list()
   print("The list provided by you is: ", final_list)

if __name__ == '__main__':
    main()
