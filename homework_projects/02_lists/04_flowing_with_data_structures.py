def add_three_copies(list_input, msg):
   for i in range(3):
      list_input.append(msg)

def main():
   msg_input : str = input("Enter a message to copy: ")
   msg_list : list[str] = []
   print(f"List Before: {msg_list}")
   add_three_copies(msg_list, msg_input)

   print("After List: ",msg_list)

if __name__ == '__main__':
    main()