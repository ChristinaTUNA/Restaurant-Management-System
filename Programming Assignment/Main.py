'''CSC1024 Programming Principles
Development of A Restaurant Management System using Python'''

# modules that are allowed in the development of the project
import os
import random
import datetime
from datetime import datetime, timedelta

# Define global data to store reservations and menu items
reservation_data = []
menu_items = []
# Dictionary to track the number of reservations made for each session
session_count = {
    'session 1': 0,
    'session 2': 0,
    'session 3': 0,
    'session 4': 0}
# Dictionary to track the number of reservations made for each specific date and session combination
date_session_count = {}


# Function to clear the screen for better presentation
def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-based systems (Linux, macOS, etc.)
        os.system('clear')


# Function to load reservation data from the file
def load_reservation_data():
    with open("reservation_23028541.txt", "r") as file:
        data = file.readlines()
        data = [line.strip() for line in data if line.strip()]
    return data


# Function to load menu items from the file
def load_menu_items():
    with open("menuItems_23028541.txt", "r") as file:
        items = file.readlines()
        items = [item.strip() for item in items if item.strip()]
    return items


# Function to save reservation data to the file
def save_reservation_data():
    with open("reservation_23028541.txt", "a") as file:
        for reservation in reservation_data:
            file.write(reservation + "\n")


# Function to display ASCII art
def display_ascii_art():
    asciiART1 = '''
  ____ _                          _             
 / ___| |__   __ _ _ __ _ __ ___ (_)_ __   __ _ 
| |   | '_ \ / _` | '__| '_ ` _ \| | '_ \ / _` |
| |___| | | | (_| | |  | | | | | | | | | | (_| |
 \____|_| |_|\__,_|_|  |_| |_| |_|_|_| |_|\__, |
                                          |___/ 
 _____ _                            
|_   _| |__  _   _ _ __ ___   ___  
  | | | '_ \| | | | '_ ` _ \ / _ \   
  | | | | | | |_| | | | | | |  __/   
  |_| |_| |_|\__, |_| |_| |_|\___|   
             |___/
 _____          _   _             _    
|_   _| __ __ _| |_| |_ ___  _ __(_) __ _ 
  | || '__/ _` | __| __/ _ \| '__| |/ _` |
  | || | | (_| | |_| || (_) | |  | | (_| |
  |_||_|  \__,_|\__|\__\___/|_|  |_|\__,_|
  '''
    print(asciiART1)


# Function to display reservation conditions
def reservation_conditions():
    print("\nReservation Conditions:")
    print
    print("• Guests must make their reservations at least 5 days in advance.")
    print("• The restaurant seating accommodates a maximum of 4 pax in a group for a single reservation.")
    print()
    print("• The restaurant only serves 4 sessions each day:")
    print("  (1) 12:00 pm - 02:00 pm")
    print("  (2) 02:00 pm - 04:00 pm")
    print("  (3) 06:00 pm - 08:00 pm")
    print("  (4) 08:00 pm - 10:00 pm")
    print()
    print("• Each session can only accommodate 8 reservations.")


# Function to handle user input for the name in reservation
def get_reservation_name():
    while True:
        name = input("Name: ").upper()
        if name == '':
            print("Invalid input. Name cannot be empty.")
        elif any(char.isdigit() for char in name):
            print("Invalid input. Name cannot contain digits.")
        else:
            return name


# Function to handle user input for reservation date
def get_reservation_date():
    # Validate reservation date
    while True:
        date_str = input("Enter reservation date (YYYY-MM-DD): ")
        try:
            reservation_date = datetime.strptime(date_str, '%Y-%m-%d')
            current_date = datetime.now()

            if current_date <= reservation_date <= current_date + timedelta(days=5):
                print("Reservation must be made at least 5 days in advance")
                continue

            elif reservation_date <= current_date:
                print("The selected date has already passed Please choose a future date")
                continue

        except ValueError:
            print('Please enter the correct format (YYYY-MM-DD)')

        return reservation_date


# Function to handle user input for reservation session
def get_reservation_session(reservation_date):
    while True:
        session = int(input("Reservation session Number (ie.3): "))
        try:
            valid_sessions = [1, 2, 3, 4]
            if session not in valid_sessions:
                print("Invalid session Please choose from session 1, session 2, session 3, or session 4")
                continue

            # Check if the session is fully booked
            date_session_key = f"{reservation_date}|{session}"
            if date_session_key in date_session_count:
                if date_session_count[date_session_key] + 1 > 4:
                    print("Sorry, the maximum number of reservations for this date and session has been reached")
                    continue

            # Check if the session is fully booked for all slots
            if session_count[f'session {session}'] >= 8:
                print(f"Sorry, {session} is fully booked Please choose another session")
                continue

        except ValueError:
            print('Invalid input Enter only an integer')
            continue

        # Increment the count for the specific date and session combination
        date_session_count[date_session_key] = date_session_count.get(date_session_key, 0) + 1

        return session


