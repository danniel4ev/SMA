from tkinter import *
import tkinter as tk
import subprocess

def main():
    def install_missing_dependencies(dependencies):
        for dependency in dependencies:
            try:
                subprocess.run(["pip", "install", dependency])
            except Exception as e:
                error_label.config(text=f"Error installing {dependency}: {str(e)}")

    def install_btn_onckick(dependencies):
        str_form.destroy()
        install_missing_dependencies(dependencies)
        end_form = tk.Tk()
        end_form.title("")
        end_form.geometry("200x40")
        end_form.resizable(width=False,height=False)
        end_form.configure(bg="white")
        tk.Label(
        master=end_form,
        text="Restart the app",
        font=("arial",16,"normal"),
        wraplength=800,
        fg="red"
    ).pack(side=TOP)

    # List of required pip dependencies
    required_dependencies = ["pillow", "customtkinter"]

    missing_dependencies = []
    for dependency in required_dependencies:
        try:
            if dependency == "pillow":
                import PIL
            elif dependency == "customtkinter":
                import customtkinter
        except ImportError:
            missing_dependencies.append(dependency)

    if missing_dependencies:
        str_form = tk.Tk()
        str_form.title("Dependency Checker")
        str_form.geometry("250x150")
        str_form.resizable(width=False,height=False)
        str_form.configure(bg="white")
        error_label = tk.Label(str_form, text="", wraplength=800, fg="red")
        error_label.pack(pady=10)
        error_message = "The following dependencies are missing:\n"
        error_message += "\n".join(missing_dependencies)

        tk.Label(
        master=str_form,
        text="To install them press the button bellow\n",
        wraplength=800,
        fg="red"
    ).pack(side=TOP)
        
        tk.Button(
        master=str_form, 
        text="Install",
        compound=LEFT,
        command=lambda : install_btn_onckick(missing_dependencies)
    ).pack(side=TOP)
        error_label.config(text=error_message)
        
        str_form.mainloop()
    else:
        from package import login_form
        login_form()


if __name__=="__main__":
    main()

