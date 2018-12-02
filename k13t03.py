"""
Welcome to the step counter 2.0. This is an application made by Iikka Pietilä
for a basic programming course at TUT.

Assignment: Kierros 13 (t. 13.10 Graafisen käyttöliittymän suunnitteleminen
            ja toteuttaminen)

Goals: "To design a program with a graphic user interface and execute it with
        Tkinter library."

By using this application user can gain insight on his/hers walking habits.

When executed, the main window will open. In the main window user can find the
functionalities: Instructions, Randomize, Count steps, Clear all.
Window also has basic menu under name "File" found (conventionally)
in upper left corner. Also on right hand side there is a blank white area
for infograph to be drawn on.

Instructions: Info on the programme and its functionalities
Randomize: Automatically fills in random values (between 3000 and 25000) to
entry fields. Can be used for testing.
Count steps: Main execution after filling in the daily steps.
Clear all: Clears all fields and data.

File -> Open: Allows user to open a file for analysis in application (file
requirements: only 7 first lines will be read. Lines must be positive numbers.
File must be in .txt format).

File -> Save: Allows user to save current data to a .txt file that can be read
again in application.

File -> Instructions: (See instructions above)

File -> Quit: Quits the application.


p.s. some print commands are left out in the code and commented out for
possible troubleshooting / debugging.


(C) Iikka Pietilä 2018

"""

import random

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog



