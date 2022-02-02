from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        #self.menu = menu()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.header = Label(self, text = "Placecholder", font = ("Arial", 30)).grid(row = 0, column = 0, columnspan= 2, sticky = N)
        
        
def main():
    root = Tk()
    root.title("Simple Adder")
    root.geometry("1920x1080")
    app = Application(root)

    root.mainloop()

main()
