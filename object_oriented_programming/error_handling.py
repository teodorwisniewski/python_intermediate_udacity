

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(ValueError):
    pass


def validate_password(username, password):
    if password == username:
        raise  InvalidPasswordError("Password is the same as the username. It is not allowed.")
    elif password in INVALID_PASSWORDS:
        raise InvalidPasswordError("Password is not legit. This password is forbidden.")





def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        validate_password(username, password)
    except InvalidPasswordError as e:
        print(e)
    else:
        account = create_account(username, password)
        print(f"The account for user:{username} was created.")
    finally:
        print("The username and password were checked.")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!