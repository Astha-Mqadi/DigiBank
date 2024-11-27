import tkinter as tk
import customtkinter as ctk  # Assuming this is your custom module
import random
import string
import tkinter.messagebox as messagebox
from tkinter import messagebox

# Set appearance mode to dark
ctk.set_appearance_mode("dark")
# Set default color theme
ctk.set_default_color_theme("dark-blue")

# Create main window
root = ctk.CTk()
root.title("DIGITEK Bank")
root.geometry("1920x1080")
root.configure(fg_color="#1B1B26")

# Create a frame for the login area
frame = ctk.CTkFrame(root, fg_color="#1B1B26")
frame.pack(pady=80)

def generate_password():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
        if (any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password)):
            break
    password_entry_signup.delete(0, ctk.END)
    password_entry_signup.insert(0, password)

def toggle_password_visibility():
    if show_password_var.get():
        password_entry_signup.configure(show="")
        confirm_password_entry_signup.configure(show="")
    else:
        password_entry_signup.configure(show="*")
        confirm_password_entry_signup.configure(show="*")

def generate_account_number():
    return ''.join(random.choice(string.digits) for _ in range(10))

def validate_signup():
    username = username_entry_signup.get()
    password = password_entry_signup.get()
    confirm_password = confirm_password_entry_signup.get()
    pin_code = pin_entry_signup.get()
    opening_balance = balance_entry_signup.get()

    if not (username and password and confirm_password and pin_code and opening_balance):
        tk.messagebox.showerror("Error", "Please fill in all fields.")
        return False

    if password != confirm_password:
        tk.messagebox.showerror("Error", "Passwords do not match.")
        return False

    if len(username) < 5 or len(username) > 20:
        tk.messagebox.showerror("Error", "The username should be between at least 5 and 20 characters long.")
        return False

    if sum(char.isalpha() for char in username) < 3:
        tk.messagebox.showerror("Error", "The username should include at least 3 letters.")
        return False

    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    for account in accounts:
        account_info = account.strip().split(',')
        if account_info[0] == f"Username: {username}":
            tk.messagebox.showerror("Error", "The username already exists.")
            return False

    if len(pin_code) != 4 or not pin_code.isdigit():
        tk.messagebox.showerror("Error", "Pin code must be exactly 4 digits.")
        return False

    if len(password) < 8:
        tk.messagebox.showerror("Error", "Password should have a minimum of 8 characters.")
        return False

    if not any(char.islower() for char in password):
        tk.messagebox.showerror("Error", "Password needs to include at least a lowercase letter.")
        return False

    if not any(char.isupper() for char in password):
        tk.messagebox.showerror("Error", "Password needs to include at least an uppercase letter.")
        return False

    if not any(char.isdigit() for char in password):
        tk.messagebox.showerror("Error", "Password needs to include at least a number.")
        return False

    if not any(char in string.punctuation for char in password):
        tk.messagebox.showerror("Error", "Password needs to include at least a special character.")
        return False

    try:
        opening_balance = int(opening_balance)
    except ValueError:
        tk.messagebox.showerror("Error", "Opening balance must be a number.")
        return False

    if opening_balance < 20:
        tk.messagebox.showerror("Error", "Minimum Starting Balance is R20.")
        return False

    return True

