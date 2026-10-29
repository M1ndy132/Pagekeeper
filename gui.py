import tkinter as tk

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("PageKeeper")

        self.icon = tk.PhotoImage(file="PageKeeperLogo.png")
        self.root.iconphoto(False, self.icon)
        self.root.geometry("1000x800")

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.menu = tk.Frame(self.root, width=200, height=800, background="#EFE8D7")
        self.content = tk.Frame(self.root, width=800, height=800, background="#2F4A38")

        self.app_name_lbl = tk.Label(self.menu, text="PageKeeper")
        
        self.content_lbl = tk.Label(self.content, text="Your Reading Space")
        
        self.menu.grid(column=0, row=0, padx=20, )
        self.content.grid(column=1, row=0, sticky=tk.W+tk.E)

        self.app_name_lbl.grid(row=0, column=0)

        self.content_lbl.grid(row=0, column=0)


        self.root.mainloop()


GUI()