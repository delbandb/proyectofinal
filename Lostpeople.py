import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# Generamos la conexión con la base de datos
db_connection = mysql.connector.connect(
    host="localhost",
    user="delband",
    password="delband",
    database="people"  
)
db_cursor = db_connection.cursor(buffered=True)

# Creamos la ventana principal
class LostPeopleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro de las personas perdidas")
        self.geometry("800x650+351+174")

        # Labels
        self.lblTitle = tk.Label(self, text="Lost People Management System", font=("Helvetica", 15), bg="black", fg="white")
        self.lblNombre = tk.Label(self, text="Introduce el nombre:", font=("Arial", 10), bg="blue", fg="white")
        self.lblApellido = tk.Label(self, text="Introduce el apellido:", font=("Arial", 10), bg="blue", fg="white")
        self.lblContacto = tk.Label(self, text="Introduce su número de contacto:", font=("Arial", 10), bg="blue", fg="white")
        self.lblUltimoSitio = tk.Label(self, text="Introduce el último sitio que se ha visto a esta persona:", font=("Arial", 8), bg="blue", fg="white")
        self.lblSexoAltura = tk.Label(self, text="Introduce su Sexo y su Altura:", font=("Arial", 10), bg="blue", fg="white")
        self.lblFecha = tk.Label(self, text="Introduce la última fecha que se ha visto a esta persona:", font=("Arial", 8), bg="blue", fg="white")
        self.lblSelect = tk.Label(self, text="Elige una opción para actualizar o eliminar datos", font=("Arial", 10), bg="blue", fg="white")
        self.lblSearch = tk.Label(self, text="Introduce su ID :", font=("Arial", 12), bg="blue", fg="white")

        # Entradas
        self.entNombre = tk.Entry(self)
        self.entApellido = tk.Entry(self)
        self.entContacto = tk.Entry(self)
        self.entUltimoSitio = tk.Entry(self)
        self.entSexoAltura = tk.Entry(self)
        self.calFecha = DateEntry(self, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024, locale='es_ES', date_pattern='y-mm-dd')
        self.entSearch = tk.Entry(self)  

        # Botones
        self.btn_register = tk.Button(self, text="Registrar", font=("Helvetica", 11), bg="green", fg="black", command=self.register_people)
        self.btn_update = tk.Button(self, text="Actualizar", font=("Helvetica", 11), bg="green", fg="black", command=self.update_people_data)
        self.btn_delete = tk.Button(self, text="Eliminar", font=("Helvetica", 11), bg="green", fg="black", command=self.delete_people_data)
        self.btn_clear = tk.Button(self, text="Borrar todo", font=("Helvetica", 11), bg="green", fg="black", command=self.clear_form)
        self.btn_show_all = tk.Button(self, text="Demostrar", font=("Helvetica", 11), bg="green", fg="black", command=self.load_people_data)
        self.btn_search = tk.Button(self, text="Buscar", font=("Helvetica", 11), bg="green", fg="black", command=self.show_search_data)
        self.btn_exit = tk.Button(self, text="Salir", font=("Helvetica", 11), bg="red", fg="black", command=self.btn_exit)

        # Treeview
        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")
        self.tvPeople = ttk.Treeview(self, show="headings", height="5", columns=columns)
        self.tvPeople.heading('#1', text='ID', anchor='center')
        self.tvPeople.column('#1', width=60, anchor='center', stretch=False)
        self.tvPeople.heading('#2', text='Nombre', anchor='center')
        self.tvPeople.column('#2', width=100, anchor='center', stretch=True)
        self.tvPeople.heading('#3', text='Apellido', anchor='center')
        self.tvPeople.column('#3', width=100, anchor='center', stretch=True)
        self.tvPeople.heading('#4', text='Número de contacto', anchor='center')
        self.tvPeople.column('#4', width=100, anchor='center', stretch=True)
        self.tvPeople.heading('#5', text='Último sitio', anchor='center')
        self.tvPeople.column('#5', width=100, anchor='center', stretch=True)
        self.tvPeople.heading('#6', text='Sexo y altura', anchor='center')
        self.tvPeople.column('#6', width=100, anchor='center', stretch=True)
        self.tvPeople.heading('#7', text='Última fecha', anchor='center')
        self.tvPeople.column('#7', width=100, anchor='center', stretch=True)

        # Scrollbars
        self.vsb_vertical = ttk.Scrollbar(self, orient="vertical", command=self.tvPeople.yview)
        self.vsb_horizontal = ttk.Scrollbar(self, orient="horizontal", command=self.tvPeople.xview)
        self.tvPeople.configure(yscrollcommand=self.vsb_vertical.set, xscrollcommand=self.vsb_horizontal.set)

        # los fondos
        self.lblTitle.place(x=250, y=20, height=27, width=300)
        self.lblNombre.place(x=40, y=70, height=23, width=300)
        self.lblApellido.place(x=40, y=100, height=23, width=300)
        self.lblContacto.place(x=40, y=129, height=23, width=300)
        self.lblUltimoSitio.place(x=40, y=158, height=23, width=300)
        self.lblSexoAltura.place(x=40, y=187, height=23, width=300)
        self.lblFecha.place(x=40, y=217, height=23, width=300)
        self.lblSelect.place(x=40, y=280, height=23, width=300)
        self.lblSearch.place(x=40, y=560, height=23, width=240)
        self.entNombre.place(x=350, y=72, height=21, width=186)
        self.entApellido.place(x=350, y=100, height=21, width=186)
        self.entContacto.place(x=350, y=129, height=21, width=186)
        self.entUltimoSitio.place(x=350, y=158, height=21, width=186)
        self.entSexoAltura.place(x=350, y=188, height=21, width=186)
        self.calFecha.place(x=350, y=218, height=21, width=186)
        self.entSearch.place(x=310, y=560, height=21, width=186)
        self.btn_register.place(x=290, y=245, height=25, width=76)
        self.btn_update.place(x=370, y=245, height=25, width=76)
        self.btn_delete.place(x=460, y=245, height=25, width=76)
        self.btn_clear.place(x=548, y=245, height=25, width=76)
        self.btn_show_all.place(x=630, y=245, height=25, width=76)
        self.btn_search.place(x=498, y=558, height=26, width=60)
        self.btn_exit.place(x=320, y=610, height=31, width=60)
        self.tvPeople.place(x=40, y=310, height=200, width=640)
        self.vsb_vertical.place(x=680, y=310, height=200)
        self.vsb_horizontal.place(x=40, y=510, width=640)

        # Database 
        self.create_table()
        self.load_people_data()

    def clear_form(self):
        self.entNombre.delete(0, tk.END)
        self.entApellido.delete(0, tk.END)
        self.entContacto.delete(0, tk.END)
        self.entUltimoSitio.delete(0, tk.END)
        self.entSexoAltura.delete(0, tk.END)
        self.calFecha.set_date('')  

    def btn_exit(self):
        mb = messagebox.askquestion('Salir de la aplicación', '¿Está seguro de que quiere salir de la aplicación?', icon='warning')
        if mb == 'yes':
            self.destroy()

    def delete_people_data(self):
        mb = messagebox.askquestion('Borrar el registro', '¿Está seguro de que quieres borrar el registro?', icon='warning')
        if mb == 'yes':
            for selection in self.tvPeople.selection():
                item = self.tvPeople.item(selection)
                Id = item["values"][0]

                if db_connection.is_connected() == False:
                    db_connection.connect()
                db_cursor.execute("USE people")
                Delete = "DELETE FROM people WHERE Id=%s"
                db_cursor.execute(Delete, (Id,))
                db_connection.commit()
            messagebox.showinfo("Información", "El registro de esta persona se ha eliminado correctamente")
            self.load_people_data()
            
    def create_table(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
            db_cursor.execute("CREATE DATABASE IF NOT EXISTS people")
            db_cursor.execute("USE people")
            db_cursor.execute(
                """CREATE TABLE IF NOT EXISTS people (
                Id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                nombre VARCHAR(30),
                apellido VARCHAR(30),
                contacto VARCHAR(20),
                ultimositio VARCHAR(30),
                sexoaltura VARCHAR(20),
                fecha DATE
                ) AUTO_INCREMENT=1"""
            )
            db_connection.commit()
            
    def register_people(self):
        try:
            if db_connection.is_connected() == False:
                db_connection.connect()
            db_cursor.execute("USE people")
            nombre = self.entNombre.get()
            apellido = self.entApellido.get()
            contacto = self.entContacto.get()
            ultimositio = self.entUltimoSitio.get()
            sexoaltura = self.entSexoAltura.get()
            fecha = self.calFecha.get_date()
            if nombre == "":
                messagebox.showinfo('Información', "Por favor, introduzca el nombre de la persona")
                self.entNombre.focus_set()
                return
            if apellido == "":
                messagebox.showinfo('Información', "Por favor, introduzca el apellido de la persona")
                self.entApellido.focus_set()
                return
            if contacto == "":
                messagebox.showinfo('Información', "Por favor, introduzca un número de contacto")
                self.entContacto.focus_set()
                return
            if ultimositio == "":
                messagebox.showinfo('Información', "Por favor, introduzca el último sitio donde se haya visto a esta persona")
                self.entUltimoSitio.focus_set()
                return
            if sexoaltura == "":
                messagebox.showinfo('Información', "Por favor, introduzca el sexo y la altura de la persona")
                self.entSexoAltura.focus_set()
                return
            if fecha == "":
                messagebox.showinfo('Información', "Por favor, introduzca la última fecha que se ha visto a esta persona")
                self.calFecha.focus_set()
                return
            query = "INSERT INTO people (nombre, apellido, contacto, ultimositio, sexoaltura, fecha) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (nombre, apellido, contacto, ultimositio, sexoaltura, fecha)
            db_cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Información", "Esta persona se ha registrado correctamente")
            self.load_people_data()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Ha ocurrido un error: {err}")

    def update_people_data(self):
        try:
            if db_connection.is_connected() == False:
                db_connection.connect()
            db_cursor.execute("USE people")

            selected_item = self.tvPeople.selection()[0]
            Id = self.tvPeople.item(selected_item, 'values')[0]

            nombre = self.entNombre.get()
            apellido = self.entApellido.get()
            contacto = self.entContacto.get()
            ultimositio = self.entUltimoSitio.get()
            sexoaltura = self.entSexoAltura.get()
            fecha = self.calFecha.get_date()

            query = """UPDATE people SET nombre=%s, apellido=%s, contacto=%s, 
                       ultimositio=%s, sexoaltura=%s, fecha=%s WHERE Id=%s"""
            values = (nombre, apellido, contacto, ultimositio, sexoaltura, fecha, Id)

            db_cursor.execute(query, values)
            db_connection.commit()
            messagebox.showinfo("Información", "Los datos de la persona se han actualizado correctamente")
            self.load_people_data()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Ha ocurrido un error: {err}")

    def load_people_data(self):
        try:
            if db_connection.is_connected() == False:
                db_connection.connect()
            db_cursor.execute("USE people")
            db_cursor.execute("SELECT * FROM people")
            rows = db_cursor.fetchall()

            self.tvPeople.delete(*self.tvPeople.get_children())
            for row in rows:
                self.tvPeople.insert("", tk.END, values=row)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Ha ocurrido un error: {err}")

    def show_search_data(self):
        for selection in self.tvPeople.selection():
            item = self.tvPeople.item(selection)
            self.Id, self.nombre, self.apellido, self.contacto, self.ultimositio, self.sexoaltura, self.fecha = item["values"]

            self.entNombre.delete(0, tk.END)
            self.entNombre.insert(0, self.nombre)
            self.entApellido.delete(0, tk.END)
            self.entApellido.insert(0, self.apellido)
            self.entContacto.delete(0, tk.END)
            self.entContacto.insert(0, self.contacto)
            self.entUltimoSitio.delete(0, tk.END)
            self.entUltimoSitio.insert(0, self.ultimositio)
            self.entSexoAltura.delete(0, tk.END)
            self.entSexoAltura.insert(0, self.sexoaltura)
            self.calFecha.set_date(self.fecha)

if __name__ == "__main__":
    app = LostPeopleApp()
    app.mainloop()








