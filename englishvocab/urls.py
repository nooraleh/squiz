from django.urls import path
from .views import (
    test_range, test_by_last_seen,
    test_by_incorrectness, test_by_random,
    load_words,
    process_correctness, process_incorrectness
)


urlpatterns = [
    path('test_range/<int:start>/<int:end>', test_range, name='test_range'),
    path('test_by_last_seen/<int:size>', test_by_last_seen, name='test_by_last_seen'),
    path('test_by_incorrectness/<int:size>', test_by_incorrectness, name='test_by_incorrectness'),
    path('test_by_random/<int:size>', test_by_random, name='test_by_random'),
    path('load_words/', load_words, name='load_words'),
    path('process_correctness/<str:word>', process_correctness, name='process_correctness'),
    path('process_incorrectness/<str:word>', process_incorrectness, name='process_incorrectness'),  
]