from abc import ABC, abstractclassmethod, abstractmethod
from qna_mapping import qna_mapping as all_qna_options
from collections import deque
from sys import exit
from random import sample

class BaseQNA(ABC):

    all_qna_options = all_qna_options
    VALID_QNA = [all_qna_options.keys()]

    def __init__(self):
        self.mode = None # mode is either chapter mode (1) or random (2)
        self.specific_qna = None
        self.quiz = deque()
        self.user_qna = None

    def __call__(self):
        self.run_logic()

    def get_random_mode(self):
        # TODO: I'm pretty sure we can implement this up here
        pass

    def get_chapter_mode(self):
        # TODO: You may be able to implement this up here too
        pass

    def get_display_page1(self):
        # TODO: This should dynamically format and produce the menu based on the class variables

        for index, mapping in all_qna_options.items():
            print(f"{index}: {mapping[0]}")

        
        self.user_qna = all_qna_options.get(
            int(input("Please select the resource you'd like to be quized on: "))
        , -1000)

        if self.user_qna == -1000:
            exit("Invalid Resource Option")

    def get_display_page2(self):
        """
        This function will ask whether the user wants to be tested in random mode
        or chapter mode, self.mode will be modified
        """
        user_mode = int(input(
            print(
                f"""
                Select the mode you'd like to be tested on for {self.user_qna[0]}:

                1: Chapter
                2: Random
                """)
        ))
        if user_mode not in {1, 2}:
            exit("Accepteble mode values are 1 or 2.")
        self.mode = user_mode


    def build_random_mode(self):
        user_q_count = int(input(f"""
            Selection the number of questions you'd like to be asked,
            (must be less than {len(self.user_qna)-2} and greater than 0)
            """))

        random_key_values = sample(range(0, len(self.user_qna) -2), user_q_count)
        for random_key_value in random_key_values:
            self.quiz.append(self.user_qna[random_key_value])

    def build_chapter_mode(self):
        print(f"Select the chapter you'd like to be quized on")
        for index, chapter_info in self.user_qna[-1].items():
            print(f"{index}: {chapter_info[0]}")

        user_chapter = int(input())
        
        for i in range(*self.user_qna[-1][user_chapter][1]):
            self.quiz.append(self.user_qna[i])

    def get_display_page3(self):
        """
        This function will be responsible for:

            1. building the qna according to the mode and the specific_qna setting
            2. qna build will be a deque
            3. if user answers correctly pop the qna off the deque
            4. if user answers incorrectly, add qna back onto the end for eventual retry

        Obviously you may have to break down 1-4 into subroutines
        """
        if self.mode == 1:
            self.build_chapter_mode()
        if self.mode == 2:
            self.build_random_mode()


    def quiz_logic(self):
        while self.quiz:
            current_qna = self.quiz.popleft()

            user_current_a = input(current_qna['q'])
            print(f"Here's your answer: {user_current_a}")
            print("\n\n")
            print(f"Here's the model answer: {current_qna['a']}")

            happy = input("Are you happy with how you're answer (y/n)? ")
            if happy == 'n':
                self.quiz.append(current_qna)

        print("""
        You've made it to the end and you've successfully answered all questions adequately,
        nice one!"""
        )

    def run_logic(self):
        self.get_display_page1()
        self.get_display_page2()
        self.get_display_page3()
        self.quiz_logic()