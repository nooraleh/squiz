import csv
import datetime
import random

from django.http.response import HttpResponse
from django.shortcuts import render
from django.db import connection

from .models import VocabWord

def home(request):
    return render(request, 'englishvocab/home.html', {})

def test_range(request, start, end):
    all_words = VocabWord.objects.all()

    start, end = max(0, start), min(len(all_words), end)
    word_range = all_words[start:end]
    return render(request, 'englishvocab/test.html', {'words': word_range})


def test_by_last_seen(request, size):
    words_by_last_seen = list(VocabWord.objects.order_by('last_seen')[:size])
    return render(request, 'englishvocab/test.html', {'words': words_by_last_seen})


def test_by_incorrectness(request, size):
    words_by_incorrect = list(VocabWord.objects.order_by('correct_count')[:size])
    return render(request, 'englishvocab/test.html', {'words': words_by_incorrect})


def test_by_random(request, size):
    words_by_random = random.sample(list(VocabWord.objects.all()), size)
    return render(request, 'englishvocab/test.html', {'words': words_by_random})


def load_words(request):
    new_word_counter = 0

    with open(r'englishvocab\new_words.csv', 'r') as csvfile:
        word_reader = csv.DictReader(csvfile, lineterminator='\n')

        for word_record in word_reader:
            if word_record['word'] not in {word.word for word in VocabWord.objects.all()}:
                word_info = {
                    'word': word_record['word'],
                    'definition': word_record['definition'],
                    'word_class': word_record['word_class'],
                    'creation_date': datetime.datetime.now(),
                    'last_seen': datetime.datetime.now(),
                    'seen_count': 0,
                    'correct_count': 0,
                }

                new_word_counter += 1

                create_new_word(**word_info)
                update_csv()

        new_words_found = bool(new_word_counter)
        if new_words_found:
            message = f"Success: {new_word_counter} New Word{'s' if new_word_counter > 1 else ''} Found"
        else:
            message = f"No New Words Found!"
                
    return render(request, 'englishvocab/load_words.html', {
        'message': message,
        })


def process_correctness(request, word):
    if request.method == 'POST':
        word_to_process = VocabWord.objects.get(word=word)
        word_to_process.seen_count += 1
        word_to_process.correct_count += 1
        word_to_process.last_seen = datetime.datetime.now()
        word_to_process.save()
        message = f"Great stuff!"

        update_csv()
    
    return render(request, 'englishvocab/question_result.html', {
        'word_to_process': word_to_process,
        'message': message,
        })


def process_incorrectness(request, word):
    if request.method == 'POST':
        word_to_process = VocabWord.objects.get(word=word)
        word_to_process.seen_count += 1
        word_to_process.last_seen = datetime.datetime.now()
        word_to_process.save()
        message = f"You'll get it the next time!"

        update_csv()

    return render(request, 'englishvocab/question_result.html', {
        'word_to_process': word_to_process,
        'message': message,
        })

def create_new_word(**kwargs):
    VocabWord.objects.create(**kwargs)


def update_csv():
    counter = 0

    with open(r'englishvocab\VocabWord_storage.csv', 'w') as f:
        writer = csv.writer(f,
            ['word','definition','word_class','creation_date','last_seen','seen_count','correct_count',],
            lineterminator='\n',
        )
        for record in VocabWord.objects.all().values_list(
            'word','definition','word_class','creation_date','last_seen','seen_count','correct_count',
            ):
            counter += 1
            writer.writerow(record)

def clear_input_csv():
    """
    Purpose: Clear out input csv `new_words.csv` once words have been
    added to the database.
    """
    pass