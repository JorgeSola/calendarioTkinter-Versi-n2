from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import date
import calendar

dt = datetime.now()

HEIGHTBTN = 50
WIDTHBTN = 50

#FRAMEWORK PARA LOS BOTONES.

class CalButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '14', 'bold'))
        
        self.__btn = ttk.Button(self, text= text, command=command, style='my.TButton')
        self.__btn.pack(side=TOP, expand=True,fill=BOTH)

# FRAMEWORK PARA LAS ETIQUETAS.

class Day(ttk.Frame):           

    cadena = ' '

    def __init__(self, parent, wlabel= 1 ,hlabel=1):
        ttk.Frame.__init__(self, parent, width=WIDTHBTN*wlabel, height=HEIGHTBTN*hlabel)

        self.pack_propagate(0)         
        
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 8')

        self.lbl = ttk.Label(self, text = self.cadena, style='my.TLabel', background='white', foreground= 'black', anchor = CENTER, borderwidth=2, relief="ridge")
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

    def valor(self, texto = None, letra = None):
        self.cadena = texto
        self.lbl.config(text = self.cadena, foreground = letra)

# Clase donde creo todos los botones, etiquetas y métodos de funcionabilidad.
        
class Calendar(ttk.Frame):
    
    month = None
    year = None
    listaEtiquetas = []
    mesActual = []
    indiceMeses = 0
    indiceAños = 0
    listaMeses =['Enero',' Febrero', 'Marzo','Abril','Mayo','Junio','Julio', 'Agosto','Septiembre','Octubre', 'Noviembre','Diciembre']
    diasSemana = ['Lunes','Martes','Miercoles','Jueves', 'Viernes', 'Sabado', 'Domingo']  

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        # CREACIÓN DE LA PRIMERA LÍNEA DEL CALENDARIO. BOTONES +  ETIQUETA QUE INDICA EL MES & AÑO

        self.btn_inicio = CalButton(self, text = '«', command = lambda: self.backFull('«'), hbtn=0.5)
        self.btn_inicio.grid(column = 0, row = 0)
        
        self.btn_volver = CalButton(self, text = '<', command = lambda: self.back('<'), hbtn=0.5)
        self.btn_volver.grid(column=1 ,row=0)

        self.lbl_mes = Day(self,  wlabel= 3, hlabel= 0.5)
        self.lbl_mes.valor(str(str(self.listaMeses[dt.month-1]) + str(' ') + str(dt.year)))
        self.lbl_mes.grid(column = 2 , row = 0, columnspan = 3)

        self.btn_moveOn = CalButton(self, text = '>', command = lambda: self.moveOn('>'), hbtn=0.5)
        self.btn_moveOn.grid(column = 5, row = 0)

        self.btn_final = CalButton(self, text = '»', command = lambda: self.moveOnFull('»'), hbtn=0.5)
        self.btn_final.grid(column=6, row=0)
        
        # Creación de los nombres de cada día. Son etiquetas fijas que no varían su texto. Lunes/Martes/X/Jueves/Viernes ...etc
            
        self.lbl_lunes = Day(self, hlabel = 0.5)
        self.lbl_lunes.valor('Lunes')
        self.lbl_lunes.grid(column = 0 , row = 1)

        self.lbl_martes = Day(self, hlabel = 0.5)
        self.lbl_martes.valor('Martes')
        self.lbl_martes.grid(column = 1 , row = 1)

        self.lbl_miercoles = Day(self, hlabel = 0.5)
        self.lbl_miercoles.valor('Miércoles')
        self.lbl_miercoles.grid(column = 2 , row = 1)

        self.lbl_jueves = Day(self, hlabel = 0.5)
        self.lbl_jueves.valor('Jueves')
        self.lbl_jueves.grid(column = 3 , row = 1)

        self.lbl_viernes = Day(self, hlabel = 0.5)
        self.lbl_viernes.valor('Viernes')
        self.lbl_viernes.grid(column = 4 , row = 1)

        self.lbl_sabado = Day(self, hlabel = 0.5)
        self.lbl_sabado.valor('Sábado')
        self.lbl_sabado.grid(column = 5 , row = 1)

        self.lbl_domingo = Day(self, hlabel = 0.5)
        self.lbl_domingo.valor('Domingo')
        self.lbl_domingo.grid(column = 6 , row = 1)

        #Creación inicial del los días del mes actual. INICIO

        self.month = dt.month
        self.year = dt.year

        self.createDays(self.month, self.year)

    #Creación de las etiquetas de los días. 42 etiquetas para cubrir todos los huecos.

    def createDays(self, month, year):

        #Primera semana

        self.lbl_1 = Day(self)
        self.lbl_1.grid(column = 0 , row = 2)
        self.listaEtiquetas.append(self.lbl_1)

        self.lbl_2 = Day(self)
        self.lbl_2.grid(column = 1 , row = 2)
        self.listaEtiquetas.append(self.lbl_2)

        self.lbl_3 = Day(self)
        self.lbl_3.grid(column = 2 , row = 2)
        self.listaEtiquetas.append(self.lbl_3)

        self.lbl_4 = Day(self)
        self.lbl_4.grid(column = 3 , row = 2)
        self.listaEtiquetas.append(self.lbl_4)

        self.lbl_5 = Day(self)
        self.lbl_5.grid(column = 4 , row = 2)
        self.listaEtiquetas.append(self.lbl_5)

        self.lbl_6 = Day(self)
        self.lbl_6.valor( None ,'red')
        self.lbl_6.grid(column = 5 , row = 2)
        self.listaEtiquetas.append(self.lbl_6)

        self.lbl_7 = Day(self)
        self.lbl_7.valor(None, 'red')
        self.lbl_7.grid(column = 6 , row = 2)
        self.listaEtiquetas.append(self.lbl_7)

        # Segunda semana

        self.lbl_8 = Day(self)
        self.lbl_8.grid(column = 0 , row = 3)
        self.listaEtiquetas.append(self.lbl_8)

        self.lbl_9 = Day(self)
        self.lbl_9.grid(column = 1 , row = 3)
        self.listaEtiquetas.append(self.lbl_9)

        self.lbl_10 = Day(self)
        self.lbl_10.grid(column = 2 , row = 3)
        self.listaEtiquetas.append(self.lbl_10)

        self.lbl_11 = Day(self)
        self.lbl_11.grid(column = 3 , row = 3)
        self.listaEtiquetas.append(self.lbl_11)

        self.lbl_12 = Day(self)
        self.lbl_12.grid(column = 4 , row = 3)
        self.listaEtiquetas.append(self.lbl_12)

        self.lbl_13 = Day(self)
        self.lbl_13.valor(None, 'red')
        self.lbl_13.grid(column = 5 , row = 3)
        self.listaEtiquetas.append(self.lbl_13)

        self.lbl_14 = Day(self)
        self.lbl_14.valor(None, 'red')
        self.lbl_14.grid(column = 6 , row = 3)
        self.listaEtiquetas.append(self.lbl_14)

        # Tercera semana.

        self.lbl_15 = Day(self)
        self.lbl_15.grid(column = 0 , row = 4)
        self.listaEtiquetas.append(self.lbl_15)

        self.lbl_16 = Day(self)
        self.lbl_16.grid(column = 1 , row = 4)
        self.listaEtiquetas.append(self.lbl_16)

        self.lbl_17 = Day(self)
        self.lbl_17.grid(column = 2 , row = 4)
        self.listaEtiquetas.append(self.lbl_17)

        self.lbl_18 = Day(self)
        self.lbl_18.grid(column = 3 , row = 4)
        self.listaEtiquetas.append(self.lbl_18)

        self.lbl_19 = Day(self)
        self.lbl_19.grid(column = 4 , row = 4)
        self.listaEtiquetas.append(self.lbl_19)

        self.lbl_20 = Day(self)
        self.lbl_20.valor(None, 'red')
        self.lbl_20.grid(column = 5 , row = 4)
        self.listaEtiquetas.append(self.lbl_20)

        self.lbl_21 = Day(self)
        self.lbl_21.valor(None, 'red')
        self.lbl_21.grid(column = 6 , row = 4)
        self.listaEtiquetas.append(self.lbl_21)

        # Cuarta semana.

        self.lbl_22 = Day(self)
        self.lbl_22.grid(column = 0 , row = 5)
        self.listaEtiquetas.append(self.lbl_22)

        self.lbl_23 = Day(self)
        self.lbl_23.grid(column = 1 , row = 5)
        self.listaEtiquetas.append(self.lbl_23)

        self.lbl_24= Day(self)
        self.lbl_24.grid(column = 2 , row = 5)
        self.listaEtiquetas.append(self.lbl_24)

        self.lbl_25 = Day(self)
        self.lbl_25.grid(column = 3 , row = 5)
        self.listaEtiquetas.append(self.lbl_25)

        self.lbl_26 = Day(self)
        self.lbl_26.grid(column = 4 , row = 5)
        self.listaEtiquetas.append(self.lbl_26)

        self.lbl_27 = Day(self)
        self.lbl_27.valor(None, 'red')
        self.lbl_27.grid(column = 5 , row = 5)
        self.listaEtiquetas.append(self.lbl_27)

        self.lbl_28 = Day(self)
        self.lbl_28.valor(None, 'red')
        self.lbl_28.grid(column = 6 , row = 5)
        self.listaEtiquetas.append(self.lbl_28)

            

        # Quinta semana.

        self.lbl_29 = Day(self)
        self.lbl_29.grid(column = 0 , row = 6)
        self.listaEtiquetas.append(self.lbl_29)

        self.lbl_30 = Day(self)
        self.lbl_30.grid(column = 1 , row = 6)
        self.listaEtiquetas.append(self.lbl_30)

        self.lbl_31 = Day(self)
        self.lbl_31.grid(column = 2 , row = 6)
        self.listaEtiquetas.append(self.lbl_31)

        self.lbl_32 = Day(self)
        self.lbl_32.grid(column = 3 , row = 6)
        self.listaEtiquetas.append(self.lbl_32)

        self.lbl_33 = Day(self)
        self.lbl_33.grid(column = 4 , row = 6)
        self.listaEtiquetas.append(self.lbl_33)

        self.lbl_34 = Day(self)
        self.lbl_34.valor(None, 'red')
        self.lbl_34.grid(column = 5 , row = 6)
        self.listaEtiquetas.append(self.lbl_34)

        self.lbl_35 = Day(self)
        self.lbl_35.valor(None, 'red')
        self.lbl_35.grid(column = 6 , row = 6)
        self.listaEtiquetas.append(self.lbl_35)


        # Sexta semana.

        self.lbl_36 = Day(self)
        self.lbl_36.grid(column = 0 , row = 7)
        self.listaEtiquetas.append(self.lbl_36)

        self.lbl_37 = Day(self)
        self.lbl_37.grid(column = 1 , row = 7)
        self.listaEtiquetas.append(self.lbl_37)

        self.lbl_38 = Day(self)
        self.lbl_38.grid(column = 2 , row = 7)
        self.listaEtiquetas.append(self.lbl_38)

        self.lbl_39 = Day(self)
        self.lbl_39.grid(column = 3 , row = 7)
        self.listaEtiquetas.append(self.lbl_39)

        self.lbl_40 = Day(self)
        self.lbl_40.grid(column = 4 , row = 7)
        self.listaEtiquetas.append(self.lbl_40)

        self.lbl_41 = Day(self)
        self.lbl_41.valor(None, 'red')
        self.lbl_41.grid(column = 5 , row = 7)
        self.listaEtiquetas.append(self.lbl_41)

        self.lbl_42 = Day(self)
        self.lbl_42.valor(None, 'red')
        self.lbl_42.grid(column = 6 , row = 7)
        self.listaEtiquetas.append(self.lbl_42)

        diaInicial = calendar.monthrange(year,month)
        indiceSemana = (date(year, month , 1).weekday())

        if self.month == 12:
            diaInicialMesAnterior = calendar.monthrange(self.year,1)
        else:
            diaInicialMesAnterior = calendar.monthrange(self.year,self.month-1)
        

        indice1 = diaInicialMesAnterior[1] - indiceSemana + 1
        for i in range (0, indiceSemana):
            self.listaEtiquetas[i].valor(indice1, 'grey')

        for day in range (1, diaInicial[1]+1):
            self.mesActual.append(day)

        contador = 0
        for i in range (indiceSemana, indiceSemana + diaInicial[1]):

            self.listaEtiquetas[i].valor(str(self.mesActual[contador]))
            contador += 1
        
        indice2 = 1
        for i in range (indiceSemana + diaInicial[1], len(self.listaEtiquetas)):
            self.listaEtiquetas[i].valor(str(indice2), 'grey')
            indice2 += 1

        
    
    # Método destruir mes anterior.

    def delete(self):
        
        listaFinDeSemana = ['7','8','14','15','21','22','28','29','35','36']        
        for i in range (0, len(self.listaEtiquetas)):
            
            if str(i) in listaFinDeSemana:
                self.listaEtiquetas[i].valor( None, 'red')
            else:
                self.listaEtiquetas[i].valor(None, 'black')

    # Método de creación de un mes nuevo

    def newMonth(self, month, year):
        self.mesActual = []

        if month == 12:
            diaInicial = calendar.monthrange(year,1)
        if month == 0:
            diaInicial = calendar.monthrange(year,12)
        else:
            diaInicial = calendar.monthrange(year,month)

        indiceSemana = (date(year, month , 1).weekday())

        if month == 12:
            diaInicialMesAnterior = calendar.monthrange(year,1)
        if month == 0:
            diaInicialMesAnterior = calendar.monthrange(year,12)
        else:
            diaInicialMesAnterior = calendar.monthrange(year,month)
        
        indice1 = diaInicialMesAnterior[1] - indiceSemana + 1
        for i in range (0, indiceSemana):
            self.listaEtiquetas[i].valor(str(indice1), 'grey')
            indice1 += 1

        for day in range (1, diaInicial[1]+1):
            self.mesActual.append(day)

        contador = 0
        for i in range (indiceSemana, indiceSemana + diaInicial[1]):

            self.listaEtiquetas[i].valor(str(self.mesActual[contador]))
            contador += 1
        
        indice2 = 1
        for i in range (indiceSemana + diaInicial[1], len(self.listaEtiquetas)):
            self.listaEtiquetas[i].valor(str(indice2), 'grey')
            indice2 += 1

    # Método para quitar un año.

    def backFull (self, simbolo):

        if simbolo == '«':
            
            self.indiceAños -= 1
            self.year = dt.year + self.indiceAños

            self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))
            self.delete()
            self.newMonth(self.month, self.year)        
            

        return self.month

    # Método para ir al mes anterior.

    def back(self, simbolo):

        if simbolo == '<':
            self.month = dt.month + self.indiceMeses 

            if self.month  == 1:
                self.indiceMeses = 12-(dt.month) 
                self.indiceAños -= 1
                self.month = dt.month + self.indiceMeses
                self.year = dt.year + self.indiceAños
                self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))
                self.delete()
                self.newMonth(self.month, self.year)
                

                
            else: 

                self.indiceMeses -= 1
                self.month = dt.month + self.indiceMeses
                self.year = dt.year + self.indiceAños
                self.delete()
                self.newMonth(self.month, self.year)
                self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))      
        
        return self.month

    # Método para pasar al siguiente año.

    def moveOnFull(self,simbolo):

        if simbolo == '»':
            
            self.indiceAños += 1
            self.year = dt.year + self.indiceAños

            self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))
            self.delete()
            self.newMonth(self.month, self.year)  
            
        return self.month
    
    # Método para ir al siguiente mes.

    def moveOn(self, simbolo):
        
        if simbolo == '>':           
            
            self.month = dt.month + self.indiceMeses 

            if self.month  == len(self.listaMeses):
                self.indiceMeses = -(dt.month) + 1
                self.indiceAños += 1
                self.month = dt.month + self.indiceMeses
                self.year = dt.year + self.indiceAños
                self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))
                self.delete()
                if self.month == 0:
                    self.newMonth(self.month+1, self.year)
                    self.indiceMeses +=1
                else:
                    self.newMonth(self.month, self.year)
                              
            else: 

                self.indiceMeses += 1
                self.month = dt.month + self.indiceMeses 
                self.year = dt.year + self.indiceAños 
                self.delete()
                self.newMonth(self.month, self.year)
                self.muestraMes(str(self.listaMeses[self.month-1]) + str(' ') + str(self.year))
                      
        return self.month

    
    # Método para eliminar el mes anterior y que aparezca en pantalla el nuevo mes seleccionado.

    def muestraMes(self, cadena):

        self.lbl_mes.destroy()
        self.lbl_mes = Day(self, wlabel= 3, hlabel= 0.5)
        self.lbl_mes.valor(cadena)
        self.lbl_mes.grid(column = 2 , row = 0, columnspan = 3)
   

            

        

        