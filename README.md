# FlexiMart Data Architecture Project

**Student Name:** Ashish Mehta
**Student ID:** BITSoM_BA_25071617
**Email:** Ashishmehta1207@gmail.com
**Date:** 2026-01-05

## Project Overview
I have built a complete end-to-end data pipeline for an e-commerce platform called FlexiMart. The project includes:
1.  **ETL Pipeline:** A Python script to extract raw dirty data, clean it, and load it into a relational database.
2.  **NoSQL Analysis:** A MongoDB schema design to handle diverse product categories like Electronics and Fashion.
3.  **Data Warehouse:** A Star Schema design (Fact and Dimension tables) to enable historical sales analysis.

## Repository Structure
├── data/                               # Input data files
├── part1-database-etl/
│   ├── etl_pipeline.py                 # Main ETL script
│   ├── schema_documentation.md         # Database documentation
│   ├── business_queries.sql            # SQL for business questions
│   └── data_quality_report.txt         # Log of cleaned data
├── part2-nosql/
│   ├── nosql_analysis.md               # Theory on RDBMS vs NoSQL
│   ├── mongodb_operations.js           # MongoDB queries
│   └── products_catalog.json           # JSON dataset
├── part3-datawarehouse/
│   ├── star_schema_design.md           # Schema design docs
│   ├── warehouse_schema.sql            # SQL to create DW tables
│   ├── warehouse_data.sql              # SQL to insert data
│   └── analytics_queries.sql           # OLAP analysis queries
└── README.md

## Technologies Used
- **Python 3.x** (pandas, sqlite3)
- **SQL** (Relational Database Design)
- **MongoDB** (Document Store concepts)

## Setup Instructions

### Part 1: ETL Pipeline
To clean the data and load the database:
```bash
# This script creates the database and loads data automatically
python part1-database-etl/etl_pipeline.py