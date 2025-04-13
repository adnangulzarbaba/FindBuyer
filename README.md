# FindBuyer: AI SupplyBot

FindBuyer is an intelligent B2B automation tool that helps material suppliers identify and connect with potential buyers. Simply select a material, upload a spreadsheet or provide an URL, and let the bot find relevant products, extract company contacts, and even send out personalized outreach emails — all in one workflow.

---

## 🚀 Features

- 🔍 **Smart Filtering**: Find products that use a specific material from uploaded sheets or web pages.
- 🕸️ **Web Scraping**: Extract product, company, and email data directly from supported websites.
- 📄 **Sheet Parsing**: Upload `.csv` or `.xlsx` files with product data.
- 📧 **Automated Email Outreach**: Send personalized supply offers to companies using your material.
- 📊 **Clean UI**: Simple and intuitive interface for uploads and results.

---

## 📁 Project Structure
findbuyer/
│
├── app.py                # Main Flask backend that handles routing and application logic
├── requirements.txt      # Python libraries and dependencies required to run the app
│
├── static/               # Directory containing static files like CSS for styling
│   └── css/
│       ├── styles_index.css    # Styling for the index page (upload and material selection)
│       └── styles_results.css  # Styling for the results page (filtered products and email form)
│
├── templates/            # Directory containing HTML files used for rendering pages
│   ├── index.html        # The main page where users select material and upload files
│   └── results.html      # Page that shows the filtered products and provides an email form
│
├── utils/                # Utility functions for scraping, reading files, and sending emails
│   ├── scraper.py        # Functions to scrape product data from a provided URL
│   ├── sheet_reader.py   # Functions to read and filter products from uploaded CSV/XLSX files
│   └── email_sender.py   # Functions to automate the sending of emails to filtered contacts
│
├── uploads/              # Temporary storage for files uploaded by users (e.g., product sheets)

