import tkinter 
class Application(tkinter.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        #self.menu = menu()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        pass

        
def main():
    root = tkinter.Tk()
    root.title("Character Selection")
    root.geometry("1920x1080")
    app = Application(root)

    root.mainloop()

main()
