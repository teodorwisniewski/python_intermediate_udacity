"""Write a function that prints a profile, given values."""


def create_profile(given_name, *surnames, **details):
    print(given_name, *surnames)
    for key, value in details.items():
        print(key, value, sep=": ")


if __name__ == '__main__':
    create_profile('Sam')
    # Sam

    create_profile('Sam', role='Instructor')
    # Sam
    # role: Instructor

    create_profile('Martin', 'Luther', 'King', 'Jr', born=1929, died=1968)
    # Martin Luther King Jr.
    # born: 1929
    # died: 1968

    create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")
    # Sebastian Thrun
    # cofounded: Udacity
    # experience: Stanford Professor




    # create_profile("Sam")
    # create_profile("Martin", "Luther", "King", "Jr.", born=1929, died=1968)
    # create_profile("Sebastian", "Thrun", cofounded="Udacity", experience="Stanford Professor")

