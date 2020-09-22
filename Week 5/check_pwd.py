def check_pwd(password):
    # list of allowed symbols
    valid_symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                     ')', '_', '+', '-', '=']
    # reject empty passwords
    if len(password) == 0:
        return False
    # reject passwords less than 8 characters
    # or greater than 20 characters
    if len(password) < 8 or len(password) > 20:
        return False
    # check for at least one lowercase letter-
    # if all chars in the password are uppercase
    if password.isupper():
        return False
    # check for at least one uppercase letter-
    # if all chars in the password are lowercase
    if password.islower():
        return False
    # check for at least one digit
    if not any(i.isdigit() for i in password):
        return False
    # check for at least one permitted symbol
    if not any(j in valid_symbols for j in password):
        return False
    else:
        return True
