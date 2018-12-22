
from tkinter import *
from tkinter import ttk
from DBMS_Project import *

class xyz:

    user = 'admin'
    passw ='admin'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        Label(text = ' Password ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.login_user).grid(row=3,column=2)


    def login_user(self):

        '''Check username and password entered are correct'''
        if self.username.get() == self.user and self.password.get() == self.passw:

            # Do the work done by the main of DBMSproject.py

            #Destroy current window
            root.destroy()

            #Open new window
            newroot = Tk()
            application = School_Portal(newroot)
            newroot.mainloop()



        else:

            '''Prompt user that either id or password is wrong'''
            self.message = Label(text = 'Username or Password incorrect. Try again!',fg = 'Red')
            self.message.grid(row=6,column=2)














if __name__ == '__main__':

    root = Tk()
    root.geometry('425x225')
    application = xyz(root)

    root.mainloop()
