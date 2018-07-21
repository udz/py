'''
https://hackernoon.com/flask-web-programming-from-scratch-9ada8088fde1

MSSQL Support in flask_SQLAlchemy
https://stackoverflow.com/questions/46739295/connect-to-mssql-database-using-flask-sqlalchemy
'''

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import urllib
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Settings
app = Flask(__name__)
#app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:123456@DESKTOP-FR8RURI/appdb'

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-FR8RURI;DATABASE=appdb;UID=sa;PWD=123456;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #To disable showing warning


db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer(),primary_key = True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def _init_(self,title,post_text):
        self.title = title
        self.post_text = post_text

#  Declaring Flask wtf form

class PostForm(FlaskForm):
    title = StringField('Title',validators = [DataRequired()])
    post_text = StringField('Post_Text',validators = [DataRequired()])

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/addpost',methods =['GET','POST'])
def add_post():
    postform = PostForm()
    if request.method == 'POST':
        pf = POST(
            postform.title.data,
            postform.post_text.data,
        )
        db.session.add(pf)
        db.session.commit()
        return redirect(url_for('view_posts'))
    return render_template('post_form.html',postform = postform)

@app.route('/posts', methods = ['GET','POST'])
def view_posts():
    posts = Post.query.all()
    return render_template('view_posts.html',posts = posts)

app = Flask(__name__)

if __name__ == '__main__':
    manager.run()