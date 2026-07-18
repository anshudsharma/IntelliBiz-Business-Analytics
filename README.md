<p align="center">
  <img src="assets/banner.png" alt="IntelliBiz Banner" width="100%">
</p>

<h1 align="center">
📊 IntelliBiz
</h1>

<h3 align="center">
AI-Powered Business Intelligence Platform
</h3>

<p align="center">
ETL • Business Analytics • Machine Learning • Artificial Intelligence
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)

![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?logo=streamlit&logoColor=white)

![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)

![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)

![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)

![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy&logoColor=white)

![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white)

![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?logo=google&logoColor=white)

![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&logoColor=white)

</p>

---

# 📖 About IntelliBiz

IntelliBiz is an AI-powered Business Intelligence platform developed to transform raw business data into meaningful insights through **Business Analytics, Machine Learning, and Generative AI**.

The platform provides organizations with an end-to-end analytics solution, beginning with **ETL (Extract, Transform, Load)** processes and continuing through **interactive dashboards**, **predictive analytics**, and an **AI-powered business advisor** capable of generating strategic recommendations.

Built using **Python**, **Streamlit**, **MySQL**, **SQLAlchemy**, **Scikit-learn**, and **Google Gemini AI**, IntelliBiz demonstrates how modern Business Intelligence systems can combine traditional analytics with Artificial Intelligence to support smarter decision-making.

Unlike conventional dashboards that only visualize historical data, IntelliBiz also incorporates predictive machine learning models and AI-generated insights, enabling businesses to anticipate future trends and make proactive decisions.

---

# 🎯 Project Objectives

The primary objectives of IntelliBiz are:

- Develop a complete ETL pipeline for structured business data.
- Design a centralized MySQL Data Warehouse.
- Generate interactive KPI dashboards for business monitoring.
- Analyze sales, customers, products, and reviews.
- Predict future business trends using Machine Learning.
- Generate AI-powered business recommendations using Google Gemini.
- Implement secure Authentication and Role-Based Access Control (RBAC).
- Support a scalable Multi-Tenant architecture.
- Demonstrate an end-to-end Business Intelligence workflow.

---
# ✨ Features

## 📊 Business Analytics

Transform raw business data into actionable insights through interactive dashboards and analytics.

- 📈 KPI Dashboard
- 💰 Sales Analytics
- 👥 Customer Analytics
- ⭐ Customer Review Analysis
- 📦 Product Performance Analytics
- 📊 Business Metrics Dashboard
- 📄 Automated Business Reports

---

## 🤖 Artificial Intelligence

Leverage Google's Gemini AI to generate intelligent business recommendations.

- 🧠 AI Business Advisor
- 💡 Strategic Business Recommendations
- 📈 Data-Driven Decision Support
- 📋 AI-Generated Business Reports

---

## 🧠 Machine Learning

Predict future business trends using machine learning models.

- 📉 Sales Forecasting
- 👤 Customer Segmentation
- 🚪 Customer Churn Prediction
- 📦 Category Demand Forecasting
- 📊 Predictive Analytics Dashboard

---

## 🔐 Authentication & Security

Secure access with Role-Based Access Control (RBAC).

- 🔑 User Authentication
- 👤 Session Management
- 🛡 Role-Based Access Control
- 🏢 Multi-Tenant Data Isolation

Supported Roles:

- **SUPER_ADMIN**
- **COMPANY_ADMIN**
- **EMPLOYEE**

---

## ⚙ Data Engineering

A complete ETL pipeline powers the analytics platform.

- 📥 Data Extraction
- 🔄 Data Transformation
- ✅ Data Validation
- 📤 Data Loading
- 🗄 MySQL Data Warehouse

---

## 🎨 Interactive Dashboard

A modern Streamlit interface provides a seamless analytics experience.

- Responsive Dashboard
- Interactive Charts
- Business KPIs
- AI Recommendations
- Predictive Insights
- Report Generation


# 🏗️ System Architecture

IntelliBiz follows a modular architecture that integrates Data Engineering, Business Analytics, Machine Learning, Artificial Intelligence, and an interactive web application into a single Business Intelligence platform.

```text
                         Olist E-Commerce Dataset
                                   │
                                   ▼
                         ETL Pipeline (Python)
                 Extract → Transform → Validate → Load
                                   │
                                   ▼
                        MySQL Data Warehouse
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        ▼                          ▼                          ▼
 Business Analytics          Machine Learning           AI Advisor
        │                          │                          │
        ├── KPI Dashboard          ├── Sales Forecasting     ├── Gemini AI
        ├── Sales Analysis         ├── Churn Prediction      ├── Recommendations
        ├── Customer Analysis      ├── Customer Segmentation └── Business Insights
        ├── Product Analysis       └── Demand Forecasting
        └── Review Analysis
                     │
                     ▼
             Streamlit Web Application
                     │
                     ▼
     SUPER_ADMIN • COMPANY_ADMIN • EMPLOYEE
```


