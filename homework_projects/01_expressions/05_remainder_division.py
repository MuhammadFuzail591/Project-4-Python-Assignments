import math
def main():
   print("-------- REMAINDER DIVISION ---------")
   number_to_divide : float = float(input("Please enter an integer to be divided: "))
   number_ti_divide_by : float = float(input("Please enter an integer to divide by: "))
   
   division_result = math.floor(number_to_divide / number_ti_divide_by)
   
   remainder_result = number_to_divide % number_ti_divide_by

   print(f"The result of the division in {division_result} with a remainder a {remainder_result}")   



if __name__ == '__main__':
   main()