def signup():
    for widget in frame.winfo_children():
        widget.destroy()

    signup_frame = ctk.CTkFrame(frame, fg_color="#222222", corner_radius=32, width=800, height=100)
    signup_frame.pack(pady=1, padx=80, fill='both', expand=True)

    signup_heading = ctk.CTkLabel(signup_frame, text="Sign Up", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#222222")
    signup_heading.pack(pady=5)

    global username_entry_signup, password_entry_signup, confirm_password_entry_signup, pin_entry_signup, balance_entry_signup, show_password_var

    username_label_signup = ctk.CTkLabel(signup_frame, text="Username:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    username_label_signup.pack(pady=4, padx=50, anchor='w')
    username_entry_signup = ctk.CTkEntry(signup_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=300, height=35, corner_radius=28)
    username_entry_signup.pack(pady=4, padx=50)

    password_label_signup = ctk.CTkLabel(signup_frame, text="Password:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    password_label_signup.pack(pady=4, padx=50, anchor='w')
    password_entry_signup = ctk.CTkEntry(signup_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), show='*', width=300, height=35, corner_radius=28)
    password_entry_signup.pack(pady=4, padx=50)

    confirm_password_label_signup = ctk.CTkLabel(signup_frame, text="Confirm Password:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    confirm_password_label_signup.pack(pady=4, padx=50, anchor='w')
    confirm_password_entry_signup = ctk.CTkEntry(signup_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), show='*', width=300, height=35, corner_radius=28)
    confirm_password_entry_signup.pack(pady=4, padx=50)

    show_password_var = tk.BooleanVar()
    show_password_checkbox = ctk.CTkCheckBox(signup_frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility, font=ctk.CTkFont('Helvetica', 12,'bold'))
    show_password_checkbox.pack(pady=1, padx=50)

    pin_label_signup = ctk.CTkLabel(signup_frame, text="Pin Code:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    pin_label_signup.pack(pady=4, padx=50, anchor='w')
    pin_entry_signup = ctk.CTkEntry(signup_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), show='*', width=300, height=35, corner_radius=28)
    pin_entry_signup.pack(pady=4, padx=50)

    balance_label_signup = ctk.CTkLabel(signup_frame, text="Opening Balance:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    balance_label_signup.pack(pady=4, padx=50, anchor='w')
    balance_entry_signup = ctk.CTkEntry(signup_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=300, height=35, corner_radius=28)
    balance_entry_signup.pack(pady=4, padx=50)

    generate_password_button = ctk.CTkButton(signup_frame, text="Generate Password", command=generate_password, corner_radius=32, width=260, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    generate_password_button.pack(pady=10, padx=50)

    submit_button_signup = ctk.CTkButton(signup_frame, text="Sign Up", command=lambda: create_account() if validate_signup() else None, corner_radius=32, width=260, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    submit_button_signup.pack(pady=10, padx=50)

    back_button_signup = ctk.CTkButton(signup_frame, text="Back", command=show_login_interface, corner_radius=32, width=260, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    back_button_signup.pack(pady=10, padx=50)

def create_account():
    username = username_entry_signup.get()
    password = password_entry_signup.get()
    pin_code = pin_entry_signup.get()
    opening_balance = balance_entry_signup.get()
    account_number = generate_account_number()

    with open("BankData.txt", "a") as file:
        file.write(f"Username: {username},Password: {password},Pin Code: {pin_code},Opening Balance: {opening_balance},Account Number: {account_number}\n")

    tk.messagebox.showinfo("Account Created", f"Account Created\nUsername: {username}\nPassword: {password}\nPin Code: {pin_code}\nOpening Balance: R{opening_balance}\nAccount Number: {account_number}")
    show_login_interface()

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
 
    if not (username and password):
        tk.messagebox.showerror("Error", "Please fill in all fields.")
        return False

    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    for account in accounts:
        account_info = account.strip().split(',')
        if account_info[0] == f"Username: {username}" and account_info[1] == f"Password: {password}" and account_info[2]:
            return True

    tk.messagebox.showerror("Login Failed", "You provided an invalid input.")
    return False

def login():
    if validate_login():
        open_account_window(username_entry.get())


def show_login_interface():
    for widget in frame.winfo_children():
        widget.destroy()

    # Adjust the size of the login frame
    login_frame = ctk.CTkFrame(frame, fg_color="#222222", corner_radius=32, width=800, height=400)
    login_frame.pack(pady=20, padx=70, fill='both', expand=True)

    welcome_label = ctk.CTkLabel(login_frame, text="DIGITEK BANKING", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#222222")
    welcome_label.pack(pady=20)

    instruction_label = ctk.CTkLabel(login_frame, text="Sign in to your account", font=ctk.CTkFont('Helvetica', 16,'bold'), fg_color="#222222")
    instruction_label.pack(pady=10)

    username_label = ctk.CTkLabel(login_frame, text="Username:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    username_label.pack(pady=10, padx=50, anchor='w')
    global username_entry
    username_entry = ctk.CTkEntry(login_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=300, height=35,corner_radius=28)
    username_entry.pack(pady=10, padx=50,)

    password_label = ctk.CTkLabel(login_frame, text="Password:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    password_label.pack(pady=10, padx=50, anchor='w')
    global password_entry
    password_entry = ctk.CTkEntry(login_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), show='*', width=300, height=35,corner_radius=28)
    password_entry.pack(pady=10, padx=50)

    login_button = ctk.CTkButton(login_frame, text="Login", command=login, corner_radius=32, width=260, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    login_button.pack(pady=10, padx=50)
    signup_button = ctk.CTkButton(login_frame, text="Sign Up", command=signup, corner_radius=32, width=260, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    signup_button.pack(pady=10, padx=50)

def open_account_window(username):
    for widget in frame.winfo_children():
        widget.destroy()

    account_frame = ctk.CTkFrame(frame, fg_color="#222222", corner_radius=32, width=800, height=600)
    account_frame.pack(pady=50, padx=70, fill='both', expand=True)

    welcome_label = ctk.CTkLabel(account_frame, text="Welcome to DIGITEK", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#222222")
    welcome_label.pack(pady=20, padx=20)
    
    username_label = ctk.CTkLabel(account_frame, text=f"{username}", font=ctk.CTkFont('Helvetica', 22, 'bold'), fg_color="#222222")
    username_label.pack(pady=10, padx=20)
    
    balance = get_balance(username)
    balance_label = ctk.CTkLabel(account_frame, text=f"Current Balance: R{balance:.2f}", font=ctk.CTkFont('Helvetica', 21,'bold'), fg_color="#222222")
    balance_label.pack(pady=20, padx=40)

    withdraw_button = ctk.CTkButton(account_frame, text="Withdraw", command=lambda: withdraw_window(username), corner_radius=32, width=250, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    withdraw_button.pack(pady=20, padx=40)

    transfer_button = ctk.CTkButton(account_frame, text="Transfer", command=lambda: transfer_window(username), corner_radius=32, width=250, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    transfer_button.pack(pady=20, padx=40)
    
    statement_button = ctk.CTkButton(account_frame, text="Bank Statement", command=lambda: bank_statement_window(username), corner_radius=32, width=250, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    statement_button.pack(pady=20, padx=40)

    logout_button = ctk.CTkButton(account_frame, text="Logout", command=show_login_interface, corner_radius=32, width=250, height=45, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    logout_button.pack(pady=20, padx=40)
    
def get_balance(username):
    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    for account in accounts:
        account_info = account.strip().split(',')
        if account_info[0] == f"Username: {username}":
            return float(account_info[3].split()[2])
    return None

def update_balance(username, new_balance):
    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    with open("BankData.txt", "w") as file:
        for account in accounts:
            account_info = account.strip().split(',')
            if account_info[0] == f"Username: {username}":
                account_info[3] = f"Opening Balance: {new_balance:.2f}"
                file.write(",".join(account_info) + "\n")
            else:
                file.write(account)
                
def withdraw_window(username):
    for widget in frame.winfo_children():
        widget.destroy()

    withdraw_frame = ctk.CTkFrame(frame, fg_color="#222222", corner_radius=28, width=800, height=400)
    withdraw_frame.pack(pady=50, padx=70, fill='both', expand=True)

    withdraw_label = ctk.CTkLabel(withdraw_frame, text="Withdraw", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#222222")
    withdraw_label.pack(pady=20, padx=20)

    amount_label = ctk.CTkLabel(withdraw_frame, text="Amount:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    amount_label.pack(pady=5, padx=20)
    amount_entry = ctk.CTkEntry(withdraw_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=260, height=35, corner_radius=28)
    amount_entry.pack(pady=10, padx=20)

    withdraw_button = ctk.CTkButton(withdraw_frame, text="Confirm", command=lambda: withdraw_amount(username, amount_entry.get()), corner_radius=32, width=240, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    withdraw_button.pack(pady=20, padx=20)

    back_button = ctk.CTkButton(withdraw_frame, text="Back", command=lambda: open_account_window(username), corner_radius=32, width=240, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    back_button.pack(pady=20, padx=20)

def withdraw_amount(username, amount):
    if not messagebox.askyesno("Confirm Withdrawal", "Would you like to make a withdrawal?"):
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    if amount <= 0:
        messagebox.showerror("Error", "Amount must be greater than zero.")
        return

    if amount < 20:
        messagebox.showerror("Error", "Minimum amount to withdraw is R20.")
        return

    balance = get_balance(username)
    if amount > balance:
        messagebox.showerror("Error", "Insufficient funds.")
        return

    new_balance = balance - amount
    update_balance(username, new_balance)
    
    with open("transactionlog.txt", "a") as file:
        file.write(f"{username} withdrew R{amount:.2f}. New balance: R{new_balance:.2f}\n")

    messagebox.showinfo("Withdrawal Successful", f"Successfully withdrew R{amount:.2f}. New balance: R{new_balance:.2f}")
    open_account_window(username)

def transfer_window(username):
    for widget in frame.winfo_children():
        widget.destroy()

    transfer_frame = ctk.CTkFrame(frame, fg_color="#222222", corner_radius=32, width=800, height=400)
    transfer_frame.pack(pady=50, padx=70, fill='both', expand=True)

    transfer_label = ctk.CTkLabel(transfer_frame, text="Transfer", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#222222")
    transfer_label.pack(pady=20, padx=20)
    
    username_label = ctk.CTkLabel(transfer_frame, text="Recipient Username:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    username_label.pack(pady=5, padx=20)
    username_entry = ctk.CTkEntry(transfer_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=260, height=35, corner_radius=28)
    username_entry.pack(pady=10, padx=20)

    recipient_label = ctk.CTkLabel(transfer_frame, text="Recipient Account Number:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    recipient_label.pack(pady=5, padx=20)
    recipient_entry = ctk.CTkEntry(transfer_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=260, height=35, corner_radius=28)
    recipient_entry.pack(pady=10, padx=20)

    amount_label = ctk.CTkLabel(transfer_frame, text="Amount:", font=ctk.CTkFont('Helvetica', 14,'bold'), fg_color="#222222")
    amount_label.pack(pady=5, padx=20)
    amount_entry = ctk.CTkEntry(transfer_frame, font=ctk.CTkFont('Helvetica', 14,'bold'), width=260, height=35, corner_radius=28)
    amount_entry.pack(pady=10, padx=20)

    transfer_button = ctk.CTkButton(transfer_frame, text="Confirm", command=lambda: validate_recipient(username, username_entry.get(), recipient_entry.get(), amount_entry.get()), corner_radius=32, width=240, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    transfer_button.pack(pady=20, padx=20)

    back_button = ctk.CTkButton(transfer_frame, text="Back", command=lambda: open_account_window(username), corner_radius=32, width=240, height=40, fg_color="#6A0DAD", hover_color="#551A8B", font=ctk.CTkFont('Helvetica', 14,'bold'))
    back_button.pack(pady=20, padx=20)


def validate_recipient(username, recipient_username, recipient_account, amount):
    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    for account in accounts:
        account_info = account.strip().split(',')
        if account_info[0] == f"Username: {recipient_username}" and account_info[-1] == f"Account Number: {recipient_account}":
            transfer_amount(username, recipient_username, recipient_account, amount)
            return
    messagebox.showerror("Error", "The Username does not belong to this account number.")

def transfer_amount(username, recipient_username, recipient_account, amount):
    if not messagebox.askyesno("Confirm Transfer", "Would you like to make a transfer?"):
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    if amount <= 0:
        messagebox.showerror("Error", "Amount must be greater than zero.")
        return

    if amount < 20:
        messagebox.showerror("Error", "Minimum amount to transfer is R20.")
        return

    sender_balance = get_balance(username)
    if amount > sender_balance:
        messagebox.showerror("Error", "Insufficient funds.")
        return

    sender_account = None
    recipient_balance = None
    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    for account in accounts:
        account_info = account.strip().split(',')
        if account_info[0] == f"Username: {username}":
            sender_account = account_info[-1].split(": ")[1]
        if account_info[-1] == f"Account Number: {recipient_account}":
            recipient_balance = float(account_info[3].split()[2])

    if recipient_account == sender_account:
        messagebox.showerror("Error", "You cannot transfer funds to your own account.")
        return

    if recipient_balance is None:
        messagebox.showerror("Error", "Recipient account not found.")
        return

    new_sender_balance = sender_balance - amount
    new_recipient_balance = recipient_balance + amount
    update_balance(username, new_sender_balance)
    update_balance_by_account_number(recipient_account, new_recipient_balance)

    with open("transactionlog.txt", "a") as file:
        file.write(f"{username} transferred R{amount:.2f} to {recipient_username}. New balance: R{new_sender_balance:.2f}\n")

    messagebox.showinfo("Transfer Successful", f"Successfully transferred R{amount:.2f} to {recipient_username}. New balance: R{new_sender_balance:.2f}")
    open_account_window(username)

def update_balance_by_account_number(account_number, new_balance):
    with open("BankData.txt", "r") as file:
        accounts = file.readlines()
    with open("BankData.txt", "w") as file:
        for account in accounts:
            account_info = account.strip().split(',')
            if account_info[-1] == f"Account Number: {account_number}":
                account_info[3] = f"Opening Balance: {new_balance:.2f}"
                file.write(",".join(account_info) + "\n")
            else:
                file.write(account)

def bank_statement_window(username):
    for widget in frame.winfo_children():
        widget.destroy()

    statement_label = ctk.CTkLabel(frame, text="Bank Statement", font=ctk.CTkFont('Helvetica', 24, 'bold'), fg_color="#1B1B26")
    statement_label.pack(pady=20)

    statement_text = ctk.CTkTextbox(frame, font=ctk.CTkFont('Helvetica', 16,'bold'), width=600, height=500)
    statement_text.pack(pady=10)

    with open("transactionlog.txt", "r") as file:
        transactions = file.readlines()

    user_transactions = [transaction for transaction in transactions if transaction.startswith(username)]
    statement_text.insert("1.0", "".join(user_transactions))
    statement_text.configure(state="disabled")

    back_button = ctk.CTkButton(frame, text="Back", command=lambda: open_account_window(username), corner_radius=20, width=240, height=45, fg_color="#6A0DAD", hover_color="#551A8B",font=ctk.CTkFont('Helvetica', 14,'bold'))
    back_button.pack(pady=10)

show_login_interface()
root.mainloop()