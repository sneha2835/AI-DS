def book_seat(booked_seats, total_seats, seat_to_book):
    if seat_to_book > total_seats or seat_to_book in booked_seats:
        print(f"Seat {seat_to_book} cannot be booked.")
    else:
        booked_seats.append(seat_to_book)
       

def cancel_seat(booked_seats, seat_to_cancel):
    if seat_to_cancel in booked_seats:
        booked_seats.remove(seat_to_cancel)
   

# input 
total_seats = 10
booked_seats = [2, 5, 7]
seat_to_book = 3 
seat_to_cancel = 5

# booking and cancelling seats
book_seat(booked_seats, total_seats, seat_to_book)
cancel_seat(booked_seats, seat_to_cancel)

# calculate available seats
available_seats = [i for i in range(1, total_seats + 1) if i not in booked_seats]
print(f"Available seats: {available_seats}")
