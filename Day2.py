import random
import tkinter as tk
root=tk.Tk()
root.title("Generate OTP")
root.geometry("400x400")
otp=tk.Label(text="")
def otp_generation():
        otp.config(text=f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")

#button creation
button=tk.Button(
    root,
    text="Generate OTP",
    command=otp_generation,
    fg="Yellow",
    bg="white",

)

#placing the button & otp on the window
button.pack(pady=20)
otp.pack(pady=20)

root.mainloop()
    
