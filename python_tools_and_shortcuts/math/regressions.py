import pandas as pd
import statsmodels.formula.api as smf

def regression_first_order(x, y):
    df = pd.DataFrame({'x' : x, 'y' : y})
    formula = 'y ~ x'
    model = smf.ols(formula = formula, data = df).fit()
    R_adj = model.rsquared_adj
    df['y_predicted'] = model.predict(df['x'])
    return df, R_adj
