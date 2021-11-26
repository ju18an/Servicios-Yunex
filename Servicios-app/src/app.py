from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

#Rutas de la Aplicacion

app.config.from_mapping( 
    SECRET_KEY = 'development'
)

# Rutas de Index
app.add_url_rule(routes["Index"], view_func=routes["Index_controller"])
app.add_url_rule(routes["Logout"], view_func=routes["Logout_Controller"])

#Rutas de Usuario
app.add_url_rule(routes["AddUser"], view_func=routes["AddUser_Controller"])
app.add_url_rule(routes["DeleteUser"], view_func=routes["DeleteUser_Controller"])
app.add_url_rule(routes["UpdateUser"], view_func=routes["UpdateUser_Controller"])

#Rutas de Roles
app.add_url_rule(routes["AddRol"], view_func=routes["AddRol_Controller"])
app.add_url_rule(routes["DeleteRol"], view_func=routes["DeleteRol_Controller"])
app.add_url_rule(routes["UpdateRol"], view_func=routes["UpdateRol_Controller"])

#Rutas de Permisos
app.add_url_rule(routes["AddPermiso"], view_func=routes["AddPermiso_Controller"])
app.add_url_rule(routes["UpdateAccess"], view_func=routes["UpdateAccess_Controller"])

#Rutas de Modulos
app.add_url_rule(routes["AddModulo"], view_func=routes["AddModulo_Controller"])
app.add_url_rule(routes["DeleteModulo"], view_func=routes["DeleteModulo_Controller"])
app.add_url_rule(routes["UpdateModulo"], view_func=routes["UpdateModulo_Controller"])
app.add_url_rule(routes["HistoryModule"], view_func=routes["HistoryModule_Controller"])
app.add_url_rule(routes["TransModule"], view_func=routes["TransModule_Controller"])

#Rutas de Stock
app.add_url_rule(routes["AddStock"], view_func=routes["AddStock_Controller"])
app.add_url_rule(routes["DeleteStock"], view_func=routes["DeleteStock_Controller"])
app.add_url_rule(routes["UpdateStock"], view_func=routes["UpdateStock_Controller"])

# Ruta del error 404
app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])