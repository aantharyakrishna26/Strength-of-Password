def strength_pass(password):
    user_points = 0
    user_feedback = []

    if len(password) >= 8:
        user_points += 1
    else:
        user_feedback.append("Password should be at least 8 characters long.")

    if any(char.isupper() for char in password):
        user_points += 1
    else:
        user_feedback.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        user_points += 1
    else:
        user_feedback.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        user_points += 1
    else:
        user_feedback.append("Add at least one digit.")

    if any(not char.isalnum() for char in password):
        user_points += 1
    else:
        user_feedback.append("Add at least one special character.")

    return user_points, user_feedback


password = input("Enter a password: ")
user_points, user_feedback = strength_pass(password)

if user_points <= 2:
    print("Password strength: Weak")
elif user_points <= 4:
    print("Password strength: Moderate")
else:
    print("Password strength: Strong")

if user_feedback:  #if not empty and has messages 
    print("\nSuggestions:")
    for suggestion in user_feedback:
        print("-", suggestion)
