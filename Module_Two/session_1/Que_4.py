# Que_4:- Create a new list called weekend_plan with at least 5 items representing things you want to do this weekend (mix of strings and numbers). Remove the last item using the pop() method and display the removed item and the updated list.

weekend_plan = ["Watch a movie", "Play cricket", 2, "Study Python", 500]

# Remove the last item
removed_item = weekend_plan.pop()

# Display the removed item
print("Removed item:", removed_item)

# Display the updated list
print("Updated list:", weekend_plan)