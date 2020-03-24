import os
import csv
import tkinter as tk
from tkinter import filedialog  # i need this...I loathe hard coded shit

# let's let the user choose the file with the gui dialog box.
root = tk.Tk()
root.withdraw()

pybankfile = filedialog.askopenfilename()
with open(pybankfile, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # skip the header
    csv_header = next(csvfile)
    print(f"CSV Header: {csv_header}")
    reader = csv.reader(csvfile)
    data = list(reader)
    #create a second_column list to store financial dollars values only
    second_column = [int(row[1]) for row in data]
    # number of months is a count (in python len(list))
    countmths = len(second_column) 
    #subtract successive elements in new array "second_column"
    d = [second_column[i + 1] - second_column[i] for i in range(len(second_column)-1)] 
    #get the sum of differences so we can average them
    dy=sum(d)
    #Median (not requested) but easily computed - save for later
    sort_col_2 = sorted(second_column)
    maxnum = max(second_column)
    minnum = min(second_column)
    tot = sum(second_column)
    avg_bal = tot / countmths
    avg_diff = dy / (countmths-1)

    #print values for TA's for homework
    print(f"minimum: {minnum}")
    print(f"maximum: {maxnum}")
    print(f"Balance: {tot}")
    print(f"Average:{round(avg_bal,2)}")
    print(f"Avg Diff:{round(avg_diff,2)}")

    