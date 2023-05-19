import pandas as pd
from datetime import datetime, timedelta
from os.path import join



delta_time = 7 
date_today = datetime.today()
date_end = date_today + timedelta(days = delta_time)

date_today = date_today.strftime('%Y-%m-%d')
date_end = date_end.strftime('%Y-%m-%d')

city = 'Sao%20Paulo'
key = 'J26VKZXTXUNURA29MMGRMJKBD'
url_api = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' +
            f'{city}/{date_today}/{date_end}?unitGroup=metric&include=days&key={key}&contentType=csv')


df = pd.read_csv(url_api)
print(df.head())
