import requests
from tkinter import *
import tkinter.messagebox


# Create a class that represents our Frame. It inherits from the Tkinter Frame class.

class Application:
    def __init__(self, windows):

        self.windows = windows
        self.windows.geometry("500x400")
        self.windows.resizable(False, False)
        self.menubar = Menu(windows)
        self.rentmenu = Menu(self.menubar, tearoff=0)
        self.rentmenu.add_command(label="Renting Car",command=self.rental_menu)
        self.rentmenu.add_command(label="Customer",command=self.customer_menu)
        self.rentmenu.add_separator()
        self.rentmenu.add_command(label="Exit",command=self.onExit)
        self.menubar.add_cascade(label="Main", menu=self.rentmenu)
        windows.config(menu=self.menubar)
        # Creating a label
        self.frame=Frame(self.windows, width=700, height=600, bg='snow3')
        self.frame.pack()
        self.label = Label(self.frame, text="Welcome to Car Rental System",wraplength=250,justify=LEFT,foreground="blue",background="khaki",font=("Courier",18,"italic"))
        self.label.pack()
        #...............Adding Photo...........
        self.logo = PhotoImage(file='rent.gif')
        self.label.config(image=self.logo)
        self.label.config(compound="left")
        # with compund parameter we can arrange the position of the label text and image
        # In order to make the image to be shown in the label, we need to make some changes below:
        self.label.img = self.logo
        self.label.config(image=self.label.img)  # now we have done the image stable than before
        self.windows.mainloop()
        # .......................Car Renting Section............................................
    def onExit(self):
        quit()

    def rental_menu(self):
        self.window= Toplevel()
        self.window.geometry("1357x759")
        self.window.resizable(False, False)
        self.left = Frame(self.window, width=800, height=720, bg='snow3')
        self.left.pack(side=LEFT)

        self.right = Frame(self.window, width=600, height=720, bg='snow3')
        self.right.pack(side=RIGHT)

        self.title = Label(self.left, text="Car Renting Section", font=('georgia 28 bold'), fg='black',bg="khaki1")
        self.title.place(x=0, y=0)
        self.m = Label(self.left, text="Car Model", font=('georgia 14 bold'), fg='black')
        self.m.place(x=0, y=100)
        self.s = Label(self.left, text="Start Date", font=('georgia 14 bold'), fg='black')
        self.s.place(x=0, y=140)

        self.stop = Label(self.left, text="Stop Date", font=('georgia 14 bold'), fg='black')
        self.stop.place(x=0, y=180)

        self.price = Label(self.left, text="Price", font=('georgia 14 bold'), fg='black')
        self.price.place(x=0, y=220)

        self.cus = Label(self.left, text="Customer ID", font=('georgia 14 bold'), fg='black')
        self.cus.place(x=0, y=260)

        self.modeltextentry1 = Entry(self.left, width=30)
        self.modeltextentry1.place(x=250, y=100)

        self.starttextentry1 = Entry(self.left, width=30)
        self.starttextentry1.place(x=250, y=140)

        self.stoptextentry1 = Entry(self.left, width=30)
        self.stoptextentry1.place(x=250, y=180)

        self.pricetextentry1 = Entry(self.left, width=30)
        self.pricetextentry1.place(x=250, y=220)

        self.customeridtextentry1 = Entry(self.left, width=30)
        self.customeridtextentry1.place(x=250, y=260)

        self.submit = Button(self.left, text="Add Renting", width=20,height=2, bg='white', command=self.add_new_rental)
        self.submit.place(x=260, y=300)

        #......................Editing Rental Data Section............................................


        self.rentid = Label(self.right, text="Rental ID", font=('arial 14 bold'))
        self.rentid.place(x=0, y=100)

        self.m = Label(self.right, text="Car Model", font=('arial 14 bold'), fg='black')
        self.m.place(x=0, y=140)

        self.s = Label(self.right, text="Start Date", font=('georgia 14 bold'), fg='black')
        self.s.place(x=0, y=180)

        self.stop = Label(self.right, text="Stop Date", font=('georgia 14 bold'), fg='black')
        self.stop.place(x=0, y=220)

        self.price = Label(self.right, text="Price", font=('georgia 14 bold'), fg='black')
        self.price.place(x=0, y=260)

        self.cus = Label(self.right, text="Customer ID", font=('georgia 14 bold'), fg='black')
        self.cus.place(x=0, y=300)

        self.rentidtextentry = Entry(self.right, width=30)
        self.rentidtextentry.place(x=280, y=100)

        self.modeltextentry = Entry(self.right, width=30)
        self.modeltextentry.place(x=280, y=140)

        self.starttextentry = Entry(self.right, width=30)
        self.starttextentry.place(x=280, y=180)

        self.stoptextentry = Entry(self.right, width=30)
        self.stoptextentry.place(x=280, y=220)

        self.pricetextentry = Entry(self.right, width=30)
        self.pricetextentry.place(x=280, y=260)

        self.customeridtextentry = Entry(self.right, width=30)
        self.customeridtextentry.place(x=280, y=300)

        self.submit2 = Button(self.right, text="Edit Renting", width=20, height=2, bg='white', command=self.edit_rental)
        self.submit2.place(x=300, y=340)

        # ......................Deleting Rental Data Section............................................

        self.rentid2 = Label(self.left, text="Rental ID", font=('arial 14 bold'))
        self.rentid2.place(x=0, y=500)
        self.rentalid2textentry = Entry(self.left, width=30)
        self.rentalid2textentry.place(x=250, y=500)
        self.submit3 = Button(self.left, text="Delete Renting", width=20, height=2, bg='white', command=self.delete_rental)
        self.submit3.place(x=260, y=540)

         #............................Defining Functions...........................
    def add_new_rental(self):
        self.value1 = self.modeltextentry1.get()
        self.value2 = self.starttextentry1.get()
        self.value3 = self.stoptextentry1.get()
        self.value4 = self.pricetextentry1.get()
        self.value5 = self.customeridtextentry1.get()
        if self.value1 == '' or self.value2 == '' or self.value3 == '' or self.value4 == '' or self.value5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            self.comment = {"model": self.value1, "rentStartDate": self.value2,
                       "rentEndDate": self.value3,"price": self.value4,"customer_id":self.value5}
            self.result = requests.post("http://localhost:5000/rentals/", json=self.comment)
            if self.result.status_code == 201:
                self.comment2 = self.result.json()
                tkinter.messagebox.showinfo(f"Added Rental Successfully")
            else:
                tkinter.messagebox.showinfo(f"Post Request failed with status : {self.result.status_code}")


    def edit_rental(self):
        self.value6= self.rentidtextentry.get()
        self.value1 = self.modeltextentry.get()
        self.value2 = self.starttextentry.get()
        self.value3 = self.stoptextentry.get()
        self.value4 = self.pricetextentry.get()
        self.value5 = self.customeridtextentry.get()
        self.rentals = requests.get(f"http://localhost:5000/rentals/{self.value6}")
        if self.rentals.status_code == 200:
            self.comment = {"id":self.value6,"model": self.value1, "rentStartDate": self.value2,
                            "rentEndDate": self.value3, "price": self.value4, "customer_id": self.value5}
            self.result = requests.put(f"http://localhost:5000/rentals/{self.value6}", json=self.comment)
            if self.result.status_code == 200:
                print(f"{self.result.status_code} OK")
                tkinter.messagebox.showinfo(f"Editted Rental successfully ")
        else:
            tkinter.messagebox.showinfo("Rental not found, please enter correct rental ID!")

    def delete_rental(self):
        self.value = self.rentalid2textentry.get()
        self.rental = requests.delete(f"http://localhost:5000/rentals/{self.value}")
        if self.rental.status_code == 200:
            tkinter.messagebox.showinfo("Rental was removed successfully")
        else:
            tkinter.messagebox.showinfo("Rental not found")


    def customer_menu(self):

        self.window = Toplevel()
        self.window.geometry("1357x759")
        self.window.resizable(False, False)
        self.left = Frame(self.window, width=800, height=720, bg='snow3')
        self.left.pack(side=LEFT)

        self.right = Frame(self.window, width=600, height=720, bg='snow3')
        self.right.pack(side=RIGHT)

        self.title = Label(self.left, text="Customer Section", font=('georgia 28 bold'), fg='black', bg="khaki1")
        self.title.place(x=0, y=0)
        self.name = Label(self.left, text="Fullname", font=('georgia 14 bold'), fg='black')
        self.name.place(x=0, y=100)
        self.address = Label(self.left, text="Address", font=('georgia 14 bold'), fg='black')
        self.address.place(x=0, y=140)
        self.phone = Label(self.left, text="Phone Number", font=('georgia 14 bold'), fg='black')
        self.phone.place(x=0, y=180)
        self.city = Label(self.left, text="City", font=('georgia 14 bold'), fg='black')
        self.city.place(x=0, y=220)

        self.nametextentry1 = Entry(self.left, width=30)
        self.nametextentry1.place(x=250, y=100)

        self.addresstextentry1 = Entry(self.left, width=30)
        self.addresstextentry1.place(x=250, y=140)

        self.phonetextentry1 = Entry(self.left, width=30)
        self.phonetextentry1.place(x=250, y=180)

        self.citytextentry1 = Entry(self.left, width=30)
        self.citytextentry1.place(x=250, y=220)

        self.submit = Button(self.left, text="Add Customer", width=20, height=2, bg='white', command=self.add_customer)
        self.submit.place(x=260, y=260)

        # ......................Editing Customer Data Section............................................

        self.customerid = Label(self.right, text="Customer ID", font=('arial 14 bold'))
        self.customerid.place(x=0, y=100)
        self.name = Label(self.right, text="Fullname", font=('georgia 14 bold'), fg='black')
        self.name.place(x=0, y=140)
        self.address = Label(self.right, text="Address", font=('georgia 14 bold'), fg='black')
        self.address.place(x=0, y=180)
        self.phone = Label(self.right, text="Phone Number", font=('georgia 14 bold'), fg='black')
        self.phone.place(x=0, y=220)
        self.city = Label(self.right, text="City", font=('georgia 14 bold'), fg='black')
        self.city.place(x=0, y=260)

        self.customeridtextentry = Entry(self.right, width=30)
        self.customeridtextentry.place(x=250, y=100)

        self.nametextentry = Entry(self.right, width=30)
        self.nametextentry.place(x=250, y=140)

        self.addresstextentry = Entry(self.right, width=30)
        self.addresstextentry.place(x=250, y=180)

        self.phonetextentry = Entry(self.right, width=30)
        self.phonetextentry.place(x=250, y=220)

        self.citytextentry = Entry(self.right, width=30)
        self.citytextentry.place(x=250, y=260)

        self.submit = Button(self.right, text="Edit Customer", width=20, height=2, bg='white',
                             command=self.edit_customer)
        self.submit.place(x=260, y=300)

        # ......................Deleting Rental Data Section............................................

        self.customerid = Label(self.left, text="Customer ID", font=('arial 14 bold'))
        self.customerid.place(x=0, y=500)
        self.customerid2textentry = Entry(self.left, width=30)
        self.customerid2textentry.place(x=250, y=500)
        self.submit = Button(self.left, text="Delete Customer", width=20, height=2, bg='white',
                             command=self.delete_customer)
        self.submit.place(x=260, y=540)

        # ............................Defining Functions...........................

    def add_customer(self):
        self.value1 = self.nametextentry1.get()
        self.value2 = self.addresstextentry1.get()
        self.value3 = self.phonetextentry1.get()
        self.value4 = self.citytextentry1.get()
        if self.value1 == '' or self.value2 == '' or self.value3 == '' or self.value4 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            self.comment = {"fullname": self.value1, "address": self.value2,"phone_number": self.value3,"city": self.value4}
            self.result=requests.post("http://localhost:5000/customers/", json=self.comment)
            if self.result.status_code == 201:
                comment2 = self.result.json()
                print("Added rental successfully")
                tkinter.messagebox.showinfo(
                    f"Added Customer Successfully")
            else:
                tkinter.messagebox.showinfo(f"Post Request failed with status : {self.result.status_code}")

    def edit_customer(self):
        self.value1 = self.customeridtextentry.get()
        self.value2 = self.nametextentry.get()
        self.value3 = self.addresstextentry.get()
        self.value4 = self.phonetextentry.get()
        self.value5 = self.citytextentry.get()

        self.rentals = requests.get(f"http://localhost:5000/customers/{self.value1}")
        if self.rentals.status_code == 200:
            self.comment = {"id": self.value1, "fullname": self.value2, "address": self.value3,
                            "phone_number": self.value4, "city": self.value5}
            self.result = requests.put(f"http://localhost:5000/customers/{self.value1}", json=self.comment)
            if self.result.status_code == 200:
                tkinter.messagebox.showinfo(f"Editted Customer successfully ")
        else:
            tkinter.messagebox.showinfo("Customer not found, please enter correct customer ID!")



    def delete_customer(self):
        self.value = self.customerid2textentry.get()
        self.customer = requests.delete(f"http://localhost:5000/customers/{self.value}")
        if self.customer.status_code == 200:
            tkinter.messagebox.showinfo("Customer was removed successfully")
        else:
            tkinter.messagebox.showinfo("Customer not found")