# 🔄 ETL Workflow

The ETL pipeline processes raw business data before it is stored in the centralized data warehouse.

```text
          Raw Dataset
               │
               ▼
         📥 Extract
               │
               ▼
       🔄 Transform
       • Data Cleaning
       • Feature Engineering
       • Data Formatting
               │
               ▼
        ✅ Validate
       • Missing Values
       • Data Integrity
       • Schema Validation
               │
               ▼
          📤 Load
               │
               ▼
      MySQL Data Warehouse
               │
               ▼
 Analytics • ML • AI Dashboard
```


# 🔐 Role-Based Access Control (RBAC)

IntelliBiz implements Role-Based Access Control to ensure secure and controlled access across different user types.

| Module | SUPER_ADMIN | COMPANY_ADMIN | EMPLOYEE |
|---------|:-----------:|:-------------:|:--------:|
| Dashboard | ✅ | ✅ | ✅ |
| KPI Dashboard | ✅ | ✅ | ✅ |
| Sales Analytics | ✅ | ✅ | ✅ |
| Customer Analytics | ✅ | ✅ | ✅ |
| AI Advisor | ✅ | ✅ | ❌ |
| Generated Reports | ✅ | ✅ | ✅ |
| Predictive Analytics | ✅ | ✅ | ❌ |
| Data Upload Portal | ✅ | ✅ | ❌ |
| Model Manager | ✅ | ❌ | ❌ |
| ML Training Dashboard | ✅ | ❌ | ❌ |


# 🤖 Artificial Intelligence

IntelliBiz integrates **Google Gemini AI** to transform business analytics into actionable strategic recommendations.

Unlike traditional dashboards that only display historical data, IntelliBiz uses Generative AI to interpret business performance and provide intelligent recommendations.

### AI Business Advisor

The AI Advisor analyzes business metrics such as:

- Revenue
- Profit
- Orders
- Profit Margin
- Customer Trends
- Sales Performance

Using this information, Gemini AI generates:

- 📈 Business Insights
- 📊 Performance Analysis
- 💡 Strategic Recommendations
- ⚠ Potential Risks
- 🚀 Growth Opportunities

The AI Advisor enables decision-makers to move beyond descriptive analytics and adopt AI-assisted business planning.



# 🧠 Machine Learning

IntelliBiz incorporates predictive Machine Learning models to forecast business performance and customer behavior.

## Implemented Models

| Model | Purpose |
|--------|---------|
| 📈 Sales Forecasting | Predict future sales trends |
| 👥 Customer Segmentation | Group customers based on purchasing behavior |
| 🚪 Churn Prediction | Identify customers likely to stop purchasing |
| 📦 Category Demand Forecasting | Estimate future product demand |

These models enable businesses to make proactive decisions rather than relying solely on historical reports.





# 📊 Analytics Modules

IntelliBiz provides a comprehensive analytics suite for monitoring business performance.

## KPI Dashboard

Displays business-wide Key Performance Indicators including:

- Total Revenue
- Total Profit
- Total Orders
- Profit Margin

---

## Sales Analytics

Analyze sales performance through:

- Revenue Trends
- Regional Performance
- Top Products
- Sales Distribution

---

## Customer Analytics

Gain insights into customer behavior through:

- Customer Segmentation
- Geographic Distribution
- Purchase Frequency
- Customer Lifetime Value

---

## Review Analytics

Understand customer satisfaction using:

- Review Scores
- Sentiment Analysis
- Rating Distribution

---

## Generated Reports

Generate summarized business reports for management and decision-making.


# ⚙️ Installation Guide

## Prerequisites

Before running IntelliBiz, ensure the following software is installed:

- Python 3.13 or later
- MySQL Server
- Git
- Streamlit

---

## Clone the Repository

```bash
git clone https://github.com/mohdayaands/IntelliBiz.git

cd IntelliBiz
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Import the Database

Import the provided SQL file into MySQL:

```text
database/IntelliBizDatabase.sql
```

---

## Run the Application

```bash
streamlit run app/login.py
```

# 🔧 Configuration

Create a `.env` file in the project root and add the following variables:

```env
# Google Gemini API
GOOGLE_API_KEY=your_google_api_key

# MySQL Database
DB_HOST=localhost
DB_PORT=3306
DB_NAME=intellibiz_db
DB_USER=root
DB_PASSWORD=your_mysql_password
```

> **Note:** The `.env` file is excluded from version control using `.gitignore` to keep sensitive credentials secure.


---

# 👨‍💻 Developer

**Anshuman Sharma**

BCA Student
Jaypee Institute of Information Technology

### Technologies Used

- Python
- Streamlit
- MySQL
- SQLAlchemy
- Pandas
- NumPy
- Scikit-learn
- Google Gemini AI
- Git & GitHub

---

⭐ If you found this project interesting, consider giving it a star on GitHub!
