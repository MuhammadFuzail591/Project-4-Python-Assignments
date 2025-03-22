def main():
   print("--------Farenheit To Celsius Convertor--------")
   farenheit_input : str = input("Enter Temperature in Farenheit  ")
   farenheit_temp : float = float(farenheit_input)

   to_celsius : float = (farenheit_temp - 32) * 5.0/9.0
   print(f"The {farenheit_temp}F is equals to {to_celsius}C")

   return

if __name__ == '__main__':
   main()