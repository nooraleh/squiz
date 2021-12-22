from qna import c_basics
from qna import cpp_basics
from qna import gregoire # from 'Professional C++'
from qna import cisco_advanced_cpp # from Cisco Academy's 'Advanced C++'


qna_mapping = {
    1: c_basics.qna,
    2: cpp_basics.qna,
    3: gregoire.qna,
    4: cisco_advanced_cpp.qna,
}