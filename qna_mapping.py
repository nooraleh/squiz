from qna.mappings import c_basics
from qna.mappings import cpp_basics
from qna.mappings import gregoire # from 'Professional C++'
from qna.mappings import cisco_advanced_cpp # from Cisco Academy's 'Advanced C++'
from qna.mappings import smith # from 'Cython - A Guide for Python Programmers'

qna_mapping = {
    1: c_basics.qna,
    # 2: cpp_basics.qna,
    # 3: gregoire.qna,
    4: cisco_advanced_cpp.qna,
    # 5: smith.qna
}