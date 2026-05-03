# 📌 Uber Eats Bangalore Restaurant Intelligence & Decision Support System

---

## 🎯 Problem Statement

Uber Eats operates a large-scale restaurant marketplace where business success depends on multiple factors such as:

- 📍 Location strategy  
- 💰 Pricing  
- 🍽️ Cuisine mix  
- ⭐ Customer ratings  
- 📱 Platform features (online ordering & table booking)  

This project builds a **SQL-driven decision support system** to answer key business questions and help stakeholders make data-driven decisions.

---

## 🧠 Objective

To analyze Uber Eats Bangalore restaurant data and develop a system that:

- Answers critical business questions using SQL  
- Uses Python for data processing  
- Displays insights in Streamlit using **tabular outputs (no charts)**  
- Mimics real-world internal analytics dashboards  

---

## 🏗️ Project Architecture

### 1️⃣ Data Processing (Python + Pandas)

- CSV data ingestion  
- Data cleaning:
  - Duplicate removal  
  - Missing value handling  
  - Rating normalization  
  - Cost standardization  
- Feature engineering:
  - Price categories (Low / Mid / Premium)  

---

### 2️⃣ Database Layer (SQL)

- Data stored in SQLite / MySQL  
- SQL-based analytics using:
  - `GROUP BY`  
  - `HAVING`  
  - `CASE WHEN`  

---

### 3️⃣ Streamlit Application

- No visualizations (pure tabular output)  

#### 📊 Dashboard Page
- Dynamic filtering (location, price, etc.)  
- SQL-based filtering queries  
- Data displayed as tables  

#### ❓ Q&A Page
- 10 predefined business questions  
- SQL-driven answers  
- Structured DataFrame output  

---

### 4️⃣ Order Data Integration

- JSON → SQL table  
- Order-level analysis  
- Combined restaurant + order insights  

---

## 📊 Key Business Questions Answered

### 📍 Location Intelligence
- Top-rated locations  
- Over-saturated areas  

### 📱 Feature Impact
- Online ordering vs ratings  
- Table booking vs ratings  

### 💰 Pricing Strategy
- Best-performing price category  
- Price vs rating analysis  

### 🍽️ Cuisine Analysis
- Most common cuisines  
- Highest-rated cuisines  
- Niche cuisine opportunities  

### ⭐ Advanced Insights
- Premium location identification  
- Best restaurants by price segment  

---

## 📈 Key Insights

- ⭐ Mid-priced restaurants achieve highest ratings  
- 📱 Online ordering improves customer ratings  
- 🍽️ Certain niche cuisines perform exceptionally well  
- 📍 Some locations are over-saturated  
- 🏆 Premium locations identified for expansion  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Database:** SQLite / MySQL  
- **App:** Streamlit  

### Libraries:
- Pandas  
- NumPy  
- sqlite3 / mysql-connector  

---

## 📂 Project Structure
Uber Eats Decision Support/
│
├── data/
│ ├── restaurants.csv
│ └── orders.json
│
├── database/
│ └── database.db
│
├── Scripts/
│ ├── clean_data.py
│ ├── create_db.py
│ ├── insert_data.py
│ └── load_orders.py
│
├── app/
│ ├── app.py
│ └── queries.py
│
└── README.md


---

## ▶️ How to Run

```bash
pip install pandas streamlit
streamlit run app/app.py

---
## 🎯 Project Deliverables

✅ Clean SQL database
✅ Python data processing scripts
✅ SQL-based analytics queries
✅ Streamlit dashboard (tabular outputs only)
✅ 10 business questions implemented
✅ GitHub-ready documentation

---

💼 Skills Demonstrated
Data Cleaning & Preprocessing
SQL Analytics
Data Engineering Basics
Dashboard Development (Streamlit)
Business Problem Solving

---

## 🚀 Conclusion

This project demonstrates how **SQL + Python + Streamlit** can be used to build a real-world decision support system, enabling businesses like Uber Eats to make smarter, data-driven decisions.






