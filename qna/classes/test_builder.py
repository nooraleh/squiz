from sys import exit

from qna.classes.qna_collections import QnaCollection
from qna.helpers import clear_screen

from qna.classes.qna_collections import QnaCollection


class TestBuilder:
    all_qna_options = QnaCollection().qna_collection
    VALID_QNA = [all_qna_options.keys()]
    INVALID_OPTION = -1_000_000

    def __init__(self):
        self.run_logic()

    def get_specific_qna(self):
        for index, qna_object in self.all_qna_options.items():
            print(f"{index}: {qna_object.title}")

        
        self.specific_qna = self.all_qna_options.get(
            int(input("Please select the resource you'd like to be quized on: "))
        , self.INVALID_OPTION)
        
        assert(self.specific_qna != self.INVALID_OPTION), exit(f"Invalid QNA option in `get_specific_qna`, aborting.")

    def get_quiz(self):
        self.quiz = self.specific_qna.build_random_mode()


    def quiz_logic(self):
        while self.quiz:
            current_qna = self.quiz.popleft()

            user_current_a = input('\033[95m' + current_qna['q'] + '\n\n \033[0m')
            print(f"\033[92m Here's your answer: {user_current_a} \033[0m")
            print("\n\n")
            print(f"\033[93m Here's the model answer: {current_qna['a']} \033[0m")

            happy = input("Are you happy with how you're answer (y/n)? ")
            if happy == 'n':
                self.quiz.append(current_qna)
            
            clear_screen()

        print("""
        You've made it to the end and you've successfully answered all questions adequately,
        nice one!"""
        )

    def run_logic(self):
        self.get_specific_qna()
        self.get_quiz()
        self.quiz_logic()