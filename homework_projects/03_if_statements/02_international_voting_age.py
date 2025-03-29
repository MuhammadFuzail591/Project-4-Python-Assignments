def main():
   age_input = int(input("How old are you...?: "))
   print(f"Your age is {age_input} So: ")
   if(age_input >= 16):
      print("You can vote in Peturksbouipo required age is 16")
   else:
      print("You cannot vote in Peturksbouipo required age is 16")

   if(age_input >= 25):
      print("You can vote in Stanlu required age is 25")
   else:
      print("You cannot vote in Stanlu required age is 25")

   if(age_input >= 45):
      print("You can vote in Stanlu required age is 45")
   else:
      print("You cannot vote in Stanlu required age is 45")


if __name__ == '__main__':
    main()