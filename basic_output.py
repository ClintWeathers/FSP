import pandas as pd
from flask import *
app = Flask(__name__)

@app.route("/")
def output():
  df = pd.read_csv('./data.csv', delimiter=',', encoding="utf-8-sig")
  df.set_index(['Name'], inplace=True)
  return df.to_html()

if __name__ == "__main__":
  app.run(debug=True)
