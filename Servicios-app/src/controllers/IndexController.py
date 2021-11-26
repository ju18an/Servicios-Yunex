from flask.views import MethodView
from flask import request, render_template, redirect, flash
from src.db import db
from flask import session
from werkzeug.security import check_password_hash


class IndexController(MethodView):

    def get(self):
        return render_template("public/Index.html")

    def post(self):

        id_usuario=request.form["id_usuario"]
        password=request.form["password"]

        with db.cursor() as cur:
            
            cur.execute("SELECT * FROM loguin WHERE usuario_id_usuario  = %s", (id_usuario))
            data=cur.fetchone()
            cur.close()
        
           

            if (data != None):

                if (check_password_hash(data[2], password)):
                    
                    session['user']=data[1]

                    return redirect('/AddUser')

                else:
        
                    flash("Contraseña Incorrecta", "error")
                    return redirect('/')
                    
            else:
                    flash("Contraseña Incorrecta", "error")
                    return redirect('/')
                   

        #return f"LOS VALORES SON {id_usuario, password}"

class LogoutController(MethodView):
    def get(self):
        
        session.pop('user')

        return redirect("/")