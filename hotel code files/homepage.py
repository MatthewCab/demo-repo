
import tkinter as tk

from TestConnectClass import make_reservation_window
from modify_reservation_screen1  import modify_reservation_window
from TestConnectClass3 import cancel_reservation_window
from TestConnectClass4 import manager_report_window


def createWindow(frame, title, description, makeCommand):
     function_name = tk.Frame(frame, width=200, height=200)
     function_name.pack(side=tk.LEFT,expand=True, fill="both")
     function_name.configure(background="white", highlightbackground="skyblue", highlightcolor="skyblue", highlightthickness=15)

     description_title = tk.Label(function_name, text=title, font=("Times New Roman", 25))
     description_title.pack()
     description_title.configure(background="white")
     function_description = tk.Label(function_name, text=description,font="150")
     function_description.pack()
     function_description.configure(background="white")

     button = tk.Button(function_name, text=title, command=makeCommand)
     button.pack()
     button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

def main():
     root = tk.Tk()

     #window pop up name
     #size of window info
     root.title("Best Hotel!!!!!")
     root.configure(background="skyblue")
     root.geometry("600x400+50+50")
     root.minsize(800,800)
     root.resizable(width=True, height=True)

     #frames in order to do 2x2 frame display
     frameTOP = tk.Frame(root, width=200, height=200)
     frameTOP.pack(side=tk.TOP, expand=True, fill="both")
     frameTOP.configure(background="pink")

     frameTOP1 = tk.Frame(root, width=200, height=200)
     frameTOP1.pack(side=tk.TOP, expand=True, fill="both")
     frameTOP1.configure(background="pink")

     frameBOTTOM = tk.Frame(root, width=200, height=200)
     frameBOTTOM.pack(side=tk.TOP,expand=True, fill="both")

     #create title "Best hotel" which is in the top background frame
     title = tk.Label(frameTOP, text="BEST HOTEL", font=("Times New Roman", 100))
     title.pack(expand=True, fill="both")

     #4 white frame boxes which will hold buttons to link to different features
     #NOTE: modify, cancel, and manager report buttons, work but need
     #the actual classes for them to link to, as of right now they
     #link to "test cases"/classes
     #since sprint/progess hasn't reached those yet 

     #make and modify frames are both in middle background frame
     #create make reservation frame with description and button
     make_reservation_title = "Make Reservation:"
     make_reservation_description = "Will be asked to select dates for a reservation.\n Will be asked number of guests for a room. \nWill be asked room type interested in."
     make_reservation_command = make_reservation_window
     createWindow(frameTOP1, make_reservation_title, make_reservation_description, make_reservation_command)

     #create modify reservation frame with description and button
     modify_reservation_title = "Modify Reservation:"
     modify_reservation_description = "Will be asked for reservation number. \nWill be redirected to update information page."
     modify_reservation_command = modify_reservation_window
     createWindow(frameTOP1, modify_reservation_title, modify_reservation_description, modify_reservation_command)

     #cancel and manager report frames are both in bottom background frame
     #create cancel reservation frame with description and button
     cancel_reservation_title = "Cancel Reservation:"
     cancel_reservation_description = "Will be asked for reservation number. \n Will be asked reason for cancellation"
     cancel_reservation_command = cancel_reservation_window
     createWindow(frameBOTTOM, cancel_reservation_title, cancel_reservation_description, cancel_reservation_command)

     #create manager info report frame with description and button
     manager_report_title = "Manager Report:"
     manager_report_description = "Will be asked for Manager ID number. \n Will return hotel information report"
     manager_report_command = manager_report_window
     createWindow(frameBOTTOM, manager_report_title, manager_report_description, manager_report_command)

     root.mainloop()

if __name__ == "__main__":
     main()