# Function to handle user input for number of people in the reservation
def get_reservation_pax():
    while True:
        pax = int(input('Number of people: '))
        try:
            # Validate number of people
            if pax <= 0:
                print("Invalid number of people Please enter a positive value")
                continue

            if pax > 4:
                remaining_pax = pax - 4
                print(f"Maximum 4 persons per reservation Please book another slot for {remaining_pax} person(s)")
                continue

        except ValueError:
            print('Invalid input Enter only an integer')
            continue

        return pax


# Function to handle user input for phone number
def get_reservation_phone():
    while True:
        phone_number = input("Phone Number: ")
        try:
            # Check if the phone number has exactly 10 digits
            if len(phone_number) != 10:
                print('Invalid input Phone number must have 10 digits')
                continue

            # Check if the phone number starts with '0'
            elif phone_number[0] != '0':
                print('Invalid input Phone number must start with 0')
                continue

        # Check if the phone number consists only of digits
        except ValueError:
            print('Invalid input Please enter digits only')
            continue

        return phone_number


# Function to handle user input for email
def get_reservation_email():
    while True:
        email = input("Email: ").lower()

        # Check if "@" and "com" are both present in the email
        if "@" not in email or ".com" not in email:
            print("Invalid email format Please enter a valid email address")

        else:
            # If the email format is valid, return the email
            return email


# Function to add a new reservation based on user input
def add_reservation():
    print("Adding a new reservation:")
    name = get_reservation_name()
    reservation_date = get_reservation_date()
    session = get_reservation_session(reservation_date)
    pax = get_reservation_pax()
    email = get_reservation_email()
    phone_number = get_reservation_phone()

    reservation_data.append(f"{reservation_date}|Session {session}|{name}|{email}|{phone_number}|{pax}")
    print()
    print()
    print("Reservation added successfully!")
    print(reservation_data)


# Function to handle canceling a reservation
def cancel_reservation():
    print("Canceling a reservation:")
    name = input("Enter the name of the reservation to cancel: ").lower()
    canceled = False
    for reservation in reservation_data:
        reservation_details = reservation.split('|')
        if reservation_details[2].lower() == name.lower():
            reservation_data.remove(reservation)
            canceled = True
            break
    if canceled:
        print(f"Reservation for {name} canceled successfully!")
    else:
        print(f"No reservation found for {name}.")


# Function to handle user input for the number of dishes in the menu selection
def get_menu_selection_count():
    while True:
        num_dishes = int(input('How many dishes would you like to select? '))
        try:
            # Validate the number of dishes in the menu selection
            if num_dishes <= 0:
                print("Invalid number of dishes. Please enter a positive value")
                continue

        except ValueError:
            print('Invalid input. Enter only an integer')
            continue

        return num_dishes

# Function to generate meal recommendations
def generate_recommendations():
    selected_items = []
    num_dishes = get_menu_selection_count()

    print("Generating meal recommendations:")
    menu_items = load_menu_items()

    for i in range(num_dishes):
        if len(selected_items) == len(menu_items):
            # If all items are already selected, break the loop
            break

        # Get a random choice from the menu_items list
        selection = random.choice(menu_items)

        # Check if the choice has already been selected
        while selection in selected_items:
            selection = random.choice(menu_items)

        selected_items.append(selection)
        print(selection)
    # Your code to generate random meal recommendations


# Function to display all reservations
def display_all_reservations():
    print("Displaying all reservations:")
    with open("reservation_23028541.txt", "r") as file:
        for line in file:
            reservation_details = line.strip().split("|")
            print("Date:", reservation_details[0])
            print("Session:", reservation_details[1])
            print("Name:", reservation_details[2])
            print("Email:", reservation_details[3])
            print("Phone Number:", reservation_details[4])
            print("Number of People:", reservation_details[5])
            print("------------------------")


# Function to display reservation details for editing
def display_reservation_details():
    name = input("Enter the name of the reservation to display details: ").strip()
    found_reservation = None

    # Find the reservation based on the name
    for reservation in reservation_data:
        reservation_details = reservation.split('|')
        if reservation_details[2].lower() == name.lower():
            found_reservation = reservation
            break
    while True:
        if found_reservation is not None:
            reservation_date, session, name, email, phone_number, pax = found_reservation.split('|')
            print("Reservation Details:")
            print(f"Date: {reservation_date}")
            print(f"Session: {session}")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Phone Number: {phone_number}")
            print(f"Number of People: {pax}")
        else:
            print(f"No reservation found for {name}.")
        break


