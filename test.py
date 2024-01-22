from functions import *
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'vriendenweekend_chat/chat_2023.txt'
chat_data = process_file(file_path)

hours_count = count_hours(chat_data)

hours = pd.DataFrame(hours_count)
hours.columns = ['hour', 'count']
hours = hours.set_index('hour')

plt.figure(figsize=(8, 6))
hours_sorted = hours.sort_values('hour', ascending=True)
plt.bar(hours_sorted.index, hours_sorted['count'], color='#25D366')
plt.title('Messages sent per hour')
plt.tight_layout()
file_name_msgs = 'hours.png'
plt.savefig('img/' + file_name_msgs)

fav_hour = int(hours_count[0][0])

print(f"Most messages were sent between {fav_hour}:00 and {fav_hour + 1}:00.")
