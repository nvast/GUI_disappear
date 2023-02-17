import tkinter as tk

window = tk.Tk()


class Disappear_app:
    def __init__(self, window):
        self.text = tk.Text(window)
        self.text.pack()
        self.text.bind("<Key> <KeyRelease>", lambda event: self.magic())
        self.timer = "stop highlighting line 15 please"
        self.delay = 1000

    def magic(self):
        if self.timer:
            window.after_cancel(self.timer)
        self.timer = window.after(self.delay, self.delete)

    def delete(self):
        self.text.delete("1.0", tk.END)


Disappear_app(window)

window.mainloop()