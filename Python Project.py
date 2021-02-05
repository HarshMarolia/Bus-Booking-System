from tkinter import *
import sqlite3
from tkinter import messagebox
import splash
window = Tk()
window.title("Bus Booking System")
window.geometry('550x400')
window.minsize(550, 400)
window.maxsize(550, 400)

#Create a database or connect to An existing database
conn = sqlite3.connect('db115.db')

#Creating Cursor
cursor = conn.cursor()

#Creating tables
cursor.execute("""CREATE TABLE IF NOT EXISTS buses(
bus_id INTEGER PRIMARY KEY AUTOINCREMENT,
fn text,
cn INTEGER,
ad text,
operator text,
bustype text,
des_from text,
des_to text,
date1 text,
dep_time text,
arr_time text,
fare INTEGER,
seats INTEGER
);""")
Label(window, text = '                         ').grid(row = 0, column = 0) #Just to make text center!
Label(window, text = 'Bus Booking Service', padx = 10,pady = 10,font='times 30 bold',relief = 'ridge',bg = 'Light grey', fg = 'Blue').grid(row=1, column = 1)

#Bus Image
photo = PhotoImage(file = "Bus1.png")
Label(window, image = photo).grid(row = 2, column = 1)

#Variables
up_val=0    #To store the difference of seats for final updation
fn = StringVar()
cn = StringVar()
ad = StringVar()
operator = StringVar()
bustype = StringVar()
des_from = StringVar()
des_to = StringVar()
date = StringVar()
dep_time = StringVar()
arr_time = StringVar()
fare = StringVar()
seats = IntVar()
from_des = StringVar()
to_des = StringVar()
date_des = StringVar()
id_select = IntVar()    #Var to store RadioButton Value.
v = StringVar() #variable to store bus type in search bus section
options = ["AC", "Non-AC", "AC-Sleeper", "Non-AC Sleeper", "All Types"]

