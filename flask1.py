from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/report')


def report():
    df = pd.read_csv('iris.csv')
    #df = df.groupby(by=['country'])['patents'].sum().to_frame()
    return df.to_html()

if __name__ == '__main__':
    app.run()

# good news.  this works. 
# bad news. it's fugly.  

# time to iterate. *dingdingding*
