import sys 
def show_menu():
    print("Menu:")
    print("1. Multiplication")
    print("2. Subtraction")
    print("3. Addition")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Quit")
    
def input_num():
    
  number1 = float(input("Type the first number: "))
  number2 = float(input("Type the second number: "))
  return number1, number2    

def Multiplication(): 

  number1, number2 = input_num()
  print(f'The multiplication between {number1} and {number2} is: {number1 * number2}')

def Subtraction():
     
  number1, number2 = input_num()
  print(f'The subtraction between {number1} and {number2} is: {number1 - number2}')

def Addition():
     
  number1, number2 = input_num()
  print(f'The sum between {number1} and {number2} is: {number1 + number2}')
    
def Division():
     
  number1, number2 = input_num()
  print(f'The division between {number1} and {number2} is: {number1 / number2}')

def Exponentiation():
     
  number1, number2 = input_num()
  print(f'The exponentiation between {number1} and {number2} is: {number1 ** number2}')
    
    

def main():
    while True:
        show_menu()
        
        opcao = input("Pick an option: ")
        
        if opcao == "1":
            Multiplication()
        elif opcao == "2":
            Subtraction()
        elif opcao == "3":
            Addition()
        elif opcao == "4":
            Division()
        elif opcao == "5":
            Exponentiation()
        elif opcao == "6":
            sys.exit()
        else:
            print("Invalid option, try again.")

if name == "main":
    main()
