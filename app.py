from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/products')
def products():
    return render_template('product/index.html')

@app.route('/products/<string:id>')
def product(id):
    return render_template('product/show.html', product=id)

@app.route('/news')
def news():
    return render_template('news/index.html')

@app.route('/news/<string:id>')
def news_show(id):
    return render_template('news/show.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts/index.html')

@app.route('/about')
def about():
    return render_template('about/index.html')
