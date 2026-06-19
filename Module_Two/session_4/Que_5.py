# Que_5:-Take a tuple of your last 7 WhatsApp call durations in minutes (e.g., (12, 5, 0, 20, 7, 3, 15)), convert it to a list, remove all calls shorter than 5 minutes, then convert it back to a tuple and print the result.<br><br><em><strong>Hint:</strong> Use a for loop or list comprehension to filter the list before converting back to tuple.</em>

call_durations = (12, 5, 0, 20, 7, 3, 15)

# Convert tuple to list
call_list = list(call_durations)

# Keep only calls that are 5 minutes or longer
call_list = [call for call in call_list if call >= 5]

# Convert back to tuple
call_durations = tuple(call_list)

print(call_durations)