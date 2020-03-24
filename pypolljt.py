import os
import csv
import tkinter as tk
from tkinter import filedialog  # i need this...I loathe hard coded shit

# let's let the user choose the file with the gui dialog box.
root = tk.Tk()
root.withdraw()

pypollfile = filedialog.askopenfilename()
with open(pypollfile, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")
    reader = csv.reader(csvfile)
    data = list(reader)
    
    #create a second_column list to store financial dollars values only
    candidates = [(row[2]) for row in data]
    # total votes (in python len(list))
    votecount = len(candidates) 
    #use the .count function
    def occur_dict(candidates):
        d = {}
        for i in candidates:
            if i in d:
                d[i] = d[i]+1
            else:
                d[i] = 1
        for key, value in d.items():
            print(key, value)
                #get the sum of differences so we can average them
    
    #Median (not requested) but easily computed - save for later
    

    #print values for TA's for homework
    #print(f"minimum: {minnum}")
    

    