from qna.classes.base_qna import BaseQNA
from qna.mappings import gregoire

class QnaCollection:
    def __init__(self):
        self.qna_classes = [
            self.Gregoire
            ]
        self.qna_collection = {
            i: qna_class()
            for i, qna_class in
            enumerate(self.qna_classes, 1)
            if not qna_class().obselete
        }


    class Gregoire(BaseQNA):
        def __init__(self):
            super().__init__(
            title="Gregoire's Professional C++",
            qna_dict = gregoire.qna,
            obselete = False,
            )