#Add Bus Section
def save():
    conn = sqlite3.connect('db115.db')
    cursor = conn.cursor()
    a1 = fn.get()
    a2 = cn.get()
    a3 = ad.get()
    a4 = operator.get()
    a5 = bustype.get()
    a6 = des_from.get()
    a7 = des_to.get()
    a8 = date.get()
    a9 = dep_time.get()
    a10 = arr_time.get()
    a11 = int(fare.get())
    a12 = int(seats.get())
    cursor.execute("""INSERT INTO buses(fn,cn,ad,operator,bustype,des_from,des_to,date1,dep_time,arr_time,fare,seats) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", (a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12))
    conn.commit()

#Operator Bus Section
def add_bus():
    window2 = Toplevel(window)
    window2.geometry('550x450')
    Label(window2, text = '                         ').grid(row = 0, column = 0)
    Label(window2, text = 'Bus Booking Service', padx = 10,pady = 10,font='times 30 bold',relief = 'ridge',bg = 'Light grey', fg = 'Blue').grid(row=1, column = 1)
    Label(window2, image = photo).grid(row = 2, column = 1)
    Label(window2, text='Bus Operator Details Filling', font = 'times 20 bold').grid(row = 4,column = 1)
    #Details
    Label(window2, text='Full Name:').grid(row=5, column=0)
    Entry(window2, textvariable = fn).grid(row = 5, column=1)
    Label(window2, text='Contact No:').grid(row=6, column=0)
    Entry(window2, textvariable = cn).grid(row = 6, column=1)
    Label(window2, text='Address:').grid(row=7, column=0)
    Entry(window2, textvariable = ad).grid(row = 7, column=1)
    def add_details():
        window2.geometry('550x700')
        Label(window2, text='Operator:').grid(row=9, column=0)
        Entry(window2, textvariable = operator).grid(row = 9, column=1)
        Label(window2, text='Bus Type:').grid(row=10, column=0)
        opt = OptionMenu(window2, bustype, *options)
        opt.config(text = "Bus Type:", width = 12, font = ("Helvetica", 10))
        opt.grid(row = 10, column=1)
        Label(window2, text='From:').grid(row=11, column=0)
        Entry(window2, textvariable = des_from).grid(row = 11, column=1)
        Label(window2, text='To:').grid(row=12, column=0)
        Entry(window2, textvariable = des_to).grid(row = 12, column=1)
        Label(window2, text='\tDate:(DD/MM/YYYY)').grid(row=13, column=0)
        Entry(window2, textvariable = date).grid(row = 13, column=1)
        Label(window2, text='Dep Time:').grid(row=14, column=0)
        Entry(window2, textvariable = dep_time).grid(row = 14, column=1)
        Label(window2, text='Arr Time:').grid(row=15, column=0)
        Entry(window2, textvariable = arr_time).grid(row = 15, column=1)
        Label(window2, text='Fare:').grid(row=16, column=0)
        Entry(window2, textvariable = fare).grid(row = 16, column=1)
        Label(window2, text='Seats:').grid(row=17, column=0)
        Entry(window2, textvariable = seats).grid(row = 17, column=1)
        def close_win():
            if fn.get()=='' or cn.get()=='' or ad.get()=='' or operator.get()=='' or bustype.get()=='' or des_from.get()=='' or des_to.get()=='' or date.get()=='' or dep_time.get()=='' or arr_time.get()=='' or fare.get()=='' or seats.get()=='':
                messagebox.showinfo(message="Fields can't be empty!")
            elif des_from.get()==des_to.get():
                messagebox.showinfo(message="Source and destination can't be same!")
            elif seats.get() == 0 or fare.get() == 0:
                messagebox.showinfo(message="Seats and Fare can't be 0")
            elif len(cn.get()) != 10:
                messagebox.showinfo(message="Contact Number should be of 10 digits")
            elif len(date.get()) != 10:
                messagebox.showinfo(message="Invalid Date!")
            elif seats.get() < 0:
                messagebox.showinfo(message="Invalid Seats!")
            else:
                window2.destroy()
                save()
                messagebox.showinfo(message="Bus Added Successfully!")
        Button(window2, text='Save', padx=5, pady=5, command = close_win).grid(row = 18, column=1)
    Button(window2, text = 'Add Details', padx=5, pady=5,command = add_details).grid(row=8,column = 1)
    
#Searched Bus Results
def search2():
    window3 = Toplevel(window)
    window3.title("Bus Booking System")
    window3.geometry('1600x800')
    Label(window3, text = 'Bus Booking Service', padx = 10,pady = 10,font='times 30 bold',relief = 'ridge',bg = 'Light grey', fg = 'Blue').grid(row=1, column = 0)
    Label(window3, image = photo).grid(row = 2, column = 0)
    Label(window3, text='Bus Details\n', font = 'times 20 bold').grid(row = 4,column = 0)
    conn = sqlite3.connect('db115.db')
    cursor = conn.cursor()
    b1 = v.get()
    b2 = from_des.get()
    b3 = to_des.get()
    b4 = date_des.get()
    if(v.get() == "All Types"):
        cursor.execute("""SELECT operator,bustype,des_from,des_to,date1,dep_time,arr_time,fare,seats From buses WHERE des_from = ? AND des_to = ? And date1 = ?""",(b2,b3,b4))
        conn.commit()
    else:
        cursor.execute("""SELECT operator,bustype,des_from,des_to,date1,dep_time,arr_time,fare,seats From buses WHERE bustype = ? AND des_from = ? AND des_to = ? And date1 = ?""",(b1,b2,b3,b4))
        conn.commit()
    all_bus = cursor.fetchall()
    if(v.get() == "All Types"):
        cursor.execute("""SELECT bus_id From buses WHERE des_from = ? AND des_to = ? And date1 = ?""",(b2,b3,b4))
        conn.commit()
    else:
        cursor.execute("""SELECT bus_id From buses WHERE bustype = ? AND des_from = ? AND des_to = ? And date1 = ?""",(b1,b2,b3,b4))
        conn.commit()
    all_id = cursor.fetchall()    
    print_bus=''
    Label(window3, text="\tOperator\t\tType\t\tFrom\t\t  To\t  \tDate\t\tDep Time\tArr Time\t\tFare\t\tSeats Availability\t\tSelect", font='times 12 bold').grid(row=5, column=0)
    count=6
    id_select.set(-1)
    for bus in all_bus:
        for one in bus:
            print_bus +=str(one)+"\t\t"
        Label(window3, text=print_bus, font='times 12').grid(row=count, column=0)
        count += 1
        print_bus=''
    count=6
    for temp in all_id: #Temp Var to give value to radiobuttons
        Radiobutton(window3, variable=id_select, value = temp).grid(row=count,column=1)
        count += 1
    Label(window3, text="Seats:").grid(row=count, column=1)
    s = StringVar()    #Var to save seats from the user
    Entry(window3, textvariable = s).grid(row=count,column=2)
    Label(window3, text="  ").grid(row=count,column=3)
    conn.commit()
    
    #Book Function
    def book():
        if id_select.get() == -1:
            messagebox.showinfo(message="Select a bus!")
        elif s.get() == '':
            messagebox.showinfo(message="Select number of seats!")
        elif s.get() == '0':
            messagebox.showinfo(message="0 seats can't be selected!")
        elif int(s.get()) < 0:
            messagebox.showinfo(message="Invalid Seat!")
        else:
            cursor.execute("SELECT seats From buses WHERE bus_id = ?",(id_select.get(),))
            s1 = cursor.fetchall()
            ans=''
            for i in s1:
                ans = i[0]
            conn.commit()
            if ans < int(s.get()):
                messagebox.showinfo(message="Invalid Seats!")
            else:
                #Database Update
                def update():
                    up_val = ans-int(s.get())
                    conn = sqlite3.connect('db115.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE buses SET seats = ? WHERE bus_id = ?",(up_val,id_select.get()))
                    cursor.fetchall()
                    conn.commit()
                update()
                window3.destroy()
                messagebox.showinfo(message="Congratulations!\n"+str(s.get())+" seats has been booked!")

    Button(window3, text="BOOK", command = book).grid(row = count+1, column=2)
    conn.commit()
    
#Search Bus Section
def search_bus():
    window2 = Toplevel(window)
    window2.geometry('550x600')
    Label(window2, text = '                         ').grid(row = 0, column = 0)
    Label(window2, text = 'Bus Booking Service', padx = 10,pady = 10,font='times 30 bold',relief = 'ridge',bg = 'Light grey', fg = 'Blue').grid(row=1, column = 1)
    Label(window2, image = photo).grid(row = 2, column = 1)
    Label(window2, text='Listing Buses', font = 'times 20 bold').grid(row = 4,column = 1)
    Label(window2, text='Bus Type:').grid(row=5, column=0)
    v.set(options[4])       #Default value is 'All Types'
    opt = OptionMenu(window2, v, *options)
    opt.config(text = "Bus Type", width = 12, font = ("Helvetica", 10))
    opt.grid(row = 5, column=1)
    Label(window2, text='From:').grid(row=6, column=0)
    Entry(window2, textvariable = from_des).grid(row = 6, column=1)
    Label(window2, text='To:').grid(row=7, column=0)
    Entry(window2, textvariable = to_des).grid(row = 7, column=1)
    Label(window2, text='\tDate:(DD/MM/YYYY)').grid(row=8, column=0)
    Entry(window2, textvariable = date_des).grid(row = 8, column=1)
    def close_win():
        window2.destroy()
    def search1():
        if from_des.get()=='' or to_des.get()=='' or date_des.get()=='':
            messagebox.showinfo(message="Fields can't be empty!")
        elif from_des.get()==to_des.get():
            messagebox.showinfo(message="Source and destination can't be same!")
        elif len(date_des.get())!= 10:
            messagebox.showinfo(message="Invalid Date!")
        else:
            close_win()
            search2()
    #Search Bus Window Buttons   
    Button(window2, text='Home', padx=5, pady=5, command = close_win).grid(row = 18, column=0)
    Button(window2, text='Search', padx=5, pady=5, command = search1).grid(row = 18, column=1)

#Main Window Buttons
Button(window, text = 'Add Bus', padx=5, pady=5,command = add_bus).grid(row=3, column=0)
Button(window, text = 'Search Bus', padx=5, pady=5, command = search_bus).grid(row=3, column=3)
window.mainloop()
