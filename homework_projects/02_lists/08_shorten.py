MAX_LENGTH : int = 3

def get_list():
   new_list = []
   elem : str = input("Enter an element or Press Enter to stop..: ")
   while elem != "":
      new_list.append(elem)
      elem : str = input("Enter an element or Press Enter to stop..: ")

   return new_list


def list_shortener(lst):
   shorten_list = []
   while len(lst) > 3:
      shorten_list.append(lst.pop())

   return shorten_list

def main():
   list_input = get_list()
   print("List Provided: ", list_input)
   new_list = list_shortener(list_input)
   print("New List",new_list)
   print("Original List: ", list_input)


if __name__ == '__main__':
    main()
