# FDA Adverse Event Reporting System (FAERS) Analysis

## Overview
This project analyzes over 3.5 million adverse event reports from the FDA's 
public FAERS database to identify trends in drug reactions, patient outcomes, 
and reporting patterns. The analysis was conducted using Python for data 
cleaning and exploration, and Power BI for interactive dashboard visualization.

---

## Tools & Technologies
- **Python** — Data cleaning, merging, and exploratory data analysis
- **Pandas** — Data manipulation and aggregation
- **Matplotlib & Seaborn** — Data visualization
- **Power BI** — Interactive dashboard development
- **GitHub** — Version control and project documentation

---

## Data Source
- **Source:** FDA Adverse Event Reporting System (FAERS)
- **Dataset:** Q4 2025 Quarterly Data Extract
- **Records Analyzed:** 3.5 million+ adverse event reports
- **Files Used:**
  - DRUG — Drug names and administration details
  - REAC — Adverse reactions reported
  - DEMO — Patient demographics
  - OUTC — Patient outcomes
  - INDI — Drug indications

---

## Project Structure

faers-adverse-event-analysis/
├── notebooks/
│   └── FAERS_Analysis.ipynb    ← Full Python analysis
├── scripts/
│   └── faers_analysis.py       ← Clean Python scripts
├── screenshots/
│   ├── page1_outcome_overview.png
│   ├── page2_gender_analysis.png
│   ├── page3_age_group_analysis.png
│   └── page4_full_detail.png
├── output/
│   └── FAERS_Analysis.pdf      ← Full dashboard export
└── README.md

---

## Methodology
1. **Data Loading** — Loaded all 5 FAERS quarterly files using Python and pandas
2. **Data Cleaning** — Standardized column names, handled missing values, 
   and removed data quality issues such as off label use appearing in 
   reaction fields
3. **Data Merging** — Merged all 5 files on primaryid to create a 
   comprehensive dataset
4. **Filtering** — Filtered to primary suspect drugs only to ensure 
   accurate adverse event attribution
5. **Analysis** — Performed exploratory data analysis across outcomes, 
   gender, age groups, and drug reactions
6. **Visualization** — Built a 4 page interactive Power BI dashboard

---

## Key Findings
- **Hospitalization** was the most common serious adverse event outcome
- **Fatigue, nausea, and headache** were the most frequently reported reactions
- **Adult patients** accounted for the largest share of adverse event reports
- **Female patients** represented the majority of reports in this dataset
- **Off label use** appeared frequently as a reported indication reflecting 
  the widespread use of drugs outside their approved indications
- The **United States** was the top reporting country by a significant margin

---

## Dashboard Preview
### Page 1 — Outcome Overview
![Outcome Overview](screenshots/page1_outcome_overview.png)

### Page 2 — Gender Analysis
![Gender Analysis](screenshots/page2_gender_analysis.png)

### Page 3 — Age Group Analysis
![Age Group Analysis](screenshots/page3_age_group_analysis.png)

### Page 4 — Full Detail Analysis
![Full Detail](screenshots/page4_full_detail.png)

---

## Dashboard PDF
[View Full Dashboard PDF](output/FAERS_Analysis.pdf)

---

## How to Run the Analysis
1. Download the FAERS quarterly data from FDA.gov
2. Place the raw files in the `data/` folder
3. Open `notebooks/FAERS_Analysis.ipynb` in Jupyter Notebook
4. Run all cells from top to bottom
5. Exported CSV files will appear in the `output/` folder
6. Load CSV files into Power BI to recreate the dashboard

---

## Data Quality Notes
- Off label use was identified and filtered from reaction analysis
- Missing values in age and gender columns are expected in voluntary 
  reporting systems like FAERS
- Analysis was limited to primary suspect drugs only to ensure accurate 
  adverse event attribution
- Administration route blank values were filtered out of visualizations

---

## Author
**Richard Li**
- LinkedIn: [https://www.linkedin.com/in/richard-li1997/]
- Email: richardz.li@outlook.com
