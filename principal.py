""" Importamos librerias de Tkinter (interfaces graficas), csv y de articulos"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import csv
import articulos

""" Creamos nuestra clase para los formularios """
class FormularioArticulos:
    def __init__(self):
        """ Creamos un objeto de nuestra clase  Inventario para usar las funciones de articulos.py"""
        self.articulo1=articulos.Articulos()
        """ Creamos una nueva ventana de Tkinter """
        self.ventana1=tk.Tk()
        """ Le ponemos  titulo """
        self.ventana1.title("Inventario de articulos")
        """ Creamos un cuaderno (formulario por pestañas) """
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        """ Estos metodos cargan los elementos dentro de las ventanas """
        self.carga_articulos()
        self.cargar_ventas()
        self.reporte_ventas_articulo()
        self.listado_completo()
        self.listado_ventas()
        self.reporte_ventas_vendedor()
        """ Le decimos a python que ejecute el cuaderno que creamos """
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
    """ Cargamos todos los elementos de la pestaña de ingreso a inventario """
    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")
        self.lblArticulosc=ttk.LabelFrame(self.pagina1, text="Artículo")
        self.lblArticulosc.grid(column=0, row=0, padx=5, pady=10)
        self.lblModelo=ttk.Label(self.lblArticulosc, text="Modelo:")
        self.lblModelo.grid(column=0, row=0, padx=4, pady=4)
        self.modelo=tk.StringVar()
        self.txtModelo=ttk.Entry(self.lblArticulosc, textvariable=self.modelo)
        self.txtModelo.grid(column=1, row=0, padx=4, pady=4)
        self.lblNombre=ttk.Label(self.lblArticulosc, text="Nombre:")
        self.lblNombre.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.txtNombre=ttk.Entry(self.lblArticulosc, textvariable=self.nombre)
        self.txtNombre.grid(column=1, row=1, padx=4, pady=4)
        self.lblPrecio = ttk.Label(self.lblArticulosc, text="Precio:")
        self.lblPrecio.grid(column=0, row=2, padx=4, pady=4)
        self.preciop = tk.StringVar()
        self.txtPrecio = ttk.Entry(self.lblArticulosc, textvariable=self.preciop)
        self.txtPrecio.grid(column=1, row=2, padx=4, pady=4)
        self.lblCantidad = ttk.Label(self.lblArticulosc, text="Cantidad:")
        self.lblCantidad.grid(column=0, row=3, padx=4, pady=4)
        self.cantidad = tk.StringVar()
        self.entrycantidad = ttk.Entry(self.lblArticulosc, textvariable=self.cantidad)
        self.entrycantidad.grid(column=1, row=3, padx=4, pady=4)
        self.btnIngresar=ttk.Button(self.lblArticulosc, text="Confirmar", command=self.ingresar)
        self.btnIngresar.grid(column=1, row=4, padx=4, pady=4)
    """ Metodo para procesar el ingreso de productos al inventario """
    def ingresar(self):
        datos=(self.modelo.get(),self.nombre.get(),self.preciop.get(),self.cantidad.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.modelo.set("")
        self.nombre.set("")
        self.preciop.set("")
        self.cantidad.set("")
    """ Cargamos la pantalla para generar una venta """
    def cargar_ventas(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Ingresar ventas")
        self.lblVentav = ttk.LabelFrame(self.pagina4, text="Venta")
        self.lblVentav.grid(column=0, row=0, padx=5, pady=10)
        self.lblModelov = ttk.Label(self.lblVentav, text="Modelo:")
        self.lblModelov.grid(column=0, row=0, padx=4, pady=4)
        self.modelov = tk.StringVar()
        self.txtModelov = ttk.Entry(self.lblVentav, textvariable=self.modelov)
        self.txtModelov.grid(column=1, row=0, padx=4, pady=4)
        self.lblCantidadv = ttk.Label(self.lblVentav, text="Cantidad:")
        self.lblCantidadv.grid(column=0, row=1, padx=4, pady=4)
        self.cantidadv = tk.StringVar()
        self.txtCantidadv = ttk.Entry(self.lblVentav, textvariable=self.cantidadv)
        self.txtCantidadv.grid(column=1, row=1, padx=4, pady=4)
        self.lblVendedorv = ttk.Label(self.lblVentav, text="Vendedor:")
        self.lblVendedorv.grid(column=0, row=2, padx=4, pady=4)
        self.vendedorv = tk.StringVar()
        self.txtVendedorv = ttk.Entry(self.lblVentav, textvariable=self.vendedorv)
        self.txtVendedorv.grid(column=1, row=2, padx=4, pady=4)
        self.btnIngresarv = ttk.Button(self.lblVentav, text="Confirmar", command=self.ingresar_venta)
        self.btnIngresarv.grid(column=1, row=4, padx=4, pady=4)
    """ Metodo que nos permite generar la venta en la base de datos """
    def ingresar_venta(self):
        datos=(self.cantidadv.get(),self.vendedorv.get(),self.modelov.get())
        modelo = (self.modelov.get(),)
        cantidad = self.articulo1.validar_inventario(modelo)
        if cantidad[0][0] < int(self.cantidadv.get()):
            mb.showinfo("Información", "No hay suficiente inventario")
        else:
            sacar_inventario  = (cantidad[0][0] - int(self.cantidadv.get()), self.modelov.get())
            self.articulo1.altav(datos)
            self.articulo1.actualizar_inventario(sacar_inventario)
            mb.showinfo("Información", "Los datos fueron cargados")
        self.modelov.set("")
        self.cantidadv.set("")
        self.vendedorv.set("")

    """ Pantalla para generacion de reporte de ventas por articulo """
    def reporte_ventas_articulo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Ventas por articulo")
        self.lblReporteva=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.lblReporteva.grid(column=0, row=0, padx=5, pady=10)
        self.lblModeloeva=ttk.Label(self.lblReporteva, text="")
        self.lblModeloeva.grid(column=0, row=0, padx=4, pady=4)
        self.Modeloeva=tk.StringVar()
        self.txtModeloeva=ttk.Entry(self.lblModeloeva, textvariable=self.Modeloeva)
        self.txtModeloeva.grid(column=0, row=1, padx=4, pady=4)
        self.btnReporteVentasArticulos=ttk.Button(self.lblReporteva, text="Consultar", command=self.GenerarRVM)
        self.btnReporteVentasArticulos.grid(column=1, row=3, padx=4, pady=4)
    """ Carga la ventana de reporte de ventas por vendedor """
    def reporte_ventas_vendedor(self):
        self.pagina7 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina7, text="Ventas por vendedor")
        self.lblReportevv=ttk.LabelFrame(self.pagina7, text="Vendedor")
        self.lblReportevv.grid(column=0, row=0, padx=5, pady=10)
        self.lblModeloevv=ttk.Label(self.lblReportevv, text="")
        self.lblModeloevv.grid(column=0, row=1, padx=4, pady=4)
        self.Modeloevv=tk.StringVar()
        self.txtModeloevv=ttk.Entry(self.lblModeloevv, textvariable=self.Modeloevv)
        self.txtModeloevv.grid(column=0, row=1, padx=4, pady=4)
        self.btnReporteVentasVendedor=ttk.Button(self.lblReportevv, text="Consultar", command=self.GenerarRVV)
        self.btnReporteVentasVendedor.grid(column=1, row=3, padx=4, pady=4)

    """ Funcion que genera el reporte de ventas por producto en un archivo csv """
    def GenerarRVM(self):
        datos=(self.Modeloeva.get(),)
        respuesta=self.articulo1.generarRVM(datos)
        if len(respuesta)>0:
            titulos = ['Modelo','Cantidad','Vendedor']
            with open('reportes_ventas.csv', 'a', encoding='UTF8') as archivo:
                escribir = csv.writer(archivo)
                escribir.writerow(titulos)
                escribir.writerows(respuesta)
            mb.showinfo("Información", "Reporte creado con exito")
    """ Funcion que genera el reporte de ventas por vendedor en formato csv """
    def GenerarRVV(self):
        datos=(self.Modeloevv.get(), )
        respuesta=self.articulo1.generarRVV(datos)
        if len(respuesta)>0:
            titulos = ['Modelo','Cantidad','Vendedor']
            with open('reportes_vendedor.csv', 'a', encoding='UTF8') as archivo:
                escribir = csv.writer(archivo)
                escribir.writerow(titulos)
                escribir.writerows(respuesta)
            mb.showinfo("Información", "Reporte creado con exito")

    """ Cargamos la pestaña de listado de productos """
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    """ Cargamos la pestaña de listado de ventas """
    def listado_ventas(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Listado ventas")
        self.lbllistadov=ttk.LabelFrame(self.pagina5, text="Ventas")
        self.lbllistadov.grid(column=0, row=0, padx=5, pady=10)
        self.btnListadov=ttk.Button(self.lbllistadov, text="Listado completo", command=self.listarVentas)
        self.btnListadov.grid(column=0, row=0, padx=4, pady=4)
        self.sctxtListadov=st.ScrolledText(self.lbllistadov, width=30, height=10)
        self.sctxtListadov.grid(column=0,row=1, padx=10, pady=10)


    """ Rellenamos la lista visual del formulario con los datos del inventario """
    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Modelo:"+str(fila[0])+"\nNombre:"+str(fila[1])+"\nPrecio:$"+str(fila[2])+"\nCantidad:"+str(fila[3])+"\n")

    """ Rellenamos la vista de ventas con los datos de las ventas """
    def listarVentas(self):
        respuesta=self.articulo1.recuperar_ventas()
        self.sctxtListadov.delete("1.0", tk.END)
        for fila in respuesta:
            self.sctxtListadov.insert(tk.END, "Modelo:"+str(fila[0])+"\nCantidad:"+str(fila[1])+"\nVendedor:"+str(fila[2])+"\n")

""" Corremos el formulario principal"""
aplicacion1=FormularioArticulos()