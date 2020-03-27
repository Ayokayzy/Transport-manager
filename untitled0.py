# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:37:52 2020

@author: theay
"""
from tkinter import *
from tkinter import ttk
import mysql.connector

def data_base():
    global mycursor
    global mydb
    mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "123Password" ,
            database = "wyk_motor"
            )
    mycursor = mydb.cursor()
#    mycursor.execute("CREATE DATABASE wyk_motor")
#     mycursor.execute("CREATE TABLE Passengers(FirstName VARCHAR(50), Surname VARCHAR(50), Address VARCHAR(50), Destination VARCHAR(50), Phone INT, Vehicle_number INT)")
    # mycursor.execute("CREATE TABLE Vehicles(Vehicle_number INT, Vehicle_address VARCHAR(50), Vehicle_destination VARCHAR(50), Num_of_passengers INT, Price INT)")

def add_passenger():
    data_base()
    f_name_info = f_name.get()
    surname_info = surname.get()
    address_info = address.get()
    destination_info = destination.get()
    seat_number_info = seat_no.get()
    phone_info = phone.get()
    n_o_k_name_info = n_o_k_name.get()
    n_o_k_phone_info = n_o_k_phone.get()
    sqlFormula = "INSERT INTO passengers(FirstName,Surname,Address,Destination,Phone) VALUES (%s, %s, %s, %s, %s)"
    passenger_info = [f_name_info, surname_info, address_info, destination_info, phone_info]
    mycursor.execute(sqlFormula, passenger_info)
    mydb.commit()

def passenger():
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x500")

    global f_name
    global surname
    global address
    global destination
    global seat_no
    global phone
    global n_o_k_name
    global n_o_k_phone

    f_name = StringVar()
    surname = StringVar()
    seat_no = StringVar()
    phone = StringVar()
    n_o_k_name = StringVar()
    n_o_k_phone = StringVar()
    
    Label(screen1, text="Enter details below", bg="grey", width="400", height="2").pack()
    Label("").pack()
    Label(screen1, text="First Name").pack()
    f_name_entry = Entry(screen1, textvariable=f_name)
    f_name_entry.pack()
    Label(screen1, text="Surname",).pack()
    s_name_entry = Entry(screen1, textvariable=surname)
    s_name_entry.pack()
    Label(screen1, text="address").pack()
    address = ttk.Combobox(screen1, values=["Ogbomosho", "Lagos", "Porthacourt", "Abuja"])
    address.pack()
    address.current(0)
    Label(screen1, text="destination").pack()
    destination = ttk.Combobox(screen1, values=["Ogbomosho", "Lagos", "Porthacourt", "Abuja"])
    destination.pack()
    destination.current(1)
    Label(screen1, text="seat number").pack()
    seat_no_entry = Entry(screen1, textvariable=seat_no)
    seat_no_entry.pack()
    Label(screen1, text="phone").pack()
    phone_entry = Entry(screen1, textvariable=phone)
    phone_entry.pack()
    Label("").pack()
    Label("").pack()
    Label(screen1, text="next of kin details").pack()
    Label("").pack()
    Label(screen1, text="name").pack()
    n_o_k_name_entry = Entry(screen1, textvariable=n_o_k_name)
    n_o_k_name_entry.pack()
    Label(screen1, text="Phone").pack()
    n_o_k_phone_entry = Entry(screen1, textvariable=n_o_k_phone)
    n_o_k_phone_entry.pack()
    Label("").pack()
    Button(screen1, text="confirm", bg="grey", height="1", width="10", command=add_passenger).pack()

def add_vehicle():
    data_base()
    number_info = number.get()
    address_info = v_address.get()
    destination_info = v_destination.get()
    price_info = price.get()
    sqlFormula = "INSERT INTO vehicles(Vehicle_number,Vehicle_address,Vehicle_destination,Price) VALUES (%s, %s, %s, %s)"
    vehicle_info = [number_info, address_info, destination_info, price_info]
    mycursor.execute(sqlFormula, vehicle_info)
    mydb.commit()
    #open a success message dialog  box

def vehicle():
    screen2.destroy()
    screen3 = Toplevel(screen)
    screen3.title("Add Vehicle")
    screen3.geometry("400x300")
    global number
    global v_address
    global v_destination
    global price

    number = StringVar()
    v_address = StringVar()
    v_destination = StringVar()
    price = StringVar()

    Label(screen3, text="Enter details below", bg="grey", width="400", height="2").pack()
    Label("").pack()
    Label(screen3, text="Vehicle number").pack()
    number_entry = Entry(screen3, textvariable=number)
    number_entry.pack()
    Label(screen3, text="address").pack()
    v_address_entry = Entry(screen3, textvariable=v_address)
    v_address_entry.pack()
    Label(screen3, text="Destination").pack()
    v_destination_entry = Entry(screen3, textvariable=v_destination)
    v_destination_entry.pack()
    Label(screen3, text="Price").pack()
    price_entry = Entry(screen3, textvariable=price)
    price_entry.pack()
    Button(screen3, text="Add Vehicle", bg="grey", width="20", height="2", command=add_vehicle).pack()

def show_vehicle_details():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Add Vehicle")
    screen2.geometry("400x300")

    Label(screen2, bg="grey", width="400", height="2", text="vehicle details").pack()
    Label(screen2, text=None).pack()

    # Button(screen2, text="add vehicle", bg="grey", width="10", height=2, command=vehicle).pack()

def check_name():
    mycursor.execute(SELECT * FROM passengers WHERE )

def show_details():
    screen5 = Toplevel(screen)
    screen5.title("details")

    Label(screen5, text="passenger Details").grid(row=0, column=0)
    Label(screen5, text="Name**").grid(row=1, column=0)
    Entry(screen5, textvariable=None).grid(row=1, column=1, columnspan=2)
    Button(screen5, text="Enter").grid(row=1, column=2)

    
def login():
    screen4 = Toplevel(screen)
    screen4.title("Login")
    screen4.geometry("400x300")

    global fullname
    fullname = StringVar()

    Label(screen4, text="Login", bg="grey", width=400, height=3).pack()
    Label(screen4, text="Enter Fullname").pack()
    nameEntry = Entry(screen4, textvariable=fullname)
    nameEntry.pack()
    Button(screen4, text="enter", command=show_details).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.title("whykay transport")
    screen.geometry("400x300")

    Label(text="select option", bg="grey", height=2, width="400", font=('calibri',13)).pack()
    Label("").pack()
    Button(text="Booking", height = "2", width = "30", command = passenger).pack()
    Label("").pack()
    Button(text="Passenger Data", height="2", width="30", command=login).pack()
    Label("").pack()
    Button(text="Vehicle Report", height="2", width="30", command=show_vehicle_details).pack()

    screen.mainloop()

main_screen()
