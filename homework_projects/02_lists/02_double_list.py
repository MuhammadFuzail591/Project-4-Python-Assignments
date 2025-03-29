def double_list(numbers: list[int]):
   list_length = len(numbers)
   
   for i in range(list_length):
      numbers[i] = numbers[i]*2
   
   return numbers

def main():
   my_list : list[int] = [1,2,3,4,5,6]
   result = double_list(my_list)
   print(f"Doubled List: {result}")



if __name__ == '__main__':
    main()