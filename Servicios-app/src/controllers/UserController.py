from flask import request, render_template, redirect, flash
from flask.views import MethodView
from flask import session
from src.db import db
from werkzeug.security import generate_password_hash


class AddUserController(MethodView):

    def get(self):

        with db.cursor() as cur:

            cur.execute("SELECT * FROM usuario")
            data = cur.fetchall()
            cur.execute("SELECT * FROM rol")
            datarol = cur.fetchall()
            cur.execute("SELECT * FROM permisos")
            dataper = cur.fetchall()
            cur.execute("SELECT * FROM usuario")
            data2 = cur.fetchall()

            return render_template('public/AddUser.html', data=data, datarol=datarol, dataper=dataper, data2=data2)

    def post(self):

        id_usuario = request.form['id']
        nombre = request.form ['nombre']
        apellido = request.form['apellido']
        correo_electronico = request.form['correo_electronico']
        telefono = request.form['telefono']
        rol_id_rol = request.form['rol_id_rol']
        permisos_id_permisos = request.form['permisos_id_permisos']
        password=request.form['password']

        password_encriptada = generate_password_hash(password)


        with db.cursor() as cur:
            try:
                cur.execute("INSERT INTO usuario (id_usuario, nombre, apellido, correo_electronico, telefono, rol_id_rol, permisos_id_permisos) VALUES(%s, %s, %s, %s, %s, %s, %s)", (id_usuario, nombre, apellido, correo_electronico, telefono, rol_id_rol, permisos_id_permisos))        
                cur.connection.commit()

                cur.execute("INSERT INTO loguin (id_loguin, usuario_id_usuario, contrasena) VALUES(null, %s, %s)",(id_usuario, password_encriptada))
                cur.connection.commit() 

                flash('El usuario se ah registrado corectamente', "success")

            except:

                flash('Ah ocurriodo un problema al registrar el usuario', "error")

        return redirect('/AddUser')

class DeleteUserController(MethodView):

    def post(self, user):

        with db.cursor() as cur:

            try:
                cur.execute("DELETE FROM loguin WHERE usuario_id_usuario = %s", (user))
                cur.connection.commit()

                cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (user))
                cur.connection.commit()
                
                flash('El usuario se ah eliminado corectamente', "success")

            except:

                flash('Ah ocurriodo un problema al eliminar el usuario', "error")

            return redirect("/AddUser")

class UpdateUserController(MethodView):
    def get(self, user):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM usuario WHERE id_usuario = %s", (user, ))
            data = cur.fetchall()
            cur.execute("SELECT * FROM rol")
            datarol = cur.fetchall()
            cur.execute("SELECT * FROM permisos")
            dataper = cur.fetchall()
            return render_template('public/UpdateUser.html', data=data, datarol=datarol, dataper=dataper)

    def post(self, user):

        id_user = request.form['id_usuario']
        name = request.form ['nombre']
        last = request.form['apellido']
        email = request.form['correo_electronico']
        phone = request.form['telefono']
        rol = request.form['rol_id_rol']
        access = request.form['permisos_id_permisos']

        with db.cursor() as cur:

            try:
                cur.execute("UPDATE usuario SET id_usuario = %s, nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, rol_id_rol = %s, permisos_id_permisos = %s WHERE id_usuario = %s", (id_user, name, last, email, phone, rol, access, user))
                cur.connection.commit()

                flash('El usuario se ah editado corectamente', "success")

            except:

                flash('Ah ocurriodo un problema al editar el usuario', "error")

            return redirect("/AddUser")