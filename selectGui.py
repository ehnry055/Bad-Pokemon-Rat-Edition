from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        #self.menu = menu()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.header = Label(self, text = "Pick a character", font = ("Arial", 30)).grid(row = 0, column = 0, columnspan= 2, sticky = E)
        
        
        
def main():
    root = Tk()
    root.title("Select Gui")
    root.geometry("1920x1080")
    app = Application(root)

    root.mainloop()

main()
