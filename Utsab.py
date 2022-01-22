from tkinter import *
import sys
from PIL import ImageTk, Image
from tkinter import messagebox
from sympy import *
import numpy as np

root = Tk()
root.title("MAIN-PAGE")
root.geometry("1140x750+0+0")

# =================================
def non_adder():
    adder = Toplevel()
    adder.title("Non-inverting Adder")
    adder.geometry("1140x750+0+0")

    top = Label(adder, text='Enter the value of Input Voltages and Resistances')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=300, y=30)

    # ========================result system start===========================

    def result_na():
        R1 = float(r1.get())
        R2 = float(r2.get())
        R3 = float(r3.get())
        R4 = float(r4.get())
        R5 = float(r5.get())
        Ra = float(ra.get())
        Rb = float(rb.get())

        V1 = float(v1.get())
        V2 = float(v2.get())
        V3 = float(v3.get())
        V4 = float(v4.get())
        V5 = float(v5.get())


        x = Label(adder, text="I1 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=500)
        i1 = Entry(adder)
        i1.config(font=('Times', 14))
        i1.pack()
        i1.place(x=700, y=500)
        # ------------------------------------------for voltage
        x = Label(adder, text="I2 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=500)
        i2 = Entry(adder)
        i2.config(font=('Times', 14))
        i2.pack()
        i2.place(x=900, y=500)

        # ====================================
        x = Label(adder, text="I3 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=550)
        i3 = Entry(adder)
        i3.config(font=('Times', 14))
        i3.pack()
        i3.place(x=700, y=550)
        x = Label(adder, text="I4 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=550)
        i4 = Entry(adder)
        i4.config(font=('Times', 14))
        i4.pack()
        i4.place(x=900, y=550)

        # ===================================
        x = Label(adder, text="I5 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=600)
        i5 = Entry(adder)
        i5.config(font=('Times', 14))
        i5.pack()
        i5.place(x=700, y=600)
        x = Label(adder, text="Ia = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=600)
        ia = Entry(adder)
        ia.config(font=('Times', 14))
        ia.pack()
        ia.place(x=900, y=600)

        # ======================================
        x = Label(adder, text="Ib = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=650)
        ib = Entry(adder)
        ib.config(font=('Times', 14))
        ib.pack()
        ib.place(x=700, y=650)

        # ======================================
        x = Label(adder, text="Vout      ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=650)
        vout = Entry(adder)
        vout.config(font=('Times', 14))
        vout.pack()
        vout.place(x=900, y=650)
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


    img = ImageTk.PhotoImage(Image.open("non_inv.jpg"))
    panel = Label(adder, image=img)
    panel.pack()
    panel.place(x= 350,y = 100)

    # ------------------------------------------for resistance
    x = Label(adder, text="R1 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=60, y=500)
    r1 = Entry(adder)
    r1.config(font=('Arial', 14))
    r1.pack()
    r1.place(x=110, y=500)
    # ------------------------------------------for voltage
    x = Label(adder, text="V1 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=500)
    v1 = Entry(adder)
    v1.config(font=('Arial', 14))
    v1.pack()
    v1.place(x=400, y=500)

    # ====================================
    x = Label(adder, text="R2 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x= 60, y=540)
    r2 = Entry(adder)
    r2.config(font=('Arial', 14))
    r2.pack()
    r2.place(x=110, y=540)
    x = Label(adder, text="V2 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=540)
    v2 = Entry(adder)
    v2.config(font=('Arial', 14))
    v2.pack()
    v2.place(x=400, y=540)

    # ===================================
    x = Label(adder, text="R3 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=60, y=580)
    v = StringVar(root, value='0')
    r3 = Entry(adder, textvariable=v)
    r3.config(font=('Arial', 14))
    r3.pack()
    r3.place(x=110, y=580)
    x = Label(adder, text="V3  = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=580)
    vv = StringVar(root, value='0')
    v3 = Entry(adder, textvariable=vv)
    v3.config(font=('Arial', 14))
    v3.pack()
    v3.place(x=400, y=580)

    # ======================================
    x = Label(adder, text="R4 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=60, y=620)
    vvv = StringVar(root, value='0')
    r4 = Entry(adder, textvariable=vvv)
    r4.config(font=('Arial', 14))
    r4.pack()
    r4.place(x=110, y=620)
    x = Label(adder, text="V4 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=620)
    vvvv = StringVar(root, value='0')
    v4 = Entry(adder, textvariable=vvvv)
    v4.config(font=('Arial', 14))
    v4.pack()
    v4.place(x=400, y=620)

    # ======================================
    x = Label(adder, text="R5 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=60, y=660)
    vvvvv = StringVar(root, value='0')
    r5 = Entry(adder, textvariable=vvvvv)
    r5.config(font=('Arial', 14))
    r5.pack()
    r5.place(x=110, y=660)
    x = Label(adder, text="V5 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=660)
    vvvvvv = StringVar(root, value='0')
    v5 = Entry(adder, textvariable=vvvvvv)
    v5.config(font=('Arial', 14))
    v5.pack()
    v5.place(x=400, y=660)
    # ======================================
    x = Label(adder, text="Ra = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=60, y=700)
    ra = Entry(adder)
    ra.config(font=('Arial', 14))
    ra.pack()
    ra.place(x=110, y=700)
    x = Label(adder, text="Rb = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=700)
    rb = Entry(adder)
    rb.config(font=('Arial', 14))
    rb.pack()
    rb.place(x=400, y=700)
    #========================================







    final = Button(adder, text="RUN", bg="green", command=result_na)
    final.config(font=('Times', 14))
    final.pack()
    final.place(x=350, y=420)

    back = Button(adder, text="BACK", bg="#ba2a20", command=adder.destroy)
    back.config(font=('Times', 14))
    back.pack()
    back.place(x=670, y=420)

    adder.mainloop()


    #============================Non Invering Adder End=================================================================

# =================================
def in_sub():
    sub = Toplevel()
    sub.title("Inverting Subtractor")
    sub.geometry("1140x750+0+0")

    top = Label(sub, text='Enter the value of Input Voltage and Resistance')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=330, y=30)


    # ========================result system start===========================
    def result_ia():
        Rf = float(rf.get())
        R1 = float(r1.get())
        R2 = float(r2.get())
        V1 = float(v1.get())
        V2 = float(v2.get())


        x = Label(sub, text="I1 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=500)
        i1 = Entry(sub)
        i1.config(font=('Times', 14))
        i1.pack()
        i1.place(x=700, y=500)
        # ------------------------------------------for voltage
        x = Label(sub, text="I2 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=900, y=500)
        i2 = Entry(sub)
        i2.config(font=('Times', 14))
        i2.pack()
        i2.place(x=940, y=500)

        # -----------------------------------------for one row gap
        x = Label(sub, text="Irf = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=550)
        irf = Entry(sub)
        irf.config(font=('Times', 14))
        irf.pack()
        irf.place(x=700, y=550)

        # ======================================
        x = Label(sub, text="Vout = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=640, y=600)
        vout = Entry(sub)
        vout.config(font=('Times', 14))
        vout.pack()
        vout.place(x=700, y=600)

        # ======================================
        x = Label(sub, text="Vrf = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=650)
        vrf = Entry(sub)
        vrf.config(font=('Times', 14))
        vrf.pack()
        vrf.place(x=700, y=650)
        # ================calculation part======================
        if R1 != 0 and R2 != 0:
            re = Rf / R1 * V1 - Rf / R2 * V2
            vout.insert(0, str(re) + " V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")
        vrf.insert(0, str(vout.get()))
        irf.insert(0, str((re) / Rf) + " A")
        # =================Result system end====================


    img = ImageTk.PhotoImage(Image.open("sub.jpg"))
    panel = Label(sub, image=img)
    panel.pack()
    panel.place(x= 350,y = 100)


    # ------------------------------------------for resistance
    x = Label(sub, text="R1 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=100, y=500)
    r1 = Entry(sub)
    r1.config(font=('Arial', 14))
    r1.pack()
    r1.place(x=150, y=500)
    # ------------------------------------------for voltage
    x = Label(sub, text="V1 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=500)
    v1 = Entry(sub)
    v1.config(font=('Arial', 14))
    v1.pack()
    v1.place(x=400, y=500)

    # ====================================
    x = Label(sub, text="R2 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=100, y=550)
    r2 = Entry(sub)
    r2.config(font=('Arial', 14))
    r2.pack()
    r2.place(x=150, y=550)
    x = Label(sub, text="V2 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=350, y=550)
    v2 = Entry(sub)
    v2.config(font=('Arial', 14))
    v2.pack()
    v2.place(x=400, y=550)

    # ======================================
    x = Label(sub, text="Rf = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=100, y=600)
    rf = Entry(sub)
    rf.config(font=('Arial', 14))
    rf.pack()
    rf.place(x=150, y=600)

    # =====================================

    final = Button(sub, text="RUN", bg="green", command=result_ia)
    final.config(font=('Times', 14))
    final.pack()
    final.place(x=350, y=420)

    back = Button(sub, text="BACK", bg="#ba2a20", command=sub.destroy)
    back.config(font=('Times', 14))
    back.pack()
    back.place(x=707, y=420)

    sub.mainloop()

# =================================
def in_adder():
    adder = Toplevel()
    adder.title("Inverting Adder")
    adder.geometry("1140x750+0+0")

    top = Label(adder, text='Enter the value of Input Voltage and Resistance')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=330, y=30)

    # ========================result system start===========================
    def result_ia():
        Rf = float(rf.get())
        R1 = float(r1.get())
        R2 = float(r2.get())
        R3 = float(r3.get())
        R4 = float(r4.get())
        R5 = float(r5.get())

        V1 = float(v1.get())
        V2 = float(v2.get())
        V3 = float(v3.get())
        V4 = float(v4.get())
        V5 = float(v5.get())

        # ------------------------------------------for resistance
        x = Label(adder, text="I1 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=500)

        i1 = Entry(adder)
        i1.config(font=('Times', 14))
        i1.pack()
        i1.place(x=700, y=500)
        # ------------------------------------------for voltage
        x = Label(adder, text="I2 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=500)
        i2 = Entry(adder)
        i2.config(font=('Times', 14))
        i2.pack()
        i2.place(x=900, y=500)

        # -----------------------------------------for one row gap
        # ====================================
        x = Label(adder, text="I3 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=550)
        i3 = Entry(adder)
        i3.config(font=('Times', 14))
        i3.pack()
        i3.place(x=700, y=550)
        x = Label(adder, text="I4 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=550)
        i4 = Entry(adder)
        i4.config(font=('Times', 14))
        i4.pack()
        i4.place(x=900, y=550)

        # ===================================
        x = Label(adder, text="I5 = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=600)
        i5 = Entry(adder)
        i5.config(font=('Times', 14))
        i5.pack()
        i5.place(x=700, y=600)
        x = Label(adder, text="Irf = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=850, y=600)
        irf = Entry(adder)
        irf.config(font=('Times', 14))
        irf.pack()
        irf.place(x=900, y=600)

        # ======================================
        x = Label(adder, text="Vout = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=640, y=650)
        vout = Entry(adder)
        vout.config(font=('Times', 14))
        vout.pack()
        vout.place(x=700, y=650)

        # ======================================
        x = Label(adder, text="Vrf = ")
        x.config(font=('Times', 14))
        x.pack()
        x.place(x=650, y=700)
        vrf = Entry(adder)
        vrf.config(font=('Times', 14))
        vrf.pack()
        vrf.place(x=700, y=700)
        # ================calculation part======================
        if R3 == 0 and R4 == 0 and R5 == 0:
            x1 = (Rf / R1) * V1 + (Rf / R2) * V2
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2) + " V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            irf.insert(0, str(-(x1/ Rf)) + " A")
        elif R4 == 0 and R5 == 0:
            x2 = (Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3) + " V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            irf.insert(0,  str(-(x2 / Rf)) + " A")
        elif R5 == 0:
            x3 = (Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4
            vout.insert(0, str((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4) + " V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            i4.insert(0, str(V4 / R4) + " A")
            irf.insert(0, str(-(x3 / Rf)) + " A")
        elif R1 != 0 and R2 != 0 and R3 != 0 and R4 != 0 and R5 != 0:
            x4 = -((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4 + (Rf / R5) * V5)
            vout.insert(0, str(
                -((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4 + (Rf / R5) * V5)) + " V")
            i1.insert(0, str(V1 / R1) + " A")
            i2.insert(0, str(V2 / R2) + " A")
            i3.insert(0, str(V3 / R3) + " A")
            i4.insert(0, str(V4 / R4) + " A")
            i5.insert(0, str(V5 / R5) + ' A')
            irf.insert(0, str(-(x4 / Rf)) + " A")
        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")

        vrf.insert(0, str(vout.get()))
        # irf.insert(0, str(
        #     (-((Rf / R1) * V1 + (Rf / R2) * V2 + (Rf / R3) * V3 + (Rf / R4) * V4 + (Rf / R5) * V5)) / Rf) + " A")
        # =================Result system end====================

    img = ImageTk.PhotoImage(Image.open("inv.jpg"))
    panel = Label(adder, image=img)
    panel.pack()
    panel.place(x=350, y=100)

    # ------------------------------------------for resistance
    x = Label(adder, text="R1 = ")
    x.pack()
    x.place(x=100, y=480)
    x.config(font=('Times', 14))

    r1 = Entry(adder)
    r1.config(font=('Times', 14))
    r1.pack()
    r1.place(x=150, y= 480)

    # ------------------------------------------for voltage
    x = Label(adder, text="V1 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=350, y=480)

    v1 = Entry(adder)
    v1.config(font=('Times', 14))
    v1.pack()
    v1.place(x=400, y= 480)

    # ====================================
    x = Label(adder, text="R2 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=100, y=520)

    r2 = Entry(adder)
    r2.config(font=('Times', 14))
    r2.pack()
    r2.place(x=150, y=520)

    x = Label(adder, text="V2 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=350, y=520)

    v2 = Entry(adder)
    v2.config(font=('Times', 14))
    v2.pack()
    v2.place(x=400, y=520)

    # ===================================
    x = Label(adder, text="R3 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=100, y=560)

    v = StringVar(root, value='0')
    r3 = Entry(adder, textvariable=v)
    r3.config(font=('Times', 14))
    r3.pack()
    r3.place(x=150, y=560)

    x = Label(adder, text="V3 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=350, y=560)

    vv = StringVar(root, value='0')
    v3 = Entry(adder, textvariable=vv)
    v3.config(font=('Times', 14))
    v3.pack()
    v3.place(x=400, y=560)

    # ======================================
    x = Label(adder, text="R4 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=100, y=600)

    vvv = StringVar(root, value='0')
    r4 = Entry(adder, textvariable=vvv)
    r4.config(font=('Times', 14))
    r4.pack()
    r4.place(x=150, y=600)

    x = Label(adder, text="V4 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=350, y=600)

    vvvv = StringVar(root, value='0')
    v4 = Entry(adder, textvariable=vvvv)
    v4.config(font=('Times', 14))
    v4.pack()
    v4.place(x=400, y=600)

    # ======================================
    x = Label(adder, text="R5 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=100, y=640)

    vvvvv = StringVar(root, value='0')
    r5 = Entry(adder, textvariable=vvvvv)
    r5.config(font=('Times', 14))
    r5.pack()
    r5.place(x=150, y=640)

    x = Label(adder, text="R5 = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=350, y=640)

    vvvvvv = StringVar(root, value='0')
    v5 = Entry(adder, textvariable=vvvvvv)
    v5.config(font=('Times', 14))
    v5.pack()
    v5.place(x=400, y=640)

    # ======================================
    x = Label(adder, text="Rf = ")
    x.config(font=('Times', 14))
    x.pack()
    x.place(x=100, y=680)

    rf = Entry(adder)
    rf.config(font=('Times', 14))
    rf.pack()
    rf.place(x=150, y=680)

    # =====================================
    final = Button(adder, text="RUN", bg="green", command=result_ia)
    final.config(font=('Times', 14))
    final.pack()
    final.place(x=350, y=420)

    back = Button(adder, text="BACK", bg="#ba2a20", command=adder.destroy)
    back.config(font=('Times', 14))
    back.pack()
    back.place(x=700, y=420)

    adder.mainloop()
    # ============================Inverting Adder End====================================================================


# ==================================
def differ():
    sub = Toplevel()
    sub.title(" Inverting Differentiator")
    sub.geometry("1140x750+0+0")


    top = Label(sub, text='Enter the value of Input Voltage(function of x) and Resistance')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=200, y=30)


    # ========================result system start===========================
    def result_ia():

        Rf = int(rf.get())
        C = int(c.get())
        Vin = str(vin.get())

        # ------------------------------------------for resistance
        x = Label(sub, text="Ic = ")
        x.config(font=('Arial',14))
        x.pack()
        x.place(x = 620,y= 500)

        ic = Entry(sub)
        ic.config(font=('Arial',14))
        ic.pack()
        ic.place(x = 665,y = 500)

        # ------------------------------------------for voltage
        x = Label(sub, text="Irf = ")
        x.config(font=('Arial',14))
        x.pack()
        x.place(x = 620,y = 530)

        irf = Entry(sub)
        irf.config(font=('Arial',14))
        irf.pack()
        irf.place(x= 665,y = 530)

        # -----------------------------------------for one row gap
        x1 = Label(sub, text="Vout = ")
        x1.config(font=('Arial',14))
        x1.pack()
        x1.place(x = 600,y = 560)

        vout = Entry(sub)
        vout.config(font=('Arial',14))
        vout.pack()
        vout.place(x = 665, y = 560)

        y = Label(sub, text="Vc = ")
        y.config(font=('Arial',14))
        y.pack()
        y.place(x = 610,y = 590)

        vc = Entry(sub)
        vc.config(font=('Arial',14))
        vc.pack()
        vc.place(x= 665,y = 590)
        # ======================================
        x = Label(sub, text="Vrf = ")
        x.config(font=('Arial',14))
        x.pack()
        x.place(x = 610,y = 620 )

        vrf = Entry(sub)
        vrf.config(font=('Arial',14))
        vrf.pack()
        vrf.place(x = 665, y = 620)
        # ================calculation part======================
        if Rf != 0 and C != 0:
            x = Symbol('x')
            re = Rf*C*diff(Vin,x)
            vout.insert(0, str(re) + " V")
            ic.insert(0, str(C*diff(Vin,x)) + " A")
            irf.insert(0, str(-re/Rf) + " A")


        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")
        re = Rf * C * diff(Vin, x)
        vrf.insert(0, str(-re))
        vc.insert(0, str(Vin) + " V ")
        # =================Result system end====================

    img = ImageTk.PhotoImage(Image.open("dif.jpg"))
    panel = Label(sub, image=img)
    panel.pack()
    panel.place(x = 310, y =90)
    # ------------------------------------------for resistance
    x = Label(sub, text="Rf = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 160,y=500)

    rf = Entry(sub)
    rf.config(font=('Arial',14))
    rf.pack()
    rf.place(x = 210,y = 500)
    # ------------------------------------------for voltage
    x = Label(sub, text="Capacitance(F) = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 50,y = 530)

    c = Entry(sub)
    c.config(font=('Arial',14))
    c.pack()
    c.place(x = 210, y = 530)
    # ====================================
    x = Label(sub, text="Vin = ")
    x.config(font = ('Arial',14))
    x.pack()
    x.place(x = 150,y = 560)

    vin = Entry(sub)
    vin.config(font=('Arial',14))
    vin.pack()
    vin.place(x = 210, y = 560)


    # =====================================
    final = Button(sub, text="RUN", bg="green",command = result_ia)
    final.config(font=('Arial', 14))
    final.pack()
    final.place(x=310, y=410)

    back = Button(sub, text="BACK", bg="#ba2a20", command=sub.destroy)
    back.config(font=('Arial', 14))
    back.pack()
    back.place(x=630, y=410)


    sub.mainloop()
# ==================================
def inte():
    sub = Toplevel()
    sub.title("Integrator")
    sub.geometry("1140x750+0+0")


    top = Label(sub, text='Enter the value of Input Voltage(function of x) and Resistance')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=250, y=30)

    # ========================result system start===========================
    def result_ia():
        C = float(c.get())
        R1 = float(r1.get())
        W = float(w.get())


        # ------------------------------------------for resistance
        x = Label(sub, text="Ic = ")
        x.config(font=('Arial',14))
        x.pack()
        x.place(x = 620, y = 500)

        i1 = Entry(sub)
        i1.config(font=('Arial',14))
        i1.pack()
        i1.place(x = 665,y = 500)
        # ------------------------------------------for voltage
        x1 = Label(sub, text="Irf = ")
        x1.config(font=('Arial',14))
        x1.pack()
        x1.place(x = 620, y = 530)

        irf = Entry(sub)
        irf.config(font=('Arial',14))
        irf.pack()
        irf.place(x = 665,y = 530)
        # ======================================
        y = Label(sub, text="Vout = ")
        y.config(font=('Arial',14))
        y.pack()
        y.place(x = 600 ,y = 560 )

        vout = Entry(sub)
        vout.config(font=('Arial',14))
        vout.pack()
        vout.place(x = 665,y = 560)
        # ======================================
        x = Label(sub, text="Vrf = ")
        x.config(font=('Arial',14))
        x.pack()
        x.place(x=615,y=590)

        vrf = Entry(sub)
        vrf.config(font=('Arial',14))
        vrf.pack()
        vrf.place(x = 665, y = 590)
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
        irf.insert(0, l)
        irf.insert(10, z)
        # =================Result system end====================

    img = ImageTk.PhotoImage(Image.open("inte.jpg"))
    panel = Label(sub, image=img)
    panel.pack()
    panel.place(x = 310,y = 90)

    # ------------------------------------------for resistance
    x = Label(sub, text="R1 = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 160,y = 500)


    r1 = Entry(sub)
    r1.config(font=('Arial',14))
    r1.pack()
    r1.place(x = 210 , y =500)

    # ------------------------------------------for voltage
    x = Label(sub, text="V1 = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 160 ,y = 530)

    v1 = Entry(sub)
    v1.config(font=('Arial',14))
    v1.pack()
    v1.place(x = 210,y = 530 )

    # ====================================
    x = Label(sub, text="Frequency in rad/s = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 27,y = 560)

    w = Entry(sub)
    w.config(font=('Arial',14))
    w.pack()
    w.place(x = 210,y = 560)

    # ======================================
    x = Label(sub, text="Capacitance(F) = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 55,y = 590)

    c = Entry(sub)
    c.config(font=('Arial', 14))
    c.pack()
    c.place(x = 210,y = 590)

    # =====================================
    final = Button(sub, text="RUN", bg="green",command = result_ia)
    final.config(font=('Arial',14))
    final.pack()
    final.place(x = 310,y = 410)

    back = Button(sub, text="BACK", bg="#ba2a20", command=sub.destroy)
    back.config(font=('Arial',14))
    back.pack()
    back.place(x=630, y=410)

    sub.mainloop()

# ========================================
def expo():
    sub = Toplevel()
    sub.title("Exponantial")
    sub.geometry("1140x750+0+0")

    top = Label(sub, text='Enter the value of Input Voltage and Resistance')
    top.config(font=('Times', 20))
    top.pack()
    top.place(x=330, y=30)

    # ======================== result system start ===========================
    def result_ia():
        IS = float(Is.get())
        R1 = float(rf.get())
        N = float(n.get())
        V1=float(v1.get())

        # ======================================
        y = Label(sub, text="Vout = ")
        y.config(font = ('Arial',14))
        y.pack()
        y.place(x = 650,y = 500)

        vout = Entry(sub)
        vout.config(font = ('Arial',14))
        vout.pack()
        vout.place(x = 730,y = 500)

        # ======================================
        x = Label(sub, text="Vrf = ")
        x.config(font = ('Arial',14))
        x.pack()
        x.place(x = 665, y = 530)

        vrf = Entry(sub)
        vrf.config(font =('Arial',14))
        vrf.pack()
        vrf.place(x = 730,y = 530)
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

    img = ImageTk.PhotoImage(Image.open("exp.jpg"))
    panel = Label(sub, image=img)
    panel.pack()
    panel.place(x= 350,y = 100)

    # ------------------------------------------for resistance
    x = Label(sub, text="R = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=180, y=500)

    rf = Entry(sub)
    rf.config(font =('Arial',14))
    rf.pack()
    rf.place(x = 220,y = 500)
    # ------------------------------------------for voltage

    x = Label(sub, text="V1 = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=170, y=530)

    v1 = Entry(sub)
    v1.config(font =('Arial',14))
    v1.pack()
    v1.place(x = 220,y = 530)
    # -------------------------------------------
    # -----------------------------------------for one row gap
    # ====================================
    x = Label(sub, text="Saturation Current(Is) = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x = 15,y=560)

    Is = Entry(sub)
    Is.config(font=('Arial', 14))
    Is.pack()
    Is.place(x = 220 , y = 560)

    # ======================================
    x = Label(sub, text="Value of n = ")
    x.config(font=('Arial',14))
    x.pack()
    x.place(x = 108, y = 590)

    n = Entry(sub)
    n.config(font=('Arial',15))
    n.pack()
    n.place(x = 220,y = 590)

    # =====================================
    final = Button(sub, text="RUN", bg="green",command = result_ia)
    final.config(font = ('Times',15))
    final.pack()
    final.place(x = 350,y = 420)

    back = Button(sub, text="BACK", bg="#ba2a20", command=sub.destroy)
    back.config(font=('Times', 15))
    back.pack()
    back.place(x = 700,y= 420)


    sub.mainloop()

# ===========================================
def logar():
    sub = Toplevel()
    sub.title("Logarithomic")
    
    sub.geometry("1140x750+0+0")

    top = Label(sub,text = 'Enter the value of Input Voltage and Resistance')
    top.config(font=('Times',20))
    top.pack()
    top.place(x = 330,y = 30)

    # ========================result system start===========================
    def result_ia():

        R = int(r.get())
        Vin = int(vin.get())
        N = int(n.get())

        # ------------------------------------------for resistance
        x = Label(sub, text="Ir = ")
        x.config(font=('Arial', 14))
        x.pack()
        x.place(x= 680,y= 500)

        ir = Entry(sub)
        ir.config(font=('Arial', 14))
        ir.pack()
        ir.place(x= 720, y=500)

        # ------------------------------------------for voltage
        x = Label(sub, text="Id = ")
        x.config(font=('Arial', 14))
        x.pack()
        x.place(x= 677 , y=540)

        id = Entry(sub)
        id.config(font=('Arial', 14))
        id.pack()
        id.place(x = 720, y = 540)

        # -----------------------------------------for one row gap
        x1 = Label(sub, text="Vout = ")
        x1.config(font=('Arial', 14))
        x1.pack()
        x1.place(x = 656 , y = 580)

        vout = Entry(sub)
        vout.config(font=('Arial', 14))
        vout.pack()
        vout.place(x = 720, y = 580)

        # ===================Vd========
        y = Label(sub, text="Vd = ")
        y.config(font=('Arial', 14))
        y.pack()
        y.place(x=670,y=620)

        vd = Entry(sub)
        vd.config(font=('Arial', 14))
        vd.pack()
        vd.place(x=720,y=620)


        # ======================================
        x = Label(sub, text="Vr = ")
        x.config(font=('Arial', 14))
        x.pack()
        x.place(x = 674,y = 660)

        vr = Entry(sub)
        vr.config(font=('Arial', 14))
        vr.pack()
        vr.place(x = 720,y= 660)
        # ================calculation part======================
        if R != 0:
            x = -1* N * (25 * 10 ^ (-3)) * np.log(Vin / (R * 5))
            vout.insert(0, str(x) + " V")
            ir.insert(0, str(Vin / R) + " A")
            id.insert(0, str(Vin / R) + " A")
            vd.insert(0,  str(-x) + " V ")
            vr.insert(0, str(-(Vin / R)) + " V ")


        else:
            messagebox.showwarning("Warning", "There may be some unfilled field between two entry")
        # vrf.insert(0, "-" + str(vout.get()) + " V ")
        # vc.insert(0, str(Vin) + " V ")
        # =================Result system end====================

    photo1 = ImageTk.PhotoImage(Image.open('log.jpg'))
    panel = Label(sub, image= photo1)
    panel.pack()
    panel.place(x = 380,y = 100)
    # ------------------------------------------for resistance

    x = Label(sub, text="R = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x = 80, y = 500 )

    r = Entry(sub)
    r.config(font=('Arial', 14))
    r.pack()
    r.place( x = 130, y = 500)
    # # ------------------------------------------for voltage
    x = Label(sub, text="Vin = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place( x = 70 , y = 550)

    vin = Entry(sub)
    vin.config(font=('Arial', 14))
    vin.pack()
    vin.place(x = 130 , y= 550)

    ## ======================================== n values

    x = Label(sub, text="n = ")
    x.config(font=('Arial', 14))
    x.pack()
    x.place(x=80, y=600)

    n = Entry(sub)
    n.config(font=('Arial', 14))
    n.pack()
    n.place(x=130, y=600)

    # # =====================================

    final = Button(sub, text="RUN", bg="green",command = result_ia)
    final.config(font=('Times', 14))
    final.pack()
    final.place(x = 350, y=420)


    back = Button(sub, text="BACK", bg="#ba2a20", command=sub.destroy)
    back.config(font=('Times', 14))
    back.pack()
    back.place(x=730, y=420)

    sub.mainloop()




# ==================================================
# main page
# ======================================================================================================
top = Label(root, text="SOLVE OP-AMP PROBLEM", width=1100, height=5, bg="green")
top.configure(font=("Times", 30))
top.pack(side="top")

one = Button(root, text="1.Inverting Adder", width=50, height=1, bg='#8a1129',command = in_adder)
one.configure(font=("Times", 20))
one.place(x=40, y=40)
one.pack()

two = Button(root, text="2.Non-Inverting Adder", width=50, height=1, bg='#7293c4',command = non_adder)
two.configure(font=("Times", 20))
two.place(x=40, y=40)
two.pack()

three = Button(root, text="3.Inverting Subtactor", width=50, height=1, bg='#b2b2d6',command = in_sub)
three.configure(font=("Times", 20))
three.place(x=40, y=40)
three.pack()

five = Button(root, text="4.Differentiator", width=50, height=1, bg='#54705c',command = differ)
five.configure(font=("Times", 20))
five.place(x=40, y=40)
five.pack()

six = Button(root, text="5.Integrator", width=50, height=1, bg='#076b6b',command = inte)
six.configure(font=("Times", 20))
six.place(x=40, y=40)
six.pack()

seven = Button(root, text="6.Logarithmic", width=50, height=1, bg='#135924', command=logar)
seven.configure(font=("Times", 20))
seven.place(x=40, y=40)
seven.pack()

eight = Button(root, text="7.Exponential", width=50, height=1, bg='#5c4727',command = expo)
eight.configure(font=("Times", 20))
eight.place(x=40, y=40)
eight.pack()

root.mainloop()
