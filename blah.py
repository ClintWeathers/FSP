# apologies in advance for the verbose commenting.
# if I dont do this, I wont remember any of this later.

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
@app.route('/blah')
# tells flask to have the URL served be localhost:5000/blah
# if it were just ('/') then it'd just be localhost:5000/
# this lets you have different urls running at the same time
# EG, if you need an about page AND a contact us page AND actual content

def report():
    df = pd.read_csv('iris.csv')
	# fucking irises

    setosa = df.loc[df.species=='setosa']
    versicolor = df.loc[df.species=='versicolor']
    virginica = df.loc[df.species=='virginica']
    # this gives me a variable I can call based on the species names
    # I'll use this eventually to CSS the fugly table by species

    #blah = df.to_html()  <-- the basic html out of Pandas
    blah = df.to_html(open('./templates/blah.html', 'w')) # <- here's the magic.
	# what happens here is pandas renders the df to (in this case) blah.html and writes it to your specific location
	# in this case, it's where the render_template function will be looking for blah.html: inside the templates folder that Flask uses.
    #return render_template('blah.html') # <- the return actually gives you the results of the render_template, using the blah.html file
					# remember, Flask is looking for that blah.html file in your templates folder.
					# you can't just stick it in your app directory and expect it to work.
    return render_template('blah.html',tables=[setosa.to_html(classes='setosa'), versicolor.to_html(classes='versicolor'), virginica.to_html(classes='virginica')],
    titles = ['Setosa', 'Versicolor', 'Virginica'])

if __name__ == '__main__':  	# <- I still have no idea what in the hell this is for.
				# near as I can tell, it's looking for something called __name__ which is defined in the Flask(__name__) line
				# and if it sees that, it kicks off the app.run, in this case, with debug turned on.
				# NOTE DONT LEAVE DEBUG ON ITS BAD VERY BAD OH SO BAD JFC ITS REALLY BAD
    app.run(debug=True)
