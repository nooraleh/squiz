from django.contrib import admin
from django.urls import path, include
# from englishvocab.views import (
#     home,
#     test_range, test_by_last_seen,
#     test_by_incorrectness, test_by_random,
#     load_words,
#     process_correctness, process_incorrectness
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('englishvocab/', include('englishvocab.urls')),
    # path('', englishvocab.views.home, name='home'),
#     path('test_range/<int:start>/<int:end>', englishvocab.views.test_range, name='test_range'),
#     path('test_by_last_seen/<int:size>', englishvocab.views.test_by_last_seen, name='test_by_last_seen'),
#     path('test_by_incorrectness/<int:size>', englishvocab.views.test_by_incorrectness, name='test_by_incorrectness'),
#     path('test_by_random/<int:size>', englishvocab.views.test_by_random, name='test_by_random'),
#     path('load_words/', englishvocab.views.load_words, name='load_words'),
#     path('process_correctness/<str:word>', englishvocab.views.process_correctness, name='process_correctness'),
#     path('process_incorrectness/<str:word>', englishvocab.views.process_incorrectness, name='process_incorrectness'),
]