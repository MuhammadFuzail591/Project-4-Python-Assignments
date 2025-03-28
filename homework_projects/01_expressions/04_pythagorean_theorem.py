import math
def main():
   print("-------- PYTHAGOREAN THEOREM ---------")
   side_AB : float = float(input("Give the length of side AB : "))
   side_AC : float = float(input("Give the length of side AC : "))
   res : float = math.sqrt((side_AB**2) + (side_AC**2))
   
   side_BC = math.sqrt(res ** 2)

   print(f"Side BC: {side_BC}")



if __name__ == '__main__':
   main()