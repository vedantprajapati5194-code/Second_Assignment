# Que_3:- Build a function book_movie_ticket(movie_name, seat_type='Regular', snacks=None) that prints a booking summary. Call the function using only positional arguments, only keyword arguments, and a mix of both to book tickets for 'Jawan' and 'Pathaan' with different seat types and snacks.<br><br><em><strong>Hint:</strong> Try calling book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')</em>

def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie Name :", movie_name)
    print("Seat Type  :", seat_type)
    print("Snacks     :", snacks)
    print("-" * 25)


# 1. Using only positional arguments
book_movie_ticket("Jawan", "VIP", "Popcorn")

# 2. Using only keyword arguments
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="Premium",
    snacks="Nachos"
)

# 3. Using a mix of positional and keyword arguments
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")