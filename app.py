import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

sys.setrecursionlimit(2000)
app = Flask(__name__)


client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts



@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    print("\n\n\n")
    #print(mars)
    #mars = {'news_title': "Mars Now", 'news_paragraph': "The giant canopy that helped land Perseverance on Mars was tested here on Earth at NASA’s Wallops Flight Facility in Virginia.tif_full.jpg'}]}
    db.mars_facts.insert_one(mars)
    return "Some scraped data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)