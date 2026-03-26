from tkinter import *
from tkinter import messagebox

def Calculate_BMI():
    try:
        weight = float(entry.get())
        height = float(entry2.get())

        if height <= 0 or weight <=0:
            messagebox.showwarning("Warning", "Height and weight must be greater than zero")
            return
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif 18.5<= bmi < 24.9:
            category = "Normal Weight"
            color = "green"
        elif 25<= bmi < 29.9:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_string = f"Your BMI: {bmi:.2f}\nCategory: {category}"
        result_label.config(text=result_string, fg=color) 

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height (e.g., 1.75) ")



window = Tk()
window.title("BMI CALCULATOR")
window.geometry("500x500")

label = Label(text = "Welcome to BMI Calculator App")
label2 = Label(text = "Please Enter Your Weight (kg)")
label2.place(x=180, y=80)
label.config(bg = "lightblue", fg = "white")
label3 = Label(text ="Please Enter Your Height (m)")
label3.place(x=180, y=160)
label.pack()

entry = Entry()
entry.place(x =185, y=100)

entry2 = Entry()
entry2.place(x =185 , y = 180)

button = Button(text = "Calculate", command = Calculate_BMI)
button.place(x=215, y=210)
result_label = Label(text="", font= ("Arial", 12, "bold"))
result_label.place(x=160, y=260)




window.mainloop()
