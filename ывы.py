from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "red"
        self.brush_size = 2
        self.setUI()

    def draw(self, event):
        self.canv.create_oval(event.x - 2, event.y - 2, event.x + 2, event.y + 2,
                              fill=self.color, outline=self.color)

    def setUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canv = Canvas(self, bg="black")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canv.grid(padx=5, pady=5, sticky=E + W + S + N)
        self.canv.bind("<B1-Motion>", self.draw)


root = Tk()
root.geometry("850x500+300+300")
app = Paint(root)
root.mainloop()