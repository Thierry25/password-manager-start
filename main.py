from tkinter import *
from tkinter import messagebox
from password import password
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def get_generated_password():
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def retrieve_information():
    # There must have a check to make sure all the fields are filled
    entered_website = website_entry.get()
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    if len(entered_username) == 0 or len(entered_password) == 0 or len(entered_website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=entered_website, message=f"These are the details entered:"
                                                                      f" \nEmail:{entered_username}\n"
                                                                      f"Password:{entered_password}\n"
                                                                      f"Is it ok to save?")
        if is_ok:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            messagebox.showinfo(title="Success", message="Your password has been successfully saved")
            return f"{entered_website} => Username: {entered_username} => Password: {entered_password}\n"


def save_password():
    data = retrieve_information()
    if data is not None:
        f = open("data.txt", "a")
        f.write(data)
        f.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website information to be entered here
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

# Email/Username to be entered here
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.insert(0, "marcelinthierry@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

# Password to be entered here
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=get_generated_password)
generate_password.grid(row=3, column=2)

# Add button to local file
add_button = Button(text="Add", command=save_password)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
