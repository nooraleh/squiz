# Notes taken in a Q & A style format from Kurt Smith's 'Cython - A Guide for Python Programmers'
qna = {
	-1: {
			1: ['Chapter 1: Cython Essentials', (1, 3)],
			2: ['Chapter 2: Compiling and Running Cython Code', (3, )],
			3: ['Chapter 3: Non-Modifying containers', (23, 28)],
			4: ['Chapter 4: ', (28, 29)],
			5: ['Chapter 5: ', (29, 30)],
			6: ['Chapter 6: ', (30, 31)],
			7: ['Chapter 7: ', (31, 36)],
			8: ['Chapter 8: ', (36, 39)],
		},
	0: "Cython - A Guide for Python Programmers",
	1: { # chapter 1: Cython Essentials
		'q':  """
		At the C-level, is a dynamic Python object:
            heap or stack allocated?
        """,
		'a': """
		A dynamic Python object is entirely heap allocated.
        """,
	},
    2: {
		'q':  """
		What type of bounds are:
            i) likely to provide improvement in performance
            ii) not likely to provide improvement in performance
            
        Once Cythonized.""",
		'a': """
		i) CPU bound programs
        ii) I/O or network bound programs.""",
	},
    3: { # chapter 2: Compiling and Running Cython Code
		'q':  """
		What is the file extension for:
            i) Cython source code.
            ii) Compiled extension module on linux.""",
		'a': """
		    i) .pyx
            ii) .so
        """,
	},
    4: {
		'q':  """
		Consider:
        
            from distutils.core import setup
            from Cython.Build import cythonize

            setup(
                ext_modules=cythonize('cfib.pyx')
            )

        i) What does the `cythonize` function do?
        ii) What does the `setup` function do?
        """,
		'a': """
		i) Converts Cython source code to C source code via Cython compiler
        ii) Turns objects into Python extension modules.
        """,
	},
    5: {
		'q':  """
		""",
		'a': """
		""",
	},
    6: {
		'q':  """
		""",
		'a': """
		""",
	},
    7: {
		'q':  """
		""",
		'a': """
		""",
	},
    8: {
		'q':  """
		""",
		'a': """
		""",
	},
    9: {
		'q':  """
		""",
		'a': """
		""",
	},
}