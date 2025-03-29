def get_list():
   new_list = []
   elem : str = input("Enter an element or Press Enter to stop..: ")
   while elem != "":
      new_list.append(elem)
      elem : str = input("Enter an element or Press Enter to stop..: ")

   return new_list

def get_last_element(lst):
   last_elem = lst[len(lst) -1]
   return last_elem

def main():
   my_list = get_list()
   last_element = get_last_element(my_list)
   print("The Last element you have provided is: ",last_element)


if __name__ == '__main__':
    main()