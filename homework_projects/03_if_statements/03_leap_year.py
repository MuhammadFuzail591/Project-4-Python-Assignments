def main():
   input_year = int(input("Enter year to check if leap or not: "))
   if(input_year%4==0 and input_year%100==0 and input_year%400==0 ):
      print(input_year, " is Leap Year")
   else:
      print(input_year, "is not a Leap Year")
if __name__ == '__main__':
    main()