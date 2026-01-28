# biostatistics-heart-study
Analyzing cardiovascular risk factors using the Framingham Heart Study dataset. Focus on Logistic Regression and Odds Ratios.


# Project: Cardiovascular Risk Analysis
Objective: To determine the clinical predictors of coronary heart disease (CHD).

Methods:
Dataset: Framingham Heart Study (4,240 observations).
Statistical Test: Logistic Regression.
Key Metrics: Odds Ratios (OR) and P-values (significance level $\alpha = 0.05$).

Standard Biostatistical Workflow:
Data Cleaning: Handling missing values in glucose and BMI.
Descriptive Stats: Understanding the mean age and blood pressure of the cohort.
Inference: Using the Logit model to find which variables are "statistically significant."

# Data Dictionary

Variable, Description, Unit
male ,Participant gender, "1=Male,  0=Female"
age, Age at exam, Years
sysBP, Systolic Blood Pressure, mmHg
TenYearCHD, 10-year risk of CHD, Binary (Target)
