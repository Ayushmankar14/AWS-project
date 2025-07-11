# 🧹 LocalGlueETL – Simulated AWS Glue Data Pipeline (CSV Processor)

This project simulates a complete **AWS Glue-style ETL pipeline** — but entirely on your **local system** using Python, shell scripting, folders, and Windows Task Scheduler. It's designed to behave like a real production pipeline with:

✅ Automated file detection  
✅ Data filtering/transformation  
✅ Logging, archiving, retry mechanism  
✅ Optional Streamlit UI for data preview

---

## 📦 Features

- 📥 Reads raw `.csv` files from `input/`
- 🧹 Filters rows based on business rule (`sales > 600`)
- 🧾 Logs row counts, errors, and activity to `logs/`
- 🗃 Archives the original CSV to `archive/` with timestamps
- 📤 Saves cleaned output to `output/`
- 🔁 Retries processing if failures occur
- ⏰ Automatically runs via Windows Task Scheduler (like AWS Glue Trigger)
- 🖥️ [Optional] Streamlit app for file upload and interactive preview

---

## 🧠 Why This Project?

> “I wanted to build a **hands-on simulation of AWS Glue**, without using cloud services — just local tools, folders, automation, and real ETL logic.”

This project shows:
- Your understanding of **ETL principles (Extract, Transform, Load)**
- Ability to design **automated pipelines**
- Comfort with **logging, file handling, scheduling, and UI**

---

## 📁 Project Structure

