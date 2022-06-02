# Notes taken in a Q & A style format from Marc Gregoire's Professional C++

qna = {
	1: { # Chapter 1: A Crash Course in C++ and the Standard Library
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
		What is the difference between std::endl and the escape character '\\n'?
		Why is use of std::endl in loops not recommended?""",
		'a': """
		The difference between std::endl and new line escape character is the std::endl adds a newline and flushes the buffer.
		The use of std::endl is loops is not recommended as there is a performance cost to flushing the buffer a repeated amount of times.
		""",
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
		ii) std::numeric_limits<double>::max(), std::numeric_limits<int>::min()""",
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
		`__func__`. It contains the name of the current function.""",
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
		iii) write the function prototype for a make_sum function with an initializer list.""",
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
		function or static data member declaration implies `inline`.

		The main motivation is for runtime performance improvements by delegating
		computatations at compile time rather than run time.
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
	39: { # Chapter 2: Working with Strings and String Views
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
		Which operator is not defined between an std::string and std::string_view?""",
		'a': """
		Concatenation (i.e the operator+ is not define for those operands.""",
	},
	45: {
		'q':  """
		When should you use `const std::string_view&` over options:
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
	59: { # chapter 3 - Coding with Style
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
	65: { # Chapter 4: Designing Professional C++ Programs
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
	75: { # Chapter 7: Memory Management
		'q':  """
		What's the main advantage of C++'s `new` keyword over C-style malloc?""",
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
		i) Which smart pointer supports pointer aliasing?
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
		How can a buffer overflow error arise with a C-style array?
		""",
		'a': """
		When writing to memory past the end of a (C-style) array.
		""",
	},
	92: { # chapter 6: Designing for Reuse
		'q':  """
		What is meant by client code?""",
		'a': """
		Code that is written to use your interfaces.""",
	},
	93: {
		'q':  """
		Fill in the blank:
		
			When designing your interface, do not expose _______ to your clients.""",
		'a': """
		implementation details""",
	},
	94: {
		'q':  """
		What is meant by an opaque class?""",
		'a': """
		A class in which a client cannot access the internal data members, either directly or via getters/setters.""",
	},
	95: {
		'q':  """
		What is meant by high cohesion of a OOP component?
		""",
		'a': """
		High cohesion is the quality of a component having encapsulated only a single task or a group
		of logically related tasks.
		""",
	},
	96: {
		'q':  """
		Give an example of a class that can be said to have low cohesion.""",
		'a': """
		A class which implements an XML parser and a random number generator (two strongly unrelated functionalities).""",
	},
	97: {
		'q':  """
		What does designing for low coupling achieve?""",
		'a': """
		Low couple achieves subsystems of discrete components that can be reused independently.""",
	},
	98: {
		'q':  """
		Give an overview of design-by-contract.""",
		'a': """
		Design-by-contract means that the documentation for a function or a class
		represents a contract with a detailed of what the responsiblity of:
		
			- the client code
			- your own function or class.""",
	},
	99: {
		'q':  """
		What are the three import aspects of design-by-contract, give an description of each.""",
		'a': """
		1) preconditions: the conditions that the client must satisfy before calling a function or method
		2) postconditons: the conditions that must be satisfied by the function or method when it has finished executing.
		3) invariants: the conditions that must be satisfied during the whole execution of the function or method.""",
	},
	100: {
		'q':  """
		What is meant by the open/closed principle?""",
		'a': """
		The open/closed principle states that software entities should be open for extension, but
		closed for modification.
		
		I.e. the entity can allow its behaviour to be extended without modifying its source code.""",
	},
	101: {
		'q':  """
		What is meant by the interface segregation principle?""",
		'a': """
		Code should not be forced to depend on methods it doesn't use.
		
		Alternative: Clients should not be forced to depend on interfaces that they do not use.""",
	},
	102: {
		'q':  """
		What is meant by the dependency inversion principle?""",
		'a': """
		High level modules should not depend on low-level modules. Both should 
		depend on abstractions.

		Abstractions should not depend on details. Details should depend on abstractions.
		""",
	},
	93: { # Chapter 8: Gaining Proficiency with Classes and Objects
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
		
			'For performance reasons, it is best to pass objects by const reference
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
			2) The delegated constructor must be the only member initializer in the ctor-initializer list.
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
		C++11 onwards has deprecated the generation of a copy constructor if the class has a user-declared copy constructor
		, the same applies to copy assignment operators.
		
		What should we do if we have a user-defined copy constructor or copy assignment operator but still want
		the compiler generated version?""",
		'a': """
		In both cases, explicitly default one:
		
		MyClass(const MyClass& src) = default;
		MyClass& operator=(const MyClass& rhs) = default;
	""",
	},
	106: { # Chapter 9: Mastering Classes and Objects 
		'q':  """
		Consider:
		
			class Foo
			{
				friend class Bar; (1)
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
		What does a function/method marked with `noexcept` specifiy?""",
		'a': """
		A function/method marked with `noexcept` specifies that it does not 
        throw exceptions.""",
	},
	111: {
		'q':  """
		Which idiom is recommended to implement an exception-safe assignment operator?""",
		'a': """
		The `copy-and-swap` idiom.""",
	},
	112: {
		'q':  """
		What is the rule of five?""",
		'a': """
		The rule of five states:
        
            If you have dynamically allocated memory in your class, then you
            should typically implement:
            
                1) Destructor
                2) Copy constructor and copy assignment operator
                3) Move constructor and moe assignment operator
        """,
	},
	113: {
		'q':  """
		What is the rule of zero? Give examples of things you can do to adopt rule of zero?""",
		'a': """
		i) The rule of zero states that you should design your classes in a way that they
            do not require any of the special member functions from the rule of five.
            
        ii) Examples: Using modern smart pointers instead of old-style dynamically allocated memory
            Using a vector<vector<int>> instead of int** for a 2d array of integers.""",
	},
	114: {
		'q':  """
		i) Do static member functions have a `this` pointer?
		ii) What members can a static member function access?
		iii) How can you call a static member function aside from via the . operator on an instance?""",
		'a': """
		i) Static member functions have no `this` pointer, can only access:
        ii) 1) private or protected static members of the class
            2) private or protected non-static members of the class
            
        You can call static member functions without a class instance,
		just namespace the class name with the scope resolution operator ::.""",
	},
	115: {
		'q':  """
		What does the `inline` do?""",
		'a': """
		The `inline` keyword is a recommendation to the compiler to insert the method/function's body
        directly at the call site of the invoker of the inline method/function.
        
        NB: `inline` is simply a hint and the compiler is free to ignore it.""",
	},
	116: {
		'q':  """
		What is one caveat to using the `inline` keyword on methods that you should bear in mind?
		""",
		'a': """
		Definitions of methods marked as `inline` must be available in every source file
        in which they are called.""",
	},
	117: {
		'q':  """
		What is a static data member in one sentence.""",
		'a': """
		A static data member is a data member associated with a class instead of an object.""",
	},
	118: {
		'q':  """
		What is one 'benefit' of declaring a data member as both `static` and `inline`?
        """,
		'a': """
		The benefit is that you do not have to write them up in the source file (.cpp). Declaring
        them in the header file is sufficient.""",
	},
	119: {
		'q':  """
		When should you declare a data member as `static const`?""",
		'a': """
		When you want 'global' constants that only apply to/are relevant to a specific class.""",
	},
	120: { # Chapter 10: 
		'q':  """
		Which keyword would you mark a class with to prevent inheritance?""",
		'a': """
		`final` e.g
        
            class Base final {};""",
	},
	121: {
		'q':  """
		What's a good rule of thumb with regard to `virtual` and super class methods?""",
		'a': """
		Rule of thumb: Make all (except constructors) virtual (inc. the destructor) to avoid
        problems associated with ommision of the virtual keyword.""",
	},
	122: {
		'q':  """
		True or false:
        
            Adding the `override` keyword for override methods in a derived class is mandatory.""",
		'a': """
		False, however it is highly recommended."""
	},
	123: {
		'q':  """
		With regards to a derive class's data members and overridden methods, what is meant by slicing?""",
		'a': """
		Slicing occurs when you cast an instance of a derived class to a base class, causing a loss of the 
        derived class's data members and overridden methods.
        
        NB: Slicing does not occur when a derived class is assigned to a pointer or 
        reference to a super class.
		
		e.g it does not occur with for example:

			Base* _base = new Derived();
		""",
	},
	124: {
		'q':  """
		What does a vtable (virtual table) introduce overhead?""",
		'a': """
		To call a virtual method, the program needs to perform an extra operation
        by dereferencing the pointer to the appropriate code to execute.""",
	},
	125: {
		'q':  """
		Which keyword can you use to prevent a derived class from overriding
        a method?""",
		'a': """
		`final` e.g
        
            virtual void some_method() final;""",
	},
	126: { # chapter 11: C++ Quirks, Oddities, and Incidentals
		'q':  """
		True or false:
        
            i) You can declare a reference to a reference e.g int& &
            ii) You cannot declare a pointer to a reference e.g int&*
            iii) You can declare a reference to a pointer e.g int*&""",
		'a': """
		    i) False
            ii) True
            iii) True""",
	},
	127: {
		'q':  """
		Consider the following guideline:
        
            Prefer references over pointers, that is, only use a pointer if a reference
            is not possible.
            
        Name a case in which we'd prefer to recieve a pointer over a reference.""",
		'a': """
		If the code receiving the variable becomes the owner of the memory and is thus
        responsible for releasing the memory. Then we must receive a pointer.""",
	},
	128: {
		'q':  """
		i) True or false:
        
            If the member function of a class is marked as constexpr, then it cannot be virtual.
            
        ii) Why?""",
		'a': """
		i) True
        ii) Because virtual functions create a vtable which is used to determine polymorphic dispatch at run time,
        which goes against the purpose of `constexpr` which is compile time determination of a function's result.
        """,
	},
	129: {
		'q':  """
		What is the difference between:
        
            i) External linkage, and;
            ii) Internal/static linkage""",
		'a': """
		    i) The name of a C++ source file is available from other source files
            ii) Internal/static linkages means that the name of a C++ source file IS NOT available from other source files.""",
	},
	130: {
		'q':  """
		i) What's an alternative to using the keyword static to achieve internal linkage?
        ii) Which is the recommended method to achieve internal linkage between
        using the `static` keyword or using your answer to (i)?""",
		'a': """
		i) Using anonymous namespace - variables/functions declared within an anonymous namespace are only
        available to the source file in which they were declared.
        
        ii) The recommended method is using anonymous namespaces.""",
	},
	131: {
		'q':  """
		i) What is the `extern` keyword used for?
        ii) What does the compiler treat a name qualified with `extern` as?
        iii) What implications does your answer to (ii) have for space allocation?
        """,
		'a': """
		i) Making variables globally accessible from multiple source files.
        ii) A declaration.
        iii) This means that the compiler doesn't allocate space for variables.
        """,
	},
	132: {
		'q':  """
		True or False:
        
            Initialization order of nonlocal variables in different source files is well defined.""",
		'a': """
		False.""",
	},
	133: {
		'q':  """
		Which is preferred:
            Pre-C++11 `typedef`s or `using` type aliases?""",
		'a': """
		`using` type aliases""",
	},
	134: {
		'q':  """
		What does <utility>'s std::as_const() function do?""",
		'a': """
		std::as_const() returns a `const` reference version of its reference parameter.""",
	},
	143: { # chapter 12: Writing generic code with templates
		'q':  """
		True or false:
        
            i) The compiler always generates code for all virtual methods of a generic/templatized class
            ii) The compiler always generates code for all non-virtual methods of a generic/templatized class""",
		'a': """
		    i) True
            ii) False, the compiler only generates code for non-virtual methods that are actually called
                for that particular type T.""",
	},
	144: {
		'q':  """
		What extension do some programmers like to give source files that are meant to be included in 
        a header file?""",
		'a': """
		ans: .inl <--""",
	},
	145: {
		'q':  """
		
        i) Why would we want to use explicitly instantiated class templates?
        ii) What is one notable implication of using explicitly instantiated class templates?""",
		'a': """
		i) To restrict the types that client code can use with our generic class.
        ii) The compiler generates code for all methods of the class template, irrespective of
            whether the methods will be methods or not.""",
	},
	146: {
		'q':  """
		True or False:
        
            i) Template parameters have to be data types.
            ii) Template parameters can have default values.""",
		'a': """
		
            i) False
            ii) True
        """,
	},
	147: {
		'q':  """
		True or false:
            Virtual methods and destructors cannot be method templates.""",
		'a': """
	    ans: True""",
	},
	148: {
		'q':  """
		For a nested template copy constructor, which syntax should you use:
        
            i)  template <typenmae T>
                template <typename E>
                
            ii) template<typename T, typename E> """,
		'a': """
		    i)""",
	},
	149: {
		'q':  """
		i) What are alternative implementations of templates called?
        ii) Give an example of the syntax of your answer to (i)""",
		'a': """
		i) ANS: Template specializations
        
        ii) 
        Specialization:
            template<>
            class Grid<const char*>
            
        Where the generalization would be:
            template<T>
            class Grid {// implementation details...}""",
	},
	150: {
		'q':  """
		i) Will a derived class which inhereits from a template (not an instance or specialization)
            result in said derived class being a template?
            
        ii) Will deriving from a specific instantiation of a class template result in a template.""",
		'a': """
		i) yes, the derived class must be a template.
        ii) the derived class in the case need not be a template.""",
	},
	151: {
		'q':  """
		When it comes to templates, when would we want to:
            i) inherit from a template
            ii) specialize a template""",
		'a': """
		    i) When we want to extend implementations and use polymorphism
            ii) When we want to customize implementation for a particular type.""",
	},
	152: {
		'q':  """
		What is the difference between `auto` and `decltype` with regard to 
            reference and `const` qualifiers?""",
		'a': """
		`auto` strips them way, decltype does not.""",
	},

	153: { # Chapter 13: Demystifying C++ I/O
		'q':  """
		What is the difference between a buffered and unbuffered stream?""",
		'a': """
		A buffered stream does not immediately send the data to the destination, but instead,
        it buffers incoming data and then sends it in blocks.
        
        An unbuffered stream, contrastingly, immediately sends data to the destination.""",
	},
	154: {
		'q':  """
		What method can you use to always force a buffered stream to send all its currently buffered
        data to the destination?""",
		'a': """
		`std::cout.flush()`""",
	},
	155: {
		'q':  """
		What is meant by the 'current position' of the stream?""",
		'a': """
		The current position is the position in the stream where the next read or write operation
        will take place.""",
	},
	156: {
		'q':  """
		Give a brief description of the `clog` stream.""",
		'a': """
		A buffered version of cerr, clog writes data to the 'error console'.""",
	},
	157: {
		'q':  """
		i) What is the difference between '\\n' and std::endl?
        ii) What should you be wary of considering your answer to (i)?""",
		'a': """
		i) std::endl add a new line in addition to flushing the buffer
        ii) Excessive buffer flushing could have performance implications""",
	},
	158: {
		'q':  """
		Consider a file as a stream destination.
        
        Which approach tends to be more performant:
        
            1) Writing to data in larger blocks
            2) Writing to data character-by-character?""",
		'a': """
		ANS: (1)""",
	},
	159: {
		'q':  """
		Not all output streams are buffered. Give an example of an output stream
        that does not buffer its output.""",
		'a': """
		ANS: cerr""",
	},
	160: {
		'q':  """
		i) Which method can be called directly on a stream to determine whether or not the stream is
        currently good (i.e. in its normal, usable state).
        
        ii) Does your answer to (i) tell you why the stream is unusable?""",
		'a': """
		i) std::cout.good()
        ii) no.""",
	},
	161: {
		'q':  """
		What does it mean for the following methods to return `true`:
        
            i)  std::cout.bad()
            ii) std::cout.fail()""",
		'a': """
		    i) This means that a fatal error has occurred (as opposed to a non-fatal condition like eof())
            ii) This means that the most recent operation has failed; however, it doesn't say anything about
                the next operations which may succeed or fail.""",
	},
    162: {
		'q':  """
		Given that both good() and fail() return `false` if the end-of-file is reached.
        State the relation between good(), fail() and eof() as a comparison that holds true.""",
		'a': """
		
            good() == (!fail() && !eof())""",
	},
    163: {
		'q':  """
		In the context of C++ streams, what is meant by a 'manipulator'?""",
		'a': """
		Manipulators are objects that make a change to the behaviour of the stream
        instead of, or in addition to, providing data for the stream to work.""",
	},
    164: {
		'q':  """
		All of the stream manipulators stay in effect for subsequent output to the stream until
        they are reset, except one.
            i) State the manipulator which is an exception
            ii) How long does your answer to (i) stay active for?""",
		'a': """
		    i) setw
            ii) setw is only active for the next single output.""",
	},
    165: {
		'q':  """
		std::cout does not immeditate flush for bluffer, does this hold true for std::cin as well?""",
		'a': """
		Not it does not as std::cin does not immediately flush the buffer.""",
	},
    166: {
		'q':  """
		What does a call to std::cin.unget() cause the stream to do?""",
		'a': """
		std::cin.unget() causes the stream to back up by one position, essentially putting
        the previous character read back on the stream.""",
	},
    167: {
		'q':  """
		What does the `std::noskipws` input manipulator tell the stream to do?""",
		'a': """
		std::noskipws tells the stream to not skip whitespace""",
	},
    168: {
		'q':  """
		What is the difference between std::cin.putback() and std::cin.unget()?""",
		'a': """
		    std::cin.putback(): Allows you to take a character as a parameter to be placed on the stream.
            std::cin.unget(): Causes the stream to back up the previous character read on the stream.
            
        Both methods allows you to move backward by one character in an input stream.""",
	},
    169: {
		'q':  """
		What does std::cin.peek() allow you to do?""",
		'a': """
		std::cin.peek() allows you to preview the next value that *would* be returned
        if you were to call std::cin.get().""",
	},
    170: {
		'q':  """
		i) What do string streams provide?
        ii) What is std::ostringstream used for?
        iii) What is std::istringstream used for?""",
		'a': """
		i) string streams provide a way to use stream semantics with std::string objects
        ii) Is used for writing data to an std::string
        iii) Is used to read data from an std::string""",
	},
    171: {
		'q':  """
		Give a brief description of each of the following constants, which may be passed
        as the second argument to a file stream constructor.
        
            i)   std::ios_base::app
            ii)  std::ios_base::ate
            iii) std::ios_base::binary
            iv)  std::ios_base::in
            v)   std::ios_base::out
            vi)  std::ios_base::trunc
        """,
		'a': """
		i)   std::ios_base::app
            - open, and go to the end before each write operation
        ii)  std::ios_base::ate
            - open, and go the the end once immediately after opening
        iii) std::ios_base::binary
            - perform input and output in binary mode as opposed to text mode.
        iv)  std::ios_base::in
            - open for input, start reading from the beginning
        v)   std::ios_base::out
            - open for output, start writing at the beginning, overwriting existing data
        vi)  std::ios_base::trunc
            - open for output, and delete all existing data (truncate)
        """,
	},
    172: {
		'q':  """
		When it comes to file stream modes, give the combination of constants that  
        specify opening a file for output in binary while truncating existing data.""",
		'a': """
		std::ios_base::trunc | std::ios_base::binary | std::ios_base::out""",
	},
    173: {
		'q':  """
		i) When data is requested from an input stream, what happens to its linked output stream?
		ii) Does the same thing happen in the vice-versa case to your answer in i? 
		""",
		'a': """
		i) Its linked output is automatically flushed
		ii) The vice-versa case is also true, this is known as flush-on-access""",
	},
    174: {
		'q':  """
		i) What method do we use do use to link streams?
		ii) Let:
			- `outfile` and `anotheroutfile` be output streams
		Use your answer to (i) to link the two output streams.""",
		'a': """
		i) std::ostream::tie
		i) outfile.tie(&anotheroutfile)""",
	},
    175: {
		'q':  """
		i) True or false:
		
			Bidirectional streams have separate pointers for the read position
			and the write position.
			
		ii) What implications does your answer to (i) have for switching between
			reading and writing?""",
		'a': """
		i) True
		ii) When switching between reading and writing, you need to seek to the
			appropriate position. E.g.
				io_data.seekp(io_data.tellg());
		""",
	},
	176: { # chapter 14: Handling Errors
		'q':  """
		Why should you always document the possible exceptions a function can throw
        in its code documentation?""",
		'a': """
		Because users of my function need to know which exceptions might get thrown
        so they can properly handle them.""",
	},
    177: {
		'q':  """
		State two reasons in favour of throwing exceptions as (exception) objects.""",
		'a': """
		1) Objects convey information by their class name e.g std::runtime_error
        2) Objects can store information, including strings that describe the exceptions.
			For instance, std::runtime_error::what().
		""",
	},
	178: {
		'q':  """
		Why should you always catch exception objects by const reference?""",
		'a': """
		1) In order to avoid object slicing, which can occur when you catch exceptions
        by value.
        2) Also to avoid unnecessary copying.""",
	},
	179: {
		'q':  """
		Why is it a good practice to reset the 'terminate handler' (the callback function) that
        gets passed to <exception>std::set_terminate() to nullptr?""",
		'a': """
		Because the 'terminate handler' applies program-wide, and we may not want
        the previous 'terminate handler' to be used once we've passed exception-handled code.
        
        NB: Using <exception>std::set_terminate() is not a recommended best practice, consider
        try/catch'ing each exception individually wherever possible.""",
	},
	180: {
		'q':  """
		What is one good use of std::set_terminate in professionally written C++?""",
		'a': """
		To set up a crash dump before terminating the process. This crash dump can then
        be loading into a debugger to allow you to figure out what the uncaught exception was,
        and what caused it.""",
	},
	181: {
		'q':  """
		What does C++ do when a function is marked `noexcept` but throws and exception anyway?""",
		'a': """
		C++ calls <exception>std::terminate() to terminate the application.""",
	},
	182: {
		'q':  """
		i) When a second exception is thrown before the first exception has been caught, what happens to the
        first exception?
        ii) What can serve as a solution to avoid the problem posed by your answer to (i)
        """,
		'a': """
		i) All information about the first exception is lost.
        ii) Nested exceptions. Use <exception>std::throw_with_nested()""",
	},
	183: {
		'q':  """
		Consider:
            size_t array_size = std::numeric_limits<size_t>::max();
            
        Declare a pointer to int `ptr` with array size `array_size` in a way that guarantees that
        `ptr` will be null if we fail to allocate memory?
        """,
		'a': """
		int* ptr = new(nothrow) int[integer_count];
        """,
	},
	184: {
		'q':  """
		If an exception leaves the constructor, will the destructor be automatically called?""",
		'a': """
		No.""",
	},
	185: {
		'q':  """
		Let:
            MyClass be a class. Write the boilerplate for the MyClass constructor which implements the
                'function-try-block' feature, catching for std::exception.""",
		'a': """
		MyClass::MyClass()
        try
            : <ctor-initializer>
        {
            /* -- constructor body */
        }
        catch (const std::exception& e)
        {
            /* Exception-handling logic. */
        }
        """,
	},
	186: { # Chapter 16: Overloading C++ Operataors
		'q':  """
		Name a few operators which you CANNOT overload?""",
		'a': """
		    1) operator.          (member access)
            2) operator sizeof    
            3) operator ::        (scope resolution)
            4) operator ?:        (ternary)
        """,
	},
    187: {
		'q':  """
		What is the main difference between overloading an operator as:
            i) a method of a class; and
            ii) a global function""",
		'a': """
		Overloading operators as a member of your class - the LHS must always
			be the data type of that class.

		Overloading operators as a global function - the LHS can be an object
			of a different type (other than that class).
        """,
	},
    188: {
		'q':  """
		i) What does Gregoire recommend with regard to choosing whether to overload operators as
        methods or as global functions?
        
        ii) Why is your answer to (i) advantageous?""",
		'a': """
		i) Make every operator a method unless you must make it a global function.
        ii) These methods can be marked as virtual, which global operators cannot. Useful
            if you plan to write overloaded operators in an inheritance tree.""",
	},
    189: {
		'q':  """
		If your overloaded operator constructs a new object to be returned, should we return
        that new object:
            1) By reference
            2) By value""",
		'a': """
		2) By value""",
	},
    190: {
		'q':  """
		i) What is `operator,` known as?
        ii) What is it responsible for?""",
		'a': """
		i) operator, is known as the comma/sequencing operator
        ii) It is resposible for separating expressions in a single statement delimited by a comma
            guaranteeing that they are evaluated left to right.""",
	},
    191: {
		'q':  """
		Name two cases of when you'd want to overload the `operator()` - function call operator?""",
		'a': """
		1) When you want objects to behave like function pointers.
        2) For multidimensional array access, since [] can only have one index.""",
	},
    192: {
		'q':  """
		i) Why should you avoid overloading operator&& and operator|| ?
        ii) Explain why your answer to (i) occurs.""",
		'a': """
		i) Because you lose short-circuit evaluation if you do so.
        ii) You lose short-circuit evaluation because both the LHS and the RHS
        have to be evaluated before they can be bound to the parameters of your overloaded
        && and ||.
        """,
	},
    193: {
		'q':  """
		i) What do we call objects of a class which has overloaded the operator() - function call operator?
        ii) True or false:
            We can only overload the operator() as a static method in a class""",
		'a': """
		i) Function objects/functors.
        ii) False. Only as a non-static.
        """,
	},
    194: {
		'q':  """
		Consider the following warning from Gregoire:
        
            Whenever you overload `operator new`, overload the corresponding form of
            `operator delete`.
            
        Why is this guideline important?""",
		'a': """
		Because if you do not overload the corresponding `operator delete`, the memory
        will be freed according to the built-in semantics, which may not be compatible.""",
	},
	195: { # Chapter 16: Overview of the C++ Standard Library 
		'q':  """
		True or false:
            The use of any functionality provided by C headers is discourages in
            favour of true C++ functionality.""",
		'a': """
		True.""",
	},
	196: {
		'q':  """
		In which Standard Library header would you find functionality for formatting
        data such as numbers and dates according to rules of a certain country or region?""",
		'a': """
		<locale>""",
	},
    197: {
		'q':  """
		In which Standard Library header would you find functionality for regular expressions?""",
		'a': """
		<regex>""",
	},
    198: {
		'q':  """
        Consider the following bad practices:

		    1) Not deleting the object at all (failing to free the storage)
            2) A piece of code deleting the storage while another piece of code is still pointing
                to that storage.
                
                
        Which ones lead to i) memory leakage ii) dangling pointer""",
		'a': """
		i) (1) leads to memory leaking as objects will accumulate and take up space that is
                not used.
        ii) (2) leads to dangling pointers at we are pointing to storage that is either no longer in use
                or had been reallocated for another purpose.
        """,
	},
    199: {
		'q':  """
		Out of:
            1) std::shared_ptr
            2) std::weak_ptr
            3) std::unique_ptr
            
        i) Which smart pointer is NOT thread-safe is all cases?""",
		'a': """
		i) std::unique_ptr is not always thread-safe. Consider using std::atomic_exchange""",
	},
    200: {
		'q':  """
		State three headers in which exception support functionality is defined.
        """,
		'a': """
		1) <exception>
        2) <stdexcept>
        3) <system_error>
        """,
	},
    201: {
		'q':  """
		In which Standard Library header would you find functionality for working with time?""",
		'a': """
		<chrono>""",
	},
    202: {
		'q':  """
		In which Standard Library header would you find functionality for working with
        variable number of arguments?""",
		'a': """
		<initializer_list>""",
	},
    203: {
		'q':  """
		Outline the affordances of the following classes that were introduced in C++17:
        
            1) std::optional
            2) std::variant
            3) std::any
        """,
		'a': """
		    1) std::optional - holds a value for a specific type, or nothing.
            2) std::variant - can hold a single valueof one of a given set of types, or nothing
            3) std::any - a class that can contain a single value of any type.
        """,
	},
    204: {
		'q':  """
		To which Standard Library header would you turn to for filesystem support?""",
		'a': """
		<filesystem>""",
	},
    205: {
		'q':  """
		Define amortized constant time.""",
		'a': """
		A way of measuring the average big-O as the number of operations tends to infinity.
        So if an operation is said to have amortized constant time, that means that in the overwhelming
        majority of cases we have O(1), but occasionally we may have O(N) <- due to resizing an std::vector e.g.""",
	},
    206: {
		'q':  """
		True or false:
        
            For std::priority_queue, removing an element with a priority tie with another
            element in well-define. """,
		'a': """
		False""",
	},
    207: {
		'q':  """
		Name two cases in which an std::set would be an viable option over an std::vector
        or an std::list?""",
		'a': """
		Case 1: If you need ordered elements and want equal performance for insertion, deletion and lookup.
        Case 2: If you want to enfornce that there are no duplicate elements.""",
	},
    208: {
		'q':  """
		Consider and explain the usage of <algorithm>'s std::clamp:
		
		template<class T, class Compare>
		constexpr const T& clamp( const T& v, const T& lo, const T& hi, Compare comp );
		""",
		'a': """
		std::clamp checks whether a value `v` is between a given minimum `lo` and a given
		maximum `hi`. 
		
		Return:
			a reference to `lo` if v < lo.
			a reference to `hi` if v > hi.
			Otherwise, return a reference to `v`.
		""",
	},
    209: {
		'q':  """
		True or false:
		
			The standard library guarantees thread safety for accessing containers simultaneously
			from multiple threads.""",
		'a': """
		""",
	},
	210: { # chapter 19: String Localization and Regular Expressions
        "q": """
        How does C++ store ASCII?""",
        "a": """
        ASCII is a 7-bit set usually stored in an 8-bit `char` type.""" 
    },
    211: {
        "q": """
        What is meant by making your source code localizable?""",
        "a": """
        It means to make your source code locale aware i.e to output different
        language translations depending on the locale in which your program is running.""" 
    },
    212: {
        "q": """
        What is the wchar_t used for in C++?""",
        "a": """
        wchar_t is used for holding a wide character. This allows for storing non-ASCII (US) characters
        such as Japanese and Arabic.""" 
    },
    213: {
        "q": """
        i) True or false:
        
            The C++ standard defines a size for wchar_t i.e compilers always use the same amount of bits.
            
        ii) What implications does your answer to (i) have for writing cross-platform code?""",
        "a": """
        i) False. Some compilers use 16 bits while others use 32 bits.
        
        ii) When writing cross-platform code, it is not safe to assume that wchar_t is of 
            a particular size.""" 
    },
    214: {
        "q": """
        i) When working with wchar_t, what should we prefix string and character literals with
        to indicate that a wide-character encoding should be used?
        
        ii) let my_wide by of type wchar_t. Define my_wide and use your answer to (i) to
            appropriately assign the character 'm'.
            """,
        "a": """
        i) We should prefix L e.g L'e'.
        
        ii) wchar_t my_wide = L'm';
        """ 
    },
    215: {
        "q": """
        i) What is the wide version of the std::string class?
        
        ii) Name two additional string classes.""",
        "a": """
        i) std::wstring
        
        ii) std::u16string, std::u32string
        """ 
    },
    216: {
        "q": """
        What is the benefit of using char16_t and char32_t instead of wchar_t?""",
        "a": """
        Benefit: char16_t is guaranteed to be at least 16 bits, char32_t is guaranteed to be at least 32 bits.
            This is independent of the compiler.
            
        Unlike wchar_t where the bit size is compiler-dependent i.e there is no minimum size guarantee for wchar_t.""" 
    },
    217: {
        "q": """
        Give a brief description of each of the following supported string prefixes:
        
        i) u8
        ii) u
        iii) U
        iv) L

        BONUS Q: Can all of these string literals be combined with the raw string literal prefix `R`?
        """,
        "a": """
        i) u8 - A `char` string literal with UTF-8 encoding.
        ii) u - A `char16_t` string literal.
        iii) U - A `char32_t` string literal.
        iv) L - A `wchar_t` string literal with a compiler-dependent encoding.
        
        BONUS ANS: Yes, they can. E.g

        const char* wchar_t s1 = LR"(Raw wide string literal.)";
        """ 
    },
    218: {
        "q": """
        i) What is the term for the C++ mechanism that groups specific data about a particular set of
        cultural parameters?
        
        ii) What is the term for an individual component of a <answer_to_i>, such as a date format, time
        format, number format and so on?""",
        "a": """
        i) Locale.
        
        ii) Facet.
        """ 
    },
    219: {
        "q": """
        For ECMAScript regular expressions, the `.` wild card character can be used to match
        any character except <fill_blank>?""",
        "a": """
        The newline character \n
        """ 
    },
    220: {
        "q": """
        i) What is meant by a:
            a) greedy regular expression?
            b) non-greedy regular expression?
        
        ii) What can you do to make a regular expression non-greedy?""",
        "a": """
        i)
            a) A greedy regular expression is one that finds the longest match possible.
            b) A non-greedy regular expression repeats its pattern as few times as possible
                while still matching the remainder of the regular expression.

        ii) In order to make a regular expression non-greedy, a `?` can be added behind the
            regex quantifier (?, *, {n, m}, +) e.g for the input: aaabbbb

        Greedy: (a+)(ab)*()        ---matches---> "aaa" "" "bbb"
        Non-greedy: (a+?)(ab)*(b+) ---matches---> "aa" "ab" "bb"
        """ 
    },
    221: {
        "q": """
        i) When it comes to regex, what do back references allow for?
        
        ii) Break down the following regular expression:
            (\d+)-.*-\1
        """,
        "a": """
        i) Back references allow you to reference a captured group inside the regular expression itself.
        
        ii)
            a) (\d+) --> one or more digits
            b) -     --> a dash
            c) .*    --> zero or more wild card characters (except newline)
            d) -     --> a dash
            e) \1    --> Exactly the same digits captures by (a)
        """ 
    },
    222: {
        "q": """
        i) What is meant by positive lookahead.
        ii) What is meant by negative lookahead.

        iii) Consider the syntax:
            a) ?! b) ?=
        Which denotes positive lookahead, and which denotes negative lookahead.

        """,
        "a": """
        i) Positive lookahead - we check whether the following characters match the regular expression
            but the lookahead pattern is not consumed (i.e part of the match).

        ii) Negative lookahead - we check whether the following characters DO NOT match the regular expression
            but the lookahead pattern is not consumed (i.e part of the match).

        iii) a) negative lookahead b) positive lookahead.
        """ 
    },
    223: {
        "q": """
        In terms of regular expression (negative and positive) lookaheads, break down the following regex's:
        
        i) a(?!b)
        ii) a(?=b)
        """,
        "a": """
        i) a(?!b) denotes negative lookahead, so we match all `a` that DO NOT HAVE a consecutive b.
            Note: b is not consumed i.e it will not be part of the match.
            
        ii) a(?=b) denotes positive lookahead, so we match all `a` that DO HAVE a consecutive b.
            Note: b is not consumed i.e it will not be part of the match.
        """ 
    },
    224: {
        "q": """
        What is the difference between <regex>'s:
        
            1) std::regex_iterator
            2) std::regex_token_iterator""",
        "a": """
            1) std::regex_iterator - iterates through every matched pattern
            2) std::regex_token_iterator - can be used to automatically iterate over all
                or selected capture groups across all matched patterns.
        """ 
    },
	225: { # Chapter 20: Additional Library Utilities
        "q": """
        What does the Ratio library allow you to do?""",
        "a": """
        The Ratio library allows you to exactly repesent any finite rational
        number that you can use at compile time.
        """ 
    },
    226: {
        "q": """
        i) Why can't we use standard arithmetic operators for the std::ratio
        objects?
        
        ii) Name the alternative template implementations of standard arithmetic
            operators for std::ratio objects.""",
        "a": """
        i) Because all operations need to happen at compile time, so standard
            arithmatic operators that may calculate at them at runtime may be
            insufficient.
            
        ii)
            1) std::ratio_add
            2) std::ratio_subtract
            3) std::ratio_multiply
            3) std::ratio_divide    
        """ 
    },
    227: {
        "q": """
        Consider the template of std::chrono::duration
        
            template<typename Rep, typename Period = std::ratio<1>>
            class duration {...};
        
        i) What does `Rep` represent
        ii) What does `Period` represent.""",
        "a": """
        i) The underlying data type to be wrapped around e.g. int64_t, float
        ii) The rational constant representing the tick period i.e the time in seconds between
        to ticket. Examples include std::ratio<1, 60>.
        
        """ 
    },
    228: {
        "q": """
        From the perspective of <chrono>, what does a `clock` class consist of?
        """,
        "a": """
        A `clock` class consists of:
            1) a time_point
            2) a duration
        """ 
    },
    229: {
        "q": """
        i) What are the three `clock`s in <chrono> that are defined by the standard?
        ii) Which of the three should you avoid and why?""",
        "a": """
        i) 1) system_clock 2) steady_clock 3) high_resolution_clock
        ii) You should avoid high_resolution_clock because depending on your compile,
            it is possible for the high_resolution_clock to be a synonym for either
            `steady_clock` or `system_clock`.
            
        """ 
    },
    230: {
        "q": """
        What are the three big components defined in the <random> header file?
        """,
        "a": """
        1) random number engines
        2) random number engine adapters
        3) distributions
        """ 
    },
    231: {
        "q": """
        Consider <random>. Describe the responsibilities of the following components:
        
        1) random number engines
        2) random number engine adapters
        3) distributions
        """,
        "a": """
        1) random number engines - responsible for generating the actual random numbers
                and storing the state for generating subsequent random numbers.
        2) random number engine adapters - modifies the results of a random number engine
                you associate it with.
        3) distributions - determines the range of the generated random numbers and how
            they are mathematically distributed within that range.
        
        """ 
    },
    232: {
        "q": """
        i) True or false:
        
            You can store a reference in an instance of std::optional.

        ii) What two methods can we use to create an std::reference_wrapper<T> and
            std::reference_wrapper<const T> respectively.
        """,
        "a": """
        i) False
        
        ii) std::ref, std::cref.
        """ 
    },
	233: { # Chapter 17: Understanding containers and iterators
		'q':  """
		Standard library containers use value semantics on elements.
        
        That is, they:
            1. store a copy of elements that they are given
            2. assign to elements with the assignment operator
            3. destroy elements with the destructor.
            
        What implications does this mean for writing classes that you
        intend to use with the Standard Library?""",
		'a': """
		You need to make sure that they are copyable i.e the copy contructor
        and copy assignment operators work as intended.""",
	},
	234: {
		'q':  """
		i) If you prefer using reference semantics. What is an alternative
        to storing pointers to elements in a SL container?
        
        ii) What functions can help us achieve (i) and in which header are they defined?""",
		'a': """
		i) Storing `std::reference_wrapper`'s
        
        ii) std::ref(), std::cref(), defined in the <functional> header.
        """,
	},
	235: {
		'q':  """
		Give an example of a move-only type i.e a type with is not
        copyable.""",
		'a': """
		std::unique_ptr
        """,
	},
	236: {
		'q':  """
		True or false:
            If a move constructor/assignment is NOT marked as `noexcept`,
            it will still be used in move construction/assignment
            of elements in a SL container.""",
		'a': """
		False""",
	},
	237: {
		'q':  """
		What is <iterator>'s std::distance used for?""",
		'a': """
		It is used for computing the distance between two iterators
        of a container.""",
	},
    238: {
		'q':  """
		Which of the following Standard Library class types support
        iteration over their elements?
        
            1) sequential containers
            2) ordered associative containers
            3) unordered associative containers
            4) container adapters
            5) bitset
            
        """,
		'a': """
		(1), (2), (3)""",
	},
    239: {
		'q':  """
		True or false:
        
            For getting the begin, end, cbegin, cend, rbegin, rend... etc
            
        It is recommended to use the non-member functions e.g std::begin()
        over their equivalent member functions e.g std::vector<int>::begin().""",
		'a': """
		True""",
	},
    240: {
		'q':  """
		Why is it preferred to use pre-increment instead of post-increment when
        iterating SL container iterators?""",
		'a': """
		Pre-increment i.e ++iter can simply return a reference to an int.
        Post-increment i.e iter++ must return a new iterator object.
        """,
	},
    241: {
		'q':  """
		What is the difference between:
            1) std::vector::size()
            2) std::vector::capacity()
            
        """,
		'a': """
		    1) std::vector::size() - returns the number of elements in a vector
            2) std::vector::capacity() - returns the number of elements the vector
                can hold without reallocation""",
	},
    242: {
		'q':  """
		What does <iterator>'s std::data() global function do?""",
		'a': """
		It returns a pointer to the block of memory containing the elements
        of the range.
        """,
	},
    243: {
		'q':  """
		i) Which category of iterator does an std::list implement?
        ii) What implications does your answer to (i) have for iterator arithmetic?""",
		'a': """
		i) bidirectional
        ii) Implications: you can traverse through the elements of an std::list
        with ++p or --p but you cannot use for example p+n or p-n.
        """,
	},
    244: {
		'q':  """
		True or false:
		
			Comparing two std::vector's with:
				1) operator==
				2) operator!=
				3) operator<, operator<=
				4) operator> operator >=

			Requires that the individual elements be comparable with the same respective
			operator. Therefore, if you intend to store ojects of a custom class in an
			std::vector and want those comparisons, operators (1)-(4) must be defined.
				
		""",
		'a': """
		True""",
	},
    245: {
		'q':  """
		What is a bit field?""",
		'a': """
		A bit field is a series of bits where individual bits or clusters of bits mean different
		things.
		
		Example usages include:
			- reducing the memory size of class/struct if possible
			- setting the stream flags when opening a file
			""",
	},
    246: {
		'q':  """
		 How can we force alignment in a struct with bitfield members?""",
		'a': """
		Force alignment in a struct with bitfield members is possible
		by including an unnamed bit field of size 0.
		
		Essential a way of using up the padding bits.
		""",
	},
    247: {
		'q':  """
		Consider the following struct:
		
			struct Node
			{
				static unsigned int x:5;
			};
		
		i) Can we compile Node?
		ii) If not, why not.
		""",
		'a': """
		i) No, we cannot compile Node.
		ii) Because bit fields cannot be static.
		""",
	},
    248: {
		'q':  """
		Consider the statement:
		
			Many C++ experts recommend avoiding std::vector<bool> in favour of the std::bitset.
			If you need a dynamically-sized bit field, then it's recommended to use 
			std::vector<T>.
			
		State the two types of T.""",
		'a': """
		1) std::int_fast8_t 
		2) unsigned char
		""",
	},
    249: {
		'q':  """
		i) What is the key difference between std::array and std::vector?
		ii) What is the purpose of your answer to (i)
		
		""",
		'a': """
		(i) Key difference: std::array is of fixed size. Unlike std::vector, it cannot
			grow or shrink in size.

		(ii) The purpose of std::array's fixed sizing is to allow the std::array to
			be allocated on the stack, rather than always demanding heap access as
			std::vector does.
		""",
	},
    250: {
		'q':  """
		True or false:
		
			For std::priority_queue, if two elements have equal priority, their relative
			order in the queue is well defined.""",
		'a': """
		False, it is undefined.
		""",
	},
    251: {
		'q':  """
		Why are we unable to use std::list as the underlying container for the std::priority_queue
		container adapter?
		""",
		'a': """
		Because std::priority_queue requires random access to its elements, which std::list does not
		provide.
		""",
	},
    252: {
		'q':  """
		With std::priority_queue, how can we customize priority?""",
		'a': """
		For std::priority_queue by default priority is determined according to `operator<`
		so we can customize priority by defining the operator< for the contained element
		data type.
		""",
	},
    253: {
		'q':  """
		Consider the excerpt:
		
			Single failures on a system can often cause multiple errors to be generated
			from different components. A good error-handling system uses error correlation
			[...]
			
		i) What is meant by error correlation
		ii) Which Standard Library class would be a good candidate for a simple error
			correlator given your answer to (i)
		""",
		'a': """
		i) Error correlation is a means to process the most important errors first 
			(not to be confused with statical concepts of similar naming)
		ii) Since error correlators prioritize the most important errors, a good
			Standard Library class candidate would be std::priority_queue.
		""",
	},
	254: {
		'q':  """
		True or false:
		
		For an std::map:

			1) Insertion is based on the key
			2) Lookup is based on the value
			3) Deletion is based on both the key and the value
		""",
		'a': """
			1) True
			2) False
			3) False, Deletion is based only on the key
		
		""",
	},
    255: {
		'q':  """
		What is the computational complexity of std::map for:
		
			1) Insertion
			2) Deletion
			3) Lookup
			
		And why?""",
		'a': """
		All of (1), (2) and (3) take logarithmic time O(log(n)) as they are based on
		some form of balanced tree implementation, such as a red-black tree.
		
		""",
	},
    256: {
		'q':  """
		Consider the following snippet:

			std::map<int, std::string> mapping;
			auto ret = mapping.insert({1, "a string"}); (1)


		i) give the full data specification for variable `ret`
		ii) How can we use your answer to (i) to confirm whether line (1)
			was successful?
		
		""",
		'a': """
		i) std::pair<std::map<int, std::string>::iterator, bool> ret;
		ii) By check ret.second (evaluates to true if insertion was successful, false if it wasn't)
		""",
	},
	257: {
		'q':  """
		i) True or false:
			For an std::map, you can modify elements through non-const
			`std::map<T1, T2>::iterator`s, but the compiler generate an
			error if you try to modify the key of an element, even through a non-const
			iterator.

		ii) Why did you go with your answer to (i)?
		""",
		'a': """

		i) True

		ii) Because if it was false we would be destroying the sorted order of the
			elements in the std::map.
		""",
	},
    258: {
		'q':  """
		Consider:
		
			std::map<int, int> src = \{ {1, 11}, {2, 22} };
			std::map<int, int> dst = \{ {2, 22}, {3, 33}, {4, 44}, {5, 55} };
			dst.merge(src); (1)

		i) What elements are contains in `src` after line (1)?
		ii) Why?
			
		""",
		'a': """
		i) `src` has \{2, 22}
		ii) Because elements in the source that are duplicates to elements in the 
			destination container are left in the source.
		
		""",
	},
    259: {
		'q':  """
		What criteria need to be satisfied for a hash function to be considered a 
		`perfect hash`?""",
		'a': """
		1) The hash function does not create any collisions
		2) The hash function must have constant O(1) lookup time
		""",
	},
	260: {
		'q':  """
		How would you go about writing a hash function for your user-defined data type?
		""",
		'a': """
		You would write a specialization of <functional>'s std::hash template
		for your user-defined data type.
		This specialization needs an implementation of the function call operator
		and returns the hash of a given user-defined data type instance.
		""",
	},
    261: {
		'q':  """
		True or false:
		
			Normally, you must not put anything in the `std` namespace; however,
			`std` class template specializations are an exception to this rule.
		""",
		'a': """
		True""",
	},
    262: {
		'q':  """
		True or false:
		
		Functions such as std::begin() and std::end() work with:
			1) Statically allocated C-style arrays accessed through pointers.
			2) Statically allocated C-style arrays not accessed through pointers.
			3) Dynamically allocated C-style arrays.
		""",
		'a': """
			1) False
			2) True
			3) False
		""",
	},
	263: {
		'q':  """
		State three reasons as to why <bitset>'s std::bitset is not considered
		to be a true Standard Library container?""",
		'a': """
		1) std::bitset is of fixed size
		2) std::bitset is not templatized on an element type
			(it is templatized on the number of bits it stores)
		3) std::bitset does not support iteration
		""",
	},
	264: { # Chapter 18 - Mastering Standard Library Algorithms
		'q':  """
		What do we call a class that overloads the function call operator i.e
        `operator()`?
        """,
		'a': """
		A function object or a functor.
        """,
	},
    265: {
		'q':  """
		Which of the following statements are correct:
        
        If <algorithm>'s std::find() fails to find an element it returns:

            1) An iterator equal to the end of the underlying container
            2) And iterator equal to the `end` iterator specified in the function call. 
        """,
		'a': """
		(2) is correct.
        """,
	},
	266: {
		'q':  """
		Some Standard Library containers, such as std::map and std::set
        provide their own versions of `find` as class methods.

        Why should you use the class method versions of `find` as opposed
        to the generic std::find as defined in <algorithm>? Give a concrete example.
        """,
		'a': """

        ANS: Because the class method versions are faster. For example, for std::map,
        the generic std::find runs in O(N) time. While std::map::find() is O(log(n)).
		""",
	},
    267: {
		'q':  """
		i) What is <functional>'s std::function used for?
        ii) Consider the following generic syntax:

            std::function<R(ArgTypes...)>

        Use this template to assign the function:
            void func(int num, const std::string& _str);

        To variable `f1`
        
        """,
		'a': """
		i) std::function can be used to point to:
            a) a function
            b) a function object
            c) a lambda expression
        Basically anything that is callable.

        ii) std::function<void(int, const std::string&)> f1 = func;
        """,
	},
    268: {
		'q':  """
		Consider the following snippet:
        
            const double data = 1.23;
            auto capturing_lambda = [data]\{ std::cout << data << std::endl; \}; (1)

        Does the variable `data` retain or loss the constness in the lambda body?
        """,
		'a': """
		`data` in the lambda body retains constness. In general,
        variables captured from the enclosing scope retain the constness of the
        variables that the lambda captures in the capture block.
        """,
	},
    269: {
		'q':  """
		i) True or false:
        
            For a lambda expression, the function call operator is marked as `const`
            by default. 

        ii) What implications, if any, does your any to (i) have for non-const variables
            captured by value in a lambda expression.

        iii) What specification can we add to the lambda if we do not want your answer
            to (ii)
        """,
		'a': """
		i) True

        ii) This means that even if you capture a non-const variable by value in a lambda
            expression, the lambda expression is not able to modify this copy.
        
        iii) If we want to modify the value we capture, we must mark the lambda as mutable
            i.e [data] () mutable \{data *= 2; std::cout << data << std::endl; \};
        """,
	},
    270: {
		'q':  """
		For lambda expressions, there are two ways to capture all variables from
        the enclosing scope.

        Explain the following capture specifications:
            1) [=] and;
            2) [&]
        
        """,
		'a': """
		1) [=] : Captures all variables from the enclosing scope by value
        2) [&] : Captures all variables from the enclosing scope by reference
        
        """,
	},
	271: {
		'q':  """
		What are generic lambda expressions?
        """,
		'a': """
		Generic lambda expressions are lambda expressions which use `auto`
        as a type in the parameter list. E.g

        auto add = lambda[](auto x, auto y) { return x+y; }
        """,
	},
    272: {
		'q':  """
		Why should you avoid using std::bind1st, std::bind2nd, std::mem_func??""",
		'a': """
		Because those functions have been officially removed frrom the C++17 standard.""",
	},
    273: {
		'q':  """
		State the five arithmetic functor class templates for binary arithmetic operations
        as defined in <functional>
        """,
		'a': """
		1) std::plus
        2) std::divides
        3) std::minus
        4) std::multiplies
        5) std::modulus
        """,
	},
    274: {
		'q':  """
		i) What are transparent operator functors?
        
        ii) True or false:
            It is recommended to always use the transparent operator functors.
        """,
		'a': """
		i) Transparent operator functors are operator functors which allow
            you to omit the template type.

            E.g. std::multiplies<>() instead of std::multiplies<int>()
        
        ii) True
        """,
	},
    275: {
		'q':  """
		State all 6 of the comparison functor class templates as defined in <functional>
        """,
		'a': """
		1) std::equal_to
        2) std::not_equal_to
        3) std::less
        4) std::greater
        5) std::less_equal
        6) std::greater_equal
        """,
	},
	276: {
		'q':  """
		State the five non-modifying counting algorithms as defined
		in <algorithm>.
        """,
		'a': """
		1) std::all_of()
		2) std::any_of()
		3) std::none_of()
		4) std::count()
		5_ std::count_if()
		""",
	},
    277: {
		'q':  """
		True or false:

		With std::copy(), as with all modifying algorithms, std::copy() can indeed insert
		elements into the destination container.
		""",
		'a': """
		False. std::copy(), like all modifying algorithms, can only overwrite whatever
		elements are there already.
		""",
	},
    278: {
		'q':  """
		i) What does std::remove not actually remove the elements in a container
		i.e it instead partitions the container into two sets; 
			1) the elements to be kept; THEN
			2) the elements to be removed.

		ii) Name the idiom that uses std::remove/std::remove_if in order to 
			get the removal functionality from the container.
		
		""",
		'a': """
		i) Algorithms such as std::remove have access only to the iterator abstaction,
			not to the container. Thus, the std::remove algorithm cannot actually remove
			the elements.

		ii) remove-erase
		""",
	},
    279: {
		'q':  """
		Why is sorting (e.g with <algorithm>'s std::sort) not relevant for:

			1) std::set
			2) std::unordered_map
		""",
		'a': """
			1) std::set is an ordered associative container and they already maintain
				elements in a sorted order
			2) std::unordered_map is an unordered associative containers and have no
				concept of sorting.
		""",
	},
    280: {
		'q':  """
		What is the return value of <algorithm>'s:
		
			1) std::is_sorted()
			2) std::is_sorted_until()
		""",
		'a': """
			1) std::is_sorted returns `true` if a given range is sorted
			2) std::is_sorted_until returns an iterator such that everything before
				this iterator is sorted.
		
		""",
	},
	281: {
		'q':  """
		Explain the usage of <algorithm>'s std::clamp() and what it returns.

		""",
		'a': """
		std::clamp(v, lo, hi) is a helper function that you can use to determine
		if a given v in inside the range (lo, hi) <- both ends exclusive.

		If returns:
			- A reference to `lo` if v < lo
			- A reference to `hi` if v > hi
			- A reference to v otherwise. 
		
		""",
	},
}