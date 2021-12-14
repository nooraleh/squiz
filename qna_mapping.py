from qna import c_basics
from qna import cpp_basics
from qna import gregoire # from 'Professional C++'


qna_mapping = {
    1: c_basics.qna,
    2: cpp_basics.qna,
    3: gregoire.qna,
}