import tkinter
import tkinter.messagebox

#CONSTANTS
TITLE = 'Weighted Average/Grade Calculator'
INSTUCTION_TEXT = 'Enter your raw scores for the following assignments and exams:'
LABEL_TEXT = ['Discussions (5% of total)', 'Revel Labs (10% of total)', 'Quizzies (10% of total)', 'Programs/Projects (15% of total)', 'Exam1 (15% of total)', 'Exam2 (15% of total)', 'Final exam (30% of total)']
BUTTON_TEXT = ['Calculate Weighted Average/Grade ','Clear','Quit']

class ScoresGUI:
    def __init__(self):
            
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title(TITLE)
        
        # Create and pack instruction frame for beginning message
        self.instruction_frame = tkinter.Frame()
        self.instruction = tkinter.Label(self.main_window,
                                   text= INSTUCTION_TEXT,width=51,anchor=tkinter.N)
        self.instruction.pack(pady=10)                     
        
        # Create the nine frames.
        self.discussions_frame = tkinter.Frame(padx=20)
        self.revel_frame = tkinter.Frame()
        self.quizzies_frame = tkinter.Frame()
        self.programs_frame = tkinter.Frame()
        self.exam1_frame = tkinter.Frame()
        self.exam2_frame = tkinter.Frame()
        self.final_frame = tkinter.Frame()
        self.calculate_frame = tkinter.Frame(pady=10)
        self.button_frame = tkinter.Frame(pady=10)
        
        # Create and pack the widgets for discussions 
        self.discussions_label = tkinter.Label(self.discussions_frame,
                    text=LABEL_TEXT[0], width=24, anchor=tkinter.E)           
        self.discussions_entry = tkinter.Entry(self.discussions_frame,
                                        width=10)   
        self.discussions_label.pack(side='left')
        self.discussions_entry.pack(side='left')

        # Create and pack the widgets for Revel labs 
        self.revel_label = tkinter.Label(self.revel_frame,
                    text=LABEL_TEXT[1], width=24, anchor=tkinter.E)        
        self.revel_entry = tkinter.Entry(self.revel_frame,
                                        width=10)   
        self.revel_label.pack(side='left')
        self.revel_entry.pack(side='left')
        
        # Create and pack the widgets for quizzies
        self.quizzies_label = tkinter.Label(self.quizzies_frame,
                    text=LABEL_TEXT[2], width=24, anchor=tkinter.E)           
        self.quizzies_entry = tkinter.Entry(self.quizzies_frame,
                                        width=10)  
        self.quizzies_label.pack(side='left')
        self.quizzies_entry.pack(side='left')
        
        # Create and pack the widgets for programs/projects
        self.programs_label = tkinter.Label(self.programs_frame,
                    text=LABEL_TEXT[3], width=24, anchor=tkinter.E)          
        self.programs_entry = tkinter.Entry(self.programs_frame,
                                        width=10) 
        self.programs_label.pack(side='left')
        self.programs_entry.pack(side='left')          

        # Create and pack the widgets for exam 1
        self.exam1_label = tkinter.Label(self.exam1_frame,
                    text=LABEL_TEXT[4], width=24, anchor=tkinter.E)
        self.exam1_entry = tkinter.Entry(self.exam1_frame,
                                        width=10)   
        self.exam1_label.pack(side='left')
        self.exam1_entry.pack(side='left')

        # Create and pack the widgets for exam 2
        self.exam2_label = tkinter.Label(self.exam2_frame,
                    text=LABEL_TEXT[5], width=24, anchor=tkinter.E)
        self.exam2_entry = tkinter.Entry(self.exam2_frame,
                                        width=10) 
        self.exam2_label.pack(side='left')
        self.exam2_entry.pack(side='left')

        # Create and pack the widgets for final exam
        self.final_label = tkinter.Label(self.final_frame,
                    text=LABEL_TEXT[6], width=24, anchor=tkinter.E)
        self.final_entry = tkinter.Entry(self.final_frame,
                                        width=10) 
        self.final_label.pack(side='left')
        self.final_entry.pack(side='left')
        
        # Create and pack the calculate button widget with result widget.
        self.calc_button = tkinter.Button(self.calculate_frame,
                                          text=BUTTON_TEXT[0],width=27,anchor=tkinter.N,
                                          command=self.combine_result)
        # Create three StringVar objects to store and update.                                  
        self.avg = tkinter.StringVar() 
        self.grade = tkinter.StringVar()
        self.combine = tkinter.StringVar()
        # Create a label to display result
        self.calculate_label = tkinter.Label(self.calculate_frame,
                                       relief='solid',
                                       width=10,
                                       textvariable=self.combine)
        self.calc_button.pack(side='left', padx=5)
        self.calculate_label.pack(side='left')
        
        # Create and pack the button widgets.     
        self.clear_button = tkinter.Button(self.button_frame,
                                          text=BUTTON_TEXT[1],
                                          command=self.clear)                                  
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy) 
        self.clear_button.pack(side='left',padx=5)
        self.quit_button.pack(side='left')

        #  Pack the frames.
        self.discussions_frame.pack()
        self.revel_frame.pack()
        self.quizzies_frame.pack()
        self.programs_frame.pack()
        self.exam1_frame.pack()
        self.exam2_frame.pack()
        self.final_frame.pack()
        self.calculate_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()    
        
    # Method for calculating the average
    def calc_avg(self):
        try: 
         # take the scores from the user for each category
            discussions = float(self.discussions_entry.get())
            revel = float(self.revel_entry.get())
            quizzies = float(self.quizzies_entry.get())
            programs = float(self.discussions_entry.get())
            exam1 = float(self.exam1_entry.get())
            exam2 = float(self.exam2_entry.get())
            final = float(self.final_entry.get())
            
        # Check for wrong input such as blank or non-numberic
        except ValueError: tkinter.messagebox.showinfo('Error!','Non-Numeric or Blank Data Entered.')

        # Update self.avg after calculating
        else: self.avg.set(format((discussions*0.5+revel+quizzies+programs*1.5+exam1*1.5+exam2*1.5+final*3)/10, '.2f'))
        
    # Method for calculating the grade letter
    def determine_grade(self):
        # Take the average score and check if it blank or not 
        avg = self.avg.get()
        if avg == '':
            return 0
        else:
            # Determind the grade base on the average 
            # Then update the self.grade
            if  float(avg) >= 89.45:
                self.grade.set('/A')
            if float(avg) < 89.45 and float(avg) >= 79.45:
                self.grade.set('/B')
            if float(avg) < 79.45 and float(avg) >= 69.45:
                self.grade.set('/C') 
            if float(avg) < 69.45 and float(avg) >= 59.45:
                self.grade.set('/D')
            if float(avg) < 59.45:
                self.grade.set('/F')  
            
    # Method for combine two results from calc_avg and determine_grade         
    def combine_result(self):
        # Call 2 calculate methods
        self.calc_avg()
        self.determine_grade()
        # Update self.combine to show final resilt
        self.combine.set(self.avg.get() + self.grade.get())
     
    # Method for clear button 
    def clear(self):
        self.discussions_entry.delete(0,'end')
        self.revel_entry.delete(0,'end')
        self.quizzies_entry.delete(0,'end')
        self.programs_entry.delete(0,'end')
        self.exam1_entry.delete(0,'end')
        self.exam2_entry.delete(0,'end')
        self.final_entry.delete(0,'end')       
        self.combine.set('')  

def main(): 
    # Create an instance of the ScoresGUI class. 
    scores = ScoresGUI()

main()
