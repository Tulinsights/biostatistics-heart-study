import pandas as pd
import statsmodels.api as sm

# Note: In a real project, you'd load the 'framingham.csv' file here.
# For now, let's look at the logic of a Logistic Regression.

def run_biostat_model(df):
    # We want to predict 'TenYearCHD' (Chronic Heart Disease)
    # Using 'age', 'sysBP' (Systolic BP), and 'cigsPerDay'
    X = df[['age', 'sysBP', 'cigsPerDay']]
    y = df['TenYearCHD']
    
    # Add a constant (intercept) for the model
    X = sm.add_constant(X)
    
    # Fit the Logistic Regression model
    model = sm.Logit(y, X).fit()
    
    # Biostatisticians care about the Summary!
    print(model.summary())
    
    # Calculate Odds Ratios
    # (Exp of the coefficients tells us how risk increases per unit)
    params = model.params
    conf = model.conf_int()
    conf['OR'] = params
    conf.columns = ['2.5%', '97.5%', 'Odds Ratio']
    print("\nOdds Ratios and 95% Confidence Intervals:")
    print(np.exp(conf))

# This is the 'gold standard' way to report clinical data results.
