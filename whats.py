from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("myform.html")

@app.route('/process', methods=['POST'])
def create_user():
    name = request.form['name']
    print request.form

   # redirects back to the '/' route
    return redirect('/')

app.run(debug=True)