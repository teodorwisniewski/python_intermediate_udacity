

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(ValueError):
    pass

def validate_password(username, password):
    if password != username and password not in INVALID_PASSWORDS:
        return True
    elif password not in INVALID_PASSWORDS:
        raise InvalidPasswordError("password is not legit")
    else:
        raise  InvalidPasswordError("password is the same as the username. It is not allowed")



def create_account(username, password):
    return (username, password)


def main(username, password):
    valid = validate_password(username, password)

    if valid:
        account = create_account(username, password)
    else:
        print("Oh no!")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!