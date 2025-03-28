def main():
   print("-------- ENERGY MASS EQUATION ---------")
   mass : float = float(input("Give the mass in KG: "))
   C : float = 299792458
   e : float = mass * (C * C )

   print(f"The Energy is equals to: {e}")





if __name__ == '__main__':
   main()