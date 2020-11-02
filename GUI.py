from tkinter import *
from tkinter import ttk
window = Tk() #create main window
window.title("Finance Calculator")

#Creates two tabs by using Notebook
nb = ttk.Notebook(window)
nb.grid(row=1, column=0,)

page1 = ttk.Frame(nb)
nb.add(page1, text="Tab1")

page2 = ttk.Frame(nb)
nb.add(page2, text="Tab2")

#Code for tab1

#creates labels, buttons and puts them in my GUI window
yearsLabel = Label(page1, text="Years")
entry1 = Entry(page1)
AmountLabel = Label(page1, text="amount")
entry2 = Entry(page1)
RateLabel = Label(page1, text="rate")
entry3 = Entry(page1)

#Calculates Future Value and presents it in the window by creating a label.
def futu():
    years = int(entry1.get())
    amount = int(entry2.get())
    rate = float(entry3.get())/100
    ans1 = round((amount * (1 + (rate))**years), 2)
    answerLabel1 = Label(page1, text=ans1)
    answerLabel1.grid(row=5, column=1)

#Calculates Present Value and presents it in the window by creating a label.
def pres():
    years = int(entry1.get())
    amount = int(entry2.get())
    rate = int(entry3.get())/100
    ans2 = round(amount / (1 + rate) ** years, 2)
    answerLabel2 = Label(page1, text=ans2)
    answerLabel2.grid(row=6, column=1)

#Creates two buttons that will run a function
button1 = Button(page1, text="Calculate Future Value", command=futu)
button2 = Button(page1, text="Calculate Present Value", command=pres)


#Organises the layout of the labels, buttons and entry boxes
yearsLabel.grid(row=2, column=0)
entry1.grid(row=2, column=1)
AmountLabel.grid(row=3, column=0)
entry2.grid(row=3, column=1)
RateLabel.grid(row=4, column=0)
entry3.grid(row=4, column=1)
button1.grid(row=5, column=0)
button2.grid(row=6, column=0)

#Code for Tab2

#To find all widgets
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

#will Track the changes in the drop down and apply a function to each selection
def change(*args):
    if var.get() == "Current Ratio":
        currentRatUI()
    elif var.get() == "Working Capital Ratio":
        workingCap()
    elif var.get() == "Debt To Equity Ratio":
        debt2equity()
    elif var.get() == "Gross Profit Margin Ratio":
        grossProfMar()

#Creates the neccessary User Interface
def currentRatUI():
    # to delete all widgets except my dropdown menu on tab2
    widget_list = all_children(page2)
    for item in widget_list:
        if item == dropDownMenu:
            pass
        else:
            item.pack_forget()
    #Make and display the interface labels and entry
    curAss = Label(page2, text="Current Assets")
    global curAssEntry
    curAssEntry= Entry(page2)
    curAss.pack()
    curAssEntry.pack()

    curLiab = Label(page2, text="Current Liabilities")
    global curLiabEntry
    curLiabEntry= Entry(page2)
    curLiab.pack()
    curLiabEntry.pack()

    #create an action button which will run the calculation function when pressed
    #without lambda... the command function is being ran without me clicking the button whick is not normal
    calcbutton = Button(page2, text="Calculate Current Ratio", command=lambda : currentRat()) #Struggled with this as without the lamda it doesn't work
    calcbutton.pack()

#calculates the current ratio and displays it in a label
def currentRat():
    global curAssEntry
    global curLiabEntry
    asset = float(curAssEntry.get())
    liability = float(curLiabEntry.get())
    ansCurrRat = round(asset/liability, 2)
    answerLabelCurrRat = Label(page2, text=ansCurrRat)
    answerLabelCurrRat.pack()



def workingCap():
    # to delete all widgets except my dropdown menu on tab2
    # this will clear the interface
    widget_list = all_children(page2)
    for item in widget_list:
        if item == dropDownMenu:
            pass
        else:
            item.pack_forget()
    # Make the relevant user interface
    wrkCap = Label(page2, text="Current Assets")
    global wrkCapEntry
    wrkCapEntry = Entry(page2)
    wrkCap.pack()
    wrkCapEntry.pack()

    wrkCap2 = Label(page2, text="Current Liabilities")
    global wrkCap2Entry
    wrkCap2Entry = Entry(page2)
    wrkCap2.pack()
    wrkCap2Entry.pack()

    # create an action button which will run the calculation function when pressed
    calcbutton = Button(page2, text="Calculate Working Capital",command=lambda : wrkingCap())
    calcbutton.pack()

# calculates working capital and displays the answer
def wrkingCap():
    global wrkCapEntry
    global wrkCap2Entry
    asset = float(wrkCapEntry.get())
    liability = float(wrkCap2Entry.get())
    ansCurrRat = round(asset - liability, 2)
    answerLabelCurrRat = Label(page2, text=ansCurrRat)
    answerLabelCurrRat.pack()

def debt2equity():
    # to delete all widgets except my dropdown menu on tab2
    widget_list = all_children(page2)
    for item in widget_list:
        if item == dropDownMenu:
            pass
        else:
            item.pack_forget()
    # Make the interface
    totalDebt = Label(page2, text="Total Debt")
    global totalDebtEntry
    totalDebtEntry = Entry(page2)
    totalDebt.pack()
    totalDebtEntry.pack()

    totalEquity = Label(page2, text="Total Equity")
    global totalEquityEntry
    totalEquityEntry = Entry(page2)
    totalEquity.pack()
    totalEquityEntry.pack()

    calcbutton = Button(page2, text="Calculate Debt To Equity", command=lambda: debt2equityCalc())
    calcbutton.pack()

def debt2equityCalc():
    global totalDebtEntry
    global totalEquityEntry
    Debts = float(totalDebtEntry.get())
    Equity = float(totalEquityEntry.get())
    ans = round(Debts/Equity, 2)
    answerLabel = Label(page2, text=ans)
    answerLabel.pack()

def grossProfMar():
    # to delete all widgets except my dropdown menu on tab2
    widget_list = all_children(page2)
    for item in widget_list:
        if item == dropDownMenu:
            pass
        else:
            item.pack_forget()
    # Make the interface
    GrossProfit = Label(page2, text="Gross Profit")
    global GrossProfitEntry
    GrossProfitEntry = Entry(page2)
    GrossProfit.pack()
    GrossProfitEntry.pack()

    Revenue = Label(page2, text="Revenue")
    global RevenueEntry
    RevenueEntry = Entry(page2)
    Revenue.pack()
    RevenueEntry.pack()

    calcbutton = Button(page2, text="Calculate Gross Profit Margin", command=lambda: GPMCalc())
    calcbutton.pack()

def GPMCalc():
    global GrossProfitEntry
    global RevenueEntry
    profit = float(GrossProfitEntry.get())
    revenue = float(RevenueEntry.get())
    ans = round(profit/revenue, 2)
    ansLabel = Label(page2, text=ans)
    ansLabel.pack(expand=True)

#Creates the Drop down menu
options = [
    "Current Ratio",
    "Working Capital Ratio",
    "Debt To Equity Ratio",
    "Gross Profit Margin Ratio"
]
var = StringVar(page2) #gives variable var a string data type
var.set(options[0]) #sets initial value of var to "Current Ratio"
var.trace("w", change) #Tracks which of the options is selected

dropDownMenu = OptionMenu(page2, var, options[0], options[1], options[2], options[3]) #Creates a drop down menu
dropDownMenu.pack() #Displays the drop down menu



#keeps the window open
window.mainloop()

