# Notes taken in a Q & A style format from Marc Gregoire's Professional C++

qna = {
	1: {
		'q':  """
		What's an alternative way of writing 'include <iostream>'
		introduced by C++20 standard?""",
		'a': """
		import <iostream>""",
	},
	2: {
		'q':  """
		What are the 3 main steps to building a C++ program?""",
		'a': """
		1) Code is run through a preprocessor
		2) the code is compiled into machine-readable object files
		3) the individual object files are linked together into a single application.""",
	},
	3: {
		'q':  """
		What are include guards such as ifndef/endif used for?""",
		'a': """
		To protect against circular includes. Prevents the header file
		from being included multiple times.""",
	},
	4: {
		'q':  """If std::cout outputs to the user console, which stream entity outputs to the error console?""",
		'a': """std::cerr""",
	},
	5: {
		'q':  """
		What is the difference between std::endl and the escape character '\n'?
		Why is use of std::endl in loops not recommended?""",
		'a': """
		En""",
	},
	6: {
		'q':  """
		What does the stream buffer do?""",
		'a': """
		The buffer is responsible for communicating/transmitting data
		to external devices e.g stdout.
		""",
	},
	7: {
		'q':  """What is std::cout in one sentence?""",
		'a': """
		A global object of type ostream, which lives in the std namespace.""",
	},
	8: {
		'q':  """When can you use a lambda (anonymous functions) in C++?""",
		'a': """
		When you can otherwise use a function pointer
		e.g in functions which take as a parameter a function pointer.""",
	},
	9: {
		'q':  """Consider
		`auto add(T1& a, T2& b)->decltype(a+b)`
		What's the term for `decltype(a+b)`
		""",
		'a': """
		Trailing return type.
		""",
	},
	10: {
		'q':  """
		What is a buffer flush?""",
		'a': """
		A buffer flush is the transfer of computer data from a
		temporary storage area to the computer's permanent memory.
		When we close a file stream object with .close, the changes
		we've made to our document since the last time are flushed
		from the buffer to permanent storage on the hard disk.""",
	},
	11: {
		'q':  """
		What's an alternative to calling .close on a stream object for automated teardown of resources?""",
		'a': """
		Enclose the file object initialization with a scope with {}, after the program
		exits the scope the file object will be automatically destructed. This is known as
		RAII (resource acquisition is initialization).""",
	},
	12: {
		'q':  """
		What is RAII (resource acquisition is initializaiton)?""",
		'a': """
		In RAII, holding a resource is a class invariant, and is tied
		to object lifetime: resource allocation is done during object initialization
		by the constructor, while resource deallocation is done during object destruction by the destructor.""",
	},
	13: {
		'q':  """Every I/O operation contains at least two steps. What are they?
		""",
		'a': """
		1) Formatting the data
		2) Communicating with/Flushing to external devices i.e file, stdin/stdout/stderr, network etc..""",
	},
	14: {
		'q':  """
		Why should you not put a using directive or using declaration in a header file at global scope?""",
		'a': """
		Because you force it on everyone who included your header file.""",
	},
	15: {
		'q':  """
		What are 0x3.ABCp-10 and 0Xb.cp12l examples of?""",
		'a': """
		Hexadecimal floating point literals.""",
	},
	16: {
		'q':  """
		What does C++ use for digital separators and provide a usage example.""",
		'a': """
		i) a single quote character `'`
		ii) int x = 23'456'789;
		""",
	},
	17: {
		'q':  """
		Initialize the variable x to 7 using:
			i) uniform initialization syntax
			ii) assignment syntax""",
		'a': """
		i) int x{7};
		ii) int x = 7;""",
	},
	18: {
		'q':  """
		i) Where can we get information regarding numeric data type limits?
		ii) how we get the double max or int min??""",
		'a': """
		i) using the std::numeric_limits class template defined in <limits>
		ii) std::number_limits<double>::max(), std::numeric_limits<int>::min()""",
	},
	19: {
		'q':  """
		Outline a difference between old-style enums and enum classes?""",
		'a': """
		With old-style enums, values are exported to the enclosing scope.
		This means that the parent scope can use the names with fully qualifying them.
		Enum classes, on the other hand, do not export their values to the enclosing scope.
		Which means qualification is necessary.
		
		Old-style enums are not type safe. You can use their values in operations with int,
		for example. Enum classes that do not inherit from a data type cannot be used
		in operators data that is not of the type of the enum class.""",
	},
	20: {
		'q':  """
		""",
		'a': """
		""",
	},
	21: {
		'q':  """
		""",
		'a': """
		""",
	},
	22: {
		'q':  """
		""",
		'a': """
		""",
	},
	23: {
		'q':  """
		""",
		'a': """
		""",
	},
	24: {
		'q':  """
		""",
		'a': """
		""",
	},
	25: {
		'q':  """
		""",
		'a': """
		""",
	},
	26: {
		'q':  """
		""",
		'a': """
		""",
	},
	27: {
		'q':  """
		""",
		'a': """
		""",
	},
	28: {
		'q':  """
		""",
		'a': """
		""",
	},
}