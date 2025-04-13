import os
from flask import Flask, render_template, request
from utils.sheet_reader import read_sheet
from utils.scraper import scrape_website
from utils.email_sender import send_emails

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    material = request.form.get('material')
    url = request.form.get('url')
    file = request.files.get('sheet')

    results = []
    emails_sent = False  # initialize

    if file and file.filename != '':
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        results = read_sheet(path, material)
    elif url:
        results = scrape_website(url, material)

    if 'send_emails' in request.form:
        emails_sent = send_emails(results, material)  # capture returned value

    return render_template(
        'results.html',
        material=material,
        products=results,
        emails_sent=emails_sent
    )


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
