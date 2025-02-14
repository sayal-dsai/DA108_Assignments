password_history = [] # maintains a list of all passwords user entered

is_strong = False # a boolean to check if the password is strong.

while not is_strong: # using a while loop to make sure the user enters a password before the program stops
    entered_password = input("Please enter a password: ")
    password_history.append(entered_password)
    password_length = len(entered_password)
    if password_length < 6:
        print("Your password is WEAK. Try again. Make it longer.") # Prompting user to make their password longer
        continue # I prefer using continue here, instead of putting the entire thing below into an else block
    # These four variables will check if the password has all the requirements
    has_special = False
    has_upper = False
    has_lower = False
    has_digit = False
    # Iterate over every character in the password
    for pwd_chr in entered_password:
        # Use python's inbuilt methods to check if the character is special, uppercase, lowercase or a digit
        # If it is, then mark the respective variable as True
        if not pwd_chr.isalnum():
            # Here, I have merely used a check to see if the character is not alphanumeric and defined that as special
            # If there had been an exhaustive list, the check would instead have been implemented as
            # if pwd_chr in special_char_list
            has_special = True
        elif pwd_chr.isupper():
            has_upper = True
        elif pwd_chr.islower():
            has_lower = True
        elif pwd_chr.isdigit():
            has_digit = True
    # Check if all four conditions are satisfied
    if has_special and has_upper and has_lower and has_digit:
        print("Your password is STRONG! Congratulations!")
        # Mark the password as strong. This will break the while loop
        is_strong = True
    else:
        # Instead of vaguely saying the password strength is medium, tell the user what the password lacks
        # So the user can add what's lacking
        print("Your password is MEDIUM. Try using some of the following:")
        whats_lacking = []
        if not has_special:
            whats_lacking.append('special characters')
        if not has_upper:
            whats_lacking.append('upper case characters')
        if not has_lower:
            whats_lacking.append('lower case characters')
        if not has_digit:
            whats_lacking.append('digits')
        for suggested_change in whats_lacking:
            print(suggested_change)