#This function adds two numbers
def addition(num1,num2):
    return num1+num2

# This function subtracts two numbers
def subtraction(num1,num2):
    return num1-num2

# This function multiplies two numbers
def multiplication(num1,num2):
    return num1*num2

# This function divides two numbers
def division(num1,num2):
    return num1/num2

# This function calculates
def calculate():
    # Take input from the user
    print('Select operation:\n+ -->for addition  - -->for subtraction  * -->for multiplication  / -->for division')
    operation=input('Enter your Choice: ')

    #Check if choice is one of the four options
    if(operation in ['+','-','*','/']):
        num1=float(input('Enter your first number: '))
        num2=float(input('Enter your second number: '))

        #Display the calculated number
        if operation=='+':
            print('{}+{}={}'.format(num1,num2,addition(num1,num2)))
        elif operation=='-':
            print('{}-{}={}'.format(num1,num2,subtraction(num1,num2)))
        elif operation=='*':
            print('{}*{}={}'.format(num1,num2,multiplication(num1,num2)))
        else:
            print('{}/{}={}'.format(num1,num2,division(num1,num2)))

    #If choice is not one of the four options
    else:
        print('You have not typed a valid operato')


new_operation=True
while(new_operation):
    calculate()
    #check if user wants another calculation
    next_operation=input('Do you want to make a new calculation? yes/no :')
    if next_operation=='no':
        new_operation==False
