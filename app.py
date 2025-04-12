from flask import Flask, render_template, request
from utils.sheet_reader import read_sheet
from utils.scraper import scrape_website
from utils.email_sender import send_emails

app = Flask(__name__)


# Home route - Upload or provide a website URL
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if user uploaded a file or provided a website URL
        file = request.files.get('file')
        url = request.form.get('url')

        if file:
            # Process the uploaded file
            file_path = f'uploads/{file.filename}'
            file.save(file_path)
            products_data = read_sheet(file_path)  # Read the sheet (Excel/CSV)
        elif url:
            # Process the URL to scrape data
            products_data = scrape_website(url)

        # Filter products based on material
        material = request.form.get('material')  # Material user selects
        filtered_data = filter_products_by_material(products_data, material)

        # Send emails to the filtered companies
        send_emails(filtered_data)

        # Show the filtered products and emails
        return render_template('results.html', products=filtered_data)

    return render_template('index.html')


# Function to filter products by material
def filter_products_by_material(products_data, material):
    return [
        product for product in products_data
        if material.lower() in product['material'].lower()
    ]


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
