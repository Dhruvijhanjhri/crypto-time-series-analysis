# 🚀 Cryptocurrency Price Forecasting with Live Data Integration

🔴 **Live Dashboard:** *(https://crypto-time-series-analysis-3n4uu4ssj9s2twiuyjunqs.streamlit.app/)*
📊 Interactive Forecasting & Analytics Platform

## 📌 Project Overview

This project focuses on **cryptocurrency price forecasting** by combining:

* Historical time-series analysis
* Machine learning & deep learning models
* Real-time market data integration
* Interactive dashboard deployment

Multiple forecasting models are implemented, evaluated, and consolidated into a unified analytics-ready dataset for business intelligence tools such as **Streamlit and Power BI**.

The project follows industry-level structuring and deployment practices, making it suitable for:

* 📄 Resume projects
* 💼 Internship applications
* 📊 Real-world analytics portfolios


## 🎯 Project Objectives

* Analyze historical cryptocurrency price trends
* Build and compare multiple forecasting models
* Integrate live market data using APIs
* Create a consolidated forecast dataset
* Deploy an interactive Streamlit dashboard
* Prepare structured outputs for BI tools


## 🧠 Models Implemented

The following forecasting models were implemented and compared:

* **ARIMA** – Statistical time-series forecasting
* **SARIMA** – Seasonal time-series modeling
* **Prophet** – Trend & seasonality modeling
* **LSTM (Deep Learning)** – Sequence-based neural network forecasting
* **Live Market Integration** – Real-time price updates

Each model’s output is standardized into a common analytics format.


## 📂 Data Sources

* 📊 **Historical Data:** Kaggle Cryptocurrency Datasets
* 🔴 **Live Data:** Binance API / CoinGecko API


## 📊 Final Forecast Dataset Structure

All models are merged into a single structured dataset:

date | crypto | forecast_price | model

This unified dataset enables:

* Model comparison
* Dashboard visualization
* Business analytics integration


## 📈 Dashboard Deployment

### 🔹 Streamlit Dashboard

* Interactive crypto selection
* Historical vs forecast comparison
* Model-based filtering
* Real-time price display
* Deployed on Streamlit Cloud

### 🔹 Power BI Dashboard

* Forecast comparison visuals
* KPI tracking
* Trend insights


## 🗂 Project Structure

```
crypto-time-series-analysis/
│
├── StremlitApp/           # Streamlit dashboard app
│   ├── data/              # Final forecast dataset
│   ├── pages/             # Dashboard pages
│   ├── utils/             # Data loaders & helpers
│   └── App.py
│
├── notebooks/             # Model development notebooks
├── dashboards/            # Power BI files
├── outputs/               # Forecast results
├── requirements.txt
└── README.md
```


## ⚙️ Tech Stack

* **Programming:** Python
* **Libraries:** Pandas, NumPy, Statsmodels, Prophet, TensorFlow, Scikit-learn
* **Visualization:** Plotly, Matplotlib
* **APIs:** Binance API, CoinGecko API
* **Dashboarding:** Streamlit, Power BI
* **Deployment:** Streamlit Cloud
* **Version Control:** Git & GitHub


## 🧪 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/crypto-time-series-analysis.git
cd crypto-time-series-analysis
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
cd StremlitApp
streamlit run App.py
```


## 🏆 Key Learnings

* Advanced time-series forecasting techniques
* Deep learning for sequential financial data
* Model performance comparison
* Real-time API integration
* Dashboard deployment on cloud platforms
* Production-level project structuring







