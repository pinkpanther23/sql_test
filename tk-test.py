import tkinter as tk
from tkinter import ttk
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

window = tk.Tk()

title = tk.Label(window, text = "SQL Database", fg='red', font=("Helvetica", 16))
title.place(x=20, y=10)

s_data = ("Select All" ,"CD #", "Mutation Status", "Run Number", "PG #", "DNA #", "DNA Barcode", "RNA #", "RNA Barcode", "Receive Date", "Result Date", "RNA Fusion Status", "Panel Type", "Sample Type")
v_data = ("Select All", "CD #", "Locus", "Genotype", "Reference", "Observed", "Mutation Type", "Gene", "Exon", "Mutation Length", "Variant Class", "Gene Class", "Coverage", "Frequency", "Coding Change", "Amino Acid Change", "Transcript", "Variant Change", "Database ID", "Fusion Read Count")

s_lbl = tk.Label(window, text = "Select from Samples", fg='blue', font=("Helvetica", 8))
s_lbl.place(x=40, y=60)

v_lbl = tk.Label(window, text = "Select from Variants", fg='blue', font=("Helvetica", 8))
v_lbl.place(x=200, y=60)

#listbox for samples table
s_lb = tk.Listbox(window, height=15, selectmode = 'multiple')
for num in s_data:
    s_lb.insert(tk.END, num)
s_lb.place(x=40, y=130)

#listbox for variants table
v_lb = tk.Listbox(window, height = 21, selectmode = 'multiple')
for num in v_data:
    v_lb.insert(tk.END, num)
v_lb.place(x=200, y=130)

def convertToString(my_list):
    seperator = ','
    my_string = seperator.join(my_list)
    return my_string

def convertToList(my_string):
    my_list = list(my_string.split(","))
    return my_list

def listbox_samples():
    listbox_values = []
    for i in s_lb.curselection():
        temp = s_lb.get(i)
        listbox_values.append(temp)
    listbox_string = convertToString(listbox_values)
    s_result.set(listbox_string)

s_result = tk.StringVar()

def createSelect(len, table):
    if(len == 1):
        sql_select = "SELECT ? FROM " + table + ";"
    elif (len == 2):
        sql_select = "SELECT ?, ? FROM " + table + ";"
    elif (len == 3):
        sql_select = "SELECT ?, ?, ? FROM " + table + ";"
    elif (len == 4):
        sql_select = "SELECT ?, ?, ?, ? FROM " + table + ";"
    elif (len == 5):
        sql_select = "SELECT ?, ?, ?, ?, ? FROM " + table + ";"
    else:
        sql_select = "SELECT ? FROM " + table + ";"
    return sql_select

def convertSelectionS(my_list):
    new_list = []
    for i in my_list:
        if(i == "CD #"):
            new_list.append("CD_num")
        elif(i == "Mutation Status"):
            new_list.append("Mutation_status")
        elif (i == "Run Number"):
            new_list.append("Run_num")
        elif (i == "PG #"):
            new_list.append("PG_num")
        elif (i == "DNA #"):
            new_list.append("DNA_num")

    return new_list

def print_S_Result():
    data = s_result.get()
    list_data = convertToList(data)
    list_size = len(list_data)
    new_list = convertSelectionS(list_data)
    combined = ', '.join(new_list)
    #sql_select = createSelect(list_size, "Samples")
    sql_select = "SELECT " + combined + " FROM Samples"
    print(sql_select)
    cur.execute(sql_select)
    #cur.execute(sql_select)
    result = cur.fetchall()
    for i in result:
        print(i)
    #for i in list_data:
        #print(i)

s_btn = tk.Button(window, text = "Submit", fg = "blue", command = listbox_samples)
s_btn.place(x=40, y=90)

v_btn = tk.Button(window, text = "Submit", fg = "blue")
v_btn.place(x=200, y=90)

btn2 = tk.Button(window, text = "Print", fg = "blue", command = print_S_Result)
btn2.place(x=90, y=90)

#print(result)

window.title("test")
window.geometry("500x600+10+20")
window.mainloop()
