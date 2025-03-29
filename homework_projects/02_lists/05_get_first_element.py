def get_list():
   new_list = []
   elem : str = input("Enter an element or Press Enter to stop..: ")
   while elem != "":
      new_list.append(elem)
      elem : str = input("Enter an element or Press Enter to stop..: ")

   return new_list

def get_first_element(lst):
   return lst[0]

def main():
   my_list = get_list()
   first_element = get_first_element(my_list)
   print("The first element you have provided is: ",first_element)


if __name__ == '__main__':
    main()