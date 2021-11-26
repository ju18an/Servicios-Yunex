from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import db

class AddRolController(MethodView):

    def get(self):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM rol")
            data = cur.fetchall()
            return render_template('public/RegistrarRol.html', data=data)

    def post(self):

        id_rol = request.form['id_rol']
        des_rol = request.form ['desc_rol']
        estado_rol = 1
        

        with db.cursor() as cur:

            try:
                cur.execute("INSERT INTO rol (id_rol, desc_rol, estado_rol) VALUES(%s, %s, %s)", (id_rol, des_rol, estado_rol))        
                cur.connection.commit()
             
                flash('El rol se ah registrado corectamente', "success")

            except:

                flash('Ah ocurrido un problema al registrar el rol', "error")

        return redirect('/AddRol')

class DeleteRolController(MethodView):

    def post(self, rol):

        with db.cursor() as cur:

            try:
                cur.execute("UPDATE rol SET estado_rol = '0' WHERE id_rol = %s", (rol))
                cur.connection.commit()

                flash('El rol se ah eliminado corectamente', "success")

            except:

                flash('Ah ocurrido un problema al eliminar el rol', "error")

            return redirect("/AddRol")

class UpdateRolController(MethodView):
    def get(self, rol):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM rol WHERE id_rol = %s", (rol, ))
            data = cur.fetchall()
            
            return render_template('public/UpdateRol.html', data=data)

    def post(self, rol):

        id_rol = request.form['id_rol']
        des_rol = request.form ['desc_rol']

        with db.cursor() as cur:

            try:

                cur.execute("UPDATE rol SET id_rol = %s, desc_rol = %s WHERE id_rol = %s", (id_rol, des_rol, rol))
                cur.connection.commit()
            
                flash('El rol se ah actualizado corectamente', "success")

            except:

                flash('Ah ocurrido un problema al actualizar el rol', "error")

            return redirect("/AddRol")

            