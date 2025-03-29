def sumlist(numbers: list[int]):
   sum : int = 0
   for i in numbers:
      sum += i
   return sum

def main():
   my_list : list[int] = [1,2,3,4,5,6]
   result = sumlist(my_list)
   print(f"List: {my_list}\nSum: {result}")



if __name__ == '__main__':
    main()