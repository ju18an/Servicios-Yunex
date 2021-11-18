from flask import request, render_template, redirect
from flask.views import MethodView
from src.db import db

class AddPermisoController (MethodView):

    def get(self):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM permisos")
            data = cur.fetchall()
            return render_template('public/RegistrarPermiso.html', data=data)

    def post(self):

        id_permiso = request.form['id_permisos']
        desc_permiso = request.form ['desc_permisos']
        

        with db.cursor() as cur:
            cur.execute("INSERT INTO permisos (id_permisos, desc_permisos) VALUES(%s, %s)", (id_permiso, desc_permiso))        
            cur.connection.commit()

        return redirect('/AddPermiso')
            
class UpdateAccessController(MethodView):
    def get(self, acce):

        with db.cursor() as cur:
            cur.execute("SELECT * FROM permisos WHERE id_permisos = %s", (acce, ))
            data = cur.fetchall()
            return render_template('public/UpdateAccess.html', data=data)

    def post(self, acce):

        id_access = request.form['id_permisos']
        desc_access = request.form ['desc_permisos']

        with db.cursor() as cur:
            cur.execute("UPDATE permisos SET id_permisos = %s, desc_permisos = %s WHERE id_permisos = %s", (id_access, desc_access, acce))
            cur.connection.commit()

            return redirect("/AddPermiso")