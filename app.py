from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)

with open('dinosaurs.csv', 'r') as csvfile:
   data = csv.DictReader(csvfile)
   dinosaurs = {row['slug']:{'name':row['name'], 'description':row['description'], 'image':row['image'], 'image-credit':row['image-credit'], 'source-url':row['source-url'], 'source-credit':row['source-credit']} for row in data}

with open ('faq.csv', 'r') as csvfile:
   faq = csv.Reader(csvfile)
   faq_list = list(faq)

@app.route('/')
@app.route('/dino')
@app.route('/dino/<dino>')
def index(dino=None):
   print(dino)
   if dino and dino in dinosaurs.keys():
      dinosaur = dinosaurs [dino]
      return render_template('dino.html', dinosaurs=dinosaurs)
   else:
      return render_template('index.html', dinosaurs=dinosaurs)
    


@app.route('/about')
def about():
   return render_template('about.html')


@app.route('/faq')
def faq(faq=None):
   return render_template('faq.html', faq_list=faq_list)

if __name__ == "__main__":
   app.run(debug = True)