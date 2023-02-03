from tkinter import *




class Alvator(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Elevator')
        Label(self, text='Elevator', font=('Times', 20), foreground='blue').pack()
        self.geometry("500x500")
        self.minsize(300, 300)
        self.maxsize(1080, 1080)
        Label(self, text="Origin and destination floor",
              font=('Times', 10)).pack()
        self.odf = Entry(self, width=40)
        self.odf.pack(pady=10)
        self.list_odf = []
        self.down = []
        self.lf = []
        self.tt=0
        self.f_ne = Label(self, text='Number of floors:---',
                          font=("Times", 12))
        self.f_ne.pack()
        self.time = Label(self, text="Total Time :{}".format(self.tt), font=("Times", 12))
        self.time.pack(pady=10)
        b_enter = Button(self, text="ENTER", command=self.entrance)
        b_enter.pack()
        b_start = Button(self, text="START", command=self.alvator_time)
        b_start.pack()
        menubar = Menu(self)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="input format: _:_ ")
        helpmenu.add_command(label="For example 3:5 ")
        helpmenu.add_command(label=" Press Enter to add an entry")
        helpmenu.add_command(label="Press Start to calculate the shortest time")
        menubar.add_cascade(label="HELP", menu=helpmenu)
        self.config(menu=menubar)

    def entrance(self):
        try:
            if self.tt!=0:
                self.tt=0
                self.time.config(text="Total Time :{}".format(self.tt),
                             font=('Times', 12), fg='black')
            enum = self.odf.get()
            x = enum.split(":")
            start = int(x[0])
            end = int(x[1])
            self.lf.append(enum)
            self.list_odf.append(end)
            self.list_odf.append(start)
            if end < start:
                self.down.append(end)
            self.f_ne.config(text="Number of floors:{}".format(
                self.lf), font=('Times', 12), fg='green')

        except ValueError:
            self.f_ne.config(
                text="Input must be in _:_ format!!! ", font=('Times', 12), fg='red')
        except TypeError:
            self.f_ne.config(
                text=" Input must be in _:_ format!!! ", font=('Times', 12), fg='red')
        except IndexError:
            self.f_ne.config(
                text=" Input must be in _:_ format!!! ", font=('Times', 12), fg='red')
        except:
            self.f_ne.config(text=" Somthing went wrong! ",
                             font=('Times', 12), fg='red')
        finally:
            self.odf.delete(0, 'end')

    def alvator_time(self):
        try:
            self.list_odf.sort()
            self.down.sort()
            print(self.list_odf)
            print(self.down)
            if len(self.down) == 0:
                self.tt = self.list_odf[-1]
            else:
                self.tt = (self.list_odf[-1]*2) - self.down[0]
            self.time.config(text="Total Time :{}".format(self.tt),
                             font=('Times', 12), fg='green')
        except:
            self.f_ne.config(text=" Somthing went wrong! ",font=('Times',12), fg='red')
        finally:
            self.list_odf = []
            self.down = []
            self.lf = []
            self.f_ne.config(text="Number of floors:---", font=('Times', 12), fg='black')
            



if __name__ == "__main__":
    alv = Alvator()
    alv.mainloop()
