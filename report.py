from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/report')


def report():
    df = pd.read_csv('data.csv')
    return render_template('report.html', df=df.to_html())

if __name__ == '__main__':
    app.run()
