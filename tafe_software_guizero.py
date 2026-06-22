from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import csv

class Startup_the_app:
    def __init__(self, master):
        '''This class will add a scrollbar. layout of widgets = {frame:'self.first_frame',
        canvas:'canvas', scrollbar:'scrollbar', frame:'main_frame'}'''
        self.first_frame = ttk.Frame(master)
        '''700 by 930 will be geometry of this app'''
        self.canvas = Canvas(self.first_frame, width=700, height=930)
        '''scrollbar will exist in first_frame, vertically scrollable and will change the canvas y view'''
        self.scrollbar = ttk.Scrollbar(self.first_frame, orient=VERTICAL, command=self.canvas.yview)

        self.main_frame = ttk.Frame(self.canvas)
        self.placing_startup_widgets()

    def placing_startup_widgets(self):
        self.first_frame.pack()
        '''Two widgets will be displayed in first_frame with pack() geometry management in horizontal
        direction.'''
        self.canvas.pack(side=LEFT, fill=Y)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        '''canvas will scroll with the scrollbar. with scroll of the scrollbar, canvas will be alerted
        the scrollbar's position and change it's region on that position.'''
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.main_frame.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        '''main_frame is a frame but we need to place in canvas as a window in. Canvas have a special
        functions for this.'''
        self.canvas.create_window((0, 0), window=self.main_frame, anchor='n')
        '''we now have 4 widgets (first_frame(master), canvas(first_frame), scrollbar(first_frame) and
        main_frame(canvas)) working together nicely.
        More widgets are required for users to interact with. and this widgets will be display on the
        main_frame'''
        HomeScreen(self.main_frame)

class HomeScreen:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.access = False

        '''ttk.Style() are normally how widgets are styled in ttk module. Styles like, font, background,
        foreground and so on.'''
        self.style = ttk.Style()
        '''this will starting frame with green color'''
        self.frame_header = ttk.Frame(self.main_frame, width=704, height=250)
        '''login_image stores the logo of the app 'TAFE NSW'.'''
        self.login_image = PhotoImage(file=r'login_screen.PNG')
        '''Images defined inside classes will be garbage collected outside of the class, so it is important
        to save the image inside a variable that will still exist outside of the class.'''
        self.login_image.img = self.login_image
        '''Before we only saved image inside of a variable, now we create the image widget through ttk Label'''
        self.login_image_label = ttk.Label(self.frame_header, image=self.login_image.img, background='#78F978')

        '''when login button is clicked python, python will run command which is defined to run destroying_frame()'''
        self.logIn = ttk.Button(self.frame_header, text='Login as staff', command=lambda: self.destroying_frame())

        self.homescreen_header()

    def homescreen_header(self):
        '''Style() is used to style all ttk widgets. '.TFrame' is a special key to tell style that you are
        styling Frame widget, there is a special key for all widgets, it is 'T' then the widget name, like:
        '.TLabel'.'''
        self.style.configure('frame_header.TFrame', relief=GROOVE, background='#78F978')
        self.frame_header.config(style='frame_header.TFrame')

        self.frame_header.grid(row=0, column=0)

        self.style.configure('label_login.TLabel', foreground='white',
                             background='#78F978', font=('Arial', 18, 'bold'))
        self.logIn.config(style='label_login.TLabel')

        self.logIn.place(x=50, y=165)
        self.login_image_label.place(x=350, y=130)

        '''All of the printing and calculating courses are done here'''
        Courses_frame(self.main_frame, self.access)

    def destroying_frame(self):
        '''My plan for changing pages will be to destroy all widgets inside main_frame and display new
        widgets to it.'''
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        '''pass plain main_frame to the login_screen class'''
        Login_screen(self.main_frame)

