import random

DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60



def main():
   print("------- SECONDS IN YEAR -------")
   
   seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

   print(f"Seconds in Year: {seconds_in_year}")
   


if __name__ == '__main__':
   main()