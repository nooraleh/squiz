from abc import ABC, abstractclassmethod, abstractmethod
from ..classes import qna_mapping as all_qna_options
from collections import deque

class BaseQNA(ABC):

    specific_mapping = None


    def __init__(self, mode, specific_qna, all_qna_options):
        self.mode = mode # chapter mode or random
        self.specific_qna = specific_qna
        self.all_qna_options = all_qna_options
        self.test_qna = deque()


    @abstractmethod
    def get_random_mode(self):
        # TODO: I'm pretty sure we can implement this up here
        pass

    @abstractmethod
    def get_chapter_mode(self):
        # TODO: You may be able to implement this up here too
        pass

    @abstractmethod
    def get_display_page1(self):
        """
        This function will have the mappings to all the QNA notes
        and allow the user to select one,

        self.specific_qna will be modified
        """
        pass


    @abstractmethod
    def get_display_page2(self):
        """
        This function will ask whether the user wants to be tested in random mode
        or chapter mode, self.mode will be modified
        """
        pass


    @abstractmethod
    def get_display_page3(self):
        """
        This function will be responsible for:

            1. building the qna according to the mode and the specific_qna setting
            2. qna build will be a deque
            3. if user answers correctly pop the qna off the deque
            4. if user answers incorrectly, add qna back onto the end for eventual retry

        Obviously you may have to break down 1-4 into subroutines
        """
        pass