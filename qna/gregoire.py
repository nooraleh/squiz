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
		i) What is a zero initializer?
		ii) Declare a float names my_float with zero initializer syntax""",
		'a': """
		i) A zero initializer is a uniform initializer with empty curly brackets {}
		ii) float my_float {}""",
	},
	21: {
		'q':  """
		Consider `float my_float {3.14f};` Cast my_float to an int using:
		i) C-style casting to i1
		ii) C++ functional cast to i2
		iii) static cast to i3
		iv) which method is the cleanest and therefore recommended?""",
		'a': """
		i) int i1 {(int)my_float};
		ii) int i2 {int(my_float)};
		iii) int i3 {static_cast<int>(my_float)}""",
	},
	22: {
		'q':  """
		What would you use to check if a floating-point number:
		i) is not-a-number (NaN)
		ii) is infinite
		iii) where are those functions defined"""
		,
		'a': """
		i) std::isnan()
		ii) std::isinf()
		iii) <cmath>""",
	},
	23: {
		'q':  """
		i) What is switch statement fallthrough?
		ii) From C++17, how can you tell the compiler that a fallthrough is intentional""",
		'a': """
		i) When a case is caught and no break is reached, the excution flow executes the following case statement.
		ii) [[fallthrough]]""",
	},
	24: {
		'q':  """
		i) What is meant by short-circuit evaluation with respect to logical expressions?
		ii) How can you leverage short-circuit evaluation for performance gains?""",
		'a': """
		i) Once the final result is certain, the rest of the expression won't be evaluated.
		ii) By putting computationally cheap logical tests first.""",
	},
	25: {
		'q':  """
		What is the local predefined variable that every function has?""",
		'a': """
		`__func__`. It contains the name fo the current function.""",
	},
	26: {
		'q':  """
		State three advantages of using std::array instead of C-style arrays in C++?
		""",
		'a': """
		1) std::array's always know their own size
		2) std::array's have iterators to easily loop over the elements
		3) std::array's are not automatically cast to a pointer to avoid certain bugs.""",
	},
	27: {
		'q':  """
		What do structured bindings allow you to do?
		""",
		'a': """
		Structured bindings allow you to declare multiple variables that are initialized with elements
		from an array, struct, pair, or tuple.""",
	},
	28: {
		'q':  """
		Consider:
			std::array<int, 3> values = {11, 22, 33};
		Use a structured binding to assign values to variables x, y, z.,
		""",
		'a': """
		auto [x, y, z] = values;""",
	},
	29: {
		'q':  """
		i) What are initializer lists used for?
		ii) Where are they defined?
		ii) write the function prototype for a make_sum function with an initializer list.""",
		'a': """
		i) Initializer lists are used for writing functions that can accept a variable number of arguments
		ii) <initializer_list>
		iii) int make_sum(initializer_list<int> _lst);""",
	},
	30: {
		'q':  """
		What does dynamic memory management allow you to do?""",
		'a': """
		Dynamic memory management allows you to build programs with data that is not of 
		fixed size at compile time.""",
	},
	31: {
		'q':  """
		Let `_integer_pointer` be of type pointer to int. Give the statement for:


		i) declaring `_integer_pointer` but you do not want to allocate memory right away.
		ii) Allocatign memory
		iii) Deallocating memory with best practice. """,
		'a': """
		int* _integer_pointer = nullptr;
		
		ii) _integer_pointer = new int
		
		iii) delete _integer_pointer;
			_integer_pointer = nullptr """,
	},
	32: {
		'q':  """
		Describe std::unique_ptr:
		i) How it differs from an ordinary 'raw' pointer
		ii) Ownership property of the object pointed to
		iii) An advantage of unique_ptr """,
		'a': """
		i) std::unique_pointer, unlike raw pointers, automatically frees the memory
		or resource when the std::unique_ptr goes out of scope or is delete.

		ii) std::unique_ptr has sole ownership of the object pointed to

		iii) std::unique_ptr guarantees that memory and resources are always freed,
		even when return statements are executed, or when exceptions are thrown.""",
	},
	33: {
		'q':  """ 
		i) What does std::shared_ptr allow for?
		ii) What happens each time a shared_ptr is assigned to a piece of data?
		iii) What conditions are needed for an object that is referenced by a std::shared_ptr(s)
		to be freed?""",
		'a': """
		i) std::shared_ptr allows for distributed ownership of the data.
		ii) A reference count is incremented indicating there is one more owner of the data.
		iii) When the reference count goes to zero, there is no longer any owner of the data 
		so the memory is automatically deallocated.
		""",
	},
	34: {
		'q':  """
		What does the `constexpr` specifier do?""",
		'a': """
		The `constexpr` specifier declares that it is possible to evaluate the value
		of the function or variable at compile time. A constexpr specifier used in a 
		function or static data member declaration implied `inline`.

		The main idea is performance improvement of programs by doing computations at
		compile time rather than run time.
		""",
	},
	35: {
		'q':  """
		What's the main difference between inline functions and constexpr functions?""",
		'a': """
		inline functions - expressions are always evaluated at run time.
		constexpr functions - expressions are evaluated at compile time.""",
	},
	36: {
		'q':  """
		i) What are the two data type qualifiers that are stripped when `auto` is used to deduce the
		type of an expression?
		ii) say you want to retain those two qualifiers but still want to use auto for a variable `var1`.
		Give the declaration.""",
		'a': """
		i) 1) reference (&) 2) const
		ii) const auto& var1 = <primary_expression>;""",
	},
	37: {
		'q':  """
		What's the difference between auto and decltype?""",
		'a': """
		Decltype, unlike auto, does not strip reference and const qualifiers.""",
	},
	38: {
		'q':  """
		Let:
			`T` be a valid data type
			`var1` be a variable name
			`arg1` ,`arg2` be literals of type T
			
		Give the syntax for:
		i) copy list initialization
		ii) direct list initializatoin""",
		'a': """
		i) T var1 = {arg1, arg2};
		i) T var1 {arg1, arg2};""",
	},
	39: {
		'q':  """
		What is meant by literal pooling?""",
		'a': """
		Literal pooling is a compiler memory optimization technique to reuse references
		to equivalent string literals.
		
		For example, if your program uses the string literal "hello" 500 times, the
		compiler is allowed to create just one instance of "hello" in memory.""",
	},
	40: {
		'q':  """
		i) What is a raw string literal in C++
		ii) Declare and initialize a raw string literal.""",
		'a': """
		i) Raw string literals are string literal that can:
			- span across multiple lines of code
			- don't require escpaing of embedded double quotes
			- escape sequences like \t and \n are processed as normal text.
			
		ii) const char* example = R"("Hello \t world!")"; """,
	},
	41: {
		'q':  """
		
		Consider the two statements:
			auto string1 = "Hello World";
			auto string2 = "Hello World";

		What changes would you make to the second statement to
		cause auto to infer that the literal is of type std::string?
		""",
		'a': """
			using namespace std::string_literals;
			// Append an s after the closing double quotes i.e:
			auto string2 = "Hello World"s;
			
		""",
	},
	42: {
		'q':  """
		What does [[noreturn]] function qualifier indicate?""",
		'a': """
		[[noreturn]] is an attribute used to indicate that the function doesn't return to the caller.
		I.e. a function where the control flow will not return to the calling function after the
		function finishes (e.g functions that exit the application, loop forever or throw exceptions.)
		
		NB: Behaviour is undefined if the function with this attribute actaully returns.""",
	},
	43: {
		'q':  """ """,
		'a': """
		""",
	},
	44: {
		'q':  """ """,
		'a': """
		""",
	},
	45: {
		'q':  """ """,
		'a': """
		""",
	},
	46: {
		'q':  """ """,
		'a': """
		""",
	},
	47: {
		'q':  """ """,
		'a': """
		""",
	},
	48: {
		'q':  """ """,
		'a': """
		""",
	},
	49: {
		'q':  """ """,
		'a': """
		""",
	},
	50: {
		'q':  """ """,
		'a': """
		""",
	},
	51: {
		'q':  """ """,
		'a': """
		""",
	},
	52: {
		'q':  """ """,
		'a': """
		""",
	},
	53: {
		'q':  """ """,
		'a': """
		""",
	},
	54: {
		'q':  """ """,
		'a': """
		""",
	},
	55: {
		'q':  """ """,
		'a': """
		""",
	},
	56: {
		'q':  """ """,
		'a': """
		""",
	},
	57: {
		'q':  """ """,
		'a': """
		""",
	},
	58: {
		'q':  """ """,
		'a': """
		""",
	},
	59: { # chapter 3 - coding with style
		'q':  """
		What are loop invariants?""",
		'a': """
		Conditions that have to be true during the execution of the loop.""",
	},
	60: {
		'q':  """
		i) What is meant by meta-information with regards to code creation?
		ii) Give some examples of meta-information.
		iii) In what case would these examples in (ii) be discourages?""",
		'a': """
		i) Meta-information provides detail about the creation of the code without
		addressing the specifics of its behaviour.
		
		ii) Examples include:
			Origin author(s),
			Code creation date,
			Code last update date,
			Change log,
			Citations of external documents or referrences to other code

		iii) Meta-information is discourage when a source-control solution (such as git) is
		in place.
			""",
	},
	61: {
		'q':  """
		What is the free tool for C++ which parsed formatted comments to automatically build
		HTML documentation, class diagrams, UNIX man pages etc?""",
		'a': """
		Doxygen""",
	},
	62: {
		'q':  """
		What is meant by the computing term `cruft`?""",
		'a': """
		Cruft refers to the gradual accumulation of small amouunts of code that 
		eventually turns a once-elegant piece of code into a mess of patches and
		special cases.""",
	},
	63: {
		'q':  """
		In object-oritented programming, what is meant by:
			i) Pull up
			ii) Push down""",
		'a': """
			i) Pull up: Move the location of code to a base class
			ii) Push down: Move the location of code to a derived class""",
	},
	64: {
		'q':  """
		Name three advantages of using pass-by-reference over pass-by-pointer in C++?""",
		'a': """
		1) References are safer than pointers because they do not directly deal with memory addresses
		and nullptr.
		2) References do not need operators such as * and & when interacting with them.
		3) Ownership/deletion responsibility is clear, unlike with pointers.""",
	},
	65: { # chapter 4: Designing professional C++ Programs
		'q':  """
		i) What is the very first step to take when starting a new program or a new
		feature for an existing program?
		
		ii) What does your answer to (i) involve?
		
		iii) What is a vital outcome of (i)""",
		'a': """
		i) Requirements analysis
		ii) Discussion with your stakeholders
		iii) A vital outcome of the requirements analysis phase is a functional requirements documents.""",
	},
	66: {
		'q':  """
		i) What does a functional requirements document do?
		ii) What doesn't a functional requirements document do?
		iii) What does a non-functional requirements document do? Give some examples?""",
		'a': """
		i) A functional requirements document describes what exactly the new piece of code
		has to do.

		ii) A functional requirements document doesn't describe how it has to implement the requirement.
		
		iii) A non-functional requirements documents described how the final system should be, as 
		opposed to what it should do. Examples include: extensibility, performance criteria satisfaction etc.""",
	},
	67: {
		'q':  """
		i) What phase comes after the requirements analysis phase?
		ii) What does your answer to i) entail?""",
		'a': """
		i) The software design phase
		ii) The software design phase is the specification of the architecture that you will
		implement to fulfill all the requirements (both functional and non-functional) of the program.""",
	},
	68: {
		'q':  """
		What are the two fundamental design rules in C++ and define them/""",
		'a': """
		1) Abstraction - separating an entity's internal implementation from its external interface.
		2) Reuse - Using code functionality from elsewhere wherever possible, using common design patterns
			for your problems. I.e. avoid reinventing the wheel wherever possible. Create code that is extensible.""",
	},
	69: {
		'q':  """
		Describe the difference between a library and a framework?""",
		'a': """
		Library - a collection of code used to accomplish a specific task, such as parsing
				XML, or the hand a specific domain, such as cryptography.
		Framework - A collection of code aruond which you design a program.
		
		Difference: A program uses a library but fits into a framework. Libraries
				provide specific functionality, while frameworks are fundamental to your
				program design and structure.""",
	},
	70: {
		'q':  """
		What's the key distinction between a library and an API?""",
		'a': """
		A library refers to the implementation, while the API refers to the published
		interface to the library.""",
	},
	71: {
		'q':  """
		Libraries that use <3_points> when handling errors should be avoided. Fill in the blank.""",
		'a': """
		Libraries that:
			1) Pop up message boxes
			2) Issue messages to stderr/cerr or stdout/cout
			3) Termination the program""",
	},
	72: {
		'q':  """
		What are two benefits of specifying performance as a function of the input size (like big-O notation)
		instead of in absolute numbers?""",
		'a': """
		1) It is platform independent
		2) It covers all possible inputs to the algorithm with one specification.
		""",
	},
	73: {
		'q':  """
		What is the meaning of orthogonality in the context of programming?
		
		Give a real world analogy of:
		i) orthogonality ii) non-orthogonality""",
		'a': """
		Orthogonality in the context of programming means 'changing A does not change B'.
		I.e. operations do not have (unintended) side effects. Each action changes just one thing.
		
		i) An orthogonal system analogy would be a radio, where changing station
			doesn't change the volume and vice versa.
		ii) A non-orthogonal system analogy would be a helicopter, where changing the speed
			can change the direction.""",
	},
	74: {
		'q':  """
		What is a sequence diagram?""",
		'a': """
		A sequence diagram shows object interactions arranged in a time sequence.""",
	},
	75: {
		'q':  """
		""",
		'a': """
		""",
	},
	76: {
		'q':  """
		""",
		'a': """
		""",
	},
	77: {
		'q':  """
		""",
		'a': """
		""",
	},
	78: {
		'q':  """
		""",
		'a': """
		""",
	},
	79: {
		'q':  """
		""",
		'a': """
		""",
	},
	80: {
		'q':  """
		""",
		'a': """
		""",
	},
	81: {
		'q':  """
		""",
		'a': """
		""",
	},
	82: {
		'q':  """
		""",
		'a': """
		""",
	},
	83: {
		'q':  """
		""",
		'a': """
		""",
	},
	84: {
		'q':  """
		""",
		'a': """
		""",
	},
	85: {
		'q':  """
		""",
		'a': """
		""",
	},
	86: {
		'q':  """
		""",
		'a': """
		""",
	},
	87: {
		'q':  """
		""",
		'a': """
		""",
	},
	88: {
		'q':  """
		""",
		'a': """
		""",
	},
}