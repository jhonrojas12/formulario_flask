from flask import Blueprint, render_template
from flask import jsonify
from flask import request

import socket

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    #return "Hello, Home!"
    #render_template("pages/home.html")
    #render_template("base.html")
    #return render_template("pages/home.html")

    user_adr=request.remote_addr
    #user_adr=request.headers.get('User-Agent')
    server_adr=socket.gethostbyname(socket.gethostname())
    return render_template("pages/home.html",info=(user_adr,server_adr))
    

@bp.route("/about")
def about():
    #render_template("pages/about.html")
    return render_template("pages/about.html")
    #return "Hello, About!"