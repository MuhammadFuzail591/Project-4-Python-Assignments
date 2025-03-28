SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "
def main():
   adjective_input : str = input("Please input Adjective: ")
   noun_input : str = input("Please input Noun: ")
   verb_input : str = input("Please input Verb: ")

   print(f"{SENTENCE_START}{adjective_input} {noun_input} {verb_input + "!"} ")

if __name__ == '__main__':
   main()