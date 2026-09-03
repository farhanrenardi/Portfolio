# Farhan Faiq Renardi | AI & Data Engineer

Results-driven AI & Data Engineer with enterprise internship background at Telkom Indonesia and Semen Indonesia Group. Proven expertise in building containerized ELT pipelines (dbt Core, PostgreSQL), production GenAI workflows (pgvector RAG, Text-to-SQL), and full-stack web applications (FastAPI, Django REST).

[![Live Portfolio](https://img.shields.io/badge/Portfolio-Live-brightgreen?style=flat-square)](https://farhanrenardi.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/farhanfaiq)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/farhanrenardi)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:farhanfaiqrenardi@gmail.com)

---

## Featured Projects

### LogistiQ - Logistics & Supply Chain ERP with Multi-Tool AI Copilot
**Undergraduate Capstone Project** | *Jan 2025 - Sep 2025*  
**Tech Stack:** Django REST, React, PostgreSQL 16 + pgvector, Gemini AI, Docker  
**Documentation:** [Live Documentation](https://farhanrenardi.github.io/LogistiQ/) | **Repository:** [GitHub Repository](https://github.com/farhanrenardi/LogistiQ)

Enterprise-grade logistics and warehouse management ERP engineered for international furniture exporter CV Qirana Furniture (Jepara, Indonesia). Replaced fragmented paper slips and manual spreadsheets with a centralized relational database and AI-driven workflows.
- **97.8% Monolith Code Reduction:** Refactored a 3,935-line monolithic frontend into modular components, reducing the root application file to 87 lines.
- **100% SQL Mutation Block Rate:** Enforced AST-level guardrails using `sqlparse` to intercept and eliminate destructive DDL/DML statements from dynamic LLM Text-to-SQL outputs.
- **Sub-150ms pgvector RAG:** Embedded warehouse SOPs and company protocols into 768-dimensional vectors with cosine similarity search for instantaneous context retrieval.
- **>90% Gemini Vision OCR:** Automated inbound delivery order extraction to structured database records in under 5 seconds (reducing manual entry time from 15 minutes).
- Centralized management of 312 raw materials and 657 item-supplier pricing maps across 10 factory subdivisions.

---

### Worka 2.0 - Automated Labor Market ELT Platform & Self-Healing Ingestion
**Self-Project** | *May 2026 - Sep 2026*  
**Tech Stack:** Python, FastAPI, dbt Core, PostgreSQL 15, pgvector, Playwright, Gemini Flash, Docker  
**Documentation:** [Live Documentation](https://farhanrenardi.github.io/-worka-jobmapper_and_scraper/) | **Repository:** [GitHub Repository](https://github.com/farhanrenardi/-worka-jobmapper_and_scraper)

End-to-end containerized ELT data platform collecting, modeling, enriching, and serving regional tech labor market intelligence at scale.
- **Kimball Star Schema via dbt Core:** Engineered modular transformation layers structuring raw postings into analytics-ready marts (`fact_job_postings`, `dim_companies`, `dim_skills`, `dim_locations`).
- **Two-Tier Self-Healing Scraper:** Headless Playwright scraper cascading to Gemini Flash vision/DOM extraction upon layout drift, preventing pipeline breakage.
- **pgvector Hybrid Matching:** Implemented dual-criteria candidate matching combining 60% semantic cosine embedding similarity with 40% exact skill taxonomy overlap.
- **High-Throughput FastAPI v2 REST API:** Built asynchronous endpoints with token-based pagination and query optimization for client consumption.

---

### Agentic DataOps - Autonomous Self-Healing ETL & Data Quality Guardian
**Capstone Project - IBM SkillsBuild** | *Aug 2026 - Sep 2026*  
**Tech Stack:** Langflow 1.0.19, Google Generative AI (Gemini Flash), Docker, PostgreSQL 16, PyArrow, Pandas  

Autonomous self-healing ETL and data quality guardian pipeline orchestrating untrusted tabular data remediation and governance.
- **Visual Multi-Stage DAG in Langflow:** Engineered automated pipeline stages covering raw ingestion, AI profiling, code extraction, and audit generation.
- **Self-Healing Dynamic Pandas Synthesis:** Leveraged Gemini Flash to detect schema drift, encoding corruption, and Excel date serial offsets, dynamically generating executable remediation scripts.
- **Vectorized High-Throughput Processing:** Processed 500k-row datasets safely in memory chunks (`chunksize=50,000`) via PyArrow and Pandas.
- **Automated PostgreSQL Schema DDL:** Dynamically synthesized clean, strongly-typed DDL schemas ready for production relational ingestion.

---

### Medical Image Classification using Deep Learning
**Open-Source** | *Jan 2025 - Sep 2025*  
**Tech Stack:** Transfer Learning (EfficientNetB3), TensorFlow, Keras, Hugging Face Spaces  
**Live Demo:** [Hugging Face Spaces Demo](https://huggingface.co/spaces/hunsolooo/Male_Pattern_Baldness)

Convolutional neural network classification system classifying stages of Male Pattern Baldness for clinical decision assistance.
- **Transfer Learning with EfficientNetB3:** Fine-tuned EfficientNetB3 architecture on augmented clinical image data, achieving **88% test accuracy**.
- Resolved dataset imbalance through geometric and photometric augmentations with hyperparameter optimization.
- Evaluated model convergence using accuracy, precision-recall curves, and multi-class confusion matrices.
- Deployed interactive live inference application with Gradio on Hugging Face Spaces.

---

### Enterprise Analytics & Decision Support
**Enterprise Impact Projects** | *Dec 2023 - May 2026*  

- **Telkom Indonesia - Employee Profile Match-Up Optimization (Nov 2025 - May 2026):**
  - Re-engineered and optimized an employee-role matching classification pipeline for the HCSP Division using **Logistic Regression (scikit-learn)**.
  - Simplified feature space and improved model interpretability for HR leadership while preserving high predictive fidelity across talent competency profiles.
  - Delivered comprehensive technical documentation and model evaluation metrics for internal system continuity.

- **Semen Indonesia Group - Sourcing & Pricing Monitoring Dashboards (Dec 2023 - Feb 2024):**
  - Designed and deployed interactive **Power BI** dashboards tracking pricing trends, regional market margins, and raw material sourcing across 45 operating territories.
  - Cut weekly executive reporting preparation time by 60% for the Pricing and Margin Management Department.
  - Built Python and Excel automated preprocessing routines for data cleansing and territory KPI tracking.

---

## Professional Experience

- **Telkom Indonesia** | Data Scientist Intern  
  *November 2025 - May 2026*  
  - Re-engineered employee talent profiling models using Scikit-learn Logistic Regression, boosting interpretability for HR decision-makers.
  - Built automated data ingestion and web scraping pipelines, processing large-scale talent datasets for internal analytics.
  - Conducted exploratory data analysis and delivered technical documentation supporting human capital strategy.

- **Semen Indonesia Group** | Data Analyst Intern  
  *December 2023 - February 2024*  
  - Developed interactive Power BI dashboards monitoring pricing, raw material sourcing, and margin trends across 45 territories.
  - Automated weekly executive reporting workflows using Python and Excel, cutting preparation overhead by 60%.
  - Partnered with Pricing and Margin Management teams to deliver quantitative market competitiveness insights.

---

## Education

- **Diponegoro University**  
  Bachelor of Engineering - Industrial Engineering  
  *September 2021 - September 2025*

---

## Technical Skills

- **Programming Languages:** Python, SQL, JavaScript, Bash
- **Data Engineering & Databases:** PostgreSQL, pgvector, dbt Core, PyArrow, Pandas, SQLite, MySQL
- **LLM Orchestration & AI Agents:** Google GenAI / Gemini API, Langflow, n8n, Prompt Engineering
- **Backend & Data Ingestion:** FastAPI, Django REST Framework, Playwright, BeautifulSoup
- **Machine Learning & Deep Learning:** Scikit-learn, TensorFlow, Keras, Transfer Learning, Model Interpretability
- **Business Intelligence & Analytics:** Power BI, Microsoft Excel, Tableau, Matplotlib
- **DevOps & Tools:** Docker, Docker Compose, Git, GitHub, Linux / Shell

---

## Contact

- **Location:** Jakarta, Indonesia
- **Phone:** +62 822-6652-0790
- **Email:** farhanfaiqrenardi@gmail.com
- **LinkedIn:** [linkedin.com/in/farhanfaiq](https://www.linkedin.com/in/farhanfaiq)
- **GitHub:** [github.com/farhanrenardi](https://github.com/farhanrenardi)
- **Portfolio:** [farhanrenardi.github.io/Portfolio](https://farhanrenardi.github.io/Portfolio/)
