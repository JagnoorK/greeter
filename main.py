from tkinter import *
import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

my_email = "ms2351491@gmail.com"
password = "wvgt vwwl hzwx suto"
time = dt.datetime.now()
today = time.weekday()

with open("quotes.txt", encoding='utf-8') as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)


def send():
    name = name_entry.get()
    subject = subject_entry.get()
    receiver = email_entry.get()
    if today == 5:

        message = MIMEText(f"Subject: {subject}\n\nHey {name}\n\nWish you very happy birthday dear", _charset="utf-8")
        submit(receiver, message)
    else:
        message = MIMEText(f"Subject: {subject}\n\nHey {name}\n\nTODAY'S quote\n\n{quote}", _charset="utf-8")
        submit(receiver, message)


def submit(receiver, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver, msg=message.as_string())
        connection.close()


window = Tk()

window.title("Greeter")
window.config(padx=50, pady=30, bg="white")  # Adjusted padx value

label = Label(text="Greetings Made Easy", bg="white", fg="black", font=("Noto Serif", 30, "bold"))
label.grid(column=1, row=0, columnspan=3, pady=(0, 20))

image1 = PhotoImage(file="greetings.png")

canvas = Canvas(width=590, height=650, bg="white", highlightthickness=0)
canvas.create_image(300, 330, image=image1)
canvas.grid(column=0, row=1, rowspan=6, padx=30)  # Adjusted padx value

text_label = Label(text="yes", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
text_label.grid(column=2, row=1, sticky="W", pady=(0, 10), padx=90, columnspan=3)

text_label2 = Label(text="Information ", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
text_label2.grid(column=3, row=1, sticky="W", pady=(0, 10))

# Receiver Information Form
name_label = Label(text="Name:", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
name_label.grid(column=3, row=2, sticky="W", pady=(0, 5))

name_entry = Entry(width=20, font=("Noto Serif", 15, "bold"))
name_entry.grid(column=4, row=2, sticky="W", pady=(0, 5))

email_label = Label(text="Email:", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
email_label.grid(column=3, row=3, sticky="W", pady=(0, 5))

email_entry = Entry(width=20, font=("Noto Serif", 15, "bold"))
email_entry.grid(column=4, row=3, sticky="W", pady=(0, 5))

subject_label = Label(text="Subject:", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
subject_label.grid(column=3, row=4, sticky="W", pady=(0, 5))

subject_entry = Entry(width=20, font=("Noto Serif", 15, "bold"))
subject_entry.grid(column=4, row=4, sticky="W", pady=(0, 5))

type_label = Label(text="Type:", fg="pink", bg="black", font=("Noto Serif", 15, "bold"))
type_label.grid(column=3, row=5, sticky="W", pady=(0, 5))

type_entry = Entry(width=20, font=("Noto Serif", 15, "bold"))
type_entry.grid(column=4, row=5, sticky="W", pady=(0, 5))

submit_button = Button(text="Send", highlightthickness=0, font=("Noto Serif", 15), command=send)
submit_button.grid(column=3, row=6, sticky="W", pady=(10, 0))

window.mainloop()
