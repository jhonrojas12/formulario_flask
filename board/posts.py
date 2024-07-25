from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from board.database import get_db
from board.postgresqldb import conexionBD

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author1 = request.form["author"] or "Anonymous"
        message1 = request.form["message"]

        if message1:
            connection = conexionBD()
            cur=connection.cursor()            
            cur.execute(
                "INSERT INTO post (author, message) VALUES (%s, %s)",
                (author1, message1),
            )
            connection.commit()
            cur.close()
            connection.close()
            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")

@bp.route("/posts")
def posts():

    connection = conexionBD()
    cur=connection.cursor()
    cur.execute("SELECT author, message, created FROM post ORDER BY created DESC")
    print('acaba de ejecutar query')
    posts = cur.fetchall()
    print(posts)
    #connection.commit()
    cur.close()
    connection.close()
    return render_template("posts/posts.html", posts=posts)

'''
@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        author = request.form["author"] or "Anonymous"
        message = request.form["message"]

        if message:
            db = get_db()
            db.execute(
                "INSERT INTO post (author, message) VALUES (?, ?)",
                (author, message),
            )
            db.commit()
            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        "SELECT author, message, created FROM post ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)
'''