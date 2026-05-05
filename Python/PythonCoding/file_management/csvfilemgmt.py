import csv
import os
from tkinter.filedialog import SaveAs

'''empid, ename
101, AAA
102, BBB'''

def write_csv(filename):
    with open(filename,"r",newline="\n") as file:
        reader = csv.DictReader(file)





def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename}deleted")
    else:
        print(f"{filename}does not exist")


filename="myfile.csv"
write_csv(filename)
print("data read from csv")
read_csv(filename)