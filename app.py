from flask import Flask, request, jsonify, render_template, url_for, flash, redirect, make_response, Response
from model import *
import datetime
import io
import csv



# define the app
app = Flask(__name__)


# model_api = load()

@app.route('/')
def outline():
    return render_template('outline.html')


@app.route('/inference', methods= ['POST','GET'])
def infer():
    if request.method == 'POST':
        Age = request.form['Age']
        Gender = request.form['Gender']
        Usage = request.form['Usage']
        Miles = request.form['Miles']

        if not Age:
            flash('Please enter your age')
            flash('Please enter your Gender')
            flash('Please enter your Usage')
            flash('Please enter your Miles')

        else : 
            fitness = search(Age, Gender, Usage, Miles)
            return render_template('inference.html', fitness = fitness)
                
    return render_template('inference.html')



if __name__ == "__main__":   
    app.run(debug=True)