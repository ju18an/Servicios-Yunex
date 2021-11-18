from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import db


class IndexController(MethodView):

    def get(self):
        return render_template("public/Index.html")