from art import logo


def divide(n1,n2):
  return n1/n2
  # result_divide = first_num / second_num
  # print(f" {first_num} / {second_num} = {result_sub}")
  # return result_divide

def multiply(n1,n2):
  return n1 * n2
  # result_mul = first_num * second_num
  # print(f" {first_num} * {second_num} = {result_sub}")
  # return result_mul
def add(n1,n2):
  return n1+n2
  # result_add = first_num + second_num
  # print(f" {first_num} + {second_num} = {result_sub}")
  # return result_add
def subtract(n1,n2):
  return n1 - n2
  # result_sub = first_num - second_num
  # print(f" {first_num} - {second_num} = {result_sub}")
  # return result_sub

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print (symbol)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation : ")
    num2 = float(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
      
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type'y' to continue calculating with {answer}, or type n to  start a new calculation. : ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()      













 
  # if operation_symbol == '/':
  #   divide(n1,n2)
  # elif operation_symbol == '*':
  #   mul(n1,n2) 
  # elif operation_symbol == '+':
  #   add()
  # elif operation_symbol == '-':
  #   sub()
  # else:
  #   print("invalid action")



