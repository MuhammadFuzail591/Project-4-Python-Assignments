def main():
   print("-------- This program is to Add Two numbers -------")
   num1_input : str = input("Enter First Number:")
   num1 : int = int(num1_input)
   num2_input : str = input("Enter Second Number:")
   num2 : int = int(num2_input)
   sum : int = num1 + num2

   print(f"The sum of {num1} and {num2} is {sum}")
   return 


if __name__ == '__main__':
   main()
