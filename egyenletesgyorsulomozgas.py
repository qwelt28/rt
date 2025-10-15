from math import erf
import tkinter as tk

def szamol():
    try:
        v0 = float(v0_szam.get())
        a = float(a_szam.get())
        t = float(t_szam.get())
        v = v0 + a * t
        s = v0 * t + 0.5 * a * t**2
        eredmeny.config(text=f"v(t) = {v}\ns(t) = {s}")
    except Exception as e:
        eredmeny.config(text=f"Hiba történt: {e}")

ablak = tk.Tk()
ablak.title("Egyenletesen gyorsuló mozgás")
ablak.geometry("320x300")

tk.Label(ablak, text="Egyenletesen gyorsuló mozgás").pack(pady=10)
tk.Label(ablak, text="v(t) = v0 + a*t     s(t) = v0*t + 0.5*a*t²").pack(pady=5)

tk.Label(ablak, text="v0 (kezdeti sebesség):").pack()
v0_szam = tk.Entry(ablak)
v0_szam.pack()
v0_szam.insert(0, "0")

tk.Label(ablak, text="a (gyorsulás):").pack()
a_szam = tk.Entry(ablak)
a_szam.pack()
a_szam.insert(0, "0")

tk.Label(ablak, text="t (idő):").pack()
t_szam = tk.Entry(ablak)
t_szam.pack()
t_szam.insert(0, "0")

tk.Button(ablak, text="számol", command=szamol).pack(pady=15)

eredmeny = tk.Label(ablak, text="Az eredményhez nyomd meg a gombot.")
eredmeny.pack(pady=10)

ablak.mainloop()
#Készítette: Jani