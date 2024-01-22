from datetime import datetime
import string
import random
import re


def process_file(file_path):
    result_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = file.read()

    pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')

    matches = pattern.findall(messages)

    for match in matches:
        date_time = match[0].split(', ')
        date = date_time[0]
        time = date_time[1]
        sender = match[1]
        message = match[2]
        result_list.append([date, time, sender, message])

    return result_list



def count_msgs_per_user(chat_data: list):
    user_entries = []
    user_freq = {}

    for entry in chat_data:
        user = entry[2]
        user_entries.append(user)

    for user in user_entries:
        user_freq[user] = user_freq.get(user, 0) + 1

    return sorted(user_freq.items(), key=lambda item: item[1], reverse=True)


def count_words_per_user(chat_data: list):
    total_word_counts = {}
    for entry in chat_data:
        user = entry[2]
        msg = entry[3]
        msg = msg.lower()
        words = msg.split()

        total_word_counts[user] = total_word_counts.get(user, 0) + len(words)

    return sorted(total_word_counts.items(), key=lambda item: item[1], reverse=True)


def count_words_total(chat_data: list):
    total_words_used = 0

    for entry in chat_data:
        msg = entry[3]
        msg = msg.lower()
        words = msg.split()

        total_words_used += len(words)

    return total_words_used


def return_longest_sentence_words(chat_data: list):
    len_sentences = {}

    for entry in chat_data:

        user = entry[2]
        msg = entry[3]

        msg_lower = msg.lower()

        word_count = len(msg_lower.split())

        if user not in len_sentences or word_count > len_sentences[user]['length']:
            len_sentences[user] = {'length': word_count, 'message': msg, 'user': user}

    sorted_len_sentences = sorted(len_sentences.items(), key=lambda item: item[1]['length'], reverse=True)

    return sorted_len_sentences


def return_longest_sentence_chars(chat_data: list):
    len_sentences = {}

    for entry in chat_data:

        user = entry[2]
        msg = entry[3]

        msg_lower = msg.lower()

        char_count = len(msg_lower)

        if user not in len_sentences or char_count > len_sentences[user]['length']:
            len_sentences[user] = {'length': char_count, 'message': msg, 'user': user}

    sorted_len_sentences = sorted(len_sentences.items(), key=lambda item: item[1]['length'], reverse=True)

    return sorted_len_sentences


def return_avg_len_sentences(chat_data: list):
    sentences = []

    for entry in chat_data:
        msg = entry[3]

        msg_lower = msg.lower()
        msg_split = msg_lower.split()

        word_count_per_sentence = len(msg_split)

        sentences.append(word_count_per_sentence)

    avg_sentences = sum(sentences) / len(sentences)

    return round(avg_sentences, 2)



def count_msgs_per_day(chat_data: list):
    message_count_by_day = {}

    for entry in chat_data:
        try:
            date = entry[0]
            date_obj = datetime.strptime(date, "%d/%m/%Y")
            day = date_obj.strftime("%d/%m/%Y")

            message_count_by_day[day] = message_count_by_day.get(day, 0) + 1

            sorted_msg_count_by_day = sorted(message_count_by_day.items(), key=lambda item: item[1], reverse=True)
        except ValueError:
            print('Found incorrect format.')
    return sorted_msg_count_by_day


def count_words_per_day(chat_data: list):
    word_count_by_day = {}

    for entry in chat_data:
        date = entry[0]
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        day = date_obj.strftime("%d/%m/%Y")
        msg = entry[3]
        msg = msg.lower()
        msg_split = msg.split()

        for word in msg_split:
            word_count_by_day[day] = word_count_by_day.get(day, 0) + 1

        sorted_word_count_by_day = sorted(word_count_by_day.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_count_by_day


def count_msgs_total(chat_data: list):
    msg_count = len(chat_data)

    return msg_count


def return_emoji(i):
    i += 1
    match i:
        case 1:
            emoji = '🥇'
        case 2:
            emoji = '🥈'
        case 3:
            emoji = '🥉'
        case _:
            emoji = ''
    return emoji


def generate_key(length: int):
    existing_keys = open('keys.txt', 'r')

    random_source = string.ascii_lowercase + string.digits
    key = ''
    for i in range(length):
        key += random.choice(random_source)

    return key


def count_hours(chat_data):
    hour_count = {}
    for entry in chat_data:
        time = entry[1]
        hour = time.split(':')[0]
        hour_count[hour] = hour_count.get(hour, 0) + 1

    sorted_hour_count = sorted(hour_count.items(), key=lambda item: item[1], reverse=True)

    return sorted_hour_count
