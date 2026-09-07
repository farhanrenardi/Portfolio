# Farhan Faiq Renardi | AI & Data Engineer

AI & Data Engineer building data pipelines, machine learning models, and production GenAI workflows across telecommunications and manufacturing enterprise environments. Designs containerized ELT systems (dbt Core, PostgreSQL), production vector search (pgvector RAG, Text-to-SQL), and backend services deployed via FastAPI and Docker.

[![Live Portfolio](https://img.shields.io/badge/Portfolio-Live-brightgreen?style=flat-square)](https://farhanrenardi.github.io/Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/farhanfaiq)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/farhanrenardi)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:farhanfaiqrenardi@gmail.com)

---

## Featured Projects

### LogistiQ - Logistics & Inventory Management System
**Undergraduate Capstone Project** | *Jan 2025 - Sep 2025*  
**Tech Stack:** Django REST, React, PostgreSQL 16 + pgvector, Gemini AI, Docker  
**Documentation:** [Live Documentation](https://farhanrenardi.github.io/LogistiQ/) | **Repository:** [GitHub Repository](https://github.com/farhanrenardi/LogistiQ)

Web-based logistics and inventory management ERP built for CV Qirana Furniture (Jepara, Indonesia) to replace paper records and fragmented spreadsheets with a centralized relational database.
- **Full-Stack Logistics ERP with RBAC:** Built an 8-role access control system managing 312 materials, 18 suppliers, and 657 item-supplier pricing maps across 10 factory subdivisions.
- **Multimodal Delivery Order OCR:** Automated supplier delivery slip extraction using Gemini Vision, cutting processing time from 15 minutes to under 5 seconds with >90% extraction accuracy.
- **AST-Guarded Text-to-SQL & RAG Assistant:** Parsed LLM-generated SQL queries with `sqlparse` to block destructive DML/DDL statements at the AST level, paired with sub-150ms pgvector cosine search over warehouse SOPs.
- **Monolith Code Reduction:** Refactored a 3,935-line monolithic frontend into modular components, reducing the root application file to 87 lines.
- **Testing & Deployment:** Containerized with Docker and verified system stability through 67 automated unit and end-to-end integration tests (100% pass rate).

---

### Worka - Job Intelligence Platform
**Personal Project** | *May 2026 - Sep 2026*  
**Tech Stack:** Python, FastAPI, dbt Core, PostgreSQL 15, pgvector, Playwright, Gemini Flash, Docker  
**Documentation:** [Live Documentation](https://farhanrenardi.github.io/-worka-jobmapper_and_scraper/) | **Repository:** [GitHub Repository](https://github.com/farhanrenardi/-worka-jobmapper_and_scraper)

End-to-end containerized ELT data platform collecting, standardizing, and serving regional tech labor market intelligence across multiple hiring portals.
- **Kimball Star Schema via dbt Core:** Ingested 2,000+ job postings from 5 portals into structured data marts (`fact_job_postings`, `dim_companies`, `dim_skills`, `dim_locations`).
- **Two-Tier Self-Healing Scraper:** Headless Playwright scraper with automated Gemini Flash visual and DOM extraction fallback when portal layouts change.
- **pgvector Skill Matcher:** Implemented dual-criteria candidate matching combining 60% semantic cosine embedding similarity with 40% exact skill taxonomy overlap.
- **Analytics API:** Built asynchronous FastAPI endpoints serving hiring market trends, salary benchmarks, and tech-stack demand metrics.

---

### Agentic DataOps - Autonomous Self-Healing ETL & Data Quality Guardian
**Capstone Project - IBM SkillsBuild** | *Aug 2026 - Sep 2026*  
**Tech Stack:** Langflow 1.0.19, Google Generative AI (Gemini Flash), Docker, PostgreSQL 16, PyArrow, Pandas  

Autonomous self-healing ETL and data quality guardian pipeline orchestrating untrusted tabular data remediation and governance.
- **Visual Multi-Stage DAG in Langflow:** Engineered automated pipeline stages covering raw ingestion, AI profiling, code extraction, and audit generation.
- **Dynamic Pandas Synthesis:** Prompted Gemini Flash to detect schema drift, encoding corruption, and Excel date serial offsets, dynamically generating executable remediation scripts.
- **Vectorized High-Throughput Processing:** Processed 500k-row datasets safely in memory chunks (`chunksize=50,000`) using PyArrow and Pandas.
- **Automated PostgreSQL Schema DDL:** Dynamically synthesized clean, strongly-typed DDL schemas ready for production relational ingestion.

---

### Medical Image Classification using Deep Learning
**Open-Source** | *Jan 2025 - Sep 2025*  
**Tech Stack:** Transfer Learning (EfficientNetB3), TensorFlow, Keras, Hugging Face Spaces  
**Live Demo:** [Hugging Face Spaces Demo](https://huggingface.co/spaces/hunsolooo/Male_Pattern_Baldness)

Convolutional neural network classification system classifying stages of Male Pattern Baldness for clinical decision assistance.
- **Transfer Learning with EfficientNetB3:** Fine-tuned EfficientNetB3 architecture on augmented clinical image data, achieving 88% test accuracy.
- **Data Augmentation:** Resolved dataset imbalance through geometric and photometric augmentations with hyperparameter optimization.
- **Live Deployment:** Deployed an interactive inference application with Gradio on Hugging Face Spaces.

---

## Professional Experience

### Data Scientist Intern | Telkom Indonesia (HCSP Division)
*November 2025 - May 2026*
- Built automated web scraping pipelines across 770 sources using Playwright and BeautifulSoup, orchestrated with n8n, saving 100+ manual hours.
- Raised dataset integrity across legacy HR systems to >90% by cleaning and validating 1,600+ employee records using Pandas.
- Trained an employee profile matchup model using Scikit-learn Logistic Regression to support candidate matching with high interpretability for HR leadership.

### Data Analyst Intern | Semen Indonesia Group (Pricing & Margin Management)
*December 2023 - February 2024*
- Cut weekly executive reporting preparation time by 60% by automating data aggregation and reporting workflows in Power BI.
- Designed and deployed 2 interactive Power BI dashboards tracking pricing trends, regional market margins, and raw material sourcing across 45 operating territories.
- Delivered weekly profitability and cost-trend analyses across operational datasets using Python and Excel to guide regional pricing decisions.

---

## Education

**Diponegoro University**  
Bachelor of Engineering - Industrial Engineering  
*September 2021 - September 2025*

---

## Certifications

- **Build an AI Agent** - IBM SkillsBuild
- **Data Engineering and AI Tracks** - Google Cloud Skills Boost

---

## Technical Skills

- **Programming Languages:** Python, SQL, JavaScript, Bash
- **Data Engineering & Databases:** PostgreSQL, pgvector, dbt Core, PyArrow, Pandas, SQLite, MySQL
- **AI & Machine Learning:** Gemini API / Google GenAI SDK, Langflow, Scikit-learn, TensorFlow, Keras, RAG, Text-to-SQL
- **Backend & Data Ingestion:** FastAPI, Django REST Framework, Playwright, BeautifulSoup, n8n
- **Business Intelligence & Analytics:** Power BI, Microsoft Excel, Tableau
- **DevOps & Tools:** Docker, Docker Compose, Git, GitHub, Linux / Shell

---

## Contact

- **Location:** Jakarta, Indonesia
- **Phone:** +62 822-6652-0790
- **Email:** farhanfaiqrenardi@gmail.com
- **LinkedIn:** [linkedin.com/in/farhanfaiq](https://www.linkedin.com/in/farhanfaiq)
- **GitHub:** [github.com/farhanrenardi](https://github.com/farhanrenardi)
- **Portfolio:** [farhanrenardi.github.io/Portfolio](https://farhanrenardi.github.io/Portfolio/)
