# Family of Distributions Analysis (Python)

This project analyzes a student dataset and visualizes the family of distributions for selected numerical variables using histograms and fitted curves.

---

## Project Overview

The goal of this project is to:

* Explore how real-world data behaves
* Identify the distribution family of each variable
* Visualize patterns using histograms
* Compare actual data against theoretical distributions

---

## Dataset

**File used:** `student_data.csv`

Contains student-related information such as:

* Age
* Study time
* Failures
* Absences
* Final grade (G3)

---

## Variables Analyzed

The following 10 numerical columns were used:

* age
* Medu (Mother's education)
* Fedu (Father's education)
* traveltime
* studytime
* failures
* famrel (Family relationship)
* goout
* absences
* G3 (Final grade)

---

## Methodology

The script performs the following steps:

* Load dataset using pandas
* Select numerical columns
* Plot histograms for each variable
* Apply density normalization
* Fit a Normal distribution curve
* Label each graph with:

  * Distribution family (top)
  * Column name (x-axis)

---

## Distribution Analysis

| Variable   | Distribution Type    |
| ---------- | -------------------- |
| age        | Approximately Normal |
| Medu       | Discrete             |
| Fedu       | Discrete             |
| traveltime | Right-skewed         |
| studytime  | Right-skewed         |
| failures   | Poisson-like         |
| famrel     | Uniform-like         |
| goout      | Normal-like          |
| absences   | Exponential          |
| G3         | Approximately Normal |

---

## Output

The program generates:

* 10 histograms in a 2×5 layout
* Each graph includes:

  * Histogram (data distribution)
  * Fitted curve
  * Distribution label
  * Column name

---

## How to Run

Install dependencies:

```bash
pip install pandas matplotlib numpy scipy
```

Run the script:

```bash
python familydistribution.py
```

---

## Notes

* Some variables are discrete and may not follow continuous distributions exactly
* Real-world data may only approximate theoretical distributions

