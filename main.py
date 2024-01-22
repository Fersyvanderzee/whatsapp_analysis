import pandas as pd
import matplotlib.pyplot as plt
from functions import *


def analyse_data(path, name_chat, year):
    # Get data from chat
    chat_data = process_file(path)
    random_key = generate_key(24)

    # Message count img
    user_count = pd.DataFrame(count_msgs_per_user(chat_data))
    user_count.columns = ['user', 'messages_count']
    user_count = user_count.set_index('user')

    plt.figure(figsize=(8, 6))
    user_count_sorted = user_count.sort_values('messages_count', ascending=True)
    plt.barh(user_count_sorted.index, user_count_sorted['messages_count'], color='#25D366')
    plt.title('Number of messages per user')
    plt.tight_layout()
    file_name_msgs = 'messages_count_chart.png'
    plt.savefig('img/' + file_name_msgs)


    # Words count img
    words_per_user = pd.DataFrame(count_words_per_user(chat_data))
    words_per_user.columns = ['user', 'words_count']
    words_per_user = words_per_user.set_index('user')

    plt.figure(figsize=(8, 6))
    words_per_user_sorted = words_per_user.sort_values('words_count', ascending=True)
    plt.barh(words_per_user_sorted.index, words_per_user_sorted['words_count'], color='#25D366')
    plt.title('Number of words per user')
    plt.tight_layout()
    file_name_words = 'words_count_chart.png'
    plt.savefig('img/' + file_name_words)


    # Message in total
    msgs_total = count_msgs_total(chat_data)


    # Words in total
    words_total = count_words_total(chat_data)


    # Average length sentences
    avg_len_sentences = return_avg_len_sentences(chat_data)


    # Top 3 busiest days (messages)
    msg_per_day = count_msgs_per_day(chat_data)
    top_3_msgs = ""
    for i in range(3):
        date, number = msg_per_day[i][0], msg_per_day[i][1]
        emoji = return_emoji(i)
        top_3_msgs += f"{emoji} {date}: {number} messages<br>"


    # Top 3 busiest days (words)
    words_per_day = count_words_per_day(chat_data)
    top_3_words = ""
    for i in range(3):
        date, number = words_per_day[i][0], words_per_day[i][1]
        emoji = return_emoji(i)
        top_3_words += f"{emoji} {date}: {number} words<br>"


    # Longest Sentence
    longest_sentence = return_longest_sentence_words(chat_data)
    longest_sentence_user = longest_sentence[0][0]
    longest_sentence_length = longest_sentence[0][1]['length']
    longest_sentence_msg = longest_sentence[0][1]['message']


    html = f"""<!DOCTYPE html>
    <html>
        <head>
            <meta name=”robots” content=”noindex”>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
    
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <link rel="stylesheet" href="style.css">
    
            <title>Whatsapp Analysis - {name_chat}</title>
        </head>
        <body>
            <div class="container-fluid p-5 text-white text-center header">
                <div>
                    <h1>{name_chat}</h1>
                    <h2>Whatsapp Analysis - {year}</h2>
                </div>
                <div class="description">
                    <p>An analysis of all the messages that been sent between 1-1-{year} and 31-12-{year}</p>
                </div>
            </div>
    
    
            <div class="container mt-5">
                <div class="row">
                    <div class="col-sm-6">
                        <img src="img/{file_name_msgs}" class="img-fluid">
                    </div>
                    <div class="col-sm-6">
                        <img src="img/{file_name_words}" class="img-fluid">
                    </div>
                </div>
            </div>
    
    
            <div class="container p-4 mt-3">
                <div class="row">
                    <div class="col-sm-4 mx-auto text-block text-block-numbers gy-2">
                        <p>💬<br>Messages sent</p>
                        <h3>{msgs_total}</h3>
                    </div>
                    <div class="col-sm-4 mx-auto text-block text-block-numbers gy-2">
                        <p>👄<br>Words sent</p>
                        <h3>{words_total}</h3>
                    </div>
                    <div class="col-sm-4 mx-auto text-block text-block-numbers gy-2">
                        <p>📏<br>Average length messages (words)</p>
                        <h3>{avg_len_sentences}</h3>
                        </h3>
                        
                    </div>
                </div>
    
            </div>
    
            <div class="container p-4">
                <div class="row">
                    <div class="col-sm-6 mx-auto text-block text-block-dates gy-2">
                        <h3>Top 3 busiest days (messages)</h3>
                        <p>{top_3_msgs}</p>
                    </div>
                    <div class="col-sm-6 mx-auto text-block text-block-dates gy-2">
                        <h3>Top 3 busiest days (words)</h3>
                        <p>{top_3_words}</p>
                    </div>
                </div>
            </div>
    
    
            <div class="container mt-5">
                <div class="col-sm-12 mx-auto text-block text-block-dates p-10">
                    <h3>🥇<br>Longest sentence</h3>
                    <p>User:<br>
                    <span class="bigger-text">{longest_sentence_user}</span><br><br>
    
                    <p>Length in words:<br>
                    <span class="bigger-text">{longest_sentence_length}</span><br><br>
    
                    <p>Message:</p>
                    <p style="font-size: 16px;">{longest_sentence_msg}</p>
                </div>
            </div>
    
        </body>
    </html>
    
    
    
    """

    html_file = open(f'{random_key}.html', 'w', encoding='utf-8')

    html_file.write(html)

    print(f'file {random_key}.html created. Should be running on www.fersyvanderzee.nl/{random_key}.html')


path = 'bermershof603_chat/_chat_b.txt'
name_chat = 'Bermershof 603'
year = 2023

analyse_data(path, name_chat, year)