class Login_screen:
    '''Login screen class will execute when the login button is pressed'''
    def __init__(self, main_frame):
        '''All the login variables and widgets are created in this init function. it contains: main_frame, login_tafe,
        login_details_frame, instruction_label, username_label, username, password_label, password and login_btn'''
        self.main_frame = main_frame
        self.login_page_frame = Frame(self.main_frame,  width=700, height=930)
        self.login_tafe = ttk.Button(self.login_page_frame, text='Tafe NSW', command=lambda: self.destroying_widgets('back'))
        self.login_details_frame = ttk.Frame(self.login_page_frame)
        self.instruction_label = ttk.Label(self.login_details_frame, text='Login with your TAFE NSW account')
        self.username_label = ttk.Label(self.login_details_frame, text='Username:', font=('Segoe UI Symbol', 14))
        self.username = ttk.Entry(self.login_details_frame, width=25, font=('Segoe UI Symbol', 14))
        self.password_label = ttk.Label(self.login_details_frame, text='Password:', font=('Segoe UI Symbol', 14))
        self.password = ttk.Entry(self.login_details_frame, width=25, font=('Segoe UI Symbol', 14), show='●')
        self.login_btn = ttk.Button(self.login_details_frame, text='Login',
                                    command=lambda: self.destroying_widgets('log_in'))
        self.style = ttk.Style()
        self.laying_login_widgets()

    def laying_login_widgets(self):
        self.login_page_frame.pack()
        '''This method does widget styling and placing them on the main_frame.'''
        self.style.configure('login_tafe.TLabel', font=('Sitka Small', 18, 'bold'))
        self.login_tafe.config(style='login_tafe.TLabel')
        self.style.configure('instruction_label.TLabel', font=('Sitka Small', 14, 'bold'))
        self.instruction_label.config(style='instruction_label.TLabel')

        self.login_tafe.place(x=10, y=10)
        self.login_details_frame.place(x=175, y=250)
        self.instruction_label.grid(row=0, column=0, columnspan=4, pady=10, sticky='n')
        self.username_label.grid(row=1, column=1, columnspan=2, sticky='w')
        self.username.grid(row=2, column=1, pady=10, columnspan=2)
        self.password_label.grid(row=3, column=1, columnspan=2, sticky='w')
        self.password.grid(row=4, column=1, pady=(10,30), columnspan=2)
        self.login_btn.grid(row=5, column=2, sticky='w')

    def destroying_widgets(self, the_btn):
        '''This method will be executed when the user clicks the login or
        back button, but either way this will destroy all the widgets in
        main_frame and class a class depending on the button clicked.'''
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        if the_btn == 'back':
            HomeScreen(self.main_frame)
        if the_btn == 'log_in':
            Welcome(self.main_frame)

class Welcome:
    '''This clas is executed when the user pressed the login button is login page.'''
    def __init__(self, main_frame):
        '''In __init__, all the relevent variables and widgets are created. variables are: main_frame, press_menu,
        header_welcome_frame, welcome_tafe, welcome_label, hamburger_menuimage.img, hamburger_menu_button,
        message_frame, and new_messages_label.'''
        self.main_frame = main_frame
        self.press_menu = False
        self.style = ttk.Style()
        self.header_welcome_frame = ttk.Frame(self.main_frame, width=704, height=250)
        self.welcome_tafe = ttk.Label(self.header_welcome_frame, text='Tafe NSW')
        self.welcome_label = ttk.Label(self.header_welcome_frame, text='Welcome!')
        self.hamburger_menu_image = PhotoImage(file=r'hamburger_menu.GIF').subsample(2,2)
        self.hamburger_menu_image.img = self.hamburger_menu_image
        self.hamburger_menu_button = tk.Button(self.header_welcome_frame, image=self.hamburger_menu_image.img,
                                               relief='flat', command=lambda: self.opening_hamburger_menu())
        self.messages_frame = ttk.Frame(self.main_frame, width=704, height=680)
        self.new_messages_label = ttk.Label(self.messages_frame, text='no new messages for you')

        self.laying_down_widgets()

    def laying_down_widgets(self):
        '''Laying down those widgets.'''
        self.style.configure('header_frame.TFrame', background='#78F978')
        self.header_welcome_frame.config(style='header_frame.TFrame')

        self.style.configure('welcome_tafe.TLabel', font=('Sitka Small', 18, 'bold'), background='#78F978')
        self.welcome_tafe.config(style='welcome_tafe.TLabel')

        self.style.configure('welcome_label.TLabel', font=('Sitka Small', 40, 'bold'), background='#78F978')
        self.welcome_label.config(style='welcome_label.TLabel')

        # self.style.configure('message_frame.TFrame', background='light grey')
        # self.messages_frame.config(style='message_frame.TFrame')

        self.style.configure('new_messages.TLabel', font=('Sitka Small', 12))
        self.new_messages_label.config(style='new_messages.TLabel')

        self.header_welcome_frame.grid(row=0, column=0)
        self.messages_frame.grid(row=1, column=0)

        self.welcome_tafe.place(x=10, y=10)
        self.welcome_label.place(x=210, y=150)
        self.hamburger_menu_button.place(x=620, y=10)
        self.new_messages_label.place(x=250, y=10)

        # self.style.configure('menu_bar.TFrame', background='grey')
    def opening_hamburger_menu(self):
        '''These function is only execiuted when the hamburger_button is clicked.
        This function opens and closes the menu_frame. this only deals with frames
        and not treeview. Treeview_function is called only opening the menu_frame
        '''
        if self.press_menu == False:
            self.press_menu = True
            self.header_welcome_frame.config(width=454)
            self.messages_frame.config(width=454)
            self.hamburger_menu_button.place(x=370, y=10)
            self.menu_bar = ttk.Frame(self.main_frame, width=250, height=930)
            # self.menu_bar.config(style='menu_bar.TFrame')
            self.menu_bar.grid(row=0, column=1, rowspan=2)
            Treeview_function(self.menu_bar, self.main_frame)
        else:
            self.press_menu = False
            self.header_welcome_frame.config(width=704)
            self.messages_frame.config(width=704)
            self.hamburger_menu_button.place(x=620, y=10)
            self.menu_bar.grid_remove()

