from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from sympy import *
import numpy as np


root = Tk()
root.title("MAIN-PAGE")
root.geometry("1140x750+0+0")


#####inverting adder start#######
# ======================================================
def in_adder():
    adder = Toplevel()
    adder.title("Inverting Adder")
    adder.geometry("1140x750+0+0")
#========================result system start===========================
    def result_ia():
        Rf = int(rf.get())
        R1 = int(r1.get())
        R2 = int(r2.get())
        R3 = int(r3.get())
        R4 = int(r4.get())
        R5 = int(r5.get())

        V1 = int(v1.get())
        V2 = int(v2.get())
        V3 = int(v3.get())
        V4 = int(v4.get())
        V5 = int(v5.get())

        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      I1      ")
        x.grid(row=20, column=0)
        i1 = Entry(f2)
        i1.grid(row=20, column=1)
        # ------------------------------------------for voltage
        x = Label(f2, text="      I2     ")
        x.grid(row=20, column=2)
        i2 = Entry(f2)
        i2.grid(row=20, column=3)
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        # ====================================
        x = Label(f2, text="      I3      ")
        x.grid(row=22, column=0)
        i3 = Entry(f2)
        i3.grid(row=22, column=1)
        x = Label(f2, text="      I4      ")
        x.grid(row=22, column=2)
        i4 = Entry(f2)
        i4.grid(row=22, column=3)
        y = Label(f2, text="")
        y.grid(row=23, column=1, rowspan=2)
        # ===================================
        x = Label(f2, text="      I5      ")
        x.grid(row=25, column=0)
        i5 = Entry(f2)
        i5.grid(row=25, column=1)
        x = Label(f2, text="      Irf      ")
        x.grid(row=25, column=2)
        irf = Entry(f2)
        irf.grid(row=25, column=3)
        y = Label(f2, text="")
        y.grid(row=26, column=1, rowspan=2)
        # ======================================
        y = Label(f2, text="      Vout      ")
        y.grid(row=28, column=0)
        vout = Entry(f2)
        vout.grid(row=28, column=1)
        y = Label(f2, text="")
        y.grid(row=32, column=1)
        # ======================================
        x = Label(f2, text="      Vrf      ")
        x.grid(row=28, column=2)
        vrf = Entry(f2)
        vrf.grid(row=28, column=3, )
        # ================calculation part======================
        if R3 == 0 and R4 == 0 and R5 == 0:
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2)+" V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0,str(V2/R2) + " A")
        elif R4 == 0 and R5 == 0:
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3)+" V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0,str(V2/R2) + " A")
            i3.insert(0,str(V3/R3) + " A")
        elif R5 == 0:
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4)+" V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0,str(V2/R2) + " A")
            i3.insert(0,str(V3/R3) + " A")
            i4.insert(0, str(V4/R4) + " A")
        elif R1 !=0 and R2!=0 and R3 != 0 and R4 != 0 and R5 != 0:
            vout.insert(0, str(-((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4+ (Rf / R5) * V5))+" V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0,str(V2/R2) + " A")
            i3.insert(0,str(V3/R3) + " A")
            i4.insert(0, str(V4/R4) + " A")
            i5.insert(0,str(V5/R5) + ' A')
        else:
            messagebox.showwarning( "Warning", "There may be some unfilled field between two entry")

        vrf.insert(0, str(vout.get()))
        # =================Result system end====================

    f1 = Frame(adder, width=500, height=800, bg="#216ade")
    f2 = Frame(adder, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      R1      ")
    x.grid(row=0, column=0)
    r1 = Entry(f2)
    r1.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      V1      ")
    x.grid(row=0, column=2)
    v1 = Entry(f2)
    v1.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      R2      ")
    x.grid(row=2, column=0)
    r2 = Entry(f2)
    r2.grid(row=2, column=1)
    x = Label(f2, text="      V2      ")
    x.grid(row=2, column=2)
    v2 = Entry(f2)
    v2.grid(row=2, column=3)
    y = Label(f2, text="")
    y.grid(row=3, column=1, rowspan=2)
    # ===================================
    x = Label(f2, text="      R3      ")
    x.grid(row=5, column=0)
    v = StringVar(root, value='0')
    r3 = Entry(f2, textvariable=v)
    r3.grid(row=5, column=1)
    x = Label(f2, text="      V3      ")
    x.grid(row=5, column=2)
    vv = StringVar(root, value='0')
    v3 = Entry(f2, textvariable=vv)
    v3.grid(row=5, column=3)
    y = Label(f2, text="")
    y.grid(row=6, column=1, rowspan=2)
    # ======================================
    x = Label(f2, text="      R4      ")
    x.grid(row=8, column=0)
    vvv = StringVar(root, value='0')
    r4 = Entry(f2, textvariable=vvv)
    r4.grid(row=8, column=1)
    x = Label(f2, text="      V4      ")
    x.grid(row=8, column=2)
    vvvv = StringVar(root, value='0')
    v4 = Entry(f2, textvariable=vvvv)
    v4.grid(row=8, column=3)
    y = Label(f2, text="")
    y.grid(row=9, column=1)
    # ======================================
    x = Label(f2, text="      R5      ")
    x.grid(row=11, column=0)
    vvvvv = StringVar(root, value='0')
    r5 = Entry(f2, textvariable=vvvvv)
    r5.grid(row=11, column=1)
    x = Label(f2, text="      V5      ")
    x.grid(row=11, column=2)
    vvvvvv = StringVar(root, value='0')
    v5 = Entry(f2, textvariable=vvvvvv)
    v5.grid(row=11, column=3)
    y = Label(f2, text="")
    y.grid(row=12, column=1)
    # ======================================
    x = Label(f2, text="      Rf      ")
    x.grid(row=14, column=0)
    rf = Entry(f2)
    rf.grid(row=14, column=1, )
    x = Label(f2, text=" ")
    x.grid(row=15, column=0)
    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade", command=result_ia)
    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=adder.destroy)
    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    adder.mainloop()
    #============================Inverting Adder End====================================================================

    #============================Non Invering Adder Start===============================================================

def non_adder():
    adder = Toplevel()
    adder.title("Non-inverting Adder")
    adder.geometry("1100x1000+0+0")
    # ========================result system start===========================

    def result_na():
        R1 = int(r1.get())
        R2 = int(r2.get())
        R3 = int(r3.get())
        R4 = int(r4.get())
        R5 = int(r5.get())
        Ra = int(ra.get())
        Rb = int(rb.get())

        V1 = int(v1.get())
        V2 = int(v2.get())
        V3 = int(v3.get())
        V4 = int(v4.get())
        V5 = int(v5.get())

        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      I1      ")
        x.grid(row=20, column=0)
        i1 = Entry(f2)
        i1.grid(row=20, column=1)
        # ------------------------------------------for voltage
        x = Label(f2, text="      I2     ")
        x.grid(row=20, column=2)
        i2 = Entry(f2)
        i2.grid(row=20, column=3)
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        # ====================================
        x = Label(f2, text="      I3      ")
        x.grid(row=22, column=0)
        i3 = Entry(f2)
        i3.grid(row=22, column=1)
        x = Label(f2, text="      I4      ")
        x.grid(row=22, column=2)
        i4 = Entry(f2)
        i4.grid(row=22, column=3)
        y = Label(f2, text="")
        y.grid(row=23, column=1, rowspan=2)
        # ===================================
        x = Label(f2, text="      I5      ")
        x.grid(row=25, column=0)
        i5 = Entry(f2)
        i5.grid(row=25, column=1)
        x = Label(f2, text="      Ia      ")
        x.grid(row=25, column=2)
        ia = Entry(f2)
        ia.grid(row=25, column=3)
        y = Label(f2, text="")
        y.grid(row=26, column=1, rowspan=2)
        # ======================================
        y = Label(f2, text="      Ib      ")
        y.grid(row=28, column=0)
        ib = Entry(f2)
        ib.grid(row=28, column=1)
        y = Label(f2, text="")
        y.grid(row=32, column=1)
        # ======================================
        x = Label(f2, text="      Vout      ")
        x.grid(row=28, column=2)
        vout = Entry(f2)
        vout.grid(row=28, column=3, )
        # ================calculation part======================
        if R3 == 0 and R4 == 0 and R5 == 0:
            vout.insert(0, str((1+Ra/Rb)*(V1*R2+V2*R1)/(R1+R2)) + " V")
            gain = 1+Ra/Rb
            Vout = (1+Ra/Rb)*(V1*R2+V2*R1)/(R1+R2)
            Vin = Vout/gain
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            ia.insert(0, str((Vout - Vin) / Ra) + " A")
            ib.insert(0, str(Vin / Rb) + " A")
        elif R4 == 0 and R5 == 0:
            vout.insert(0, str((1+Ra/Rb)*(R2*R3*V1+R1*R3*V2+R1*R2*V3)/(R1*R2+R2*R3+R1*R3)) + " V")
            gain = 1 + Ra / Rb
            Vout = (1+Ra/Rb)*(R2*R3*V1+R1*R3*V2+R1*R2*V3)/(R1*R2+R2*R3+R1*R3)
            Vin = Vout / gain

            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            ia.insert(0, str((Vout - Vin) / Ra) + " A")
            ib.insert(0, str(Vin / Rb) + " A")
        elif R5 == 0:
            vout.insert(0, str((1+Ra/Rb)*(R2*R3*R4*V1 + R1*R3*R4*V2 + R2*R1*R4*V3 + R2*R3*R1*V4)/(R1*R2*R3 + R1*R2*R4 + R1*R3*R4 + R2*R3*R4)) + " V")
            gain = 1 + Ra / Rb
            Vout = (1+Ra/Rb)*(R2*R3*R4*V1 + R1*R3*R4*V2 + R2*R1*R4*V3 + R2*R3*R1*V4)/(R1*R2*R3 + R1*R2*R4 + R1*R3*R4 + R2*R3*R4)
            Vin = Vout / gain
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            i4.insert(0, str(V4 / R4) + " A")
            ia.insert(0, str((Vout - Vin) / Ra) + " A")
            ib.insert(0, str(Vin / Rb) + " A")
        elif R1 != 0 and R2 != 0 and R3 != 0 and R4 != 0 and R5 != 0:
            vout.insert(0, str((1+Ra/Rb)*(R2*R3*R4*R5*V1 + R1*R3*R4*R5*V2 + R2*R1*R4*R5*V3 + R2*R3*R1*R5*V4 + R2*R3*R4*R1*V5)/(R2*R3*R4*R5 + R1*R3*R4*R5 + R2*R1*R4*R5 + R2*R3*R1*R5 + R2*R3*R4*R1)) + " V")
            gain = 1 + Ra / Rb
            Vout = (1+Ra/Rb)*(R2*R3*R4*R5*V1 + R1*R3*R4*R5*V2 + R2*R1*R4*R5*V3 + R2*R3*R1*R5*V4 + R2*R3*R4*R1*V5)/(R2*R3*R4*R5 + R1*R3*R4*R5 + R2*R1*R4*R5 + R2*R3*R1*R5 + R2*R3*R4*R1)
            Vin = Vout / gain
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            i4.insert(0, str(V4 / R4) + " A")
            i5.insert(0, str(V5 / R5) + ' A')
            ia.insert(0, str((Vout - Vin) / Ra) + " A")
            ib.insert(0, str(Vin / Rb) + " A")
        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")

        #vrf.insert(0, str(vout.get()))

    f1 = Frame(adder, width=500, height=800, bg="#216ade")
    f2 = Frame(adder, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      R1      ")
    x.grid(row=0, column=0)
    r1 = Entry(f2)
    r1.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      V1      ")
    x.grid(row=0, column=2)
    v1 = Entry(f2)
    v1.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      R2      ")
    x.grid(row=2, column=0)
    r2 = Entry(f2)
    r2.grid(row=2, column=1)
    x = Label(f2, text="      V2      ")
    x.grid(row=2, column=2)
    v2 = Entry(f2)
    v2.grid(row=2, column=3)
    y = Label(f2, text="")
    y.grid(row=3, column=1, rowspan=2)
    # ===================================
    x = Label(f2, text="      R3      ")
    x.grid(row=5, column=0)
    v = StringVar(root, value='0')
    r3 = Entry(f2, textvariable=v)
    r3.grid(row=5, column=1)
    x = Label(f2, text="      V3      ")
    x.grid(row=5, column=2)
    vv = StringVar(root, value='0')
    v3 = Entry(f2, textvariable=vv)
    v3.grid(row=5, column=3)
    y = Label(f2, text="")
    y.grid(row=6, column=1, rowspan=2)
    # ======================================
    x = Label(f2, text="      R4      ")
    x.grid(row=8, column=0)
    vvv = StringVar(root, value='0')
    r4 = Entry(f2, textvariable=vvv)
    r4.grid(row=8, column=1)
    x = Label(f2, text="      V4      ")
    x.grid(row=8, column=2)
    vvvv = StringVar(root, value='0')
    v4 = Entry(f2, textvariable=vvvv)
    v4.grid(row=8, column=3)
    y = Label(f2, text="")
    y.grid(row=9, column=1)
    # ======================================
    x = Label(f2, text="      R5      ")
    x.grid(row=11, column=0)
    vvvvv = StringVar(root, value='0')
    r5 = Entry(f2, textvariable=vvvvv)
    r5.grid(row=11, column=1)
    x = Label(f2, text="      V5      ")
    x.grid(row=11, column=2)
    vvvvvv = StringVar(root, value='0')
    v5 = Entry(f2, textvariable=vvvvvv)
    v5.grid(row=11, column=3)
    y = Label(f2, text="")
    y.grid(row=12, column=1)
    # ======================================
    x = Label(f2, text="      Ra      ")
    x.grid(row=14, column=0)
    ra = Entry(f2)
    ra.grid(row=14, column=1 )
    x = Label(f2, text="      Rb      ")
    x.grid(row=14, column=2)
    rb = Entry(f2)
    rb.grid(row = 14 ,column = 3 )
    x = Label(f2, text="  ")
    x.grid(row=15, column=0)
    #========================================







    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade",command = result_na)
    final.grid(row=18, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=adder.destroy)
    back.grid(row=18, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=19, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    adder.mainloop()


    #============================Non Invering Adder End=================================================================

    #============================Inverting subtarctor start=============================================================

# ========================================
#       Inverting Subtractor
def in_sub():
    sub = Toplevel()
    sub.title("Inverting Subtractor")
    sub.geometry("1100x1000+0+0")
#========================result system start===========================
    def result_ia():
        Rf = int(rf.get())
        R1 = int(r1.get())
        R2 = int(r2.get())
        V1 = int(v1.get())
        V2 = int(v2.get())


        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      I1      ")
        x.grid(row=20, column=0)
        i1 = Entry(f2)
        i1.grid(row=20, column=1)
        # ------------------------------------------for voltage
        x = Label(f2, text="      I2     ")
        x.grid(row=20, column=2)
        i2 = Entry(f2)
        i2.grid(row=20, column=3)
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        x1 = Label(f2, text="      Irf     ")
        x1.grid(row=25, column=0)
        irf = Entry(f2)
        irf.grid(row=25, column=1)
        y = Label(f2, text="")
        y.grid(row=26, column=1, rowspan=2)
        # ======================================
        y = Label(f2, text="      Vout      ")
        y.grid(row=28, column=0)
        vout = Entry(f2)
        vout.grid(row=28, column=1)
        y = Label(f2, text="")
        y.grid(row=32, column=1)
        # ======================================
        x = Label(f2, text="      Vrf      ")
        x.grid(row=28, column=2)
        vrf = Entry(f2)
        vrf.grid(row=28, column=3, )
        # ================calculation part======================
        if R1!=0 and R2!=0:
            re=Rf/R1*V1- Rf/R2*V2
            vout.insert(0,str(re)+ " V")
            i1.insert(0,str(V1/R1) + " A")
            i2.insert(0, str(V2/R2)+ " A")
        else:
            messagebox.showwarning( "Warning", "There may be some unfilled field between two entry")
        vrf.insert(0, str(vout.get()))
        irf.insert(0, str((re) / Rf) + " A")
        # =================Result system end====================
    f1 = Frame(sub, width=500, height=800, bg="#216ade")
    f2 = Frame(sub, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      R1      ")
    x.grid(row=0, column=0)
    r1 = Entry(f2)
    r1.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      V1      ")
    x.grid(row=0, column=2)
    v1 = Entry(f2)
    v1.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      R2      ")
    x.grid(row=2, column=0)
    r2 = Entry(f2)
    r2.grid(row=2, column=1)
    x = Label(f2, text="      V2      ")
    x.grid(row=2, column=2)
    v2 = Entry(f2)
    v2.grid(row=2, column=3)
    y = Label(f2, text="")
    y.grid(row=3, column=1, rowspan=2)
    # ======================================
    x = Label(f2, text="      Rf      ")
    x.grid(row=14, column=0)
    rf = Entry(f2)
    rf.grid(row=14, column=1, )
    x = Label(f2, text=" ")
    x.grid(row=15, column=0)
    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade", command=result_ia)
    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=sub.destroy)
    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    sub.mainloop()
# ======== Inverting Subtractor done =========
# =============================================
def differ():
    sub = Toplevel()
    sub.title(" Inverting Differentiator")
    sub.geometry("1100x1000+0+0")

    # ========================result system start===========================
    def result_ia():

        Rf = int(rf.get())
        C = int(c.get())
        Vin = str(vin.get())


        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      Ic      ")
        x.grid(row=20, column=0)
        ic = Entry(f2)
        ic.grid(row=20, column=1)
        # ------------------------------------------for voltage
        x = Label(f2, text="      Irf     ")
        x.grid(row=20, column=2)
        irf = Entry(f2)
        irf.grid(row=20, column=3)
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        x1 = Label(f2, text="      Vout     ")
        x1.grid(row=25, column=0)
        vout = Entry(f2)
        vout.grid(row=25, column=1)
        y = Label(f2, text="      Vc      ")
        y.grid(row=25, column=2)
        vc = Entry(f2)
        vc.grid(row=25, column=3)
        y = Label(f2, text="")
        y.grid(row=26, column=1)
        # ======================================
        x = Label(f2, text="      Vrf      ")
        x.grid(row=27, column=0)
        vrf = Entry(f2)
        vrf.grid(row=27, column=1 )
        # ================calculation part======================
        if Rf != 0 and C != 0:
            x = Symbol('x')
            re = Rf*C*diff(Vin,x)
            vout.insert(0, str(re) + " V")
            ic.insert(0, str(C*diff(Vin,x)) + " A")
            irf.insert(0, str(-re/Rf) + " A")


        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")
        vrf.insert(0, "-"+str(vout.get())+" V ")
        vc.insert(0, str(Vin) + " V ")
        # =================Result system end====================

    f1 = Frame(sub, width=500, height=800, bg="#216ade")
    f2 = Frame(sub, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      Rf      ")
    x.grid(row=0, column=0)
    rf = Entry(f2)
    rf.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      C      ")
    x.grid(row=0, column=2)
    c = Entry(f2)
    c.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      Vin      ")
    x.grid(row=2, column=0)
    vin = Entry(f2)
    vin.grid(row=2, column=1)
    y = Label(f2, text="            ")
    y.grid(row=3, column=0)


    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade", command=result_ia)
    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=sub.destroy)
    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    sub.mainloop()

# =====================================================
# Inverting Integrator
def inte():
    sub = Toplevel()
    sub.title("Integrator")
    sub.geometry("1100x1000+0+0")

    # ========================result system start===========================
    def result_ia():
        C = float(c.get())
        R1 = float(r1.get())
        W = float(w.get())

        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      I1      ")
        x.grid(row=20, column=0)
        i1 = Entry(f2)
        i1.grid(row=20, column=1)
        # ------------------------------------------for voltage
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        x1 = Label(f2, text="      Irf     ")
        x1.grid(row=25, column=0)
        irf = Entry(f2)
        irf.grid(row=25, column=1)
        y = Label(f2, text="")
        y.grid(row=26, column=1, rowspan=2)
        # ======================================
        y = Label(f2, text="      Vout      ")
        y.grid(row=28, column=0)
        vout = Entry(f2)
        vout.grid(row=28, column=1)
        y = Label(f2, text="")
        y.grid(row=32, column=1)
        # ======================================
        x = Label(f2, text="      Vrf      ")
        x.grid(row=28, column=2)
        vrf = Entry(f2)
        vrf.grid(row=28, column=3, )
        # ================calculation part======================

        vout.delete(0, END)
        z = v1.get()
        ex = W * C / R1
        x = Symbol('x')
        print(z, str(z))
        Z = integrate(z, x)
        k = '-j' + str(ex)

        vout.insert(0, Z)
        vout.insert(-1, k)
        m = str(vout.get())
        vrf.insert(0, m[1:])

        l = 1 / R1
        i1.insert(0, l)
        i1.insert(10, z)
        # =================Result system end====================

    f1 = Frame(sub, width=500, height=800, bg="#216ade")
    f2 = Frame(sub, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      R1      ")
    x.grid(row=0, column=0)
    r1 = Entry(f2)
    r1.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      V1      ")
    x.grid(row=0, column=2)
    v1 = Entry(f2)
    v1.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      Frequency in rad/s     ")
    x.grid(row=2, column=0)
    w = Entry(f2)
    w.grid(row=2, column=1)
    y = Label(f2, text="")
    y.grid(row=3, column=1, rowspan=2)
    # ======================================
    x = Label(f2, text="    Capacitor in F      ")
    x.grid(row=14, column=0)
    c = Entry(f2)
    c.grid(row=14, column=1, )
    x = Label(f2, text=" ")
    x.grid(row=15, column=0)
    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade", command=result_ia)
    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=sub.destroy)
    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    sub.mainloop()


# ===========================================
def logar():
    sub = Toplevel()
    sub.title("Logarithomic")
    sub.config(bg = '#82ba91')
    sub.geometry("1140x750+0+0")



    # ========================result system start===========================
    def result_ia():

        R = int(r.get())
        Vin = int(vin.get())

        x1 = Label(f2, text="      ")
        x1.grid(row=20, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=20, column=1, rowspan=2)
        # ------------------------------------------for resistance
        x = Label(f2, text="      Ir      ")
        x.config(font=('Arial', 14))
        x.grid(row=20, column=0)
        ir = Entry(f2)
        ir.grid(row=20, column=1)
        # ------------------------------------------for voltage
        x = Label(f2, text="      Id     ")
        x.config(font=('Arial', 14))
        x.grid(row=20, column=2)
        id = Entry(f2)
        id.grid(row=20, column=3)
        # -------------------------------------------
        x1 = Label(f2, text="")
        x1.grid(row=21, column=0)
        x2 = Label(f2, text="")
        x2.grid(row=21, column=1, rowspan=2)
        # -----------------------------------------for one row gap
        x1 = Label(f2, text="      Vout     ")
        x1.config(font=('Arial', 14))
        x1.grid(row=25, column=0)
        vout = Entry(f2)
        vout.grid(row=25, column=1)
        y = Label(f2, text="      Vd      ")
        y.config(font=('Arial', 14))
        y.grid(row=25, column=2)
        vd = Entry(f2)
        vd.grid(row=25, column=3)
        y = Label(f2, text="")
        y.grid(row=26, column=1)
        # ======================================
        x = Label(f2, text="      Vr      ")
        x.config(font=('Arial', 14))
        x.grid(row=27, column=0)
        vr = Entry(f2)
        vr.grid(row=27, column=1)
        # ================calculation part======================
        if R != 0:
            x = -1*(25*10^(-3))*np.log(Vin/(R*5))
            vout.insert(0, str(x) + " V")
            ir.insert(0, str(Vin/R) + " A")
            id.insert(0, str(Vin / R ) + " A")
            vd.insert(0, "-" + str(x) + " V ")
            vr.insert(0, "-" + str(Vin / R) + " V ")


        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")
        #vrf.insert(0, "-" + str(vout.get()) + " V ")
        #vc.insert(0, str(Vin) + " V ")
        # =================Result system end====================

    f1 = Frame(sub, width=500, height=800, bg="#216ade")
    f2 = Frame(sub, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("log.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      R     ")
    x.config(font=('Arial',14))
    x.grid(row=0, column=0)
    r = Entry(f2)
    r.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      Vin      ")
    x.config(font=('Arial', 14))
    x.grid(row=0, column=2)
    vin = Entry(f2)
    vin.grid(row=0, column=3)
    y = Label(f2,text = " ")
    y.grid(row=1, column=0)
    # -------------------------------------------


    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade",width = 1,height = 1, command=result_ia)
    final.config(font=('Arial',12))

    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20",width = 1,height = 1, command=sub.destroy)
    back.config(font=('Arial', 12))


    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    sub.mainloop()

# ============================================================================================================================
# Exponential
def expo():
    sub = Toplevel()
    sub.title("Exponantial")
    sub.geometry("1100x1000+0+0")

    # ========================result system start===========================
    def result_ia():
        IS = float(Is.get())
        R1 = float(rf.get())
        N = float(n.get())
        V1=float(v1.get())

        # ======================================
        y = Label(f2, text="      Vout      ")
        y.grid(row=28, column=0)
        vout = Entry(f2)
        vout.grid(row=28, column=1)
        y = Label(f2, text="")
        y.grid(row=32, column=1)
        # ======================================
        x = Label(f2, text="      Vrf      ")
        x.grid(row=28, column=2)
        vrf = Entry(f2)
        vrf.grid(row=28, column=3, )
        # ================calculation part======================

        rr=R1*IS
        rrr=(V1)/(N*.0258)
        x = Symbol('x', real=True)
        z=simplify(log(exp(rrr)))

        vout.delete(0, END)
        vout.insert(0, rr*z)
        m = str(vout.get())
        vrf.insert(0, m)


        # =================Result system end====================

    f1 = Frame(sub, width=500, height=800, bg="#216ade")
    f2 = Frame(sub, width=500, height=800)

    img = ImageTk.PhotoImage(Image.open("op.jpg"))
    panel = Label(f1, image=img)
    # ------------------------------------------for resistance
    x = Label(f2, text="      Rf      ")
    x.grid(row=0, column=0)
    rf = Entry(f2)
    rf.grid(row=0, column=1)
    # ------------------------------------------for voltage
    x = Label(f2, text="      V1      ")
    x.grid(row=0, column=2)
    v1 = Entry(f2)
    v1.grid(row=0, column=3)
    # -------------------------------------------
    x1 = Label(f2, text="")
    x1.grid(row=1, column=0)
    x2 = Label(f2, text="")
    x2.grid(row=1, column=1, rowspan=2)
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(f2, text="      Saturation Current(Is)     ")
    x.grid(row=2, column=0)
    Is = Entry(f2)
    Is.grid(row=2, column=1)
    y = Label(f2, text="")
    y.grid(row=3, column=1, rowspan=2)
    # ======================================
    x = Label(f2, text="    Value of n      ")
    x.grid(row=14, column=0)
    n = Entry(f2)
    n.grid(row=14, column=1, )
    x = Label(f2, text=" ")
    x.grid(row=15, column=0)
    # =====================================
    final = Button(f2, text="RUN", padx=80, pady=20, bg="#216ade", command=result_ia)
    final.grid(row=17, column=1)

    back = Button(f2, text="BACK", padx=60, pady=20, bg="#ba2a20", command=sub.destroy)
    back.grid(row=17, column=3)

    y = Label(f2, text="", height=2)
    y.grid(row=18, column=0)

    panel.pack()
    f1.pack(side="left")
    f2.pack(side="left")
    sub.mainloop()


# ==================================================
# main page
# ===========================================================================================================================
top = Label(root, text="SOLVE OP-AMP PROBLEM", width=1100, height=5, bg="#06d13c")
top.configure(font=("Courier", 30))
top.pack(side="top")


one = Button(root, text="1.Inverting Adder", width=50, height=1, bg = '#54705c', command=in_adder)
one.configure(font=("Courier", 15))
one.place(x=40, y=40)
one.pack()

two = Button(root, text="2.Non-Inverting Adder", width=50, height=1,bg = '#54705c',command = non_adder)
two.configure(font=("Courier", 15))
two.place(x=40, y=40)
two.pack()

three = Button(root, text="3.Inverting Subtactor", width=50, height=1,bg = '#54705c',command = in_sub)
three.configure(font=("Courier", 15))
three.place(x=40, y=40)
three.pack()

four = Button(root, text="4.Multiplier", width=50, height=1,bg = '#54705c')
four.configure(font=("Courier", 15))
four.place(x=40, y=40)
four.pack()

five = Button(root, text="5.Differentiator", width=50, height=1,bg = '#54705c',command = differ)
five.configure(font=("Courier", 15))
five.place(x=40, y=40)
five.pack()

six = Button(root, text="6.Intigrator", width=50, height=1,bg = '#54705c',command = inte)
six.configure(font=("Courier", 15))
six.place(x=40, y=40)
six.pack()

seven = Button(root, text="7.Logarithimic", width=50, height=1, bg = '#54705c',command = logar)
seven.configure(font=("Courier", 15))
seven.place(x=40, y=40)
seven.pack()

eight = Button(root, text="7.Exponential", width=50, height=1, bg = '#54705c',command = expo)
eight.configure(font=("Courier", 15))
eight.place(x=40, y=40)
eight.pack()

root.mainloop()
