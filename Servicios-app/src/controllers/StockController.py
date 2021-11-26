from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import db

class AddStockController(MethodView):

    def get(self):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM almacenes")
            data = cur.fetchall()
            return render_template('public/AddStock.html', data=data)

    def post(self):

        id_stock = request.form['id_almacen']
        usuario_id_usuario = request.form ['id_usuario']
        desc_almacen = request.form['desc_almacen']
        estado_almacen = 1

        with db.cursor() as cur:

            try:
                cur.execute("INSERT INTO almacenes (id_almacen, usuario_id_usuario, desc_almacen, estado_almacen) VALUES(%s, %s, %s, %s)", (id_stock, usuario_id_usuario, desc_almacen, estado_almacen))        
                cur.connection.commit()

                flash('El almacen se ah registrado corectamente', "success")

            except:
                flash('Ah ocurrido un problema al registrar el almacen', "error")


        return redirect('/AddStock')

class DeleteStockController(MethodView):

    def post(self, stock):

        with db.cursor() as cur:

            try:
                cur.execute("DELETE FROM almacenes WHERE id_almacen = %s", (stock))
                cur.connection.commit()

                flash('El almacen se ah eliminado corectamente', "success")

            except:
                flash('Ah ocurrido un problema al eliminar el almacen', "error")

            return redirect("/AddStock")

class UpdateStockController(MethodView):
    def get(self, stock):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM almacenes WHERE id_almacen = %s", (stock, ))
            data = cur.fetchall()
            return render_template('public/UpdateStock.html', data=data)

    def post(self, stock):

        id_stock = request.form['id_almacen']
        usuario_id_usuario = request.form ['id_usuario']
        desc_almacen = request.form['desc_almacen']
        estado_almacen = request.form['estado_almacen']

        with db.cursor() as cur:

            try:
                cur.execute("UPDATE almacenes SET id_almacen = %s, usuario_id_usuario = %s, desc_almacen = %s, estado_almacen = %s WHERE id_almacen = %s", (id_stock, usuario_id_usuario, desc_almacen, estado_almacen, stock))
                cur.connection.commit()
                
                flash('El almacen se ah editado corectamente', "success")

            except:
                flash('Ah ocurrido un problema al editar el almacen', "error")

            return redirect("/AddStock")

        #return f"los valores son {id_stock, usuario_id_usuario, desc_almacen, estado_almacen, stock}"

    