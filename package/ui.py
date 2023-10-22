#region Import & Default Vars
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as cstk
from .bl import *
from PIL import Image
from time import strftime, localtime
cstk.set_default_color_theme('blue')
#endregion

def login_form():

    def login_btn_onclick(username_var, password_var, form):
        username = username_var.get()
        password = password_var.get()

        status, output =  login_user_bl(username, password)

        if status=="ERROR":
            username_var.set("")
            password_var.set("")
            messagebox.showerror("Error", output)
    
        elif status=="SUCCESS":
            messagebox.showinfo("Success", output)
            form.destroy()
            main_page_form(username=username)

    def register_btn_onclick(form):
        form.destroy()
        register_form()
        
    form = cstk.CTk()

    #region config
    form.title("Login form")
    form.geometry("400x350")
    form.resizable(width=False,height=False)
    form.configure(bg="white",padx=50, pady=50)
    #endregion

    #region VARIABLE

    username_var = StringVar()
    password_var = StringVar()

    #endregion

    #region Username
    cstk.CTkLabel(
        master=form, 
        text="Username : ", 
        font=("arial",16,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=form,
        font=("arial",14,"normal"),
        textvariable=username_var,
    ).pack(side=TOP, fill=X, pady=(0,20))

    #endregion

    #region Password

    cstk.CTkLabel(
        master=form, 
        text="Password : ", 
        font=("arial",16,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=form,
        font=("arial",14,"normal"),
        textvariable=password_var,
        show="*"
    ).pack(side=TOP, fill=X, pady=(0,20))


    #endregion

    #region BUTTON
    
    user_login_img = cstk.CTkImage(light_image=Image.open(r'images\key-16.png'))
    user_register_img = cstk.CTkImage(light_image=Image.open(r'images\add-1-user-16.png'))


    cstk.CTkButton(
        master=form, 
        text="Login",
        font=("arial",16,"bold"),
        image=user_login_img,
        compound=LEFT,
        command=lambda : login_btn_onclick(username_var, password_var, form)
    ).pack(side=TOP, fill=X)


    cstk.CTkButton(
        master=form, 
        text="Register",
        font=("arial",16,"bold"),
        image=user_register_img,
        compound=LEFT,
        command=lambda : register_btn_onclick(form)

    ).pack(side=TOP, fill=X, pady=(5,0))

    #endregion

    form.mainloop()

def register_form():

    def back_btn_onclick(form):
        form.destroy()
        login_form()

    def reset_btn_onclick(firstname_var, lastname_var, username_var, email_var, password_var, confirm_password_var):
        firstname_var.set("")
        lastname_var.set("")
        username_var.set("")
        email_var.set("")
        password_var.set("")
        confirm_password_var.set("")

    def register_btn_onclick(firstname_var, lastname_var, username_var, email_var, password_var, confirm_password_var, form):
        
        firstname = firstname_var.get()
        lastname = lastname_var.get()
        username = username_var.get()
        email = email_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        status, output =  register_user_bl(firstname, lastname, username, email, password, confirm_password)

        if status=="ERROR":
            firstname_var.set("")
            lastname_var.set("")
            username_var.set("")
            email_var.set("")
            password_var.set("")
            confirm_password_var.set("")
            messagebox.showerror("Error", output)
    
        elif status=="SUCCESS":
            messagebox.showinfo("Success", output)
            form.destroy()
            login_form()
 
    form = cstk.CTk()

    #region config
    form.title("Register User")
    form.geometry("500x570")
    form.resizable(width=False,height=False)
    form.configure(bg="white")
    #endregion

    #region VARIABLE

    firstname_var = StringVar()
    lastname_var = StringVar()
    username_var = StringVar()
    email_var = StringVar()
    password_var = StringVar()
    confirm_password_var = StringVar()

    #endregion

    #region Frame
    header = cstk.CTkFrame(master=form, height=80)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = cstk.CTkFrame(master=form, height=80)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = cstk.CTkFrame(master=form)
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)
    #endregion

    #region HEADERTITLE
    register_title_img = cstk.CTkImage(light_image=Image.open(r'images\add-1-user-32.png'))

    cstk.CTkLabel(
        master=header, 
        text=" Register user", 
        font=("arial",16,"bold"),
        image=register_title_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))
    #endregion

    #region Firstname
    cstk.CTkLabel(
        master=body, 
        text="Firstname : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=firstname_var
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

    #region Lastname
    cstk.CTkLabel(
        master=body, 
        text="Lastname : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=lastname_var
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

    #region USERNAME
    cstk.CTkLabel(
        master=body, 
        text="Username : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=username_var
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

    #region EMAIL
    cstk.CTkLabel(
        master=body, 
        text="Email : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=email_var
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

    #region PASSWORD
    cstk.CTkLabel(
        master=body, 
        text="Password : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=password_var,
        show="*"
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

   #region CONFRIMPASSWORD
    cstk.CTkLabel(
        master=body, 
        text="Confirm password : ", 
        font=("arial",14,"normal"),
        anchor=W
    ).pack(side=TOP, fill=X)

    cstk.CTkEntry(
        master=body,
        font=("arial",14,"normal"),
        textvariable=confirm_password_var,
        show="*"
    ).pack(side=TOP, fill=X, pady=(0,10))
    #endregion

    #region BUTTON

    register_back_img = cstk.CTkImage(light_image=Image.open(r'images\back-16.png'))
    register_user_register_img = cstk.CTkImage(light_image=Image.open(r'images\done-16.png'))
    register_reset_img = cstk.CTkImage(light_image=Image.open(r'images\reset-16.png'))



    cstk.CTkButton(
        master=footer, 
        text="Register",
        font=("arial",16,"bold"),
        image=register_user_register_img,
        compound=LEFT,
        command=lambda : register_btn_onclick(firstname_var, lastname_var, username_var, email_var, password_var, confirm_password_var, form)
    ).pack(side=LEFT, padx=(10,0))

    cstk.CTkButton(
        master=footer, 
        text="Back",
        font=("arial",16,"bold"),
        image=register_back_img,
        compound=LEFT,
        command= lambda : back_btn_onclick(form)
    ).pack(side=RIGHT, padx=(0,10))

    cstk.CTkButton(
        master=footer, 
        text="Reset",
        font=("arial",16,"bold"),
        image=register_reset_img,
        compound=LEFT,
        command=lambda : reset_btn_onclick(firstname_var, lastname_var, username_var, email_var, password_var, confirm_password_var)
    ).pack(side=RIGHT, padx=(0,10))

    #endregion

    form.mainloop()

def load_data(category):
    status, output =  get_data_bl(category=category)

    if status=="ERROR":
        messagebox.showerror("Error", output)
        return tuple()

    elif status=="SUCCESS":
        return output
    
def main_page_form(username):

    std_list = load_data("student")
    cls_list = load_data("class")

    form = cstk.CTk()

    #region Variable
    count = IntVar() 
    count.set(len(std_list))
    #endregion

    #region config
    form.title("Monitoring Panel")
    form.geometry("850x700")
    form.resizable(width=False,height=False)
    #endregion

    #region MENU
    menubar = Menu(form)

    def migrate_std(e=None):
        form.destroy()
        show_student_form(username)

    def migrate_cls(e=None):
        form.destroy()
        show_class_form(username)


    utility = Menu(menubar, tearoff=0)
    utility.add_command(
        label="Show Students",
        accelerator="Ctrl+S",
        command=migrate_std
    )
    utility.add_command(
        label="Show Class",
        accelerator="Ctrl+C",
        command=migrate_cls
    )
    utility.add_separator()
    utility.add_command(label="Exit", command=form.destroy)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...")

    menubar.add_cascade(label="Utility", menu=utility, foreground='blue')
    menubar.add_cascade(label="Help", menu=helpmenu)

    form.config(menu=menubar)

    form.bind_all("<Control-s>",migrate_std)
    form.bind_all("<Control-c>",migrate_cls)
    #endregion

    #region Frame
    header = cstk.CTkFrame(master=form, height=80)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    status_bar = cstk.CTkFrame(master=form, height=25)
    status_bar.pack(side=BOTTOM, fill=X)
    status_bar.propagate(False)
    

    body = cstk.CTkFrame(master=form)
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)
    #endregion

    #region HEADERTITLE
    main_title_img = cstk.CTkImage(light_image=Image.open(r'images\user-menu-32.png'))

    cstk.CTkLabel(
        master=header, 
        text=" Students' Monitoring Dashboard", 
        font=("arial",14,"bold"),
        image=main_title_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))
    #endregion

    #region GRID
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('Treeview.Heading', background="#2b2b2b", foreground="white", font=('arial', 14, "bold"))
    s.configure("Treeview", background="#2b2b2b", foreground = 'white', font=('arial', 12))
    s.configure('Scrollbar', background="#2b2b2b", foreground = 'white')

    scr_frame = cstk.CTkScrollableFrame(body)
    scr_frame.pack(side=LEFT, fill=BOTH, expand=True)

    std_grid = ttk.Treeview(scr_frame, selectmode="browse" ,column=("firstname", "lastname", "nationalcode", "classes"), show='headings', height=len(std_list))
    std_grid.column("# 1", anchor=CENTER, width=50)
    std_grid.heading("# 1", text="Firstname")
    std_grid.column("# 2", anchor=CENTER, width=100)
    std_grid.heading("# 2", text="Lastname")
    std_grid.column("# 3", anchor=CENTER, width=80)
    std_grid.heading("# 3", text="National code")
    std_grid.column("# 4", anchor=CENTER)
    std_grid.heading("# 4", text="Classes")

    for std in std_list:
        new_data = []
        std_info = tuple(std.values())
        new_data.extend(std_info[0:3])
        new_data.append(show_std_class_bl(student=std, class_data=cls_list))
        std_grid.insert('', 'end', values=new_data)
        

    std_grid.pack(fill=X, expand=False)
    #endregion

    #region STATUSBARSECTION
    main_count_img = cstk.CTkImage(light_image=Image.open(r'images\user-16.png'))

    cstk.CTkLabel(
        master=status_bar, 
        text=" Count of studemts : ",
        font=("arial", 12, "normal"),
        image=main_count_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))

    cstk.CTkLabel(
        master=status_bar, 
        textvariable=count,
        font=("arial", 12, "normal")
    ).pack(side=LEFT)


    def show_time():
        # Get the current time
        current_time = strftime('%H:%M:%S %p', localtime())
        status_var.set(f"Time: {current_time}")
        # Update the time every 1000 milliseconds (1 second)
        status_bar.after(1000, show_time)

    status_var = StringVar()
    cstk.CTkLabel(status_bar,
        textvariable=status_var
    ).pack(side=RIGHT)
    show_time()

    #endregion

    form.mainloop()
    
def show_student_form(username):

    handling_data = "student"

    # Dictionary to store course checkbox values
    global course_list
    course_list = {}
    class_list = load_data('class')
    for course in class_list:
        course_list[course['class_name']] = [course['class_id'], False]
    # Dictionary to store BooleanVar objects
    global course_list_var
    course_list_var = {}

    
    def close_form():
            form.destroy()
            main_page_form(username)

    def add_student_form(grid, count):

        global course_list
        course_list = {}
        class_list = load_data('class')
        for course in class_list:
            course_list[course['class_name']] = [course['class_id'], False]
        # Dictionary to store BooleanVar objects
        global course_list_var
        course_list_var = {}

        def add_btn_onclick(firstname_var, lastname_var, ncode_var, age_var, gender_var, course_list, course_list_var, grid, form, count):

            firstname = firstname_var.get()
            lastname = lastname_var.get()
            ncode = ncode_var.get()
            age = age_var.get()
            gender = gender_var.get()

            for option, var in course_list_var.items():
                course_list[option][1] = var.get()

            status1, output1 =  add_student_bl(firstname, lastname, ncode, age, gender)

            if status1=="ERROR":
                messagebox.showerror("Error", output1)
        
            elif status1=="SUCCESS":

                status2, output2 = std_to_class_bl(course_list.values(), ncode)

                if status2=="ERROR":
                    messagebox.showerror("Error", output1)
                    
                elif status2=="SUCCESS":
                    form.destroy()
                    grid.insert('', 'end', values=(firstname, lastname, ncode, age, gender))
                    grid.config(height=len(load_data(category=handling_data)))
                    count.set(count.get()+1)
                    messagebox.showinfo("Success", output1)
        
        form = cstk.CTkToplevel()

        #region config
        form.title("Add Student")
        form.geometry("500x700")
        form.resizable(width=False,height=False)
        form.grab_set()
        #endregion

        #region VARIABLE
        firstname_var = StringVar()
        lastname_var = StringVar()
        ncode_var = StringVar()
        age_var = StringVar()
        gender_var = StringVar()
        class_list_var = StringVar()
        #endregion

        #region Frame
        header = cstk.CTkFrame(master=form, height=80)
        header.pack(side=TOP, fill=X)
        header.propagate(False)

        footer = cstk.CTkFrame(master=form, height=80)
        footer.pack(side=BOTTOM, fill=X)
        footer.propagate(False)

        body = cstk.CTkFrame(master=form)
        body.pack(fill=BOTH, expand=True, padx=10, pady=10)
        body.propagate(False)
        #endregion

        #region FORMLABEL
        std_addd_img = cstk.CTkImage(light_image=Image.open(r'images\add-user-32.png'))

        cstk.CTkLabel(
            master=header, 
            text=" Add Student", 
            font=("arial",16,"bold"),
            image=std_addd_img,
            compound=LEFT
        ).pack(side=LEFT,padx=(10,0))
        #endregion

        #region Firstname
        cstk.CTkLabel(
            master=body, 
            text="Firstname : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=firstname_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region Lastname
        cstk.CTkLabel(
            master=body, 
            text="Lastname : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=lastname_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region PHONE
        cstk.CTkLabel(
            master=body, 
            text="National code : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=ncode_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region AGE
        cstk.CTkLabel(
            master=body, 
            text="Age : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=age_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region GENDER
        cstk.CTkLabel(
            master=body, 
            text="Gender : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkOptionMenu(
            master=body,
            font=("arial",14,"normal"),
            values=("male", "female", "other"),
            fg_color="#343638",
            variable=gender_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region Student Class
        cstk.CTkLabel(
            master=body, 
            text="Classes : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        class_form = cstk.CTkScrollableFrame(body, orientation=VERTICAL)
        class_form.pack(side=LEFT, fill=BOTH, expand=True)

        for option, list_value in course_list.items():
            default_value = list_value[1]
            var = BooleanVar(value=default_value)
            course_list_var[option] = var  # Store the BooleanVar in the dictionary

            # Create and add checkboxes to the form
            checkbox = cstk.CTkCheckBox(class_form, text=option, variable=var)
            checkbox.pack(fill=BOTH)

        #endregion

        #region BUTTON
        std_add_img = cstk.CTkImage(light_image=Image.open(r'images\done-16.png'))
        std_back_img = cstk.CTkImage(light_image=Image.open(r'images\back-16.png'))

        cstk.CTkButton(
            master=footer, 
            text="Confirm",
            font=("arial",16,"bold"),
            image=std_add_img,
            compound=LEFT,
            command=lambda : add_btn_onclick(firstname_var, lastname_var, ncode_var, age_var, gender_var, course_list, course_list_var, grid, form, count)
        ).pack(side=LEFT, padx=(10,0))


        cstk.CTkButton(
            master=footer, 
            text="Back",
            font=("arial",16,"bold"),
            image=std_back_img,
            compound=LEFT,
            command=form.destroy
        ).pack(side=RIGHT, padx=(0,10))

        #endregion


        form.mainloop()

    def edit_btn_onclick(grid):
        selected_rows = grid.selection()

        if not selected_rows:
            messagebox.showerror("Error", "Select a row")
        else:

            selected_item = selected_rows[0]
            selected_val = grid.item(selected_item, "values")

            firstname = selected_val[0]
            lastname = selected_val[1]
            ncode = selected_val[2]
            age = selected_val[3]
            gender = selected_val[4]

            edit_student_form(firstname, lastname, ncode, age, gender, grid)

    def edit_student_form(firstname, lastname, ncode, age, gender, grid):

        # Dictionary to store course checkbox values
        # class_list = load_data('class')
        participated_courses = grep_std_classes_bl(class_list, ncode)
        for course in class_list:
            if course['class_id'] in participated_courses:
                course_list[course['class_name']] = [course['class_id'], True]
        def confirm_btn_onclick(ncode, firstname_var, lastname_var, ncode_var, age_var, gender_var, course_list, course_list_var, grid, form):
            new_firstname = firstname_var.get()
            new_lastname = lastname_var.get()
            new_ncode = ncode_var.get()
            new_age = age_var.get()
            new_gender = gender_var.get()

            for option, var in course_list_var.items():
                course_list[option][1] = var.get()

            status1, output1 =  edit_student_bl(ncode, new_firstname, new_lastname, new_ncode, new_age, new_gender)

            if status1=="ERROR":
                messagebox.showerror("Error", output1)
        
            elif status1=="SUCCESS":

                # changable_cid = []
                # for course in course_list.values():
                #     if course[1]:
                #         changable_cid.append(course[0])

                status2, output2 = std_to_class_bl(course_list.values(), ncode)

                if status2=="ERROR":
                    messagebox.showerror("Error", output1)
                    
                elif status2=="SUCCESS":
                    form.destroy()
                    selected_item =  grid.selection()[0]
                    grid.item(selected_item, values=(new_firstname, new_lastname, new_ncode, new_age, new_gender))
                    messagebox.showinfo("Success", output1)

            
        form = cstk.CTkToplevel()

        #region config
        form.title("Edit Student")
        form.geometry("500x700")
        form.resizable(width=False,height=False)
        form.configure(bg="white")
        form.grab_set()
        #endregion

        #region VARIABLE
        firstname_var = StringVar()
        firstname_var.set(firstname)

        lastname_var = StringVar()
        lastname_var.set(lastname)

        ncode_var = StringVar()
        ncode_var.set(ncode)
        
        age_var = StringVar()
        age_var.set(age)
        
        gender_var = StringVar()
        gender_var.set(gender)
        #endregion

        #region Frame
        header = cstk.CTkFrame(master=form, height=80)
        header.pack(side=TOP, fill=X)
        header.propagate(False)

        footer = cstk.CTkFrame(master=form, height=80)
        footer.pack(side=BOTTOM, fill=X)
        footer.propagate(False)

        body = cstk.CTkFrame(master=form)
        body.pack(fill=BOTH, expand=True, padx=10, pady=10)
        body.propagate(False)
        #endregion

        #region FORMLABEL
        std_edit_img = cstk.CTkImage(light_image=Image.open(r'images\edit-user-32.png'))

        cstk.CTkLabel(
            master=header, 
            text=" Edit Student", 
            font=("arial",16,"bold"),
            image=std_edit_img,
            compound=LEFT
        ).pack(side=LEFT,padx=(10,0))
        #endregion

        #region Firstname
        cstk.CTkLabel(
            master=body, 
            text="Firstname : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=firstname_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region Lastname
        cstk.CTkLabel(
            master=body, 
            text="Lastname : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=lastname_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region NATIONAL CODE
        cstk.CTkLabel(
            master=body, 
            text="Nationa code : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=ncode_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region AGE
        cstk.CTkLabel(
            master=body, 
            text="Age : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=age_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region GENDER
        cstk.CTkLabel(
            master=body, 
            text="Gender : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkOptionMenu(
            master=body,
            font=("arial",14,"normal"),
            values=("male", "female", "other"),
            fg_color="#343638",
            variable=gender_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion


        #region Student Class
        cstk.CTkLabel(
            master=body, 
            text="Classes : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        class_form = cstk.CTkScrollableFrame(body, orientation=VERTICAL)
        class_form.pack(side=LEFT, fill=BOTH, expand=True)

        for option, list_value in course_list.items():
            default_value = list_value[1]
            var = BooleanVar(value=default_value)
            course_list_var[option] = var  # Store the BooleanVar in the dictionary

            # Create and add checkboxes to the form
            checkbox = cstk.CTkCheckBox(class_form, text=option, variable=var)
            checkbox.pack(fill=BOTH)

        #endregion

        #region BUTTON
        std_save_img = cstk.CTkImage(light_image=Image.open(r'images\done-16.png'))
        std_back_img = cstk.CTkImage(light_image=Image.open(r'images\back-16.png'))

        cstk.CTkButton(
            master=footer, 
            text="Save",
            font=("arial",14,"bold"),
            image=std_save_img,
            compound=LEFT,
            command=lambda : confirm_btn_onclick(ncode, firstname_var, lastname_var, ncode_var, age_var, gender_var, course_list, course_list_var, grid, form)
        ).pack(side=LEFT, padx=(10,0))


        cstk.CTkButton(
            master=footer, 
            text="Back",
            font=("arial",14,"bold"),
            image=std_back_img,
            compound=LEFT,
            command=form.destroy
        ).pack(side=RIGHT, padx=(0,10))

        #endregion



        form.mainloop()

    def remove_btn_onclivk(grid, count):

        selected_rows = grid.selection()

        if not selected_rows:
            messagebox.showerror("Error", "Select a row")
        else:

            selected_item = selected_rows[0]
            selected_val = grid.item(selected_item, "values")

            ncode = selected_val[2]
            
            status1, output1 = remove_data_bl(category=handling_data, uid=ncode)
            status2, output2 = delete_std_from_class_bl(ncode)

            if status1=="ERROR":
                messagebox.showerror("Error", output1)

            elif status2=="ERROR":
                messagebox.showerror("Error", output2)
        
            elif status1=="SUCCESS" and status2=="SUCCESS":
                grid.delete(selected_item)
                grid.config(height=len(load_data(handling_data)))
                count.set(count.get()-1)
                messagebox.showinfo("Success", output1)
            
    data_list = load_data(handling_data)

    form = cstk.CTk()

    #region Variable
    count = IntVar() 
    count.set(len(data_list))
    #endregion

    #region config
    form.title("Student Manager")
    form.geometry("850x700")
    form.resizable(width=False,height=False)
    #endregion

    #region Frame
    header = cstk.CTkFrame(master=form, height=80)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    status_bar = cstk.CTkFrame(master=form, height=25)
    status_bar.pack(side=BOTTOM, fill=X)
    status_bar.propagate(False)

    footer = cstk.CTkFrame(master=form, height=80)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    

    body = cstk.CTkFrame(master=form)
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)
    #endregion

    #region HEADERTITLE
    std_title_img = cstk.CTkImage(light_image=Image.open(r'images\team-32.png'))

    cstk.CTkLabel(
        master=header, 
        text=" Students' List", 
        font=("arial",16,"bold"),
        image=std_title_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))
    #endregion

    #region GRID
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('Treeview.Heading', background="#2b2b2b", foreground="white", font=('arial', 14, "bold"))
    s.configure("Treeview", background="#2b2b2b", foreground = 'white', font=('arial', 12))
    s.configure('Scrollbar', background="#2b2b2b", foreground = 'white')

    scr_frame = cstk.CTkScrollableFrame(body)
    scr_frame.pack(side=LEFT, fill=BOTH, expand=True)

    std_grid = ttk.Treeview(scr_frame, selectmode="browse" ,column=("firstname", "lastname", "nationalcode", "age", "gender"), show='headings', height=len(data_list))
    std_grid.column("# 1", anchor=CENTER)
    std_grid.heading("# 1", text="Firstname")
    std_grid.column("# 2", anchor=CENTER)
    std_grid.heading("# 2", text="Lastname")
    std_grid.column("# 3", anchor=CENTER)
    std_grid.heading("# 3", text="National code")
    std_grid.column("# 4", anchor=CENTER)
    std_grid.heading("# 4", text="Age")
    std_grid.column("# 5", anchor=CENTER)
    std_grid.heading("# 5", text="Gender")

    for std in data_list:
        std_grid.insert('', 'end', values=tuple(std.values()))
        

    std_grid.pack(fill=X, expand=False)
    #endregion

    #region BUTTON

    std_add_img = cstk.CTkImage(light_image=Image.open(r'images\add-user-16.png'))
    std_edit_img = cstk.CTkImage(light_image=Image.open(r'images\edit-user-16.png'))
    std_remove_img = cstk.CTkImage(light_image=Image.open(r'images\denied-16.png'))



    cstk.CTkButton(
        master=footer, 
        text="Add Student",
        font=("arial",16,"bold"),
        image=std_add_img,
        compound=LEFT,
        command=lambda : add_student_form(std_grid, count)
    ).pack(side=LEFT, padx=(10,0))

    cstk.CTkButton(
        master=footer, 
        text="Edit Student",
        font=("arial",16,"bold"),
        image=std_edit_img,
        compound=LEFT,
        command=lambda : edit_btn_onclick(std_grid)
    ).pack(side=LEFT, padx=(10,0))

    cstk.CTkButton(
        master=footer, 
        text="Remove Student",
        font=("arial",16,"bold"),
        image=std_remove_img,
        compound=LEFT,
        command= lambda : remove_btn_onclivk(std_grid, count)
    ).pack(side=RIGHT, padx=(0,10))

    #endregion

    #region STATUSBARSECTION
    std_count_img = cstk.CTkImage(light_image=Image.open(r'images\user-16.png'))

    cstk.CTkLabel(
        master=status_bar, 
        text=" Count of students : ",
        font=("arial", 12, "normal"),
        image=std_count_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))

    cstk.CTkLabel(
        master=status_bar, 
        textvariable=count,
        font=("arial", 12, "normal")
    ).pack(side=LEFT)


    def show_time():
        # Get the current time
        current_time = strftime('%H:%M:%S %p', localtime())
        status_var.set(f"Time: {current_time}")
        # Update the time every 1000 milliseconds (1 second)
        status_bar.after(1000, show_time)

    status_var = StringVar()
    cstk.CTkLabel(status_bar,
        textvariable=status_var
    ).pack(side=RIGHT)
    show_time()


    #endregion

    form.protocol("WM_DELETE_WINDOW", close_form)
    form.mainloop()

def show_class_form(username):

    handling_data = "class"

    
    def close_form():
            form.destroy()
            main_page_form(username)


    def add_class_form(grid, count):

        def add_btn_onclick(class_id_var, class_name_var, start_date_var, day_var, grid, form, count):
            class_id = class_id_var.get()
            class_name = class_name_var.get()
            start_date = start_date_var.get()
            day = day_var.get()

            status, output =  add_class_bl(class_id, class_name, start_date, day)

            if status=="ERROR":
                messagebox.showerror("Error", output)
        
            elif status=="SUCCESS":
                form.destroy()
                grid.insert('', 'end', values=(class_id, class_name, start_date, day))
                grid.config(height=len(load_data(category=handling_data)))
                count.set(count.get()+1)
                messagebox.showinfo("Success", output)
        
        form = cstk.CTkToplevel()

        #region config
        form.title("Class Manager")
        form.geometry("500x600")
        form.resizable(width=False,height=False)
        form.grab_set()
        #endregion

        #region VARIABLE
        class_id_var = StringVar()
        class_name_var = StringVar()
        start_date_var = StringVar()
        day_var = StringVar()
        #endregion

        #region Frame
        header = cstk.CTkFrame(master=form, height=80)
        header.pack(side=TOP, fill=X)
        header.propagate(False)

        footer = cstk.CTkFrame(master=form, height=80)
        footer.pack(side=BOTTOM, fill=X)
        footer.propagate(False)

        body = cstk.CTkFrame(master=form)
        body.pack(fill=BOTH, expand=True, padx=10, pady=10)
        body.propagate(False)
        #endregion

        #region FORMLABEL
        cls_addd_img = cstk.CTkImage(light_image=Image.open(r'images\plus-32.png'))

        cstk.CTkLabel(
            master=header, 
            text=" Add Class", 
            font=("arial",16,"bold"),
            image=cls_addd_img,
            compound=LEFT
        ).pack(side=LEFT,padx=(10,0))
        #endregion

        #region CLASS ID
        cstk.CTkLabel(
            master=body, 
            text="Class ID : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=class_id_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region CLASS NAME
        cstk.CTkLabel(
            master=body, 
            text="Class Name : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=class_name_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region CLASS START DATE
        cstk.CTkLabel(
            master=body, 
            text="Start Date : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=start_date_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region DAY of CLASS
        cstk.CTkLabel(
            master=body, 
            text="Day of the Class : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkOptionMenu(
            master=body,
            font=("arial",14,"normal"),
            values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"),
            fg_color="#343638",
            variable=day_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region BUTTON
        cls_add_img = cstk.CTkImage(light_image=Image.open(r'images\done-16.png'))
        cls_back_img = cstk.CTkImage(light_image=Image.open(r'images\back-16.png'))

        cstk.CTkButton(
            master=footer, 
            text="Confirm",
            font=("arial",16,"bold"),
            image=cls_add_img,
            compound=LEFT,
            command=lambda : add_btn_onclick(class_id_var, class_name_var, start_date_var, day_var, grid, form, count)
        ).pack(side=LEFT, padx=(10,0))


        cstk.CTkButton(
            master=footer, 
            text="Back",
            font=("arial",16,"bold"),
            image=cls_back_img,
            compound=LEFT,
            command=form.destroy
        ).pack(side=RIGHT, padx=(0,10))

        #endregion

        form.mainloop()


    def edit_btn_onclick(grid):
        selected_rows = grid.selection()

        if not selected_rows:
            messagebox.showerror("Error", "Select a row")
        else:

            selected_item = selected_rows[0]
            selected_val = grid.item(selected_item, "values")

            class_id = selected_val[0]
            class_name = selected_val[1]
            start_date = selected_val[2]
            day = selected_val[3]

            edit_class_form(class_id, class_name, start_date, day, grid)

    def edit_class_form(class_id, class_name, start_date, day, grid):

        def confirm_btn_onclick(class_id, class_name_var, start_date_var, class_id_var, day_var, grid, form):
            new_class_name = class_name_var.get()
            new_start_date = start_date_var.get()
            new_class_id = class_id_var.get()
            new_day = day_var.get()

            status, output =  edit_class_bl(class_id, new_class_name, new_start_date, new_day)

            if status=="ERROR":
                messagebox.showerror("Error", output)
        
            elif status=="SUCCESS":
                form.destroy()
                selected_item =  grid.selection()[0]
                grid.item(selected_item, values=(class_id, new_class_name, new_start_date, new_day))
                messagebox.showinfo("Success", output)

            
        form = cstk.CTkToplevel()

        #region config
        form.title("Edit Class")
        form.geometry("500x600")
        form.resizable(width=False,height=False)
        form.configure(bg="white")
        form.grab_set()
        #endregion

        #region VARIABLE
        class_name_var = StringVar()
        class_name_var.set(class_name)

        start_date_var = StringVar()
        start_date_var.set(start_date)

        class_id_var = StringVar()
        class_id_var.set(class_id)
        
        day_var = StringVar()
        day_var.set(day)
        
        #endregion

        #region Frame
        header = cstk.CTkFrame(master=form, height=80)
        header.pack(side=TOP, fill=X)
        header.propagate(False)

        footer = cstk.CTkFrame(master=form, height=80)
        footer.pack(side=BOTTOM, fill=X)
        footer.propagate(False)

        body = cstk.CTkFrame(master=form)
        body.pack(fill=BOTH, expand=True, padx=10, pady=10)
        body.propagate(False)
        #endregion

        #region FORMLABEL
        cls_edit_img = cstk.CTkImage(light_image=Image.open(r'images\scroll-32.png'))

        cstk.CTkLabel(
            master=header, 
            text=" Edit Class", 
            font=("arial",16,"bold"),
            image=cls_edit_img,
            compound=LEFT
        ).pack(side=LEFT,padx=(10,0))
        #endregion

        #region CLASS ID
        cstk.CTkLabel(
            master=body, 
            text="Class ID : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            state="disabled",
            textvariable=class_id_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region CLASS NAME
        cstk.CTkLabel(
            master=body, 
            text="Class Name : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=class_name_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region CLASS START DATE
        cstk.CTkLabel(
            master=body, 
            text="Start Date : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkEntry(
            master=body,
            font=("arial",14,"normal"),
            textvariable=start_date_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region DAY of CLASS
        cstk.CTkLabel(
            master=body, 
            text="Day of the Class : ", 
            font=("arial",14,"normal"),
            anchor=W
        ).pack(side=TOP, fill=X)

        cstk.CTkOptionMenu(
            master=body,
            font=("arial",14,"normal"),
            values=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"),
            fg_color="#343638",
            variable=day_var
        ).pack(side=TOP, fill=X, pady=(0,20))
        #endregion

        #region BUTTON
        cls_save_img = cstk.CTkImage(light_image=Image.open(r'images\done-16.png'))
        cls_back_img = cstk.CTkImage(light_image=Image.open(r'images\back-16.png'))

        cstk.CTkButton(
            master=footer, 
            text="Save",
            font=("arial",14,"bold"),
            image=cls_save_img,
            compound=LEFT,
            command=lambda : confirm_btn_onclick(class_id=class_id, class_name_var=class_name_var, start_date_var=start_date_var, class_id_var=class_id_var, day_var=day_var, grid=grid, form=form)
        ).pack(side=LEFT, padx=(10,0))


        cstk.CTkButton(
            master=footer, 
            text="Back",
            font=("arial",14,"bold"),
            image=cls_back_img,
            compound=LEFT,
            command=form.destroy
        ).pack(side=RIGHT, padx=(0,10))

        #endregion



        form.mainloop()

    def remove_btn_onclivk(grid, count):

        selected_rows = grid.selection()

        if not selected_rows:
            messagebox.showerror("Error", "Select a row")
        else:

            selected_item = selected_rows[0]
            selected_val = grid.item(selected_item, "values")

            class_id = selected_val[0]
            
            status, output = remove_data_bl(category=handling_data, uid=class_id)

            if status=="ERROR":
                messagebox.showerror("Error", output)
        
            elif status=="SUCCESS":
                grid.delete(selected_item)
                grid.config(height=len(load_data(handling_data)))
                count.set(count.get()-1)
                messagebox.showinfo("Success", output)
            
    data_list = load_data(handling_data)

    form = cstk.CTk()

    #region Variable
    count = IntVar() 
    count.set(len(data_list))
    #endregion

    #region config
    form.title("Class Manager")
    form.geometry("850x700")
    form.resizable(width=False,height=False)
    #endregion

    #region Frame
    header = cstk.CTkFrame(master=form, height=80)
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    status_bar = cstk.CTkFrame(master=form, height=25)
    status_bar.pack(side=BOTTOM, fill=X)
    status_bar.propagate(False)

    footer = cstk.CTkFrame(master=form, height=80)
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)
    

    body = cstk.CTkFrame(master=form)
    body.pack(fill=BOTH, expand=True)
    body.propagate(False)
    #endregion

    #region HEADERTITLE
    cls_title_img = cstk.CTkImage(light_image=Image.open(r'images\document-32.png'))

    cstk.CTkLabel(
        master=header, 
        text=" Classes' List", 
        font=("arial",14,"bold"),
        image=cls_title_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))
    #endregion

    #region GRID
    s = ttk.Style()
    s.theme_use('winnative')
    s.configure('Treeview.Heading', background="#2b2b2b", foreground="white", font=('arial', 14, "bold"))
    s.configure("Treeview", background="#2b2b2b", foreground = 'white', font=('arial', 12))
    s.configure('Scrollbar', background="#2b2b2b", foreground = 'white')

    scr_frame = cstk.CTkScrollableFrame(body)
    scr_frame.pack(side=LEFT, fill=BOTH, expand=True)

    cls_grid = ttk.Treeview(scr_frame, selectmode="browse" ,column=("cid", "cn", "stdate", "day"), show='headings', height=len(data_list))
    cls_grid.column("# 1", anchor=CENTER)
    cls_grid.heading("# 1", text="Class ID")
    cls_grid.column("# 2", anchor=CENTER)
    cls_grid.heading("# 2", text="Class Name")
    cls_grid.column("# 3", anchor=CENTER)
    cls_grid.heading("# 3", text="Start Date")
    cls_grid.column("# 4", anchor=CENTER)
    cls_grid.heading("# 4", text="Day")

    for cls in data_list:
        cls_grid.insert('', 'end', values=tuple(cls.values()))
        

    cls_grid.pack(fill=X, expand=False)
    #endregion

    #region BUTTON

    cls_add_img = cstk.CTkImage(light_image=Image.open(r'images\new-window-16.png'))
    cls_edit_img = cstk.CTkImage(light_image=Image.open(r'images\edit-16.png'))
    cls_remove_img = cstk.CTkImage(light_image=Image.open(r'images\trash-1-16.png'))



    cstk.CTkButton(
        master=footer, 
        text="Add Class",
        font=("arial",16,"bold"),
        image=cls_add_img,
        compound=LEFT,
        command=lambda : add_class_form(cls_grid, count)
    ).pack(side=LEFT, padx=(10,0))

    cstk.CTkButton(
        master=footer, 
        text="Edit Class",
        font=("arial",16,"bold"),
        image=cls_edit_img,
        compound=LEFT,
        command=lambda : edit_btn_onclick(cls_grid)
    ).pack(side=LEFT, padx=(10,0))

    cstk.CTkButton(
        master=footer, 
        text="Remove Class",
        font=("arial",16,"bold"),
        image=cls_remove_img,
        compound=LEFT,
        command= lambda : remove_btn_onclivk(cls_grid, count)
    ).pack(side=RIGHT, padx=(0,10))

    #endregion

    #region STATUSBARSECTION
    cls_count_img = cstk.CTkImage(light_image=Image.open(r'images\menu-16.png'))

    cstk.CTkLabel(
        master=status_bar, 
        text=" Count of Classes : ",
        font=("arial", 12, "normal"),
        image=cls_count_img,
        compound=LEFT
    ).pack(side=LEFT,padx=(10,0))

    cstk.CTkLabel(
        master=status_bar, 
        textvariable=count,
        font=("arial", 12, "normal")
    ).pack(side=LEFT)


    def show_time():
        # Get the current time
        current_time = strftime('%H:%M:%S %p', localtime())
        status_var.set(f"Time: {current_time}")
        # Update the time every 1000 milliseconds (1 second)
        status_bar.after(1000, show_time)

    status_var = StringVar()
    cstk.CTkLabel(status_bar,
        textvariable=status_var
    ).pack(side=RIGHT)
    show_time()

    #endregion

    form.protocol("WM_DELETE_WINDOW", close_form)
    form.mainloop()

