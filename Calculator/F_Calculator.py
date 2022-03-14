import re

#########################################################
####################### HELP MESSAGES ###################
#########################################################
def f_help():

    print("Letters and () is not avaible")
    print("Operations are done from left to right according to the order of the operation ")
    print("Operation avaible and their order: ")
    print(" 1 Exponential (^)")
    print(" 2 Multiply (*)")
    print(" 2 Division (/)")
    print(" 3 Addition (+)")
    print(" 3 Substraction (-)")


#########################################################


#########################################################
##################### READING VALIDATION ################
#########################################################

# Function to identify if there are letter in the operation
def is_operation(operation):

    reg_exp = r"[^\^+/*\-\d.]"
    return not (re.search(reg_exp,operation) is not None)

# Global checking

def Check_op(operation):
    # Checks for letters
    if is_operation(operation):

        # Check if the first sign is *, / o ^
        if operation[0] == "*" or operation[0] == "/" or operation[0] == "^":
            return False, None

        else:
            # Delete blanks
            operation_wb = operation.replace(" ","")
            return True,operation_wb

    else:
        return False, None
#########################################################

#########################################################
######## IDENTIFICATION OF NUMBERS AND SIGNS ############
#########################################################

def Id_Sig_Numb (operation_wb):

    regex = r"((([\^])|([*/]))|)(([+-]|)(\d+[.]\d+|\d+))"

    matches = re.finditer(regex, operation_wb, re.MULTILINE)

    Signs_exp = []
    Signs_md = []
    Numbers = []

    for matchNum, match in enumerate(matches, start=1):

        Signs_exp.append(match.group(3)) # List with signs ^
        Signs_md.append(match.group(4)) # List with signs *, /
        Numbers.append(float(match.group(5))) # List with number

    return Signs_exp,Signs_md,Numbers

########################################################
"""
#########################################################
###################### Operation ########################
#########################################################

# Exponential

def Exponetial():

# Multiply
def Multiply():

# Division
def Division():

########################################################
"""
