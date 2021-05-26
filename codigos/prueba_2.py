from tkinter import *

class Test():
    def __init__(self):
        self.root = Tk()
        self.text = StringVar()
        self.text.set("Test")
        self.label = Label(self.root, textvariable=self.text)

        self.button = Button(self.root,
                                text="Click to change text below",
                                command=self.changeText)
        self.button.pack()
        self.label.pack()
        self.root.mainloop()

    def changeText(self):
        self.text.set("Text updated")        

app=Test()