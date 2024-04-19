def get_next_input():
    """Function that returns the user's next input."""
    user_choice = int(input("Choose what to do next\n"
                            "1 - Display all packages and truck mileage\n"
                            "2 - Single package lookup for given time\n"
                            "3 - All package display for given time\n"
                            "4 - Exit the program\n"
                            "Input: "))
    return user_choice