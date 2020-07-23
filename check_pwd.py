def check_pwd(password):
    # reject empty passwords
    if len(password) == 0:
        return False
    # reject passwords less than 8 characters
    if len(password) < 8:
        return False
    else:
        return True
