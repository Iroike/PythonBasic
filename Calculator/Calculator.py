# Library
import cmath
import F_Calculator as cal

# Welcome message
print("WELCOME")
print("Instruction:")
print("Use -help to more information about operation")
print("Use cancel or exit to finish the calculator")
print("Letters and () is not avaible")



# Operating loop
while True:

    # Reading by keyboard
    operation = input("Introduce a operation: ")

    # Check stop
    if operation == "cancel" or operation == "exit":
        break

    # Check help
    elif operation == "-help":
        cal.f_help()

    else:
        # Check if is a operation
        is_operation, operation = cal.Check_op(operation)


        if is_operation:
            # Resolve operation
            print("Your operation is: ",operation)
            Signs_exp,Signs_md,Numbers = cal.Id_Sig_Numb(operation)

            ## Exponetial
            while True:
                if "^" in Signs_exp:
                    pos_exp = Signs_exp.index("^")

                    Numbers[pos_exp - 1] = Numbers[pos_exp - 1] ** Numbers[pos_exp]

                    Numbers.pop(pos_exp)
                    Signs_exp.pop(pos_exp)
                    Signs_md.pop(pos_exp)

                else:
                    break

            ## Multiply and Division
            while True:
                if ("*" not in Signs_md) and ("/" not in Signs_md):
                    break

                if ("*" in Signs_md):
                    pos_mul = Signs_md.index("*")
                else:
                    pos_mul = None

                if ("/" in Signs_md):
                    pos_div = Signs_md.index("/")
                else:
                    pos_div = None



                if pos_div is None:
                    Numbers[pos_mul - 1] = Numbers[pos_mul - 1] * Numbers[pos_mul]

                    Numbers.pop(pos_mul)
                    Signs_exp.pop(pos_mul)
                    Signs_md.pop(pos_mul)

                elif pos_mul is None:
                    Numbers[pos_div - 1] = Numbers[pos_div - 1] / Numbers[pos_div]

                    Numbers.pop(pos_div)
                    Signs_exp.pop(pos_div)
                    Signs_md.pop(pos_div)

                elif pos_div < pos_mul:
                    Numbers[pos_div - 1] = Numbers[pos_div - 1] / Numbers[pos_div]

                    Numbers.pop(pos_div)
                    Signs_exp.pop(pos_div)
                    Signs_md.pop(pos_div)

                elif pos_mul < pos_div:
                    Numbers[pos_mul - 1] = Numbers[pos_mul - 1] * Numbers[pos_mul]

                    Numbers.pop(pos_mul)
                    Signs_exp.pop(pos_mul)
                    Signs_md.pop(pos_mul)

            ## Addition and Substraction
            Result = 0
            for Number in Numbers:
                Result = Result + Number

            ## Result
            print("Result : ",Result)

        else:
            print("Not is a operation")

print("Goodbye")
