import numpy as np
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm

from .config.precision_config import float_tse, int_tse

def compute_verbose_adf_dict(
    time_series : np.array,
    p_value_cutoff : float_tse = 0.05,
    autolag : str = 'AIC',
) -> dict:

    # 
    # move this to a separate library
    #
    def interpret_adf_results(reject_null):
        if reject_null:
            return "Reject the null hypothesis (H0). The time series is likely stationary."
        else:
            return "Fail to reject the null hypothesis (H0). The time series is likely non-stationary (has a unit root)."

    time_series = np.asarray(time_series)
    adf_result = adfuller(time_series, autolag = autolag)
    adf_statistic, p_value, lags_used = adf_result[0], adf_result[1], adf_result[2]
    reject_null = p_value <= p_value_cutoff    

    ###################
    #   Effect size   #
    ###################

    # https://chatgpt.com/g/g-p-691e4c3854dc8191a7c55a19b076e227/c/691e4c6b-8394-8327-b721-281514d34622
    
    dy = np.diff(time_series)
    Tdy = len(dy)
    k = lags_used

    # Dependent variable: Δy_t for t = k+1, …, Tdy
    dep = dy[k:]               # shape: (Tdy - k, )

    # Lagged level term: y_{t-1} aligned with dep
    y_lag = time_series[k:Tdy]           # shape: (Tdy - k, )

    # Lagged differences: Δy_{t-i} for i = 1..k
    if k > 0:
        X_lags = np.column_stack([
            dy[k - i:Tdy - i]  # each has length Tdy - k
            for i in range(1, k + 1)
        ])
    else:
        X_lags = None

    # Now build the full design matrix X (example for regression='ct')
    T = len(dep)               # effective sample size
    trend = np.arange(1, T + 1)

    X_parts = [
        np.ones(T),            # intercept
        trend,                 # deterministic trend
        y_lag                  # y_{t-1}
    ]
    if X_lags is not None:
        X_parts.append(X_lags)

    X = np.column_stack(X_parts)

    # Fit OLS to get gamma (coefficient on y_{t-1})
    model = sm.OLS(dep, X).fit()

    # In this layout: [const, trend, y_{t-1}, lagged Δy...]
    gamma_hat = model.params[2]
    phi_hat = 1 + gamma_hat

    # Half-life effect size
    if abs(phi_hat) < 1:
        half_life = np.log(0.5) / np.log(abs(phi_hat))
    else:
        half_life = np.inf

    #################
    #   Reporting   #
    #################
    
    adf_result_dict = {
        'what' : 'Augmented Dickey-Fuller Test Results',
        'ADF_statistic' : adf_statistic,
        'p_value' : p_value,
        'lags_used' : lags_used,
        'n' : adf_result[3],
        'reject_null' : reject_null,
        'interpretation' : interpret_adf_results(reject_null),
        'critical_values' : {},
        'effect_size' : {
            'gamma_hat' : gamma_hat,
            'gamma_hat_what' : 'AR(1) coefficient from regression',
            'phi_hat' : phi_hat,
            'phi_hat_what' : 'Estimated AR coefficient so the deviation from a unit root is abs(1 - phi_hat)',
            'estimated_deviation_from_unit_root' : np.abs(1. - phi_hat),
            'half_life' : half_life,
            'half_life_what' : 'Estimated half-life of shocks',
        },
    }

    for key, value in adf_result[4].items():
        adf_result_dict['critical_values'][key] =  float_tse(value)

    return adf_result_dict

