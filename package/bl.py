#region Import & Default Vars
from .dal import *
user_file_path = r"file\users.txt"
student_file_path = r"file\students.txt"
class_file_path = r"file\classes.txt"
#endregion

def convert_dict_to_text(data_list):
    return list(map(lambda item : f"{item}\n"  ,data_list))

def convert_text_to_dict(data_list):
    return list(map(lambda item : eval(item.strip())  ,data_list))

def register_user_bl(firstname, lastname, username, email, password, confirm_password):
    
    err_message = []


    status, output = read_dal(file_path=user_file_path)

    err_file = False

    if status=="ERROR":
            err_message.append(f"File Error!")   
            err_file = True

    elif status=="SUCCESS":
        user_list = convert_text_to_dict(output) 


    

    if not email:
        err_message.append("Email is empty")
    elif not err_file:

        for user in user_list:
            if user["email"] == email:
                err_message.append(f"{email} already exists!!")
                break  


    if not username:
        err_message.append("Username is empty")

    elif not err_file:
    
        for user in user_list:
            if user["username"] == username:
                err_message.append(f"{username} already exists!!")
                break  


    if not firstname:
        err_message.append("Firstname is empty")

    if not lastname:
        err_message.append("Lastname is empty")

    if not password:
        err_message.append("Password is empty")

    if not confirm_password:
        err_message.append("Confirm password is empty")

    if password != confirm_password:
        err_message.append("Passwords don't match")



    if err_message:
        return ("ERROR", "\n".join(err_message))
    
    user = {
        "firstname":firstname,
        "lastname":lastname,
        "username":username,
        "email":email,
        "password":password
    }

    status, output = save_dal(content = f"{user}\n", file_path=user_file_path)


    if status=="ERROR":
        return ("ERROR", "Save Error")
    
    elif status=="SUCCESS":
        return ("SUCCESS", "Account created successfully!")

def login_user_bl(username, password):
    
    err_message = []

    status, output = read_dal(file_path=user_file_path)

    err_file = False

    if status=="ERROR":
            err_message.append(f"File Error!")   
            err_file = True

    elif status=="SUCCESS":
        user_list = convert_text_to_dict(output) 


    if not username:
        err_message.append("Username is empty")

    elif not err_file:
    
        for user in user_list:
            if user["username"] == username and user["password"] == password:
                break  
        else:
            err_message.append(f"{username} not found!!")


    if not password:
        err_message.append("Password is empty")


    if err_message:
        return ("ERROR", "\n".join(err_message))
    
    return ("SUCCESS", "Logged in successfully!")

def get_data_bl(category):
    
    err_message = []

    if category == "student":
        file_type = student_file_path
    elif category == "class":
        file_type = class_file_path
    else:
        err_message.append("Unspecified Category!")

    status, output = read_dal(file_path=file_type)

    if status=="ERROR":
        return ("ERROR", "File error!!!")
        
    elif status=="SUCCESS":
        contacts = convert_text_to_dict(output)
        return ("SUCCESS", tuple(contacts))
     
def show_std_class_bl(student, class_data):

    err_message = []

    if not student:
        err_message.append("Student is empty")

    if not class_data:
        err_message.append("Class data is empty")

    if err_message:
        return ("ERROR", "\n".join(err_message))
   
    res = []
    
    for course in class_data:
        if student['nationalcode'] in course['students']:
            res.append(f"{course['class_name']},")
    
    if len(res) == 0:
        return "No classes assigned yet!"
    else:
        return res

def remove_data_bl(category, uid):

    err_message = []

    if category == "student":
        file_type = student_file_path
        key_code = "nationalcode"

    elif category == "class":
        file_type = class_file_path
        key_code = "class_id"

    else:
        err_message.append("Unspecified Category!")
   
    status, output = read_dal(file_path=file_type)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)

        for data in data_list:
            if data[key_code] == uid:
                data_list.remove(data)
                break  
        else:
            return ("ERROR", f"{uid} not found!!!")
        

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=file_type, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Removed successfully!")

def edit_student_bl(ncode, new_firstname, new_lastname, new_ncode, new_age, new_gender):

    err_message = []

    if not new_firstname:
        err_message.append("Firstname is empty")

    if not new_lastname:
        err_message.append("Lastname is empty")

    if not new_ncode:
        err_message.append("National code is empty")
    
    if not new_age:
        err_message.append("Age is empty")
    
    if not new_gender:
        err_message.append("Gender is empty")

    if err_message:
            return ("ERROR", "\n".join(err_message))

   
    status, output = read_dal(file_path=student_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)

        if ncode!=new_ncode:
            for data in data_list:
                if data["nationalcode"] == new_ncode:
                    return ("ERROR", f"{new_ncode} already exists!!!")


        for data in data_list:
            if data["nationalcode"] == ncode:
                data["firstname"] = new_firstname
                data["lastname"] = new_lastname
                data["nationalcode"] = new_ncode
                data["age"] = new_age
                data["gender"] = new_gender
                break  
        

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=student_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Edited successfully!")

