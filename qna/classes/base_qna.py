from random import sample
from collections import deque

class BaseQNA():
    def __init__(
        self,
        title,
        qna_dict,
        obselete
        ):
        self.title = title
        self.qna_dict = qna_dict
        self.random_mode = True
        self.obselete = obselete

    def build_random_mode(self, size = 10):
        if not self.random_mode:
            raise NotImplementedError(f"{self.__name__}.random_mode evaluates to False")

        user_q_size = int(input(
            print(
                f"""
                Select the number of questions you'd like to be tested on for {self.title}:
                """)
            )
        )

        random_key_values = sample(
            range(0, len(self.qna_dict) -2),
            min(user_q_size, len(self.qna_dict)),
        )

        return deque(
            self.qna_dict[random_key_value]
            for random_key_value in
            random_key_values
        )