from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)


# Add pyperclip if you want to autocopy to clipboard the password after its generated

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web_value = web_entry.get()
    email_value = email_username_entry.get()
    password_value = password_entry.get()

    new_data = {
        web_value: {
            "email":email_value,
            "password":password_value,
        }
    }

    if len(web_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Ooops",message="Make sure your website/email/password not empty")
        return
    else:
        try:
            data_file = open("data.json", "r") 
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
            
        else:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            data_file.close()
            web_entry.focus()

# ---------------------------- SEARCH EMAIL AND PASSWORD ------------------------------- #
def find_password():
    try:
        data_file = open("data.json", "r")
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File Not Found.")
    else:
        data = json.load(data_file)
        web_name = web_entry.get()
        try:
            email_val = data[web_name]["email"]
            password_val = data[web_name]["password"]
        except KeyError:
            messagebox.showinfo(title="Error",message=f"Key Error, no details for the {web_name}, maybe you haven't save it.")
        else:
            messagebox.showinfo(title=f"{web_name}",message=f"Email: {email_val}\nPassword: {password_val}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Label and Entry
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
web_entry = Entry(width=26)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=26)
password_entry.grid(column=1, row=3)

# button
search_btn = Button(text="Search", command=find_password)
search_btn.config(font=('Arial', 5), width=10)
search_btn.grid(column=2, row=1)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.config(font=('Arial', 5), width=10)
generate_btn.grid(column=2, row=3)


add_btn = Button(text="Add", width=32, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()