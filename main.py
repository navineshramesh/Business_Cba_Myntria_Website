
from flask import Flask, abort, render_template, redirect, url_for, flash, request, session
@app.route("/home")
def about():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=False, port=5002)
