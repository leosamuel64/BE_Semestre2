from flask import Flask, render_template, redirect, session
app=Flask(__name__)
app.template_folder = "template"
app.static_folder="static"
app.config.from_object('myApp.config')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/prevision.html')
def prevision():
    return render_template("prevision.html")

@app.route('/administration.html')
def administration():
    return render_template("administration.html")

@app.route('/compte.html')
def compte():
    return render_template("compte.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/webmaster.html')
def webmaster():
    return render_template("webmaster.html")

