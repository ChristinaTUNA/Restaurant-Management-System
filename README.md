# 🍽️ Restaurant Management System (Python)

A console-based reservation and menu management system built as my **CSC1024 Programming Principles – Final Assessment (Year 1)**.  
The project simulates a restaurant system with booking, cancellation, meal recommendations, and file storage features.


## 🚀 Features
- Add, update, or cancel reservations  
- Validate input (name, date, session, pax, phone, email)  
- Manage session & seating limits (max 4 pax per booking, 8 reservations per session)  
- Display all reservations or specific details  
- Generate random meal recommendations  
- Save & load data from text files  


## 🛠️ Programming Techniques
- **Global data & dictionaries**: Track reservations, sessions, and seating  
- **Modules used**:  
  - `os` → clear screen  
  - `datetime` → date/time handling & validation  
  - `random` → meal recommendations  
- **File handling**: Load & save reservations and menu items (`.txt` files)  
- **Functions**: Organized into adding, canceling, updating, displaying, and recommendation generation  
- **Input validation**: Ensures proper format for names, dates, sessions, pax, phone numbers, and emails  



## ▶️ How to Run
1. Clone or download this repository  
2. Ensure `reservation_23028541.txt` and `menuItems_23028541.txt` exist in the same folder  
3. Run in terminal:
   ```bash
   python restaurant.py
