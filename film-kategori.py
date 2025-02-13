from tkinter import *
class Film:
    def __init__(self):
        window = Tk()
        window.title("OSCAR ÖDÜLÜ KAZANANLAR")
        Label(window , text = "Film Türü").grid(row = 0 , column = 0)
        Label(window , text = "Film Listesi").grid(row = 0 , column = 1)
        dosyam = open("film.txt","r")
        self.filmtürü = {satır.split(",")[1].rstrip() for satır in dosyam}
        self.L = list(self.filmtürü)
        self.L.sort()

        self.türseçim = StringVar()
        self.türlistesi = Listbox(window , height=len(self.L) , width = 15 , listvariable = self.türseçim)
        self.türlistesi.grid(row = 1 , column=0 , padx = 10 , sticky=N)
        self.türlistesi.bind("<<ListboxSelect>>" , self.filmgetir)
        self.türseçim.set(self.L)

        self.gelenfilmler = StringVar()
        self.filmlistesi = Listbox(window , height = len(self.L) , width=15 , listvariable=self.gelenfilmler)
        self.filmlistesi.grid(row = 1 , column = 1 , sticky=NSEW)
        window.mainloop()
    def filmgetir(self , e):
        degerim = self.türlistesi.get(self.türlistesi.curselection())
        filmler = [satır.split(",")[0] for satır in open("film.txt" , "r") if satır.split(",")[1].rstrip() == degerim]
        self.gelenfilmler.set(tuple(filmler))
film = Film()

