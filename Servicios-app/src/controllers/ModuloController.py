from flask import request, render_template, redirect, sessions
from flask.views import MethodView
from src.db import db
from flask import session
import datetime

class AddModuloController(MethodView):

    def get(self):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM modulos")
            data = cur.fetchall()

            cur.execute("SELECT * FROM almacenes")
            datastock = cur.fetchall()
            return render_template('public/AddModule.html', data=data, datastock=datastock)

    def post(self):

        id_modulo = request.form['id_modulo']
        nombre = request.form ['nombre']
        proyecto = request.form['proyecto']
        fabricante = request.form['fabricante']
        proveedor = request.form['proveedor']
        cliente = request.form['cliente']
        modelo = request.form['modelo']
        fecha_creacion = request.form['fecha_creacion']
        fecha_inicio_operacion = request.form['fecha_inicio_operacion']
        ubicacion = request.form['ubicacion']
        estado_modulo = 1
        sessionuser = session['user']
        fecha = datetime.datetime.now()
        desctranslado = "Creación del modulo"

        with db.cursor() as cur:
            cur.execute("INSERT INTO modulos (id_modulo, nombre, proyecto, fabricante, proveedor, cliente, modelo, fecha_creacion, fecha_inicio_operacion, ubicacion, estado_modulo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id_modulo, nombre, proyecto, fabricante, proveedor, cliente, modelo, fecha_creacion, fecha_inicio_operacion, ubicacion, estado_modulo))        
            cur.connection.commit()

        with db.cursor() as cur:
            cur. execute("INSERT INTO historial (modulos_id_modulo, usuario_id_usuario, fecha_translado, desc_translado) VALUES (%s, %s, %s, %s)", (id_modulo, sessionuser, fecha, desctranslado))
            cur.connection.commit()

        return redirect('/AddModulo')

class DeleteModuloController(MethodView):

    def post(self, modulo):

        with db.cursor() as cur:
            cur.execute("DELETE FROM modulos WHERE id_modulo = %s", (modulo))
            cur.connection.commit()

            return redirect("/AddModulo")

class UpdateModuloController(MethodView):
    def get(self, modulo):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM modulos WHERE id_modulo = %s", (modulo, ))
            data = cur.fetchall()
            return render_template('public/UpdateModulo.html', data=data)

    def post(self, modulo):

        id_modulo = request.form['id_modulo']
        nombre = request.form ['nombre']
        proyecto = request.form['proyecto']
        fabricante = request.form['fabricante']
        proveedor = request.form['proveedor']
        cliente = request.form['cliente']
        modelo = request.form['modelo']
        fecha_creacion = request.form['fecha_creacion']
        fecha_inicio_operacion = request.form['fecha_inicio_operacion']
        estado_modulo = request.form['estado_modulo']

        with db.cursor() as cur:
            cur.execute("UPDATE historial SET modulos_id_modulo= %s  WHERE modulos_id_modulo = %s", (id_modulo, modulo))
            cur.connection.commit()
            
        with db.cursor() as cur:
            cur.execute("UPDATE modulos SET id_modulo = %s, nombre = %s, proyecto = %s, fabricante = %s, proveedor = %s, cliente = %s, modelo = %s, fecha_creacion = %s, fecha_inicio_operacion = %s, estado_modulo = %s WHERE id_modulo = %s", (id_modulo, nombre, proyecto, fabricante, proveedor, cliente, modelo, fecha_creacion, fecha_inicio_operacion, estado_modulo, modulo))
            cur.connection.commit()
        
        

            return redirect("/AddModulo")

class TranslateModuloController(MethodView):
    def get(self):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM modulos")
            data = cur.fetchall()
            cur.execute("SELECT * FROM almacenes")
            dataalm = cur.fetchall()
            return render_template('public/TranslateModulo.html', data=data, dataalm=dataalm)
    
    def post(self):

        stock = request.form['alm_origen']

        with db.cursor() as cur:
            cur.execute("SELECT * FROM modulos WHERE ubicacion = %s", (stock))
            data = cur.fetchall()
            cur.execute("SELECT * FROM almacenes")
            dataalm = cur.fetchall()

            return render_template('public/TranslateModuloInv.html', data=data, dataalm=dataalm)
        #return f"El almacen es {stock}"

class TranslateModuloFinController(MethodView):
    def get(self):
        return "ENTRO AL GET"
 
    def post(self, modulo):

        return f"Los valores son {modulo}"