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

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/findbuyer.git
   cd findbuyer

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run the app:**
   ```bash
   python app.py

---

## 🧪 Usage

1. Enter the name of a material (e.g., `Steel`).
2. Either of the two:
   - Upload a spreadsheet of products (`.csv` or `.xlsx`)
   - Paste a product listing URL.
3. View filtered results with matched companies and emails.
4. Click “Send Email” to automatically reach out with your supply offer.

---

## 🔐 Notes

- Make sure to configure your SMTP credentials in `email_sender.py`.
- Web scraping works for specific HTML structures — may need to adapt selectors per site.

---

## 🤝 Contributing

PRs welcome! Feel free to fork the repo and suggest improvements.

---

## 📄 License

MIT License © 2025

