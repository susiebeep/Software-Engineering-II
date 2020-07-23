def check_pwd(password):
    # reject empty passwords
    if len(password) == 0:
        return False
    # reject passwords less than 8 characters
    # or greater than 20 characters
    if len(password) < 8 or len(password) > 20:
        return False
    else:
        return True
