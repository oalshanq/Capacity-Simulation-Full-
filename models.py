
import pandas as pd

def load_data():
    data = {
        'Indicator': [
            'Total Population (2024)',
            'Saudi Nationals (2024)',
            'Non-Saudi Residents (2024)',
            'Annual Population Growth Rate (2024)',
            'Elderly Population (60+)',
            'Hospital Beds per 10,000 Population (2019)',
            'Physicians and Dentists per 10,000 Population (2019)',
            'Nurses including Midwives per 10,000 Population (2019)',
            'Total Number of Nurses (2023)',
            'Obesity Rate among Adults (15+ years) (2023)',
            'Overweight Individuals (15+ years) (2023)',
            'Basic Healthcare Coverage (2024)',
            'Saudi Unemployment Rate (Q4 2024)'
        ],
        'Value': [
            35300280,
            19600000,
            15700000,
            '4.7%',
            '3.81%',
            22.5,
            33.1,
            58.2,
            235461,
            '23.1%',
            '45.1%',
            '95.9%',
            '7.0%'
        ]
    }
    return pd.DataFrame(data)
