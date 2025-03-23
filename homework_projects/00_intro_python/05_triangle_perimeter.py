def main():
   print("------ TRIANGLE PERIMETER CALCULATOR -------")
   side_1 : float = float(input("Enter The Length of Side a (side) "))
   side_2 : float = float(input("Enter The Length of Side b (side) "))
   side_3 : float = float(input("Enter The Length of Side c "))

   perimeter = side_1 + side_2 + side_3


   print(f"The perimeter of triangle with given sides is {perimeter}")

if __name__ == '__main__':
   main()