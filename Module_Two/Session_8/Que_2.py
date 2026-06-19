# Que_2:- Create a function called format_username that takes a username (positional argument) and an optional prefix (default value 'user_'). The function should return the username with the prefix added. Test the function with and without providing the prefix.

def format_username(username, prefix="user_"):
    return prefix + username


# Calling function without providing prefix
print(format_username("vedant"))

# Calling function with a custom prefix
print(format_username("vedant", "admin_"))