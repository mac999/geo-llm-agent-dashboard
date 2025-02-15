import pandas as pd
from datetime import datetime, timedelta
from random import randint
from django.db import models

def IoT_model_from_file():
    save_sample_iot_dataset()
    df = pd.read_csv('iot_dataset_sample.csv')
    json_dict = df.to_dict('records')
    return json_dict

def save_sample_iot_dataset():
    # Create a DataFrame
    df = pd.DataFrame({
        'time': [datetime.now() - timedelta(days=i) for i in range(10)],
        'open': [randint(100, 200) for _ in range(10)],
        'high': [randint(200, 300) for _ in range(10)],
        'low': [randint(50, 100) for _ in range(10)],
        'close': [randint(50, 250) for _ in range(10)],
    })

    # Convert the 'time' column to a string in the format 'YYYY-MM-DD'
    df['time'] = df['time'].dt.strftime('%Y-%m-%d')

    # Save the DataFrame to a CSV file
    df.to_csv('iot_dataset_sample.csv', index=False)