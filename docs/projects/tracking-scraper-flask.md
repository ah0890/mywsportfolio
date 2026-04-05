# 📦 BuffaloEx Tracking Scraper

A Flask-based web scraping API that fetches tracking details from BuffaloEx and generates a downloadable PDF report.

---
## 🔗 Repository Link

👉 https://github.com/ahaulakh0890/buffalotracking

---
## 🚀 Features

🔍 Track shipments using tracking number\
  🤖 Automated scraping using Selenium\
  📄 Generate professional PDF reports\
  ⚡ Fast API response\
  🌐 Headless browser execution (server-friendly)

---

## 🛠️ Tech Stack

* Python
* Flask
* Selenium
* ReportLab

---

## 📂 Project Structure

```
project/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Chrome & Chromedriver

Make sure you have:

* Google Chrome installed
* Chromedriver installed and path configured

Example path (Linux):

```
/usr/bin/chromedriver
```

---

## ▶️ Run the Application

```bash
python app.py
```

Server will start at:

```
http://localhost:5000
```

---

## 📡 API Usage

### Endpoint:

```
GET /track?number=TRACKING_NUMBER
```

### Example:

```
http://localhost:5000/track?number=ABC123456
```

---

## 📄 Output

* Returns a downloadable PDF file containing:

  * Basic shipment info
  * Sign status
  * Logistics records

---

## ⚠️ Notes

* This project uses Selenium, so it may be slower than direct API scraping
* Works best in server environments like Linux / PythonAnywhere
* Ensure Chromedriver version matches your Chrome version

---


## 👨‍💻 Author

**Amjad Hassan**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
