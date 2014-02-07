from Tkinter import *

app = Tk()
app. title("CAPCOM")
app.geometry("450x250+700+300")
app.configure(bg='black')

button = Button(app, text = "Done")
button.grid()

button2 = Button(app)
button.grid()
button2.configure(text ="But if they did... click here")


app.mainloop()
