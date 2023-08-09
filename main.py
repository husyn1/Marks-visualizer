from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import csv
import pandas as pd






root=Tk()
root.title("marks manager")
root.geometry("300x300")
root.resizable(False,False)

def openfilering():
    tf =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CSV file", "*.csv"),("CSV file","*.txt"), ("CSV files","*.rtf"),("all files","*.*")))
    loc=tf
    data = pd.read_csv(loc)
    total_marks=data.sum(axis=0, skipna=True)
    avg_marks=round(total_marks/len(data.index))

    
    marks_with_avg=pd.DataFrame(avg_marks)
    marks_dictionary=marks_with_avg.to_dict()
    mark_dict=marks_dictionary.get(0,{})
    
    root.destroy()

    # print(markdict)

    
    
    



    plt.title("Subject averages")

    names = list(mark_dict.keys())
    values = list(mark_dict.values())

    plt.bar(range(len(mark_dict)), values, tick_label=names)
    
    plt.show()




    
    


    

 
open_button = Button(root, text="Open Text File", command=openfilering)

open_button.place(x=100, y=100)











root.mainloop()