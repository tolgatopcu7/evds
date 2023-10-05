import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Farklı Frameleri Yönetme")

        self.center_window(400, 300)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Frame1, Frame2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Frame1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bu Frame 1")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Diğer Frame'e Git", command=lambda: controller.show_frame(Frame2))
        button.pack()

class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bu Frame 2")
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Önceki Frame'e Git", command=lambda: controller.show_frame(Frame1))
        button.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
