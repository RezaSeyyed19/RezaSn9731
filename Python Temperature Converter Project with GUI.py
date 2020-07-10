from tkinter import messagebox
# -----------Setting----------
def Converter():
    root = Tk()
    root.title("Unit Converter")
    root.geometry("600x525")
    root.resizable(False, False)
    color = "yellow"
    root.configure(bg=color)
    def R_S():
        Label_RS_Team = Label(root, text="R.S Team", font=("Vivaldi", 15), bg="pink", )
        Label_RS_Team.place(x=495)
    R_S()
    Label_RS_Team = Label(root, text="Temperature Convert", font=("Algerian", 12), bg="pink")
    Label_RS_Team.place(x=1)
    color1 = "gray"
    color2 = "red"
    color3 = "yellow"
    color4 = "green"
    # --------------------- Frames --------------------------
    # Frame_1 = Frame(root, width=600, height=150, bg=color)
    # Frame_1.pack(side=TOP)
    #
    # Frame_2 = Frame(root, width=600, height=150, bg="black")
    # Frame_2.pack(side=TOP)
    #
    # Frame_3 = Frame(root, width=600, height=150, bg="yellow")
    # Frame_3.pack(side=TOP)
    #
    # Frame_3 = Frame(root, width=600, height=150, bg="blue")
    # Frame_3.pack(side=TOP)
    # --------------------- Define --------------------------
    Num_C = StringVar()
    Num_K = StringVar()
    Num_R = StringVar()
    Num_F = StringVar()
    Res_C = StringVar()
    Res_K = StringVar()
    Res_R = StringVar()
    Res_F = StringVar()
    Res_C_1 = StringVar()
    Res_K_1 = StringVar()
    Res_R_1 = StringVar()
    Res_F_1 = StringVar()
    Res_C_2 = StringVar()
    Res_K_2 = StringVar()
    Res_R_2 = StringVar()
    Res_F_2 = StringVar()
    Res_C_3 = StringVar()
    Res_K_3 = StringVar()
    Res_R_3 = StringVar()
    Res_F_3 = StringVar()

    # -------------------- Error Function -------------------------
    def ErrMsg(ms):
        if ms == "Error":
            messagebox.showerror("Error", "Please Enter True Number!!!!")

    # -------------------- Celciuse Function -------------------------

    def C_F():
        try:
            value1 = (float(Num_C.get()) * 1.8) + 32
            Res_F.set(value1)
        except:
            ErrMsg("Error")

    def C_K():
        try:
            value2 = float(Num_C.get()) + 273.15
            Res_K.set(value2)
        except:
            ErrMsg("Error")

    def C_R():
        try:
            value3 = (float(Num_C.get()) * 1.8) + 491.67
            Res_R.set(value3)
        except:
            ErrMsg("Error")

    # -------------------- Kelvin Function -------------------------

    def K_C():
        try:
            value4 = float(Num_K.get()) - 273.15
            Res_C_1.set(value4)
        except:
            ErrMsg("Error")

    def K_F():
        try:
            value5 = ((float(Num_K.get())-273.15) * 1.8) + 32
            Res_F_1.set(value5)
        except:
            ErrMsg("Error")

    def K_R():
        try:
            value6 = ((float(Num_K.get())-273.15) * 1.8) + 491.67
            Res_R_1.set(value6)
        except:
            ErrMsg("Error")

    # -------------------- Farenheite Function -------------------------

    def F_C():
        try:
            value7 = (float(Num_F.get()) - 32) * 5/9
            Res_C_2.set(value7)
        except:
            ErrMsg("Error")

    def F_K():
        try:
            value8 = ((float(Num_F.get())-32)/1.8) + 273.15
            Res_K_2.set(value8)
        except:
            ErrMsg("Error")

    def F_R():
        try:
            value9 = float(Num_F.get()) + 459.67
            Res_R_2.set(value9)
        except:
            ErrMsg("Error")

    # -------------------- Ranklin Function -------------------------

    def R_C():
        try:
            value10 = (float(Num_R.get()) - 491.67) / 1.8
            Res_C_3.set(value10)
        except:
            ErrMsg("Error")

    def R_K():
        try:
            value11 = ((float(Num_R.get()) - 491.67) / 1.8) + 273.15
            Res_K_3.set(value11)
        except:
            ErrMsg("Error")

    def R_F():
        try:
            value12 = float(Num_R.get()) - 459.67
            Res_F_3.set(value12)
        except:
            ErrMsg("Error")

    # ---------------- Labels and Entries (C)------------------

    L_C_L = Label(root, bg=color3, text="(Celsius):درجه سلسیوس را وارد کنید")
    L_C_L.place(x=225, y=0)

    L_C_E = Entry(root, textvariable=Num_C)
    L_C_E.place(x=250, y=25)

    Btn_C_K = Button(root, text="Calculate Kelvin", command=lambda: C_K(), bg=color1)
    Btn_C_K.place(x=50, y=55)

    Res_C_K = Label(root, textvariable=Res_K, bg=color)
    Res_C_K.place(x=50, y=85)

    Btn_C_F = Button(root, text="Calculate Fahrenheit", command=lambda: C_F(), bg=color1)
    Btn_C_F.place(x=250, y=55)

    Res_C_F = Label(root, textvariable=Res_F, bg=color)
    Res_C_F.place(x=250, y=85)

    Btn_C_R = Button(root, text="Calculate Rankin", command=lambda: C_R(), bg=color1)
    Btn_C_R.place(x=450, y=55)

    Res_C_R = Label(root, textvariable=Res_R, bg=color)
    Res_C_R.place(x=450, y=85)

    # ---------------- Labels and Entries (K)------------------

    L_K_L = Label(root, bg=color3, text="(Kelvin):درجه کلوین را وارد کنید")
    L_K_L.place(x=235, y=135)

    L_K_E = Entry(root, textvariable=Num_K)
    L_K_E.place(x=250, y=160)

    Btn_K_C = Button(root, text="Calculate Celsius", command=lambda: K_C(), bg=color2)
    Btn_K_C.place(x=50, y=190)

    Res_K_C = Label(root, textvariable=Res_C_1, bg=color)
    Res_K_C.place(x=50, y=220)

    Btn_K_F = Button(root, text="Calculate Fahrenheit", command=lambda: K_F(), bg=color2)
    Btn_K_F.place(x=250, y=190)

    Res_K_F = Label(root, textvariable=Res_F_1, bg=color)
    Res_K_F.place(x=250, y=220)

    Btn_K_R = Button(root, text="Calculate Rankin", command=lambda: K_R(), bg=color2)
    Btn_K_R.place(x=450, y=190)

    Res_K_R = Label(root, textvariable=Res_R_1, bg=color)
    Res_K_R.place(x=450, y=220)

    # ---------------- Labels and Entries (K)------------------

    L_F_L = Label(root, bg=color3, text="(Fahrenheit):درجه فارنهایت را وارد کنید")
    L_F_L.place(x=225, y=260)

    L_F_E = Entry(root, textvariable=Num_F)
    L_F_E.place(x=250, y=285)

    Btn_F_C = Button(root, text="Calculate Celsius", command=lambda: F_C(), bg=color3)
    Btn_F_C.place(x=50, y=315)

    Res_F_C = Label(root, textvariable=Res_C_2, bg=color)
    Res_F_C.place(x=50, y=345)

    Btn_F_K = Button(root, text="Calculate Kelvin", command=lambda: F_K(), bg=color3)
    Btn_F_K.place(x=260, y=315)

    Res_F_K = Label(root, textvariable=Res_K_2, bg=color)
    Res_F_K.place(x=250, y=345)

    Btn_F_R = Button(root, text="Calculate Rankin", command=lambda: F_R(), bg=color3)
    Btn_F_R.place(x=450, y=315)

    Res_F_R = Label(root, textvariable=Res_R_2, bg=color)
    Res_F_R.place(x=450, y=345)

    # ---------------- Labels and Entries (K)------------------

    L_R_L = Label(root, bg=color3, text="(Rankin):درجه رانکین را وارد کنید")
    L_R_L.place(x=235, y=385)

    L_R_E = Entry(root, textvariable=Num_R)
    L_R_E.place(x=250, y=410)

    Btn_R_C = Button(root, text="Calculate Celsius", command=lambda: R_C(), bg=color4)
    Btn_R_C.place(x=50, y=440)

    Res_R_C = Label(root, textvariable=Res_C_3, bg=color)
    Res_R_C.place(x=50, y=470)

    Btn_R_K = Button(root, text="Calculate Kelvin", command=lambda: R_K(), bg=color4)
    Btn_R_K.place(x=260, y=440)

    Res_R_K = Label(root, textvariable=Res_K_3, bg=color)
    Res_R_K.place(x=250, y=470)

    Btn_R_F = Button(root, text="Calculate Fahrenheit", command=lambda: R_F(), bg=color4)
    Btn_R_F.place(x=450, y=440)

    Res_R_F = Label(root, textvariable=Res_F_3, bg=color)
    Res_R_F.place(x=450, y=470)

    root.mainloop()
Converter()
