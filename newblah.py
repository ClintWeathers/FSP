from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    df = pd.read_csv('iris.csv')
    #data.set_index(['Name'], inplace=True)
    df.index.name=None
    setosa = df.loc[df.species=='setosa']
    versicolor = df.loc[df.species=='versicolor']
    virginica = df.loc[df.species=='virginica']
    return render_template('view.html',tables=[setosa.to_html(classes='setosa'), versicolor.to_html(classes='versicolor'), virginica.to_html(classes='virginica')],
    titles = ['Setosa', 'Versicolor', 'Virginica'])

if __name__ == "__main__":
    app.run(debug=True)
