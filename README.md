# streamflow-realtime-project

# ⚡ Real-Time E-Commerce Data Engineering Project
End-to-end real-time data pipeline built with **Kafka, Spark Structured Streaming, Delta Lake, and Snowflake**, powering analytics dashboards in **Power BI/Tableau**.

---

## 📖 Description
This project simulates a real-time e-commerce system.  
It ingests **live order/customer events** into Kafka, processes them with **PySpark Streaming**, stores data in **Delta Lake/Snowflake** (Bronze → Silver → Gold layers), and visualizes insights in **BI dashboards**.  

Designed to demonstrate **scalable streaming data engineering architecture**.

---

## ✨ Features
- ⚡ **Real-time ingestion** using Kafka Producers  
- 🔄 **Stream processing** with Spark Structured Streaming  
- 🛢️ **Delta Lake & Snowflake storage** (Bronze → Silver → Gold)  
- 📊 **Analytics dashboards** with Power BI / Tableau  
- 🏗️ **Star & Snowflake schemas** for reporting  
- 🔒 **Checkpointing & fault tolerance** in Spark  

---

## 📂 Folder Structure


realtime-project/


├── producer/ # Kafka Producers (simulate events)
│ └── order_producer.py
│
├── consumer/ # Spark Streaming jobs
│ ├── order_consumer.py
│ └── checkpoint/ # Spark checkpoints
│
├── storage/ # Storage scripts
│ ├── delta/ # Delta Lake scripts
│ └── snowflake/ # Snowflake integration
│
├── config/ # Configuration files
│ ├── kafka_config.json
│ └── spark_config.json
│
├── dashboard/ # Dashboards
│ ├── powerbi_dashboard.pbix
│ └── tableau_dashboard.twb
│
├── docs/ # Documentation
│ ├── architecture.png
│ └── data_model.md
│
├── tests/ # Unit tests
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🛠️ Installation
```bash
# 1️⃣ Clone the repository
git clone https://github.com/<BhavanaUpadhyay1>/streamflow-realtime-project.git

# 2️⃣ Navigate into the folder
cd streamflow-realtime-project

# 3️⃣ Create & activate virtual environment
python -m venv realtime_env
realtime_env\Scripts\activate   # (Windows)
source realtime_env/bin/activate # (Mac/Linux)

# 4️⃣ Install dependencies
pip install -r requirements.txt

## 🚀 Usage

### 1️⃣ Start Kafka Services (Windows Example)
```bash
# Start Zookeeper
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

# Start Kafka broker
.\bin\windows\kafka-server-start.bat .\config\server.properties

# Create Kafka topic
.\bin\windows\kafka-topics.bat --create --topic orders --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

2️⃣ Run Producer (simulate order events)
python producer/order_producer.py

3️⃣ Run Spark Consumer (process events from Kafka)
spark-submit consumer/order_consumer.py

📊 Analytics

Bronze Layer → Raw Kafka events

Silver Layer → Cleaned & structured data

Gold Layer → Facts & Dimensions for BI

Connect Power BI/Tableau to Snowflake/Delta Lake and build KPIs like:

Sales by region

Active customers

Top products

🤝 Contributing

Fork the repo

Create a new branch: git checkout -b feature-name

Commit changes: git commit -m "Add feature"

Push: git push origin feature-name

Open Pull Request

📜 License

This project is licensed under the MIT License — see LICENSE
 for details.

📧 Contact

Author: Bhavana Upadhyay
GitHub: BhavanaUpadhyay1

Email: bhavanaupadhyay360@gmail.com

