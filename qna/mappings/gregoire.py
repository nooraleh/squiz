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
		'q':  """
		What problem does <string_view>'s std::string_view solve?""",
		'a': """
		std::string_view is a drop-in replacement for:
			const std::string&
		but without the overhead i.e string_view doesn't copy a string.""",
	},
	44: {
		'q':  """
		What can you not do with an std::string and std::string_view?""",
		'a': """
		Concatenation (i.e the operator+ is not define for those operands.""",
	},
	45: {
		'q':  """
		When should you use an std::string_view over options:
			1) const std::string&
			2) const char*
		in a function parameter specification????""",
		'a': """
		Whenever a function or method requires a read-only string as one of its parameters.""",
	},
	46: {
		'q':  """
		In computer science, what is a callback?""",
		'a': """
		A callback is a function which is passed to another function as an argument.""",
	},
	47: {
		'q':  """Describe polymorphism.""", # chapter 5: Designing with Objects
		'a': """
		Polymorphism is the notion that objects that adhere to a standard set of 
		properties and methods can be used interchageably.""",
	},
	48: {
		'q':  """
		What is the Liskov substitution principle?""",
		'a': """
		The Liskov substitution principle states that objects of a superclass must be interchangeable
		with objects of a subclass without breaking the program.""",
	},
	49: {
		'q':  """
		Outline three things that good object-oriented hierarchy accomplishes?""",
		'a': """
		1) Organizes classes into meaningful functional relationships
		2) Supports code reuse by factoring common functionality to base classes
		3) Avoids having derived classes that override much of the parent's functionality, unless
		the parent is an abstract base class.""",
	},
	50: {
		'q':  """
		In OOP, what is the interface to a class?""",
		'a': """
		The collection of publicly accessible properties and methods.""",
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
	75: { # chapter 7: Memory management
		'q':  """
		What's the main advantage of the C++ `new` keyword over C-style malloc?""",
		'a': """
		`new` doesn't just allocate memory, it's calls the object's constructor (which malloc does not)""",
	},
	76: {
		'q':  """
		What's the main advantage of C++ keyword delete/delete[] over C-style free? """,
		'a': """
		With delete/delete[], the destructor is called and the object is properly cleaned up.""",
	},
	77: {
		'q':  """
		Consider:
			int* ptr = new int;
			
		Configure this statement to not throw an exception, instead returning a pointer if memory
		allocation fails.""",
		'a': """
			int* ptr = new(nothrow) int;""",
	},
	78: {
		'q':  """
		Name one advantage of putting an array on the heap. """,
		'a': """
		You can define the arrays size at run time.""",
	},
	79: {
		'q':  """
		Is the following statement true or false:
		
			'You should always use delete on anything allocated with new,
			you should always use delete[] on anything allocated with new[]'
		""",
		'a': """
		True.""",
	},
	80: {
		'q':  """
		Why is using static_cast on a pointer type safer than C-style pointer casting?""",
		'a': """
		Because the compiler refuses to static cast on pointers to unrelated (through inheritance) data types.""",
	},
	81: {
		'q':  """
		Which one of these statements is the odd one out? Why?
		
			void double_ints(int* the_array, size_t size);
			void double_ints(int the_array[], size_t size);
			void double_ints(int the_array[2], size_t size);

		""",
		'a': """
		Trick question. The compiler ignores any number between the square brackets
		and array and pointers can be used interchangeable from a syntactical perspectic.
		Therefore all three statements are functionally identical.
		""",
	},
	82: {
		'q':  """
		Give a high level overview of the garbage collection approach known as 'mark and sweep'. """,
		'a': """
		With the 'mark and sweep' approach, the garbage collector periodically examines every single
		pointer and annotates the fact that the references memory is still in use.
		
		At the end of the cycle, any memory that hasn't been marked is deemed to be not in-use and is freed.""",
	},
	83: {
		'q':  """
		Say we have a shared pointer variable names shrd_ptr:
		
			i) Invoke the method to get direct access to the underlying pointer.
			ii) In what situations would using this method be helpful.
		""",
		'a': """
			i) shrd_ptr.get()
			ii) When we need to pass the pointer to a function that requires a raw pointer.""",
	},
	84: {
		'q':  """
		Consider the following snippet (assume Simple is a defined class):
		
			auto p_unq_simple = std::make_unique<Simple>();
		(1)	p_unq_simple.reset();
		(2)	p_unq_simple.reset(new Simple());
		
		Example what's happening in:
		i) line (1)
		ii) line (2)""",
		'a': """
		i) Free the resource and set to nullptr.
		ii) Free the resource and set to a new simple instance.
	""",
	},
	85: {
		'q':  """
		Say you have a shared pointer, name 'ptr_shared_var'. Invoke the method to retrieve
		the number of std::share_ptr instances that are sharing the same resource.""",
		'a': """
		ptr_shared_var.use_count()""",
	},
	86: {
		'q':  """
		What functions are available for casting std::shared_ptr entities?""",
		'a': """
		1) const_pointer_cast
		2) dynamic_pointer_cast
		3) static_pointer_cast
		4) reinterpret_pointer_cast
	""",
	},
	87: {
		'q':  """
		i) Explain the double deletion problem with respect to smart pointers
		ii) What should you do to avoid the double deletion problem?""",
		'a': """
		i) Double deletion problem: When a constructor is called once and the destructor
		is called twice because two distinct instances of a std::share_ptr to the same object
		was declared.
		
		ii) To avoid the double deletion problem, make a copy of the first shared_ptr instance
		and assign to the second.""",
	},
	88: {
		'q':  """
		i) Which smart pointer supports aliasing?
		ii) What does aliasing of this smart pointer allow for?""",
		'a': """
		i) std::shared_ptr
		
		ii) The std::shared_ptr aliasing allows an std::shared_ptr to share ownership over a 
			pointer with another shared_ptr, but while pointing to a difference objects (the stored pointer)""",
	},
	89: {
		'q':  """
		Outline two ways of convert an std::weak_ptr to an std::shared_ptr.""",
		'a': """
		1) Use the .lock() method on a std::weak_ptr instance, which returns an std::shared_ptr.
		2) Create a new std::shared_ptr instance with an std::weak_ptr as an argument.""",
	},
	90: {
		'q':  """
		What does std::shared_pointer<T>::reset do?""",
		'a': """
		It replaces the managed object with an object pointed to by argument ptr. """,
	},
	91: {
		'q':  """
		How does a buffer overflow error arise?""",
		'a': """
		When writing to memory past the end of a (C-style) array.""",
	},
	92: { # chapter 6: Designing for reuse
		'q':  """
		""",
		'a': """
		""",
	},
	93: {
		'q':  """
		""",
		'a': """
		""",
	},
	94: {
		'q':  """
		""",
		'a': """
		""",
	},
	95: {
		'q':  """
		""",
		'a': """
		""",
	},
	96: {
		'q':  """
		""",
		'a': """
		""",
	},
	97: {
		'q':  """
		""",
		'a': """
		""",
	},
	98: {
		'q':  """
		""",
		'a': """
		""",
	},
	99: {
		'q':  """
		""",
		'a': """
		""",
	},
	100: {
		'q':  """
		""",
		'a': """
		""",
	},
	101: {
		'q':  """
		""",
		'a': """
		""",
	},
	102: {
		'q':  """
		""",
		'a': """
		""",
	},
	103: {
		'q':  """
		""",
		'a': """
		""",
	},
	104: {
		'q':  """
		""",
		'a': """
		""",
	},
	105: {
		'q':  """
		""",
		'a': """
		""",
	},
	93: { # chapter 8: Gaining proficiency with classes and objects
		'q': 
		"""
		True or false:

			'Class definitions are statements'
		""",
		'a': """
		True. That's why they must end in semicolons.""",
	},
	94: {
		'q':  """
		True or false:
		
			'Strict CANNOT have methods members like classes can'
			
		""",
		'a': """
		False. Structs can have methods.""",
	},
	95: {
		'q':  """
		What's the default access specifier for a:
			
			i) class
			ii) struct""",
		'a': """
		
			i) private
			ii) public
		""",
	},
	96: {
		'q':  """
		What do C++ programmers sometimes call a constructor?""",
		'a': """
		A ctor.""",
	},
	97: {
		'q':  """
		What is the most vexing parse in C++?""",
		'a': """
		The most vexing parse is a counterintuitive form of syntactic ambiguity resolution in C++.
		In certain situations, the C++ grammar cannot distinguish between the creation of an object
		parameter and specification of a function's type.
		
		In those situation, the compiler is required to interpret the line as a function type
		specification.
		
		E.g:
			// calling Spreadsheet's parameterless constructor
			// however compiler interprets is as a function called my_cell which returns a Spreadsheet.
			Spreadsheet my_cell();""",
	},
	98: {
		'q':  """
		Name two ways to avoid the most vexing problem.""",
		'a': """
		1) When calling an object's parameterless constructor on the stack, omit the parentheses.
		2) Use uniform initialization (since C++11)""",
	},
	99: {
		'q':  """
		Let MyClass be a class. Say MyClass is designed to only have static methods
		, and you do not want to write a constructors for MyClass.
		
		i) Give the syntax for explicitly deleting the default constructor
		ii) What's the term for your answer to (i)""",
		'a': """
		i) MyClass() = delete;
		ii) Explicitly deleted constructors.
		
		""",
	},
	100: {
		'q':  """
		With ctor-initializers, what order are the data members initialized in?""",
		'a': """
		ctor-initializers initialize data members in the order in which they are declared in the
		class definition, not the order in the ctor-initializer.""",
	},
	101: {
		'q':  """
		Consider the following statement:
		
			'For performance reason, it is best to pass objects by const reference
			insteaad of by value'.

		Why is this true?
		""",
		'a': """
		Because when passing by reference, we only copy over the address of the passed object.
		When passing by value, we call the passed arguments copy constructor which usually
		has more overhead than simply copying the address.""",
	},
	102: {
		'q':  """
		i) What is an initializer-list constructor?
		
		ii) Let EvenSquence be a proposed class. Write the sequence for an
		EvenSequence initializer-list constructor for arguments of type double.""",
		'a': """
		i) An initializer-list constructor is a construct with only std::initializer_list<T> as first parameter.

		
		ii)

			#include <initializer_list>
			class EvenSequence
			{
			public:
				EvenSequence(std::initializer_list<double> args)
				{
				}
			};
		""",
	},
	103: {
		'q':  """
		i) What is a delegating constructor.
		ii) Give two constraints for delegating constructors to be valid.""",
		'a': """
		i) Delegating constructors allow constructors to call another constructor from the same class
		ii)
		
			1) This call must be placed in the ctor-initializer (not the body)
			2) The delegating constructor must be the only member initializer in the ctor-initializer list.
		""",
	},
	104: {
		'q':  """
		In which order are data member objects of a class destroyed?""",
		'a': """
		In the reverse order of their declaration in the class definition.""",
	},
	105: {
		'q':  """
		C++11 onwards has deprecated the generation of a copy constructor is the class has a user-declared copy constructor
		, the same applies to copy assignment operators.
		
		What should we do if we have a user define copy constructor or copy assignment operator but still want
		the compiler generated version?""",
		'a': """
		In both cases, explicitly default one:
		
		MyClass(const MyClass& src) = default;
		MyClass& operator=(const MyClass& rhs) = default;
	""",
	},
	106: { # chapter 9: Mastering Classes and Objects 
		'q':  """
		Consider:
		
			class Foo
			{
				frience class Bar; (1)
			};
		
		What implications does line (1) have for Bar?
		""",
		'a': """
		All the methods of Bar can access private and protected members of Foo.""",
	},
	107: {
		'q':  """
		What are destructors implicitly marked as?""",
		'a': """
		Destructors are implicitly marked as `noexcept`, since they should not throw any exceptions.""",
	},
	108: {
		'q':  """
		What is a dangling pointer?""",
		'a': """
		A pointer that no longer points to valid memory.""",
	},
	109: {
		'q':  """
		Say you have class which dynamically allocates memory. What steps should you take
		to ensure against memory leaks/mismanagement.""",
		'a': """
		Steps to take: write your own:
			1) copy constructor
			2) assignment operator
			
		to provide a deep copy of the memory.""",
	},
	110: {
		'q':  """
		""",
		'a': """
		""",
	},
	111: {
		'q':  """
		""",
		'a': """
		""",
	},
	112: {
		'q':  """
		""",
		'a': """
		""",
	},
	113: {
		'q':  """
		""",
		'a': """
		""",
	},
	114: {
		'q':  """
		""",
		'a': """
		""",
	},
	115: {
		'q':  """
		""",
		'a': """
		""",
	},
	116: {
		'q':  """
		""",
		'a': """
		""",
	},
	117: {
		'q':  """
		""",
		'a': """
		""",
	},
	118: {
		'q':  """
		""",
		'a': """
		""",
	},
	119: {
		'q':  """
		""",
		'a': """
		""",
	},
	120: {
		'q':  """
		""",
		'a': """
		""",
	},
	121: {
		'q':  """
		""",
		'a': """
		""",
	},
	122: {
		'q':  """
		""",
		'a': """
		""",
	},
	123: {
		'q':  """
		""",
		'a': """
		""",
	},
	124: {
		'q':  """
		""",
		'a': """
		""",
	},
	125: {
		'q':  """
		""",
		'a': """
		""",
	},
	126: {
		'q':  """
		""",
		'a': """
		""",
	},
	127: {
		'q':  """
		""",
		'a': """
		""",
	},
	128: {
		'q':  """
		""",
		'a': """
		""",
	},
	129: {
		'q':  """
		""",
		'a': """
		""",
	},
	130: {
		'q':  """
		""",
		'a': """
		""",
	},
	131: {
		'q':  """
		""",
		'a': """
		""",
	},
	132: {
		'q':  """
		""",
		'a': """
		""",
	},
	133: {
		'q':  """
		""",
		'a': """
		""",
	},
	134: {
		'q':  """
		""",
		'a': """
		""",
	},
	135: {
		'q':  """
		""",
		'a': """
		""",
	},
	136: {
		'q':  """
		""",
		'a': """
		""",
	},
	137: {
		'q':  """
		""",
		'a': """
		""",
	},
	138: {
		'q':  """
		""",
		'a': """
		""",
	},
	139: {
		'q':  """
		""",
		'a': """
		""",
	},
	140: {
		'q':  """
		""",
		'a': """
		""",
	},
	141: {
		'q':  """
		""",
		'a': """
		""",
	},
	142: {
		'q':  """
		""",
		'a': """
		""",
	},
	143: {
		'q':  """
		""",
		'a': """
		""",
	},
	144: {
		'q':  """
		""",
		'a': """
		""",
	},
	145: {
		'q':  """
		""",
		'a': """
		""",
	},
	146: {
		'q':  """
		""",
		'a': """
		""",
	},
	147: {
		'q':  """
		""",
		'a': """
		""",
	},
	148: {
		'q':  """
		""",
		'a': """
		""",
	},
	149: {
		'q':  """
		""",
		'a': """
		""",
	},
	150: {
		'q':  """
		""",
		'a': """
		""",
	},
}