#1173. Immediate Food Delivery I
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    n_immediate = len(delivery[delivery['order_date']==delivery['customer_pref_delivery_date']])
    perc = round(100 * n_immediate / len(delivery), 2)
    return pd.DataFrame({'immediate_percentage': [perc]})

#1907. Count Salary Categories
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cnt_low = accounts['income'].apply(lambda x: True if x<20000 else False).sum()
    cnt_high = accounts['income'].apply(lambda x: True if x>50000 else False).sum()
    cnt_med = accounts['income'].apply(lambda x: True if x>=20000 and x<=50000 else False).sum()
    return pd.DataFrame({"category": ['Low Salary', 'Average Salary', 'High Salary'],
                         "accounts_count": [cnt_low, cnt_med, cnt_high]})


#Alternative approach
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Filter accounts for each category using boolean indexing
    low_salary_count = (accounts['income'] < 20000).sum()
    average_salary_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_salary_count = (accounts['income'] > 50000).sum()

    # Create a DataFrame with the counts
    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary_count, average_salary_count, high_salary_count]})

    return result
