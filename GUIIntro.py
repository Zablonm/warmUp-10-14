import tkinter as tk

root = tk.Tk()
root.title("User Information Form")

label_name = tk.Label(root, text="Full Name")
label_country = tk.Label(root, text="Country")
label_age = tk.Label(root, text="Age")

entry_name = tk.Entry(root)
entry_country = tk.Entry(root)
entry_age = tk.Entry(root)

label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_country.grid(row=1, column=0, padx=10, pady=5)
entry_country.grid(row=1, column=1, padx=10, pady=5)

label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age.grid(row=2, column=1, padx=10, pady=5)

def submit_action():
    name = entry_name.get()
    country = entry_country.get()
    age = entry_age.get()
    print(f"Name: {name}, Country: {country}, Age: {age}")

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
