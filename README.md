# Healthcare Revenue Cycle Management (RCM) Azure Data Engineering Platform

## Project Overview

This project demonstrates the design and implementation of an end-to-end Healthcare Revenue Cycle Management (RCM) Data Engineering Platform on Microsoft Azure. The platform integrates healthcare transactional data from multiple source systems, processes it through a Medallion Architecture (Bronze, Silver, and Gold layers), and delivers curated datasets for enterprise reporting and analytics.

The primary objective of this project is to build a scalable, metadata-driven, and auditable data platform that supports healthcare reporting, operational analytics, and data quality monitoring.

---

## Business Problem

Healthcare organizations generate large volumes of data across patient encounters, claims, providers, transactions, and insurance systems. These datasets often reside in siloed operational databases, making enterprise reporting difficult and time-consuming.

Key challenges addressed by this solution:

* Data fragmentation across multiple systems
* Lack of centralized reporting datasets
* Data quality and validation issues
* Limited auditability and lineage tracking
* Manual reporting processes
* Delayed business insights

This platform centralizes healthcare data and transforms it into trusted analytical datasets for downstream reporting and decision-making.

---

## Solution Architecture

Source Systems (Azure SQL Database)

↓

Azure Data Factory (ADF)

↓

Azure Data Lake Storage Gen2 (Bronze Layer)

↓

Azure Databricks + PySpark

↓

Silver Layer (Validated & Cleansed Data)

↓

Gold Layer (Business Ready Data)

↓

Power BI Reporting & Analytics

---

## Technology Stack

### Cloud Platform

* Microsoft Azure

### Data Ingestion

* Azure Data Factory (ADF)

### Data Storage

* Azure SQL Database
* Azure Data Lake Storage Gen2 (ADLS)

### Data Processing

* Azure Databricks
* PySpark
* Delta Lake

### Reporting

* Power BI

### External Integrations

* ICD Code API
* NPI Provider API

### Monitoring & Auditing

* Audit Framework
* Metadata Driven Processing

---

## Data Flow

### Step 1: Source Data Ingestion

Healthcare transactional datasets are stored in Azure SQL Database and ingested using Azure Data Factory.

Example source tables include:

* Patients
* Providers
* Transactions
* Departments
* Insurance Claims

---

### Step 2: Bronze Layer

Raw data is landed into ADLS Gen2 Bronze containers without modification.

Objectives:

* Preserve source data
* Maintain historical records
* Enable traceability
* Support reprocessing

---

### Step 3: Silver Layer

Azure Databricks processes Bronze data and applies:

* Data cleansing
* Data standardization
* Null handling
* Data quality validation
* Business rule enforcement

Invalid records are quarantined for further review.

---

### Step 4: Gold Layer

Silver datasets are transformed into business-ready analytical datasets.

Gold layer datasets support:

* Revenue analytics
* Claims reporting
* Provider analytics
* Patient activity reporting
* Executive dashboards

---

## Metadata Driven Framework

The solution utilizes metadata-driven processing to improve scalability and maintainability.

Benefits:

* Reduced code duplication
* Dynamic pipeline execution
* Simplified onboarding of new datasets
* Improved operational efficiency

---

## Audit Framework

An enterprise audit framework is implemented to track:

* Pipeline execution status
* Source row counts
* Target row counts
* Processing timestamps
* Data quality metrics
* Exception tracking

Audit information enables operational monitoring and troubleshooting.

---

## Data Quality Rules

Sample validation rules implemented:

* Mandatory field validation
* Null value detection
* Duplicate record detection
* Invalid provider identifiers
* Invalid patient identifiers
* Transaction completeness checks

Records failing validation are flagged for review.

---

## API Integrations

### ICD Code API

Integrated external ICD API services to enrich healthcare diagnosis information.

Capabilities:

* ICD code validation
* Diagnosis enrichment
* Standardized medical coding

### NPI Provider API

Integrated National Provider Identifier (NPI) API to enrich provider information.

Capabilities:

* Provider verification
* NPI validation
* Provider metadata enrichment

---

## Repository Structure

```text
Healthcare-RCM-Azure-Data-Engineering

├── Screenshots
│   ├── Azure SQL Database
│   ├── Azure Data Factory
│   ├── ADLS Bronze Layer
│   ├── ADLS Silver Layer
│   ├── ADLS Gold Layer
│   ├── Databricks
│   └── Audit Framework

├── Project Document
│   └── Technical Design & Implementation Document

├── Databricks
│   ├── Bronze_Silver_Gold Processing
│   ├── ICD API Extraction
│   ├── NPI API Extraction
│   └── Audit Framework Scripts

├── ADF
│   └── Pipeline Definitions
```

---

## Key Features

* End-to-End Azure Data Engineering Solution
* Medallion Architecture (Bronze, Silver, Gold)
* Metadata Driven ETL Framework
* Audit Framework Implementation
* Data Quality Validation
* ICD Code API Integration
* NPI API Integration
* Enterprise Reporting Support
* Scalable Cloud Architecture

---

## Future Enhancements

* Azure Key Vault Integration
* CI/CD Deployment Pipelines
* Incremental Data Loading
* Automated Data Quality Dashboards
* Real-Time Streaming Ingestion
* Data Catalog & Lineage Tracking

---

## Author

Gopal HS

Healthcare Revenue Cycle Management (RCM) Azure Data Engineering Project

Microsoft Azure | Azure Data Factory | ADLS Gen2 | Databricks | PySpark | Delta Lake | Power BI