class All_courses:
    '''This class shows users all the courses but this screen is only accessed by staff members.'''
    def __init__(self, main_frame):
        '''create relevant variabels and widgets.'''
        self.main_frame = main_frame
        self.access = True
        self.style = ttk.Style()
        self.firstlevel_frame = ttk.Frame(self.main_frame)
        '''tafe logo here is a button, whenever clicked on it, it will destroy the screen and go a screen back.
        first it calls a function (destroying_all_courses) and going back occurs in that function'''
        self.all_courses_tafe = ttk.Button(self.firstlevel_frame, text='Tafe NSW', command=self.destroying_All_courses)
        self.new_course_lebel = ttk.Label(self.firstlevel_frame, text='Add new course', font=('Segoe UI Symbol', 14))
        self.add_course_image = PhotoImage(file=r'assets/add_course.png').subsample(15,15)
        self.add_course_image.img = self.add_course_image
        '''When user clicks on the add new button python will call a function'''
        self.add_course_btn = ttk.Button(self.firstlevel_frame, image=self.add_course_image.img,
                                         command=lambda: toplevel_window(Add_new_course, self.main_frame))
        self.laying_widgets()

    def laying_widgets(self):
        '''laying all the widgets down'''
        self.firstlevel_frame.grid(row=0, column=0)

        self.style.configure('all_courses_tafe.TLabel', font=('Sitka Small', 18, 'bold'))
        self.all_courses_tafe.config(style='all_courses_tafe.TLabel')

        self.all_courses_tafe.grid(row=0, column=0, padx=(0,330), pady=(10,0))
        self.new_course_lebel.grid(row=0, column=1, sticky='e', pady=(10,0))
        self.add_course_btn.grid(row=0, column=2, sticky='w', pady=(10,0))

        '''calling this call will print all the courses'''
        Courses_frame(self.main_frame, self.access)

    def destroying_All_courses(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        Welcome(self.main_frame)

class Add_new_course:
    '''This class creates a toplevel window for user to entry the new course details.
    This class also goes on to create the course as well.'''
    def __init__(self, master, main_frame):
        self.main_frame = main_frame
        '''All the relevent variables and widgets are created in here.'''
        self.create_new_course = Toplevel(master)
        self.create_new_course.geometry('500x550+100+100')
        self.create_new_course.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('label.TLabel', font=('Sitka Small', 16))
        self.style.configure('entry.TEntry', font=('Sitka Small', 16))

        self.name_label = ttk.Label(self.create_new_course, text='Course name:', style='label.TLabel')
        self.name_entry = ttk.Entry(self.create_new_course, width=40, style='entry.TEntry')

        self.number_label = ttk.Label(self.create_new_course, text='Course Number:', style='label.TLabel')
        self.number_entry = ttk.Entry(self.create_new_course, width=40, style='entry.TEntry')

        self.level_label = ttk.Label(self.create_new_course, text='Level:', style='label.TLabel')
        self.level_combobox = ttk.Combobox(self.create_new_course, value=['Beginner', 'Intermediate', 'Advanced'],
                                           width=37, state='readonly')

        self.duration_label = ttk.Label(self.create_new_course, text='Duration(weeks):', style='label.TLabel')
        self.duration_entry = ttk.Entry(self.create_new_course, width=40, style='entry.TEntry')

        self.fees_label = ttk.Label(self.create_new_course, text='Fees(AUD):', style='label.TLabel')
        self.fees_entry = ttk.Entry(self.create_new_course, width=40, style='entry.TEntry')

        self.cancel_image = PhotoImage(file=r'assets/cancel.PNG').subsample(3,3)
        self.cancel_image.img = self.cancel_image
        self.cancel_btn = ttk.Button(self.create_new_course, image=self.cancel_image.img,
                                     command=self.create_new_course.destroy)

        self.create_image = PhotoImage(file=r'assets/create.PNG').subsample(3,3)
        self.create_image.img = self.create_image
        self.create_btn = ttk.Button(self.create_new_course, image=self.create_image.img,
                                     command=self.create_btn_pressed)

        self.laying_widgets()
    def laying_widgets(self):
        '''here, all the widgets are grided onto the toplevel window.'''
        self.name_label.grid(row=0, column=0, pady=(70,10), padx=10, sticky='w')
        self.name_entry.grid(row=0, column=1, pady=(70,10), sticky='e')

        self.number_label.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.number_entry.grid(row=1, column=1, pady=10, sticky='e')

        self.level_label.grid(row=2, column=0, pady=10, padx=10, sticky='w')
        self.level_combobox.grid(row=2, column=1, pady=10, sticky='e')
        self.level_combobox.set('Beginner')

        self.duration_label.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        self.duration_entry.grid(row=3, column=1, pady=10, sticky='e')

        self.fees_label.grid(row=4, column=0, pady=10, padx=10, sticky='w')
        self.fees_entry.grid(row=4, column=1, pady=10, sticky='e')

        self.cancel_btn.grid(row=5, column=0, pady=(70,0), sticky='e')
        self.create_btn.grid(row=5, column=1, pady=(70,0))

    def create_btn_pressed(self):
        '''This method will only run when the save button is clicked. it is important to check that
        users are creating the course with correct syntax. if count is more than 0 then the syntax
        is incorrect.'''
        count = 0
        if self.name_entry.get().isspace() == True or self.name_entry.get() == '':
            messagebox.showinfo('Course Name', 'Course name can not be empty.')
            self.create_new_course.destroy()
            Add_new_course(root, self.main_frame)
            count += 1
        elif self.number_entry.get().isupper() == False or (self.number_entry.get().count(' ')) > 0:
            messagebox.showinfo('Course Number', 'Course number must be all capital letters.')
            self.create_new_course.destroy()
            Add_new_course(root, self.main_frame)
            count += 1
        elif self.duration_entry.get().isnumeric() == False:
            messagebox.showinfo('Course Duration', 'Course Duration must be a numeric.')
            self.create_new_course.destroy()
            Add_new_course(root, self.main_frame)
            count += 1
        else:
            try:
                self.fees_entry = int(self.fees_entry.get())
            except ValueError:
                try:
                    self.fees_entry = float(self.fees_entry.get())
                    self.fees_entry = str(round(self.fees_entry, 2))
                    dot = (str(self.fees_entry).find('.'))
                    if len((str(self.fees_entry))[dot:]) == 2:
                        self.fees_entry = str(self.fees_entry) + '0'
                except:
                    messagebox.showinfo('Course Fees', 'Unrecognizable Course fees number.')
                    self.create_new_course.destroy()
                    Add_new_course(root, self.main_frame)
                    count += 1
        if count == 0:
            '''This will just append the new given values and add to the courses text file'''
            with open('courses.txt', 'a') as file:
                # file.write('\n')
                file.write(self.name_entry.get() + ',' + self.number_entry.get() + ',' + self.level_combobox.get() + ',' +
                           self.duration_entry.get() + ',' + str(self.fees_entry))
            messagebox.showinfo('Successfully Created', 'Your course was successfully created.')
            self.create_new_course.destroy()
            for frame in self.main_frame.winfo_children():
                frame.destroy()
            All_courses(self.main_frame)


class Edit_course:
    '''This clas will be executed when the user wants to edit a course.'''
    def __init__(self, master, num, sortby, main_frame):
        '''In this contructor method, all widgets are contained in this Toplevel app are
        defined here.'''
        self.save_course = Toplevel(master)
        self.num = num
        self.sortby = sortby
        self.main_frame = main_frame

        self.save_course.geometry('500x550+100+100')
        self.save_course.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('label.TLabel', font=('Sitka Small', 16))
        self.style.configure('entry.TEntry', font=('Sitka Small', 16))

        self.name_label = ttk.Label(self.save_course, text='Course name:', style='label.TLabel')
        self.name_entry = ttk.Entry(self.save_course, width=40, style='entry.TEntry')

        self.number_label = ttk.Label(self.save_course, text='Course Number:', style='label.TLabel')
        self.number_entry = ttk.Entry(self.save_course, width=40, style='entry.TEntry')

        self.level_label = ttk.Label(self.save_course, text='Level:', style='label.TLabel')
        self.level_combobox = ttk.Combobox(self.save_course, value=['Beginner', 'Intermediate', 'Advanced'],
                                        width=37, state='readonly')

        self.duration_label = ttk.Label(self.save_course, text='Duration(weeks):', style='label.TLabel')
        self.duration_entry = ttk.Entry(self.save_course, width=40, style='entry.TEntry')

        self.fees_label = ttk.Label(self.save_course, text='Fees(AUD):', style='label.TLabel')
        self.fees_entry = ttk.Entry(self.save_course, width=40, style='entry.TEntry')

        self.cancel_image = PhotoImage(file=r'cancel.PNG').subsample(3,3)
        self.cancel_image.img = self.cancel_image
        self.cancel_btn = ttk.Button(self.save_course, image=self.cancel_image.img,
                                     command=self.save_course.destroy)

        self.save_image = PhotoImage(file=r'save.PNG').subsample(3,3)
        self.save_image.img = self.save_image
        self.create_btn = ttk.Button(self.save_course, image=self.save_image.img,
                                     command=self.save_btn_pressed)

        self.laying_widgets()
    def laying_widgets(self):
        '''Laying down those widgets in Toplevel window (in save_course variable).'''
        self.name_label.grid(row=0, column=0, pady=(70,10), padx=10, sticky='w')
        self.name_entry.grid(row=0, column=1, pady=(70,10), sticky='e')
        self.name_entry.insert(0, self.sortby[self.num][0])

        self.number_label.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        self.number_entry.grid(row=1, column=1, pady=10, sticky='e')
        self.number_entry.insert(0, self.sortby[self.num][1])

        self.level_label.grid(row=2, column=0, pady=10, padx=10, sticky='w')
        self.level_combobox.grid(row=2, column=1, pady=10, sticky='e')
        self.level_combobox.set(self.sortby[self.num][2])

        self.duration_label.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        self.duration_entry.grid(row=3, column=1, pady=10, sticky='e')
        self.duration_entry.insert(0, self.sortby[self.num][3])

        self.fees_label.grid(row=4, column=0, pady=10, padx=10, sticky='w')
        self.fees_entry.grid(row=4, column=1, pady=10, sticky='e')
        self.fees_entry.insert(0, self.sortby[self.num][4])

        self.cancel_btn.grid(row=5, column=0, pady=(70,0), sticky='e')
        self.create_btn.grid(row=5, column=1, pady=(70,0))


    def save_btn_pressed(self):
        '''This function is only ran when the save button is clicked.'''
        '''This count variable is created to count if the syntax in Entry widget is incorrect or not.
        count will add to one if there is there is wrong syntax, and it will be used to print 
        showinfo messagebox.'''
        count = 0
        '''name__entry requires the entry to not be emtry or all spaces.'''
        if self.name_entry.get().isspace() == True or self.name_entry.get() == '':
            messagebox.showinfo('Course Name', 'Course name can not be empty.')
            self.save_course.destroy()
            Edit_course(root, self.num, self.sortby, self.main_frame)
            count += 1

            '''number_entry requires the entry to uppercase and not have  have spaces.'''
        elif self.number_entry.get().isupper() == False or (self.number_entry.get().count(' ')) > 0:
            messagebox.showinfo('Course Number', 'Course number must be all capital letters.')
            self.save_course.destroy()
            Edit_course(root, self.num, self.sortby, self.main_frame)
            count += 1

            '''self.duration_entry requires entry to be numeric'''
        elif self.duration_entry.get().isnumeric() == False:
            messagebox.showinfo('Course Duration', 'Course Duration must be a numeric.')
            self.save_course.destroy()
            Edit_course(root, self.num, self.sortby, self.main_frame)
            count += 1
        else:
            try:
                self.fees_entry = int(self.fees_entry.get())
            except ValueError:
                try:
                    self.fees_entry = float(self.fees_entry.get())
                    self.fees_entry = str(round(self.fees_entry, 2))
                    dot = (str(self.fees_entry).find('.'))
                    if len((str(self.fees_entry))[dot:]) == 2:
                        self.fees_entry = str(self.fees_entry) + '0'
                except:
                    messagebox.showinfo('Course Fees', 'Unrecognizable Course fees number.')
                    self.save_course.destroy()
                    Edit_course(root, self.num, self.sortby, self.main_frame)
                    count += 1
        '''count will equal to 0 if no syntax error was found in any entry.'''
        if count == 0:
            data = []
            with open('courses.txt', 'r') as file:
                csv_reader = csv.reader(file)
                for i in csv_reader:
                    data.append(i)
            for index in range(len(data)):
                if data[index][1] == (self.sortby[self.num][1]):
                    updated = [self.name_entry.get(), self.number_entry.get(), self.level_combobox.get(),
                                      self.duration_entry.get(), self.fees_entry]
                    del data[index]
                    data.insert(index, updated)
            with open('courses.txt', 'w', newline='') as file:
                csv_writer = csv.writer(file)
                for a in data:
                    csv_writer.writerow(a)
            messagebox.showinfo('Successfully Updated', 'Your course was successfully Updated.')
            self.save_course.destroy()
            for frame in self.main_frame.winfo_children():
                frame.destroy()
            All_courses(self.main_frame)

class Courses_frame:
    def __init__(self, main_frame, access):
        self.main_frame = main_frame
        self.access = access

        '''this class works with searchbar, search_label and sortby_combobox, and sorting the courses.
        all methods defined here will be sorting the courses and storing then inside self.sortby list
        '''
        self.style = ttk.Style()
        self.sortby = []
        '''searchbar, all course label and sortby combobox will be inside frame_functions frame and
        all the courses will be printed inside the course_frame frame.'''
        self.frame_functions = ttk.Frame(self.main_frame)
        self.course_frame = ttk.Frame(self.main_frame)

        '''This searchbar will not have a button to press search, it will search for whatever
         user inputs in searchbar. This worked through the use of tkinter StringVar() and 
        trace() function. When a user writes something in the searchbar, it will be saved 
        to the self.variable and self.variable.trace() will automatically run.
        '''
        self.variable = StringVar()
        self.searchbar = ttk.Entry(self.frame_functions, width=60, textvariable=self.variable)

        '''this line will run when user inputs something in searchbar. it calls a function.'''
        self.variable.trace('w', self.searchbar_data)
        self.course_label = ttk.Label(self.frame_functions, text='All Courses')
        self.sortby_label = ttk.Label(self.frame_functions, text='Sort by:')
        self.combo_box = ttk.Combobox(self.frame_functions, width=8,
                                      values=['A-Z', 'Duration', 'Fees', 'Level'],
                                      state='readonly', font=('Segoe UI Symbol', 20))

        self.adding_courseframe_extra_widgets()

    def adding_courseframe_extra_widgets(self):
        self.frame_functions.grid(row=1, column=0)
        self.course_frame.grid(row=2, column=0)

        self.style.configure('search_label.TLabel', font=('Segoe UI Symbol', 30))
        self.course_label.config(style='search_label.TLabel')

        self.style.configure('sortby_label.TLabel', font=('Segoe UI Symbol', 20))
        self.sortby_label.config(style='sortby_label.TLabel')

        self.combo_box.set('A-Z')
        self.combo_box.bind('<<ComboboxSelected>>', self.calculating_sortby_order)
        '''widgets inside frame_functions is placed in grid geometry management.'''
        self.searchbar.grid(row=0, column=0, columnspan=3, padx=167, pady=(100, 30), ipady=10)
        self.course_label.grid(row=1, column=0)
        self.sortby_label.grid(row=1, column=1, sticky='e')
        self.combo_box.grid(row=1, column=2, sticky='w')
        self.calculating_sortby_order(0)

    def calculating_sortby_order(self, event):
        '''In this function courses are added and sorted in self.sortby.'''
        '''self.sortby is cleared just to be safe. ALl courses are then read and add from 
        courses text file to self.sortby list.'''
        self.sortby.clear()
        with open('courses.txt', 'r') as file:
            csv_reader = csv.reader(file)
            for i in csv_reader:
                self.sortby.append(i)

        '''for sorting in A-Z, Duration, and Fees, my plan is to create a bubble sort
        algorithm. Creating a separate method for the bubble sort algorithm will make
        the code look clearer. this Three will call that method'''
        if self.combo_box.get() == 'A-Z':
            self.bubble_sort(0)
        elif self.combo_box.get() == 'Duration':
            self.bubble_sort(3)
        elif self.combo_box.get() == 'Fees':
            self.bubble_sort(4)
        elif self.combo_box.get() == 'Level':
            '''for sorting levels, my plan is to create a separate for loop
            method and call it independently for each level.'''
            self.for_Level('Beginner')
            self.for_Level('Intermediate')
            self.for_Level('Advanced')

        '''in this line all calculation is finished. this calls printing method in the class'''
        Adding_courses(self.main_frame, self.sortby, self.course_frame, self.access)

    def bubble_sort(self, num):
        '''in position 3 and 4 in each line contains a number but is saved as
        string data type. Converted them into integers or floating point.'''
        if num == 3 or num == 4:
            for i in range(len(self.sortby)):
                try:
                    self.sortby[i][num] = int(self.sortby[i][num])
                except:
                    try:
                        self.sortby[i][num] = float(self.sortby[i][num])
                    except:
                        pass
        turns = True
        while turns:
            turns = False
            for i in range(len(self.sortby) - 1):
                '''bubble sort is comparing an element to an element in font.
                if the element before is bigger then, those two element is
                swapped via creating an extra variable like shown below.
                '''
                if self.sortby[i][num] > self.sortby[i + 1][num]:
                    swap = self.sortby[i]
                    self.sortby[i] = self.sortby[i + 1]
                    self.sortby[i + 1] = swap
                    turns = True

    def for_Level(self, level):
        with open('courses.txt', 'r') as file:
            '''for sorting levels, this had to be ran three times.
            first it appends beginner course into the list, followed by
            intermediate then advanced.'''
            csv_reader = csv.reader(file)
            for i in csv_reader:
                if i[2] == level:
                    self.sortby.append(i)
                    '''after appending, the old line needed to be removed.'''
                    self.sortby.remove(i)
        '''after this method, python continues from calculating_sortby() method'''

    def searchbar_data(self, *args):
        '''this function will run when user will type something inside the searchbar.
        it will call Searching_courses class.'''
        Searching_courses(self.variable, self.sortby, self.course_frame, self.access, self.main_frame)

class Adding_courses:
    def __init__(self, main_frame, sortby, course_frame, access):
        '''This function does styling and then calls the Printing_courses class'''
        self.main_frame = main_frame
        self.sortby = sortby
        self.course_frame = course_frame
        self.access = access

        self.style = ttk.Style()

        self.courses_styling()

    def courses_styling(self):
        '''stying the course name, course number, course button.'''
        self.style.configure('course_name.TLabel', font=('Segoe UI Symbol', 20))
        self.style.configure('course_number.TLabel', font=('Segoe UI Symbol', 14))
        self.style.configure('course_button.TLabel', background='#F2F3F4', font=('Segoe UI Symbol', 8))
        self.printing_courses()

    def printing_courses(self):
        for number in range(len(self.sortby)):
            '''calling Printing_courses in a for loop. for len of self.sortby.'''
            Printing_courses(number, self.sortby, self.course_frame, self.access, self.main_frame)

class Searching_courses:
    '''Searching courses.'''
    def __init__(self, variable, sortby, course_frame, access, main_frame):
        '''define important variables'''
        self.variable = variable
        self.sortby = sortby
        self.course_frame = course_frame
        self.access = access
        self.main_frame = main_frame
        '''self.search will equal to the text inside the searchbar.'''
        self.search = self.variable.get()
        self.search_functions()

    def search_functions(self):
        '''only starting searching if the self.search in not empty.'''
        if self.search != '':
            '''logic: first remove all the courses printed before. so can print new courses.
            Loop through the self.sortby list (contains all courses) and while looping, use find()
            function to find if self.search is in self.sortby[num][0](any course name). If it is
            then print the course in that row.'''
            for number in self.course_frame.winfo_children():
                number.destroy()
            courses = 0
            for number in range(len(self.sortby)):
                pos = (self.sortby[number][0].lower()).find(self.search.lower())
                if pos != -1:
                    '''printing the courses is done in Printing_courses class.'''
                    Printing_courses(number, self.sortby, self.course_frame, self.access, self.main_frame)
                    courses += 1
        else:
            '''if the self.search is empty then print all the courses.'''
            for number in range(len(self.sortby)):
                Printing_courses(number, self.sortby, self.course_frame, self.access, self.main_frame)

class Printing_courses:
    def __init__(self, number, sortby, course_frame, access, main_frame):
        '''defining relevent varibales'''
        self.number = number
        self.sortby = sortby
        self.course_frame = course_frame
        self.access = access
        self.main_frame = main_frame
        self.loop_printing()

    def loop_printing(self):
        '''Printing the courses in a for loop. To make the for loop buttons work, 'lambda number=self.numebr:
        self.open_this(number)' is used.'''
        course = ttk.LabelFrame(self.course_frame, width=600, height=150)
        course_name = ttk.Label(course, text=self.sortby[self.number][0], style='course_name.TLabel')
        course_number = ttk.Label(course, text=self.sortby[self.number][1], style='course_number.TLabel')
        level = ttk.Label(course, text='Level: ' + self.sortby[self.number][2], style='course_number.TLabel')
        duration = ttk.Label(course, text='Duration: ' + str(self.sortby[self.number][3]) + ' weeks',
                             style='course_number.TLabel')
        fees = ttk.Label(course, text='Fees: $' + str(self.sortby[self.number][4]), style='course_number.TLabel')
        button = ttk.Button(course, text='Course Info...', style='course_button.TLabel',
                            command=lambda number=self.number: self.open_this(number))

        course.grid(row=self.number * 2 + 2, column=0, columnspan=3)
        course_name.place(x=10, y=10)
        course_number.place(x=10, y=50)
        level.place(x=30, y=75)
        duration.place(x=200, y=75)
        fees.place(x=400, y=75)
        button.place(x=500, y=100)

    def open_this(self, number):
        '''This method will be executed when the course button is pressed. it takes 'number' as a parameter,
        it is a number of a line in self.sortby that is clicked.'''
        Each_course_frame(self.sortby, number, self.course_frame, self.access, self.main_frame)

class Each_course_frame:
    def __init__(self, sortby, number, frame_functions, access, main_frame):
        '''This class will be executed when 'Course Info' button is clicked. This class will
        show more information about the course that was clicked.'''
        self.style = ttk.Style()
        self.sortby = sortby
        self.number = number
        self.frame_functions = frame_functions
        self.access = access
        self.main_frame = main_frame
        '''This bollen variable will help to either to show the option of edit and delete button or not.'''
        self.option_open = False
        '''This frame will contain course_name, course_numer, level_frame, level, duration_frame, duration,
        fees_frame, fees and close_button. And oportion_button if the user is loged in as a teacher.'''
        self.course_frame = ttk.Frame(self.frame_functions, width=600, height=350)
        self.course_name = ttk.Label(self.course_frame, text=self.sortby[number][0])
        self.course_number = ttk.Label(self.course_frame, text=self.sortby[number][1])
        self.level_frame = ttk.Frame(self.course_frame, width=65, height=65)
        self.level = ttk.Label(self.level_frame, text=f"Level:\n{self.sortby[number][2]}")
        self.duration_frame = ttk.Frame(self.course_frame, width=65, height=65)
        self.duration = ttk.Label(self.duration_frame, text=f"Duration:\n{self.sortby[number][3]} weeks")
        self.fees_frame = ttk.Frame(self.course_frame, width=65, height=65)
        self.fees = ttk.Label(self.fees_frame, text=f"Fees:\n${self.sortby[number][4]}")

        self.close_image = PhotoImage(file='assets/close.PNG').subsample(2,2)
        self.close_image.img = self.close_image
        self.button_close = ttk.Button(self.course_frame, image=self.close_image, command=lambda: self.close_course())

        self.option_btn = PhotoImage(file=r'assets/ellipsis.png').subsample(10,11)
        self.style.configure('option_menu.TButton', relief=FLAT)
        '''access will be True if they have logined in as staff. In that case user will have extra option to
        edit the course.'''
        if self.access == True:
            self.option_btn.img = self.option_btn
            self.option_btn = ttk.Button(self.course_frame, image=self.option_btn.img,
                                         command= lambda: self.option_menu(number))
            self.option_btn.config(style='option_menu.TButton')
            self.option_btn.place(x=530, y=20)

            self.menu_option = ttk.Frame(self.course_frame)
            '''When clicked edit, it will call save_course() function with the parameters of 'Edit_course' class,
             'number' and 'self.sortby' list'''
            self.edit_btn = ttk.Button(self.menu_option, text='Edit', command=lambda: save_course(Edit_course, number,
                                                                                                  self.sortby,
                                                                                                  self.main_frame))
            '''When clicked delete, it will call delete_course() function with the parameters of 'self.sortby' and
            'number'.'''
            self.delete_btn = ttk.Button(self.menu_option, text='Delete', command=lambda: delete_course(self.sortby,
                                                                                                        number,
                                                                                                        self.main_frame))

        self.styling()

    def styling(self):
        '''Styling all the Labels and Frames'''
        self.style.configure('course_name.TLabel', font=('Segoe UI Symbol', 20))
        self.course_name.config(style='course_name.TLabel')

        self.style.configure('course_number.TLabel', font=('Segoe UI Symbol', 14))
        self.course_number.config(style='course_number.TLabel')
        self.level.config(style='course_number.TLabel')
        self.duration.config(style='course_number.TLabel')
        self.fees.config(style='course_number.TLabel')

        self.style.configure('course_frame.TFrame', relief=GROOVE)
        self.course_frame.config(style='course_frame.TFrame')

        self.laying_widgets()
    def laying_widgets(self):
        '''Placing these widgets onto the course_frame'''
        self.course_frame.grid(row=self.number*2+3, column=0, columnspan=3)
        self.course_name.place(x=30, y=60)
        self.course_number.place(x=30, y=100)
        self.level_frame.place(x=100, y=170)
        self.level.grid(row=0, column=0)
        self.duration_frame.place(x=250, y=170)
        self.duration.grid(row=0, column=0)
        self.fees_frame.place(x=400, y=170)
        self.fees.grid(row=0, column=0)
        self.button_close.place(x=10, y=10)

    def close_course(self):
        '''This method will run if they press the close
        button, in that case this will destroy the frame
        '''
        self.course_frame.destroy()

    def option_menu(self, number):
        '''This method will run if the user clicks on option menu.
        Depending on whether self.opetion_open is True or False, it
        will either create two buttons (edit and delete) for users or
        close those two button from users.'''
        if self.option_open == False:
            self.menu_option.place(x=515, y=60)
            self.edit_btn.grid(row=0, column=0, pady=10)
            self.delete_btn.grid(row=1, column=0)
            self.option_open = True
        else:
            self.menu_option.place_forget()
            self.option_open = False

class Treeview_function:
    '''Creating treeview in the welcome page.'''
    def __init__(self, menu_bar, main_frame):
        self.main_frame = main_frame
        self.menu_bar = menu_bar
        self.welcome_treeview = ttk.Treeview(self.menu_bar)
        self.insert_options()

    def insert_options(self):
        '''places the treeview in the top-right corner. whenever threeview is selected, bind
        function calls menu_selected function. This method goes on to insert new treeview
        opetions.'''
        self.welcome_treeview.place(x=10, y=10)
        self.welcome_treeview.bind('<<TreeviewSelect>>', self.menu_selected)
        self.welcome_treeview.config(selectmode='browse')
        self.welcome_treeview.insert('', '0', 'all_course', text='All Course')
        self.welcome_treeview.insert('', '1', 'courses', text='Courses')
        self.welcome_treeview.insert('', '2', 'help', text='Help')
        self.welcome_treeview.insert('', 'end', 'logout', text='Logout')
        self.welcome_treeview.heading('#0', text='Menu')
        with open('courses.txt', 'r') as file:
            csv_reader = csv.reader(file)
            for course in csv_reader:
                self.welcome_treeview.insert('courses', 'end', course[0], text='- '+ course[0])

    def menu_selected(self, event):
        '''this method is called when a threeview option is selected. only logout and
        all course gives an output. if user creates logout, python will call HomeScreen class
        and if all_courses then python will call All_courses class'''
        selected = self.welcome_treeview.selection()
        if selected[0] == 'logout':
            for widgets in self.main_frame.winfo_children():
                widgets.destroy()
            HomeScreen(self.main_frame)
        elif selected[0] == 'all_course':
            for widgets in self.main_frame.winfo_children():
                widgets.destroy()
            All_courses(self.main_frame)

root = Tk()
def main():
    '''the black color is to show that screen is out of reach.
    next is calling a calss which will run all the app function.'''
    root.config(bg='black')
    Startup_the_app(root)
    root.mainloop()

def toplevel_window(cls, main_frame):
    '''This function is call when the user clicks on add new course button.
    this function takes one parameter (cls) and calls that class with the
    parameter (root).'''
    cls(root, main_frame)

def save_course(cls, num, sortby, main_frame):
    cls(root, num, sortby, main_frame)

def delete_course(sortby, num, main_frame):
    '''This will be called to delete a course. logic: delete the
    course from sortby and then write the self.sortby in course
    text file.'''
    del sortby[num]
    with open('courses.txt', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for i in sortby:
            csv_writer.writerow(i)
    messagebox.showinfo('Successfully Deleted', 'Your course was successfully deleted.')
    for frame in main_frame.winfo_children():
        frame.destroy()
    All_courses(main_frame)

'''this if statement is certain to run as __name__ always equals to '__main__'. '''
if __name__ == '__main__':
    '''used to call startup functions'''
    main()
