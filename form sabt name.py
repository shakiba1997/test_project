from tkinter import *
from tkinter import messagebox
from tkinter import ttk


Screen = Tk()
Screen.geometry("%dx%d+%d+%d" % (1520, 790, 0, 0))
Screen.title("فرم ثبت نام")
Screen.iconbitmap("img/titr.ico")


UserAll = []


def Register(user):
    if int(user["Age"]) >= 18:
        if Exist (user):
            messagebox.showerror("توجه", "این دانشجو قبلا ثبت شده است")
            return False
        else:
            UserAll.append(user)
            messagebox.showinfo("انجام شد", "ثبت نام شما با موفقیت انجام شد")
            return True
    else:
        messagebox.showwarning("توجه", "برای ورود به دانشگاه سنتون کم میباشد")
        return False




def OnClickReg():
    name = Name.get()
    family = Family.get()
    age = Age.get()
    codemelly = CodeMelly.get()
    number = Number.get()
    Us = {"Name": name, "Family": family, "Age": age, "CodeMelly": codemelly, "Number": number}
    Result = Register(Us)
    if Result == True:
        ListItem = [Name, Family, Age, CodeMelly, Number]
        insertData(ListItem)
        Clear(ListItem)


def Clear(listval):
    for item in listval:
        item.set("")


def insertData(value):
    tbl.insert("", "end", text="1", values=[value[4].get(), value[3].get(), value[2].get(), value[1].get(), value[0].get()])


def GetSelection(e):
    Selection_Row = tbl.selection()
    if Selection_Row != ():
        btnEdit.place(x=150, y=160)
        ListItem = [Name, Family, Age, CodeMelly, Number]
        Clear(ListItem)
        Name.set(tbl.item(Selection_Row)["values"][4])
        Family.set(tbl.item(Selection_Row)["values"][3])
        Age.set(tbl.item(Selection_Row)["values"][2])
        CodeMelly.set(tbl.item(Selection_Row)["values"][1])
        Number.set(tbl.item(Selection_Row)["values"][0])


def Search(value):
    ListSec = []
    for item in UserAll:
        if item["Name"] == value or item["Family"] == value or item["Age"] == value or item["CodeMelly"] == value or item["Number"] == value:
            ListSec.append(item)
        return ListSec
def OnClickSearch():
    query = txtSearch.get()
    result = Search(query)
    CleanTable()
    Load(result)


def Load(value):
    for item in value:
        tbl.insert("", "end", text="1", values=[item["Number"], item["CodeMelly"], item["Age"], item["Family"], item["Name"]])


def CleanTable():
    for item in tbl.get_children():
        sel = (str(item),)
        tbl.delete(sel)


def Exist(value):
    for item in UserAll:
        if value["Name"] == item["Name"] and value["Family"] == item["Family"] and value["Age"] == item["Age"] and value["CodeMelly"] == item["CodeMelly"] and value["Number"] == item["Number"]:
            return True
    return False


def OnClickDelete():
    result = messagebox.askquestion("هشدار", "آیا مطمئن هستید که می خواهید این داده را حذف کنید؟")
    if result == "yes":
        Delete()


def Delete():
    Selection_Row = tbl.selection()
    if Selection_Row != ():
        SelectItem = tbl.item(Selection_Row)["values"]
        Dic = {"Name": SelectItem[4], "Family": SelectItem[3], "Age": str(SelectItem[2]),
               "CodeMelly": str(SelectItem[1]), "Number": str(SelectItem[0])}
        tbl.delete(Selection_Row)
        UserAll.remove(Dic)


def OnClickEdit():
    Selection_Row = tbl.selection()
    SelectItem = tbl.item(Selection_Row)["values"]
    Dic = {"Name": SelectItem[4], "Family": SelectItem[3], "Age": str(SelectItem[2]),
            "CodeMelly": str(SelectItem[1]), "Number": str(SelectItem[0])}
    indexUs = UserAll.index(Dic)
    UserAll[indexUs] = {"Name": Name.get(), "Family": Family.get(), "Age": str(Age.get()), "CodeMelly": str(CodeMelly.get()), "Number": str(Number.get())}
    btnEdit.place_forget()
    ListItem = [Name, Family, Age, CodeMelly, Number]
    Clear(ListItem)


#search
lblSearch = Label(Screen, text="جستوجو")
lblSearch.place(x=1200, y=10)
txtSearch = Entry(Screen)
txtSearch.place(x=1250, y=10)
btnSearch = Button(Screen, text="جستوجوکن", command=OnClickSearch).place(x=1250, y=40)



#labels
lblName = Label(Screen, text="نام").place(x=20, y=10)
lblFamily = Label(Screen, text="نام خانوادگی").place(x=10, y=40)
lblAge = Label(Screen, text="سن").place(x=20, y=70)
lblCodeMelly = Label(Screen, text="کد ملی").place(x=20, y=100)
lblNumber = Label(Screen, text="شماره تماس").place(x=10, y=130)


#vars
Name = StringVar()
Family = StringVar()
Age = StringVar()
CodeMelly = StringVar()
Number = StringVar()


#inputs
txtName = Entry(Screen, textvariable=Name, justify="right")
txtName.place(x= 80, y= 10)
txtFamily = Entry(Screen, textvariable=Family, justify="right")
txtFamily.place(x= 80, y= 40)
txtAge = Entry(Screen, textvariable=Age, justify="right")
txtAge.place(x=80, y=70)
txtCodeMelly = Entry(Screen, textvariable=CodeMelly, justify="right")
txtCodeMelly.place(x=80, y=100)
txtNumber = Entry(Screen, textvariable=Number, justify="right")
txtNumber.place(x=80, y=130)


#btns
btnRegister = Button(Screen, text="ثبت نام", command=OnClickReg)
btnRegister.place(x=80, y=160)
btnDelete = Button(Screen, text="حذف", bg="red", fg="black", command=OnClickDelete)
btnDelete.place(x=80, y=190)
btnEdit = Button(Screen, text="ویرایش", bg="#f5821d", fg="black", command=OnClickEdit)
btnEdit.place_forget()

#tabel
tbl = ttk.Treeview(Screen, columns=("c1", "c2", "c3", "c4", "c5"), show="headings", height=20)
tbl.column("#5", width=50)
tbl.heading("#5", text="نام")

tbl.column("#4", width=80)
tbl.heading("#4", text="نام خانوادگی")

tbl.column("#3", width=50)
tbl.heading("#3", text="سن")

tbl.column("#2", width=50)
tbl.heading("#2", text="کد ملی")

tbl.column("#1", width=80)
tbl.heading("#1", text="شماره تماس")
tbl.bind("<Button-1>", GetSelection)
tbl.place(x=80, y=220)


Screen.mainloop()


