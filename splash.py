from tkinter import *
root = Tk()
root.geometry('1100x600')
Label(root, text='        ').grid(row=0, column=0)
Label(root, text='Project Title: Bus Booking System', font='Arial 20 bold').grid(row = 0, column = 1)
Label(root, text='Developed as part of the course Advanced Programming Lab-1 And DBMS', font='Arial 18 bold').grid(row=1, column=1)
Label(root, text='Developed By: Harsh Marolia, 191B115, 9336653668, maroliaharsh@gmail.com.', fg='blue', font='Arial 15 bold').grid(row=2, column=1)
Label(root, text='\n-----------------------\n', fg='blue', font='Arial 15 bold').grid(row=3, column=1)
Label(root, text='Project Supervisors: Dr. Mahesh Kumar, Dr. NILESHKUMAR R.PATEL, Dr. AMIT KUMAR SRIVASTAVA. \n\n\n\n\n\n\n\n\n', fg='green', font='Arial 15 bold').grid(row=4,column=1)
Label(root, text='Make mouse movement over this screen to close!', fg='red', font='Arial 18 bold').grid(row=5, column=1)
def close(e = 2):
    root.destroy()

root.bind('<Motion>', close)
root.mainloop()
