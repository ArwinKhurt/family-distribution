📊 Family of Distributions Analysis (Python)

This project analyzes a student dataset and visualizes the family of distributions for selected numerical variables using histograms and fitted curves.

📌 Project Overview

The goal of this project is to:

Explore how real-world data behaves
Identify the distribution family of each variable
Visualize patterns using histograms
Compare actual data against theoretical distributions
📁 Dataset
File used: student_data.csv
Contains student-related information such as:
Age
Study time
Failures
Absences
Final grade (G3)
📊 Variables Analyzed

The following 10 numerical columns were used:

age
Medu (Mother's education)
Fedu (Father's education)
traveltime
studytime
failures
famrel (Family relationship)
goout
absences
G3 (Final grade)
📈 Methodology
Load dataset using pandas
Select numerical columns
Plot histograms for each variable
Apply density normalization
Fit a Normal distribution curve
Label each graph with:
Distribution family (top)
Column name (x-axis)
🧠 Distribution Analysis
Variable	Distribution Type
age	Approximately Normal
Medu	Discrete
Fedu	Discrete
traveltime	Right-skewed
studytime	Right-skewed
failures	Poisson-like
famrel	Uniform-like
goout	Normal-like
absences	Exponential (highly skewed)
G3	Approximately Normal
🖼️ Output

The program generates:

10 histograms in a 2×5 layout
Each graph includes:
Histogram (data distribution)
Fitted