class root:
    def __init__(self):
        # Create main window here
        self.__mainwindow = Tk()
        self.__mainwindow.title("Step counter")


        # Menu labeled "File" is created here
        self.__menubar = Menu(self.__mainwindow)

        # File menu ingredients and their functions are defined here
        self.__filemenu = Menu (self.__menubar, tearoff = 0)
        self.__filemenu.add_command(label = "Open", command = self.open)
        self.__filemenu.add_command(label = "Save", command = self.save)
        self.__filemenu.add_separator()
        self.__filemenu.add_command(label = "Instructions",
                                    command = self.instructions)
        self.__filemenu.add_separator()
        self.__filemenu.add_command(label = "Quit", command = self.quit)
        self.__menubar.add_cascade(label = "File", menu=self.__filemenu)
        self.__mainwindow.config(menu = self.__menubar)



        # Create button for instructions. Button calls for method named
        # instructions.
        self.__button_instructions = Button(self.__mainwindow, text =
                                            "Instructions",
                                            command = self.instructions)

        self.__button_instructions.grid(row=0, column = 3, sticky = E+N)


        # Create button for randomized values. Button calls for method named
        # randomize.
        self.__button_randomize = Button(self.__mainwindow, text = "Randomize",
                                         command = self.randomize)
        self.__button_randomize.grid(row = 0, column = 4, sticky = E+N)


        # Create titles as labels for columns.
        self.__label_days = Label(self.__mainwindow, text = "Day", font="bold")
        self.__label_days.grid(row = 1, column = 1, sticky = W, padx = 5)

        self.__label_steps = Label(self.__mainwindow, text = "Steps taken",
                                   font = "bold")
        self.__label_steps.grid(row=1, column=2, sticky = W)

        self.__label_info = Label(self.__mainwindow, text = "Stats",
                                  font = "bold")
        self.__label_info.grid(row = 1, column = 3, sticky = W, padx = 10)


        # Create titles as labels for each weekday.
        self.__label_day1 = Label(self.__mainwindow, text = "Monday")
        self.__label_day1.grid(row = 2, column = 1, sticky = W, padx = 5)

        self.__label_day2 = Label(self.__mainwindow, text="Tuesday")
        self.__label_day2.grid(row=3, column=1, sticky = W, padx = 5)

        self.__label_day3 = Label(self.__mainwindow, text="Wednesday")
        self.__label_day3.grid(row=4, column=1, sticky = W, padx = 5)

        self.__label_day4 = Label(self.__mainwindow, text="Thursday")
        self.__label_day4.grid(row=5, column=1, sticky = W, padx = 5)

        self.__label_day5 = Label(self.__mainwindow, text="Friday")
        self.__label_day5.grid(row=6, column=1, sticky = W, padx = 5)

        self.__label_day6 = Label(self.__mainwindow, text="Saturday")
        self.__label_day6.grid(row=7, column=1, sticky = W, padx = 5)

        self.__label_day7 = Label(self.__mainwindow, text="Sunday")
        self.__label_day7.grid(row=8, column=1, sticky = W, padx = 5)


        # Create entry field for each day of the week. User can enter
        # daily taken steps.
        self.__entry_monday = Entry(self.__mainwindow)
        self.__entry_monday.grid(row = 2, column = 2)

        self.__entry_tuesday = Entry(self.__mainwindow)
        self.__entry_tuesday.grid(row = 3, column = 2)

        self.__entry_wednesday = Entry(self.__mainwindow)
        self.__entry_wednesday.grid(row = 4, column = 2)

        self.__entry_thursday = Entry(self.__mainwindow)
        self.__entry_thursday.grid(row = 5, column = 2)

        self.__entry_friday = Entry(self.__mainwindow)
        self.__entry_friday.grid(row = 6, column = 2)

        self.__entry_saturday = Entry(self.__mainwindow)
        self.__entry_saturday.grid(row = 7, column = 2)

        self.__entry_sunday = Entry(self.__mainwindow)
        self.__entry_sunday.grid(row = 8, column = 2)


        # Create info labels for general stats and information on taken
        # steps.
        self.__label_sum = Label(self.__mainwindow,
                                 text="Total sum of steps: ")
        self.__label_sum.grid(row=2, column=3, sticky=W, padx=10)


        self.__label_over9k = Label(self.__mainwindow, text = "Days with over "
                                                              "9000 steps "
                                                              "taken: ")
        self.__label_over9k.grid(row = 3, column = 3, sticky = W, padx = 10)


        self.__label_longest = Label(self.__mainwindow, text = "Longest "
                                                               "distance "
                                                               "walked during "
                                                               "a day (km): ")
        self.__label_longest.grid(row=4, column=3, sticky = W, padx = 10)


        self.__label_calories = Label(self.__mainwindow, text = "Total calories "
                                                                "consumed by "
                                                                "walking: ")
        self.__label_calories.grid(row=5, column=3, sticky = W, padx = 10)


        # Create value labels for general stats and information on taken
        # steps. Will update when count steps is executed.
        self.__label_sum_value = Label(self.__mainwindow, text="empty")
        self.__label_sum_value.grid(row=2, column=4)

        self.__label_over9k_value = Label(self.__mainwindow, text="empty")
        self.__label_over9k_value.grid(row=3, column=4)

        self.__label_longest_value = Label(self.__mainwindow, text="empty")
        self.__label_longest_value.grid(row=4, column=4)

        self.__label_calories_value = Label(self.__mainwindow, text="empty")
        self.__label_calories_value.grid(row=5, column=4)


        # Create button for main functionality execution.
        self.__button_countsteps = Button(self.__mainwindow, text = "Count"
                                                                    " steps",
                                          command = self.draw)
        self.__button_countsteps.grid(row = 9, column = 2, sticky = N+W,
                                      pady = 20)


        # Create button to clear all fields. Calls for method clearall and
        # evokes a question dialog where action can be canceled or okayed.
        self.__button_clearall = Button(self.__mainwindow, text = "Clear all",
                                        command = self.clearall)
        self.__button_clearall.grid(row = 9, column = 3, sticky = N+W,
                                    pady = 20)


        # Create a canvas (sort of a container) for bars for graphical
        # representation of steps data.
        self.__canvas = Canvas(self.__mainwindow, width = 400, height = 300,
                               bg = "white")
        self.__canvas.grid(row=1, column=5, columnspan = 7, rowspan=10, sticky=W,
                           pady = 10, padx = 10)


        # Create labels for each bar on canvas. Each day is its own label and
        # each day gets its own bar as rectangle on canvas.
        self.__graphlabel_mo = Label(self.__mainwindow, text = "Mon", padx = 10)
        self.__graphlabel_mo.grid(row = 11, column = 5, sticky = W)

        self.__graphlabel_tu = Label(self.__mainwindow, text="Tue", padx=10)
        self.__graphlabel_tu.grid(row=11, column=6, sticky=W)

        self.__graphlabel_we = Label(self.__mainwindow, text="Wed", padx=10)
        self.__graphlabel_we.grid(row=11, column=7, sticky=W)

        self.__graphlabel_th = Label(self.__mainwindow, text="Thu", padx=10)
        self.__graphlabel_th.grid(row=11, column=8, sticky=W)

        self.__graphlabel_fr = Label(self.__mainwindow, text="Fri", padx=10)
        self.__graphlabel_fr.grid(row=11, column=9, sticky=W)

        self.__graphlabel_sa = Label(self.__mainwindow, text="Sat", padx=10)
        self.__graphlabel_sa.grid(row=11, column=10, sticky=W)

        self.__graphlabel_su = Label(self.__mainwindow, text="Sun", padx=10)
        self.__graphlabel_su.grid(row=11, column=11, sticky=W)


        # Create labels for y-axis on graph. Steps of 30000, 15000 and 0 are
        # shown in far right of graph.
        self.__graphlabel_30000 = Label(self.__mainwindow, text = "30 000",
                                        padx = 5)
        self.__graphlabel_30000.grid(row = 1, column = 12, sticky = W)

        self.__graphlabel_15000 = Label(self.__mainwindow, text = "15 000",
                                        padx = 5)
        self.__graphlabel_15000.grid(row = 6, column = 12, sticky = W)

        self.__graphlabel_0 = Label(self.__mainwindow, text = "0",
                                        padx = 5)
        self.__graphlabel_0.grid(row = 10, column = 12, sticky = W)


    def instructions(self):
        # Called from main window, tells instructions on how to use the
        # application.
        messagebox.showinfo("Instructions",
                            "Welcome to weekly Step counter application. \n \n"
                            "Insert your daily steps into the allocated slots\n"
                            "and press button that is labeled ´count steps´\n"
                            "\n"
                            "On right you can see some stats and info of your\n"
                            "steps. On far right you can see a graphical\n"
                            "representation of the steps you've taken this \n"
                            "week. It is assumed that user would not walk \n"
                            "more than 30000 steps per day \n\n"
                            "Randomize button is for testing purposes. It \n"
                            "produces pseudo random values into daily slots.\n"
                            "Randomized data is set between 3000 and 25000\n"
                            "steps. Each entered value must be more than \n"
                            "0. Only numbers are accepted.\n\n"
                            "In the graph, yellow means that user should \n"
                            "have walked more. Green is good. Limit from \n"
                            "yellow to green is 9000 steps."
                            "\n\n"
                            "You can also open a .txt file with steps for \n"
                            "each day on separate rows: File -> Open \n"
                            "To save session go to File -> Save and a .txt \n"
                            "will be saved with each value on its own row."
                            "\n\n"
                            "Keep up with the good work\n\n\n"
                            "(C) 2018 Iikka Pietilä")


    def randomize(self):
        # Fill in Steps Taken fields with random numbers between 3000 and
        # 25000

        # Produce pseudo random values
        var1 = StringVar()
        var1.set(int(random.randint(3000, 25000)))

        var2 = StringVar()
        var2.set(int(random.randint(3000, 25000)))

        var3 = StringVar()
        var3.set(int(random.randint(3000, 25000)))

        var4 = StringVar()
        var4.set(int(random.randint(3000, 25000)))

        var5 = StringVar()
        var5.set(int(random.randint(3000, 25000)))

        var6 = StringVar()
        var6.set(int(random.randint(3000, 25000)))

        var7 = StringVar()
        var7.set(int(random.randint(3000, 25000)))

        # Place the variables into the fields in GUI
        self.__entry_monday.configure(text=var1)
        self.__entry_tuesday.configure(text=var2)
        self.__entry_wednesday.configure(text=var3)
        self.__entry_thursday.configure(text=var4)
        self.__entry_friday.configure(text=var5)
        self.__entry_saturday.configure(text=var6)
        self.__entry_sunday.configure(text=var7)

        self.draw()


    def draw(self):
        """
        This executes the main functionalities. Is called by pressing
        count steps button. Also executes on randomize.

        Graph bars are given tags "bar" and method starts by clearing bars.
        It then gets values from daily entries.

        """

        try:

            # Get values for daily entries from fields.
            mo = int(self.__entry_monday.get())
            tu = int(self.__entry_tuesday.get())
            we = int(self.__entry_wednesday.get())
            th = int(self.__entry_thursday.get())
            fr = int(self.__entry_friday.get())
            sa = int(self.__entry_saturday.get())
            su = int(self.__entry_sunday.get())

            # Form a list from given values for later usage.
            entrylist = [mo, tu, we, th, fr, sa, su]
            #print("Entry list:", entrylist)

            mo = int(mo)
            tu = int(tu)
            we = int(we)
            th = int(th)
            fr = int(fr)
            sa = int(sa)
            su = int(su)

            for values in entrylist:
                if values <= 0:
                    messagebox.showerror("Error",
                                         "Please make sure that all the values "
                                         "you entered are positive. Only "
                                         "numbers are accepted.")

        except ValueError:
            messagebox.showerror("Error", "Please make sure that all the values "
                                          "you entered are positive. Only "
                                          "numbers are accepted.")

            return


        self.__canvas.delete("bar")

        # Entered values are transformed for drawing on the canvas. Division
        # by 100 is to fit the value to the canvas. Subtraction from 300 is to
        # enable drawing from bottom of canvas (as (x=0, y=0) is upper left
        # corner of drawing area.

        # These are not computed through e.g. a list because I had hard time
        # feeding them to the canvas object later on from data structure.
        # There is most likely a smart way to do this but I failed :<.

        mo = mo / 100
        mo = 300 - mo
        tu = tu / 100
        tu = 300 - tu
        we = we / 100
        we = 300 - we
        th = th / 100
        th = 300 - th
        fr = fr / 100
        fr = 300 - fr
        sa = sa / 100
        sa = 300 - sa
        su = su / 100
        su = 300 - su

        # Draw the bars on graph (rectangles). Draws yellow if according entry
        # is less than 9000 and green if 9000 or more. Mo = monday,
        # tu = tuesday etc.

        if entrylist[0] >= 9000:
            self.__canvas.create_rectangle(10, 300, 20, mo, fill="green",
                                           tags = "bar")
        elif entrylist[0] < 9000:
            self.__canvas.create_rectangle(10, 300, 20, mo, fill="yellow",
                                           tags = "bar")


        if entrylist[1] >= 9000:
            self.__canvas.create_rectangle(70, 300, 80, tu, fill = "green",
                                           tags = "bar")
        elif entrylist[1] < 9000:
            self.__canvas.create_rectangle(70, 300, 80, tu, fill = "yellow",
                                           tags = "bar")


        if entrylist[2] >= 9000:
            self.__canvas.create_rectangle(132, 300, 142, we, fill="green",
                                           tags="bar")
        elif entrylist[2] < 9000:
            self.__canvas.create_rectangle(132, 300, 142, we, fill="yellow",
                                           tags="bar")


        if entrylist[3] >= 9000:
            self.__canvas.create_rectangle(195, 300, 205, th, fill="green",
                                           tags="bar")
        elif entrylist[3] < 9000:
            self.__canvas.create_rectangle(195, 300, 205, th, fill="yellow",
                                           tags="bar")


        if entrylist[4] >= 9000:
            self.__canvas.create_rectangle(255, 300, 265, fr, fill="green",
                                           tags="bar")
        elif entrylist[4] < 9000:
            self.__canvas.create_rectangle(255, 300, 265, fr, fill="yellow",
                                           tags="bar")


        if entrylist[5] >= 9000:
            self.__canvas.create_rectangle(310, 300, 320, sa, fill="green",
                                           tags="bar")
        elif entrylist[5] < 9000:
            self.__canvas.create_rectangle(310, 300, 320, sa, fill="yellow",
                                           tags="bar")


        if entrylist[6] >= 9000:
            self.__canvas.create_rectangle(370, 300, 380, su, fill="green",
                                           tags="bar")
        elif entrylist[6] < 9000:
            self.__canvas.create_rectangle(370, 300, 380, su, fill="yellow",
                                           tags="bar")


        # Methods to fill labels under stats are called. Above created list
        # of entry values is fed to each.
        self.over9kChecker(entrylist)
        self.longestChecker(entrylist)
        self.caloriesCounter(entrylist)
        self.totalsum(entrylist)


    def open(self):
        # Method for opening a file is created. An error is raised if 7 first
        # rows of file has something else than a number. Number positiveness
        # is evaluated in the next step when the values are fed to the entry
        # fields. If succesfull, draw method is called with entered values.

        self.__mainwindow.filename = filedialog.askopenfilename(initialdir = "/",
                                                                title = "Select"
                                                                        "file")
        #print(self.__mainwindow.filename)

        file = open(self.__mainwindow.filename, "r")
        lines = file.readlines()

        messagebox.showinfo("Load succesful", self.__mainwindow.filename + "\n"
                            "Loaded succesfully.")

        try:
            var1 = StringVar()
            var1.set(int(lines[0]))

            var2 = StringVar()
            var2.set(int(lines[1]))

            var3 = StringVar()
            var3.set(int(lines[2]))

            var4 = StringVar()
            var4.set(int(lines[3]))

            var5 = StringVar()
            var5.set(int(lines[4]))

            var6 = StringVar()
            var6.set(int(lines[5]))

            var7 = StringVar()
            var7.set(int(lines[6]))

            self.__entry_monday.configure(text=var1)
            self.__entry_tuesday.configure(text=var2)
            self.__entry_wednesday.configure(text=var3)
            self.__entry_thursday.configure(text=var4)
            self.__entry_friday.configure(text=var5)
            self.__entry_saturday.configure(text=var6)
            self.__entry_sunday.configure(text=var7)

            self.draw()


        except ValueError:
            messagebox.showerror("Error",
                                 "Unable to use values from opened file. "
                                 "Please make sure that the file you "
                                 "tried to open only has positive numbers "
                                 "as values on each row.")


    def save(self):
        # Method for saving a file is created. Entries are gathered to a list
        # and from list written to a file (.txt by default) with a break (\n).


        # Get values for daily entries from fields.
        mo = int(self.__entry_monday.get())
        tu = int(self.__entry_tuesday.get())
        we = int(self.__entry_wednesday.get())
        th = int(self.__entry_thursday.get())
        fr = int(self.__entry_friday.get())
        sa = int(self.__entry_saturday.get())
        su = int(self.__entry_sunday.get())

        # Form a list from given values for saving.
        templist = [mo, tu, we, th, fr, sa, su]
        #print(templist)

        self.__mainwindow.filename = filedialog.asksaveasfile(initialdir = "/",
                                                              mode="w",
                                                              defaultextension=
                                                              ".txt")

        for item in templist:
            self.__mainwindow.filename.write(str(item))
            self.__mainwindow.filename.write("\n")

        self.__mainwindow.filename.close()


    def over9kChecker(self, list):
        # This function receives daily steps exceeding 1000 steps limit as a list
        # and counts the days that number of steps was over 9000. Number of these
        # days is saved in variable counter and written to according label..

        self.__label_over9k_value.configure(text = "")

        #print("list in checker: ", list)
        counter = 0
        for values in list:
            if values >= 9000:
                counter = counter + 1

        #print("over9k counter: ", counter)

        var = IntVar()
        var.set = counter

        self.__label_over9k_value.configure(text = counter)


    def longestChecker(self, list):
        # This function calculates the rough estimate of distance walked and
        # returns the value in kilometers. Distance is estimated through a simple
        # transformation where 2500 steps is considered equivalent to 1.5 km.

        sortedList = sorted(list)
        sortedList.reverse()
        steps = sortedList[0]
        y = steps / 2500 * 1.5

        var = IntVar()
        var.set = y
        y = int(y)

        self.__label_longest_value.configure(text = y)

        # variable y receives as its value the estimate of kilometres and returns
        # it to main


    def caloriesCounter(self, list):
        # This function calculates the rough estimate of consumed calories.
        # Function receives approved steps as a list and then the total sum of
        # steps is created. Sum of steps is translated into kilometres and from
        # kilometres the estimate of consumed calories is calculated. This value
        # is then returned to main.

        steps_sum = sum(list)
        kilometres = steps_sum / 2500 * 1.5
        calories = kilometres * 50
        calories = int(calories)

        var = IntVar()
        var.set = calories
        self.__label_calories_value.configure(text = calories)


    def totalsum(self, list):
        totalsum = sum(list)

        var = IntVar()
        var.set = totalsum

        self.__label_sum_value.configure(text = totalsum)


    def clearall(self):
        # Called from the main window. Calls for an okay/cancel dialogbox.
        # If user selects "ok", all the fields will be cleared. Cannot be
        # undone.
        if messagebox.askokcancel("Clear all fields", "Are you sure you want"
                                                     " to clear all fields?"):

            self.__label_longest_value.configure(text = "")
            self.__label_over9k_value.configure(text = "")
            self.__label_calories_value.configure(text = "")
            self.__label_sum_value.configure(text = "")

            self.__entry_monday.delete(0, END)
            self.__entry_tuesday.delete(0, END)
            self.__entry_wednesday.delete(0, END)
            self.__entry_thursday.delete(0, END)
            self.__entry_friday.delete(0, END)
            self.__entry_saturday.delete(0, END)
            self.__entry_sunday.delete(0, END)

            self.__canvas.delete("bar")

    def quit(self):
        # Ends the execution of the program.
        if messagebox.askokcancel("Quit?", "Are you sure you want to quit?"):
            self.__mainwindow.destroy()


    def start(self):
        # Start main window here
        self.__mainwindow.mainloop()

def main():
    ui = root()
    ui.start()


main()