def edit_class_bl(class_id, new_class_name, new_class_start_date, new_class_day):

    err_message = []

    if not new_class_name:
        err_message.append("Class name is empty")

    if not new_class_start_date:
        err_message.append("Class start date is empty")

    if not new_class_day:
        err_message.append("Class day is empty")


    if err_message:
            return ("ERROR", "\n".join(err_message))

   
    status, output = read_dal(file_path=class_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)

        for data in data_list:
            if data["class_id"] == class_id:
                data["class_name"] = new_class_name
                data["class_start_date"] = new_class_start_date
                data["class_day"] = new_class_day
                break  
        

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=class_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Edited successfully!")

def std_to_class_bl(class_list, national_code):

    err_message = []

    if not class_list:
        err_message.append("Class ID is empty")

    if not national_code:
        err_message.append("National code is empty")


    if err_message:
            return ("ERROR", "\n".join(err_message))
    

    if len(class_list) == 0:
        return ("SUCCESS", "Success message!")

   
    status, output = read_dal(file_path=class_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)

        for clss in class_list:
            for data in data_list:
                if data["class_id"] == clss[0] and clss[1] and national_code not in data["students"]:
                    data["students"].append(national_code)
                    break
                elif data["class_id"] == clss[0] and not clss[1] and national_code in data["students"]:
                    data["students"].remove(national_code)
                    break
        

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=class_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Student added successfully!")

def delete_std_from_class_bl(national_code):

    err_message = []

    if not national_code:
        err_message.append("National code is empty")


    if err_message:
            return ("ERROR", "\n".join(err_message))

   
    status, output = read_dal(file_path=class_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)

        for clss in data_list:
            if national_code in clss["students"]:
                clss["students"].remove(national_code)
        

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=class_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Student deleted successfully!")

def grep_std_classes_bl(class_list, national_code):
    err_message = []

    if not class_list:
        err_message.append("Class list is empty")

    if not national_code:
        err_message.append("National code is empty")


    if err_message:
            return ("ERROR", "\n".join(err_message))
    
    res = []
    for item in class_list:
        if national_code in item['students']:
            res.append(item['class_id'])

    return res

def add_student_bl(firstname, lastname, ncode, age, gender):

    err_message = []

    if not firstname.strip():
        err_message.append("Firstname is empty")

    if not lastname.strip():
        err_message.append("Lastname is empty")

    if not ncode.strip():
        err_message.append("National code is empty")
    
    if not age.strip():
        err_message.append("Age is empty")
    
    if not gender.strip():
        err_message.append("Gender is empty")

    if err_message:
            return ("ERROR", "\n".join(err_message))

   
    status, output = read_dal(file_path=student_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)


        for data in data_list:
            if data["nationalcode"] == ncode:
                return ("ERROR", f"{ncode} already exists!!!")

        new_data = {
            'firstname': firstname, 
            'lastname': lastname, 
            'nationalcode': ncode,
            'age': age,
            'gender': gender
        }

        data_list.append(new_data)

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=student_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Student added successfully!")

def add_class_bl(class_id, class_name, class_start_date, class_day):

    err_message = []

    if not class_id.strip():
        err_message.append("Class ID is empty")

    if not class_name.strip():
        err_message.append("Class name is empty")

    if not class_start_date.strip():
        err_message.append("Class start date is empty")
    
    if not class_day.strip():
        err_message.append("Class day is empty")
    

    if err_message:
            return ("ERROR", "\n".join(err_message))

   
    status, output = read_dal(file_path=class_file_path)

    if status=="ERROR":
        return ("ERROR", "File Error")
    
    elif status=="SUCCESS":
        
        data_list = convert_text_to_dict(output)


        for data in data_list:
            if data["class_id"] == class_id:
                return ("ERROR", f"{class_id} already exists!!!")
                  

        new_data = {
            'class_id': class_id, 
            'class_name': class_name, 
            'class_start_date': class_start_date,
            'class_day': class_day,
            'students' : []
        }

        data_list.append(new_data)

        data_txt = convert_dict_to_text(data_list)
        status, output = save_dal(content = data_txt, file_path=class_file_path, mode="w", write_state="wl")

        if status=="ERROR":
            return ("ERROR", "Error message")
        
        elif status=="SUCCESS":
            return ("SUCCESS", "Class added successfully!")

