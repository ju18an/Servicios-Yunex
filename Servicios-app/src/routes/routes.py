from src.controllers.StockController import *
from src.controllers.ModuloController import *
from src.controllers.PermisosController import *
from src.controllers.UserController import *
from src.controllers.RolController import *
from src.controllers.IndexController import *
from src.controllers.errors import NotFoundController

routes = {
        # Ruta del Index
            "Index": "/", "Index_controller": IndexController.as_view("Index"), 

        # Rutas del Usuario
            "AddUser": "/AddUser", "AddUser_Controller": AddUserController.as_view("hello"),
            "DeleteUser": "/DeleteUser/<user>", "DeleteUser_Controller": DeleteUserController.as_view("DeleteUser"),
            "UpdateUser": "/UpdateUser/<user>", "UpdateUser_Controller": UpdateUserController.as_view("UpdateUser"),
        
        # Rutas del Rol
            "AddRol": "/AddRol", "AddRol_Controller": AddRolController.as_view("AddRol"),
            "DeleteRol": "/DeleteRol/<rol>", "DeleteRol_Controller": DeleteRolController.as_view("DeleteRol"),
            "UpdateRol": "/UpdateRol/<rol>", "UpdateRol_Controller": UpdateRolController.as_view("UpdateRol"),
             
        #Rutas del Permiso
            "AddPermiso": "/AddPermiso", "AddPermiso_Controller": AddPermisoController.as_view("AddPermiso"),
            "UpdateAccess": "/UpdateAccess/<acce>", "UpdateAccess_Controller": UpdateAccessController.as_view("UpdateAccess"),

        #Rutas del Modulo
            "AddModulo": "/AddModulo", "AddModulo_Controller": AddModuloController.as_view("AddModulo"),
            "DeleteModulo": "/DeleteModulo/<modulo>", "DeleteModulo_Controller": DeleteModuloController.as_view("DeleteModulo"),
            "UpdateModulo": "/UpdateModulo/<modulo>", "UpdateModulo_Controller": UpdateModuloController.as_view("UpdateModulo"),
            "TranslateModulo": "/TranslateModulo", "TranslateModulo_Controller": TranslateModuloController.as_view("TranslateModulo"),
            "TranslateModuloFin": "/TranslateModuloFin/<modulo>", "TranslateModuloFin_Controller": TranslateModuloFinController.as_view("TranslateModuloFin"),

        #Rutas de Stock
            "AddStock": "/AddStock", "AddStock_Controller": AddStockController.as_view("AddStock"),
            "DeleteStock": "/DeleteStock/<stock>", "DeleteStock_Controller": DeleteStockController.as_view("DeleteStock"),
            "UpdateStock": "/UpdateStock/<stock>", "UpdateStock_Controller": UpdateStockController.as_view("UpdateStock"),

        #Rutas del 404
            "not_found_route": 404, "not_found_controller": NotFoundController.as_view("not_found"),
        }