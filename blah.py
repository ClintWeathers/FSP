from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/blah')


def report():
    df = pd.read_csv('iris.csv')

    #blah = df.to_html()
    blah = df.to_html(open('./templates/blah.html', 'w'))
    return render_template('blah.html')

if __name__ == '__main__':
    app.run(debug=True)

# good news.  this works.
# bad news. it's fugly.

# time to iterate. *dingdingding*