# Function to handle updating/editing a reservation
def update_reservation():
    name = input("Enter the name of the reservation to update: ").strip()
    found_reservation = None

    # Find the reservation based on the name
    for reservation in reservation_data:
        reservation_details = reservation.split('|')
        if reservation_details[2].lower() == name.lower():
            found_reservation = reservation
            break

    if found_reservation is not None:
        reservation_date, session, name, email, phone_number, pax = found_reservation.split('|')
        print("Current Reservation Details:")
        print(f"Date: {reservation_date}")
        print(f"Session: {session}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone Number: {phone_number}")
        print(f"Number of People: {pax}")

        # Prompt the user for changes
        print('')
        print('Update reservation:')
        print(f'[d] to update date \n[s] to update session\n[n] to update name\n[e] to update email\n[p] to update phone number\n[c] to cancel')
        update_choice = input("Enter the corresponding alphabet to update specific info: ").lower()

        if update_choice == 'd':
            new_reservation_date = get_reservation_date()
            reservation_data.remove(found_reservation)
            reservation_data.append(f"{new_reservation_date}|{session}|{name}|{email}|{phone_number}|{pax}")
            print("Reservation date updated successfully!")
        elif update_choice == 's':
            new_session = get_reservation_session(reservation_date)
            reservation_data.remove(found_reservation)
            reservation_data.append(f"{reservation_date}|Session {new_session}|{name}|{email}|{phone_number}|{pax}")
            print("Reservation session updated successfully!")
        elif update_choice == 'n':
            new_name = get_reservation_name()
            reservation_data.remove(found_reservation)
            reservation_data.append(f"{reservation_date}|{session}|{new_name}|{email}|{phone_number}|{pax}")
            print("Reservation name updated successfully!")
        elif update_choice == 'e':
            new_email = get_reservation_email()
            reservation_data.remove(found_reservation)
            reservation_data.append(f"{reservation_date}|{session}|{name}|{new_email}|{phone_number}|{pax}")
            print("Reservation email updated successfully!")
        elif update_choice == 'p':
            new_phone_number = get_reservation_phone()
            reservation_data.remove(found_reservation)
            reservation_data.append(f"{reservation_date}|{session}|{name}|{email}|{new_phone_number}|{pax}")
            print("Reservation phone number updated successfully!")
        elif update_choice == 'x':
                new_pax = get_reservation_pax()
                reservation_data.remove(found_reservation)
                reservation_data.append(f"{reservation_date}|{session}|{name}|{email}|{phone_number}|{new_pax}")
        elif update_choice == 'c':
            print("Reservation update canceled.")
        else:
            print("Invalid choice. Update canceled.")
    else:
        print(f"No reservation found for {name}.")


# Function to handle user input and execute the corresponding action
def handle_user_input():
    while True:
        print()
        print()
        choice = input("Enter 1-6 to go to a specific section: ")
        
        if choice == "1":
            add_reservation()
        elif choice == "2":
            cancel_reservation()
        elif choice == "3":
            update_reservation()
        elif choice == "4":
            display_all_reservations()
        elif choice == "5":
            generate_recommendations()
        elif choice == "6":
            save_reservation_data()
            quit_session()
            break
        else:
            print("Invalid choice. Please choose again.")


# Function to display the main menu
def display_main_menu():
    print("===== Charming Thyme Trattoria Management System =====")
    print("[1] Add Reservation(s)")
    print("[2] Cancel Reservation(s)")
    print("[3] Update/Edit Reservation(s)")
    print("[4] Display All Reservations")
    print("[5] Generate Meal")
    print("[6] Exit")
    print("======================================================")


# Function to move to next page
def next_page(pages):
    button_label = "Next"
    print()
    print()
    print(f"[{button_label}]")
    while True:
        user_input = input("Press Enter to continue or 'q' to quit: ").lower()
        if user_input == 'q':
            quit_session()
            break

        elif user_input == '':
            clear_screen()
            pages()
            break

        else:
            clear_screen()
            print('INVALID INPUT')


# Function to handle the reservation process
def reservation_process():
    next_page(reservation_conditions)
    add_reservation()
    next_page(display_main_menu)
    handle_user_input()


# Function to display the summary of a specific reservation
def display_booking_summary(reservation):
    print("===== Booking Summary =====")
    for reservation in reservation_data:
        reservation_details = reservation.split('|')
        print(f"Date: {reservation_details[0]}")
        print(f"Session: {reservation_details[1]}")
        print(f"Name: {reservation_details[2]}")
        print(f"Email: {reservation_details[3]}")
        print(f"Phone Number: {reservation_details[4]}")
        print(f"Number of People: {reservation_details[5]}")
        print("------------------------")
    

# Function to quit the reservation process
def quit_session():
    clear_screen()
    print('❤ ❤ ❤\nThank you for using our reservation system.\nWe appreciate your visit. Please come again!\n❤ ❤ ❤')

# MAIN PROGRAM
def main():
    display_ascii_art()
    reservation_data = load_reservation_data()
    menu_items = load_menu_items()
    reservation_process()
    display_booking_summary(reservation_data)

    return reservation_data, menu_items

main()