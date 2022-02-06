from abc import ABC, abstractmethod
from random import sample
from collections import deque

class BaseQNA():
    def __init__(
        self,
        title,
        chapter_info,
        qna_dict,
        obselete
        ):
        self.title = title
        self.chapter_info = chapter_info
        self.qna_dict = qna_dict
        self.random_mode = True
        self.chapter_mode = bool(chapter_info)
        self.obselete = obselete

    def build_random_mode(self, size = 10):
        if not self.random_mode:
            raise NotImplementedError(f"{self.__name__}.random_mode evaluates to False")

        random_key_values = sample(range(0, len(self.qna_dict) -2), size)

        return deque(
            self.qna_dict[random_key_value]
            for random_key_value in
            random_key_values
        )

    def build_chapter_mode(self, user_chapter = 10):
        return deque(
            self.qna_dict.get(i)
            for i in range(*self.chapter_info[user_chapter][1])
            if self.qna_dict.get(i) is not None
        )