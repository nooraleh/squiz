things_i_need_to_go_over = {
	1: "passing multidimensional arrays to functions in c",
	2: "structs, pointers and memory allocation",
	3: "The entire priority of operators in C, you should easily know what ++b.a[2]-- should give, for example.",
	4: "How to malloc for various things inc. an array of structs.",
	5: "An array of functions in C",
	6: "Practice bitwise operations in C - find exercises.",
	7: "Reading/writing streams exercises in C. You should be able to easily do exercises previous of https://edube.org/quiz/c-essentials-part-2/c-essentials-part-2-module-7-quiz",
	8: "Size of common data types in bytes. I.e. when you put in sizeof(data_type)",
	9: "Common file processing functions and their expected parameters",
	9: "values of SEEK_SET, SEEK_CUR, SEEK_END",
	10: "preprocessor directives",
	11: "switch/case statements in C",
	


	# c++
	12: "common c++ manipulators: scientific, fixed etc",
	13: """
	c++ data types:

	This computing environment uses:
	1 bytes for chars
	2 bytes for shorts
	4 bytes for ints
	8 bytes for longs
	4 bytes for floats
	8 bytes for doubles
	1 byte for bools
	8 bytes for pointers
	""",
	14: """
	
	type promotion rules
	
	data of type char or short int will be converted to type int (this is called an integer promotion);
	data of type float undergoes a conversion to type double (floating point promotion);
	if there’s any value of type double in the expression, the other data will be converted to a double;
	if there’s any value of type long int in the expression, the other data will be converted to long int;
	""",
	15: """
	
	string methods
	
	.compare, .substr, .size, .length, .find, .capacity,
	.max_size, .reserve, .resize, .clear, .empty, .append, .push_back, .insert.
	.assign, .erase

	S.compare(substr_start, substr_length, other_string,  other_substr_start, other_substr_length)
	""",
	16: "definitely revise array of arrays: initialization, mem allocation, for looping etc",
	17: "revise type conversions used in binary operations",
	18: "floating points in c++",
	19: """ component visibility rules ---
	1. a static component accesses a static component = always possible
	2. a static component accesses a non-static component = e.g a static function calling a non-static function. This fails.
	3. a non-static component accesses a static component = always possible.
	4. a non-static component accesses a non-static component = always possible.
	
	""",
	20: """ class friendship rules ---
		1. a class may be a friend of many classes
		2. a class may have many friends
		3. a friend’s friend isn’t my friend
		4. friendship isn’t inherited – the subclass has to define its own friendships

		function friendship rules --

		1. a friendship declaration must contain a complete prototype of the friend function (including return type); a function with the same name, but incompatible in the sense of the parameters’ conformance, will not be recognized as a friend
		2. a class may have many friend functions
		3. a function may be a friend of many classes
		4. a class may recognize as friends both global and member functions
	
	""",
	21: """ Dynamic Casting rules ---
		1. dynamic_cast is used at run time to find out the correct down-cast
		2. Needs at least one virtual function in the base class to work.
		3. If dynamic_cast is successful, dynamic_cast returns a value of type new_type
		4. If the cast fails and new_type is a pointer, it returns a null pointer of that type
		5. If the cast fails and new_type is a reference type, is throws an exception that matches a handler of type std::bad_cast.
	""",
	22: """ Static Casting rules ---
		1. static casting a subclass (privately inherited) pointer to a superclass pointer fails at compile time
		2. static_cast can be used for all upcasts, but not for confused down casts
		3. static_cast should be preferred when converting to void* or from void*
	""",
	23: """ Const Casting rules ---
		1. The expression const_case<T>(v) can be used to change the const or v
	""",
	24: """ to revise ---
		Revise public, protected and private inheritance combinations
	""",
	25: """ to revise ---
		Go over the exception class hierarchy from module 3
	""",
	26: """
	quirk to watch out for: 
	"""


}

knowledge = {
	'C': {
		1: {
			"q": "Define portability with respect to high level programming languages",
			"a": "It is the feature of programs written in high level programming languages being able to be translated into any number of different machine languages.",
		},
		2: {
			"q": "Define compilation",
			"a": "It is the process of translating from a high-level language to machine language.",
		},
		3: {
			"q": "Define an executable file",
			"a": "It is a file containing the translation of your high-level program in machine language.",
		},
		4: {
			"q": "What is meant by linking?",
			"a": "It is the phase of joining/glueing executable code with other executable code.",
		},
		5: {
			"q": """What is the name of lines at the top of a C source file e.g:
			#include <stdio.h> ?
			#include <stdlib.h>
			""",
			"a": "Preprocessor directive.",
		},
		6: {
			"q": "What is the name for files ending in .h?",
			"a": "Header files.",
		},
		7: {
			"q": "What is a function prototype?",
			"a": """It is the part of the C funtion that describes:
			<return_value_type> <function_name>(<function_formal_argument_type_and_name>),
			often defined at the top of a C file to make the function available in all parts of the file
			""",
		},
		8: {
			"q": "What is 'int Counter;' and example of?",
			"a": """Variable declaration""",
		},
		9: {
			"q": "In C, how many decimal floating point numbers does a i) single-precision ii) double precision floating point number have",
			"a": """i) 6 decimal digits of precisions ii) 15""",
		},
		9: {
			"q": """Explain the concept of an implementation dependent issue""",
			"a": """When a compiled statement yields difference results dependent on the compiler.
			For example, when a int value outside the range of possible values is assigned. Some
			compiled may yet the max/min value, some a random value, and some will throw up an error.
			""",
		},
		10: {
			"q": """What is meant by a left-sided binding""",
			"a": """That calculation of an expression is conducted from left to right. I.e
			3 + 4 + 1 = 7 + 1 = 8 <- This is how C calculates expressions internally.
			""",
		},
		11: {
			"q": """Define a literal""",
			"a": """A literal is a symbol which uniquely identifies its value. E.g. 100.0, 'A', 233 .""",
		},
		12: {
			"q": """Explain the concept of a format specifier""",
			"a": """Symbols such as %d, %f, etc embedded into a string which hints at the type of placeholder substitution to take place.""",
		},
		13: {
			"q": """Explain the concept of a cascade with respect to C decision making.""",
			"a": """When the if, else if, else blocks all have one level of indentation only, as opposed to nesting which have ifs within ifs.""",
		},
		14: {
			"q": """How many bits does each int type have: i) short ii) int iii) long iiv) long long.""",
			"a": """i)16 ii)16 iii)32 iv)64. Recall that the range of values is [0, 2 to the bits] if unsigned, [-2**(bits-1), 2**(bits-1)] if signed.""",
		},
		15: {
			"q": """How many bits are there in 1 bytes""",
			"a": """8.""",
		},
		16: {
			"q": """What type modifiers does C not allow for types float and double?""",
			"a": """short and unsigned.""",
		},
		17: {
			"q": """Describe the phenomenon of a numerical anomaly with respect to C computation?""",
			"a": """When we add/subtract a large float/double with a small (close to 0) float/double we find the latter disappears without trace""",
		},
		18: {
			"q": """What is integer promotion?""",
			"a": """When data of type `char` or `short int` is implicity converted to `int` at runtime.""",
		},
		19: {
			"q": """What is the word for the part of the declaraion placed on the RHS of the = in:
				'int x = 0;'""",
			"a": """An initiator.""",
		},
		20: {
			"q": """What is the name for the variable which is used for counting the loop's turns?""",
			"a": """A control variable.""",
		},
		21: {
			"q": """What do the following symbols mean with regards to bitwise operations?
			(i)& (ii)| (iii)~ (iv)^ (v)<< (vi)>>""",
			"a": """i) conjunction ii) disjunction iii) negation iv) exclusive or v)bit shift to the left vi) bit shift to the right""",
		},
		22: {
			"q": """What is commonly understood as a nibble?""",
			"a": """A nibble is a 4-bit aggregation, also known as a half-byte.
			The terms low-nibble and high-nibble denote the nibbles containing the less signifance and more significant bits respectively.""",
		},
		23: {
			"q": """What are amorphous pointers""",
			"a": """Pointers that can be used to point to any data of any type. Note that these cannot be subject to the dereference operator.""",
		},
		24: {
			"q": """
			i) What is the distinctive exception with regards to literal assignment to pointers?
			ii) What are these pointers called?""",
			"a": """i) Assigning 0 ii) null pointers. PS. There's an unwritten rule to avoid assigning null pointers""",
		},
		25: {
			"q": """What difference does index assigning a string with apostraphies vs quotes make?""",
			"a": """apostrophies are of type char, quotes are of type *char""",
		},
		26: {
			"q": """What difference does index assigning a string with apostraphies vs quotes make?""",
			"a": """apostrophies are of type char, quotes are of type *char""",
		},
		27: {
			"q": """Let `word` be an array and i be an int, prove that word[i] == i[word]""",
			"a": """ word[i] = *(word + i) = *(i + word) = i[word]""",
		},
		28: {
			"q": """Let p be a pointer. What does the compiler think we're doing when we write p[-1]?""",
			"a": """*(p-1)""",
		},
		29: {
			"q": """Let p be of type int** (pointer to a pointer to an int). Express p[r][c] in terms of pointer dereferencing.""",
			"a": """p[r][c] = *(p[r] + c)  = *(*(p+r) + c). This should output the int.""",
		},
		30: {
			"q": """What is declarative difference between i) int *array[10] and ii) int (*array)[10] ii) int *(*array)[10];""",
			"a": """
			i) Is a 10-element array of pointers to data of type int.
			ii) Is a pointer to a 10-element array of type int
			iii) Is a pointer to a 10 element array of pointers which point to type int""",
		},
		31: {
			"q": """When the compiler knows that an entity (e.g. function) has been declared,
			but knows nothing about the entity's type - what does the compiler assume?""",
			"a": """That the entity is an `int` type.""",
		},
		32: {
			"q": """Need to learn about pointer dereferencing and post-pre-incre-decrementation. i.e *p++ vs *(p)++""",
			"a": """That the entity is an `int` type.""",
		},
		33: {
			"q": """More things to go over: order precedences of bitwise operations: Intricacies of the for loop.""",
			"a": """That the entity is an `int` type.""",
		},
		34: {
			"q": """Does C allow default values for the format parameters in functions: i.e 
			\n
			int example_func(int param1 = 1)??
			""",
			"a": """No it does not and will trigger a compilation error.""",
		},
		35: {
			"q": """Explain the difference between  """,
			"a": """No it does not and will trigger a compilation error.""",
		},
		36: {
			"q": """What are the sub-elements of `struct`s composed of? How are they identified?""",
			"a": """They are called fields (can be any type). They are identified by the field name.""",
		},
		37: {
			"q": """What is the custom for struct tag naming?""",
			"a": """Using capital letters.""",
		},
		38: {
			"q": """Let _strct be the name of a structured variable and _field be a field. Use C's selection operator to get the value of _field.""",
			"a": """_strct._field (<- this expression is called a selector). The selection operator's priority is equal to the indexing operator []""",
		},
		39: {
			"q": """What type cannot be used as a field to a struct?""",
			"a": """A struct cannot be a field of itself. So you can't have recursive structs but you can define a struct as a field within a different struct.""",
		},
		40: {
			"q": """Let sp be a pointer to a struct STRCT, let f be a field of STRCT. Use an appropriate operator to get the value of f from sp.""",
			"a": """sp->f. This is equivalent to (*sp).f""",
		},
		41: {
			"q": """Outline the differences between structs and unions.""",
			"a": """
			Structs:
			1) Field are place successively in memory.
			2) Every field has its own part of the computer memory
			3) The size of the structure is not less than the total size of all of its fields.

			Unions:
			1) Fields are placed in the same memory location.
			2) Contents of union fields are indistinguishable.
			3) The unions initializer has to have one element (as there is actually one value to initialize.).
			""",
		},
		42: {
			"q": """What is the universal principle regarding declaring a formal parameter which is an array?""",
			"a": """
			You're allowed to disregard the information about the size of the first dimension,
			but the remaining sizes have to be provided. I.e. arr[][2], arr[][][6]
			""",
		},
		43: {
			"q": """What does the keyword/attribute `extern` indicate?""",
			"a": """It indicates that the function or variable described in the declaration is defined in a different source file.""",
		},
		44: {
			"q": """What are you allowed to omit from function prototypes in header files.""",
			"a": """You're allowed to omit parameter names, as you're only obliged to specify parameter types.""",
		},
		45: {
			"q": """What's the difference between <> and double quotes when specifying the header files?""",
			"a": """
			<>: The preprocessor will look for the included files in the standard locations e.g /usr/include.
			double quotes: The preprocessor will look for the included file in the same directory where the original file processed by the preprocessor was located.
			""",
		},
		46: {
			"q": """Explain the difference between an l-value and an r-value.""",
			"a": """
			l-values:
				1) Refer to a memory location
				2) May appear of the LHS or RHS
			r-values:
				1) Refer to a data value that is stored at some address in memory.
				2) Can be used on the RHS but NOT on the LHS
			""",
		},
		47: {
			"q": """What is the data type used for file opening and closing in C""",
			"a": """FILE* """,
		},
		48: {
			"q": """In C, any stream operation must be preceded by the fopen() function invocation. What are the three well-defined exceptions to this rule?""",
			"a": """
			`stdin`, `stdout`, `stderr`. When our program starts these streams are already opened and don't require extra preparation.
			""",
		},
		49: {
			"q": """What variable can we use to identify/diagnose the cause of a failure related to operating with streams?""",
			"a": """
			`errno`. This is located in errno.h as `extern int errno;`.
			Can be passed to string::strerror() to get a text describing the meaning of the error.
			""",
		},
		50: {
			"q": """What functions allow us to i) know the current file position ii) set the current file position.""",
			"a": """i) ftell ii) fseek""",
		},
		51: {
			"q": """In file processing, when does the end of file (EOF) state occur?""",
			"a": """When there's nothing more to read in the file. use `feof` which returns 0 if in EOF state.""",
		},
		52: {
			"q": """What is a segmentation fault?""",
			"a": """A memory access violation caused by a program attempting to access an illegal memory location.""",
		},
		53: {
			"q": """What is a:
				i) wild pointer?
				ii) void pointer?
				iii) dangling pointer?
				iv) null pointer?
			""",
			"a": """
				i) wild: when the pointer is uninitialized.

				ii) void: can store the address of any data type. Of type (void *)

				iii) Dangling: A pointer pointing to a memory location that has already been deleted/freed.

				iv) null: when the pointer value is NULL.
			"""
		},
		54: {
			"q": """What are some of the common causes of segmentation faults:""",
			"a": """
			1) writing to a read-only portion of the memory.
			2) accessing an array out of bounds
			3) using a variable's value as an address, like in scanf
			4) dereferencing a null pointer
			5) dereferencing or assigning to an uninitalized pointer (wild pointer)
			6) dereferencing or assigning to a freed pointer
			7) buffer overflow.
			8) stack overflow
			""",
		},
		55: {
			"q": """When does buffer overflow occur?""",
			"a": """It occurs when a program overruns the buffer's boundary and overwrites adjacent memory locations. E.g
			
			int main(void) {
				char s[3]; // 3-element array, each of type char
				strcpy(s, "hello"); // "hello" is larger than the s array so lo\0 will be writting to adjacent memory.
			}
			""",
		},
		56: {
			"q": """Let prog.c be a C source file. What would you enter into the command line to know what your source code looks like after preprocessing?""",
			"a": """gcc -E prog.c""",
		},
		57: {
			"q": """Consider #define <identifier> <text>. What is: i) the identifier often called, ii) the process of replacing the text with the identifier?""",
			"a": """i) macro ii) macro substitution""",
		},
		58: {
			"q": """Give the generalised form of a parameterised macro""",
			"a": """#define <identifier>(<parameter_list>) <text>. Note there can't be any space between ( and the identifier.""",
		},
		59: {
			"q": """Name the macro used for getting out the line number in the source code. What is it useful for?""",
			"a": """i) __LINE__ ii) debugging""",
		},
		60: {
			"q": """Name the macro used for getting the name of the current source file.""",
			"a": """__FILE__""",
		},
		61: {
			"q": """Name the macro used for getting the i) date ii) time of the source file's compilation.""",
			"a": """i) __DATE__ ii) __TIME__""",
		},
		62: {
			"q": """What's a clever preprocessor directive for abstracting variable inspection task?""",
			"a": """#define SNAP(X) printf("variable "#X" = %d\n", X);""",
		},
		63: {
			"q": """Let:
			1. DEBUG be a macro identifier used in a conditional preprocessor directive.
			2. prog.c be the C source file containing the direcive.
			
			How would we define it from command line and therefore include any code within the ifdef/endif block?""",
			"a": """gcc -D DEBUG prog.c""",
		},
		64: {
			"q": """
			Name the three storage classes and what they each represent:
			
			1) extern: 
			
			2) static: 
			
			3) register: """,
			"a": """
			
			1) extern: 
			
			2) static: variable is brought to life when the function starts and is destroyed when the program finishes.
				It does not allow the scope of the variable to be extended beyond the parent module
				i.e. it's not going to be accessible in other modules.
			
			3) register: qualifier to not store data in conventional memory, instead in registers.
				Variables with this declaration cannot be used as an argument to address-of &, since they have no address.
			""",
		},
		62: {
			"q": """Define internal linkage?""",
			"a": """When an entity (variable or function) has coverage limited to a single module.""",
		},
	},
	'C++': {
		1: {
			"q": """What are the i) << ii) >> operators called?""",
			"a": """ i) The insertion operator, commonly used with cout. ii) the extraction operator, commonly used with cin""",
		},
		2: {
			"q": """Consider the for loop:
				for(intializor; conditional; modifier)

				if the initializor, conditional and modifier is empty, what is presumed to be there instead?
			""",
			"a": """Presumed to have 1, this edge case will lead to an infinite loop."""
		},
		3: {
			"q": """What's one limitation to passing by reference e.g int &bval?""",
			"a": """The actual parameter passed must be a variable, not a literal.""",
		},
		4: {
			"q": """Name the mechanism which allows us to have more than one function of the same name?""",
			"a": """Overloading""",
		},
		5: {
			"q": """What keyword is used to request the creation of a new memory block?""",
			"a": """`new`""",
		},
		6: {
			"q": """What keyword is used to free/release a memory block we no longer need?""",
			"a": """`delete`. delete[] for arrays""",
		},
		7: {
			"q": """Give two ways of initializing the variable `pet_name` to the string Lassie""",
			"a": """
			i) string pet_name = "Lassie";, <- assignment style
			
			ii) string pet_name("Lassie"); <- functional style
			""",
		},
		8: {
			"q": """Name one important limitation of string concatenation?""",
			"a": """String concatenation cannot concatenate literals""",
		},
		9: {
			"q": """What is the name space in one sentence?""",
			"a": """The name space is a space in which a particular name has an unambiguous and clear meaning.""",
		},
		10: {
			"q": """What's the official name for ::?""",
			"a": """Scope resolution operator""",
		},
		11: {
			"q": """What's an anonymous namespace""",
			"a": """A namespace defined like so:
			
			namespace <missing_name> {
				int troll = 1;
			}

			This kind of namespace is implicitly and automatically used in a source file where it's visible.
			""",
		},
		12: {
			"q": """i) What is encapsulation? ii) How would you implement encapsulation in C++?""",
			"a": """
			i) The ability to hide selected values against unauthorized accessed.
			ii) private:
			""",
		},
		13: {
			"q": """Let Class1 be a pre-define class and Class2 be a proposed child class. How would you code this in C++?""",
			"a": """
			class Class2:Class1 {

			};
			""",
		},
		14: {
			"q": """Are class components (methods and attributes) public or private by default?""",
			"a": """C++ class components are private by default.""",
		},
		15: {
			"q": """How do we specify class constructors in C++?""",
			"a": """We define a function with a name identical to its home class. Do not specify a return type.""",
		},
		16: {
			"q": """Explain the concept of memory leaks in C++?""",
			"a": """Memory leaks occur when unused (but still allocated) memory grows in size, affecting system performance.""",
		},
		17: {
			"q": """Where are entities created by the `new` keyword stored?""",
			"a": """In a specific memory region called a heap.""",
		},
		18: {
			"q": """Are constructors from inner objects invoked before or after constructors from outer objects?""",
			"a": """Before""",
		},
		19: {
			"q": """
			Let A be a class and X, Y, Z be proposed subclasses. How would you define:
			i) X as a subclass of A
			ii) X, Y, Z as superclasses of A""",
			"a": """
			i) class X: {<visibility_specifier>} X {...};
			ii) class A: X, Y, Z {...};

			""",
		},
		20: {
			"q": """Explain private inheritance?""",
			"a": """
			When a visibility specifier isn't specified for an inherited subclass,
			private inheritance means that all public superclass components turn into private access,
			and private superclass components won't be accessible at all.""",
		},
		21: {
			"q": """What does the keyword access specifier `protected` do?""",
			"a": """
			`protected` means that any component marked with it behaves like a
			public component when used by any of the subclasses and looks
			like a private component to the rest of the world.
			This only applies to publicly inherited classes.""",
		},
		22: {
			"q": """
			i) Must you declare const in constant pointers before or after the *?
			ii) Do variables qualified with const have to be initialized?""",
			"a": """
			i) After.
			ii) They do.""",
		},
		23: {
			"q": """Outline the syntactic difference between constant pointers,
			pointers to constants and constant pointers to constants.""",
			"a": """
			i) constant pointers e.g.: int * const ptr = &val;
			ii) pointers to constants: const int *ptr = &val;
			iii) const pointers to const: const int * const ptr = &val;""",
		},
		24: {
			"q": """How would you declare a const member function?""",
			"a": """
			<type> <function_name>(<params>) const {<body>}.
			Note the placement of const between the parameter list and function body.""",
		},
		25: {
			"q": """What is a friend of a class able to do?""",
			"a": """
			A friend of a class can access or use private and protect and protected components of the class.""",
		},
		26: {
			"q": """What does the volatile keyword qualifier do?""",
			"a": """
			It indicates that a variable can be changed by a background process/routine.
			Every reference to the volatile variable will reload the content from main memory.
			It will not use the copy of the variable which can be present in the register.
			Compiler optimizations are not applied on the volatile variable.""",
		},
		27: {
			"q": """
			i) What is an EOF state? ii) Name two ways this can be brought about""",
			"a": """
			i) The event in which there is no more data to process
			ii) ctrl+D in linux, the actual end of a disk file containing data.
			""",
		},
		28: {
			"q": """A function which throws an exceptions,
			may but doesn't have to specify the types of the entities being throws.
			Let int func(void)  be a function. 
			i) Give the form if func throws a string
			ii) The form if func throws a class named Class
			iii) The generalised from if func throws x1, x2, ... ,xn params
			iv) if func throws no exceptions at all""",
			"a": """
			i) int func(void) throw (string) {}
			ii) int func(void) throw (Class) {}
			iii) int func(void) throw (x1, x2, ..., xn) {}
			iv ) int func(void) throw () {}
			""",
		},
		29: {
			"q": """What are unexpected exceptions?""",
			"a": """Exceptions incompatible with the specification made.""",
		},
		30: {
			"q": """What does the explicit keyword do?""",
			"a": """It protects the constructor from being used in any context requiring the use of implicit conversions.""",
		},
		31: {
			"q": """
			Describe the purpose of:
			i) logic_error: 
			ii) domain_error:
			iii) bad_exception
			""",
			"a": """
			i) logic_error: Designed to represent all the exceptions caused by a violation of the rules imposed by the logic of the algorithm/program.
			ii) domain_error: designed to represent all exceptions caused by the data exceeding the permissible range.
			iii) bad_exception: is thrown when a function tries to throw an exception not specified inside its throw specification.
			""",
		},
		32: {
			"q": """
			i) Give the specialized form of the catch statement that's able to catch all passing exceptions
			ii) What is one drawback to this?""",
			"a": """
			i) catch(...) {<exception_handling_logic>}
			iii) This form that neither identify the exception object, nor make any use of it.""",
		},
		33: {
			"q": """What is the purpose of virtual functions?""",
			"a": """To enable the ability of ruuntime polymorphism.""",
		},
		34: {
			"q": """
			i) What do pure virtual functions do?
			ii) Let void make_sound() be a method in a class, specify make_sound as a pure virtual function""",
			"a": """
			i) The enforce subclasses to implement the function, cause the class with a
				pure virtual function to be an 'abstract class'.
			ii) virtual void make_sound() = 0;
				""",
		},
		35: {
			"q": """What is the formal definition of an abstract class in C++?""",
			"a": """A class which has at least one pure virtual function.""",
		},
		36: {
			"q": """
			i) What are smart pointers?
			ii) What are the three types of smart pointer in C++""",
			"a": """
			i) A container or a wrapper for a raw pointer.
			Unlike raw pointers, they deallocate memory automatically.
			ii) std::unique_ptr, std::shared_ptr, std::weak_ptr""",
		},
		37: {
			"q": """What is a function template?""",
			"a": """
			A function template is a generalization of an algorithm. It's a single
			declaration that can generate declarations for similar, but distinct functions
			Each generated function implements the algorithm for operands of different types.
			A function template is not an actual function. It's a recipe for generating functions.""",
		},
		38: {
			"q": """What is an infix operator?""",
			"a": """Operators place in between their arguments""",
		},
		39: {
			"q": """What are the four non-overloadable operators?""",
			"a": """
			i) ?:
			ii) .
			iii) ::
			iv) sizeof
			""",
		},
		40: {
			"q": """
			Consider the following code:
			usr_class obj1;
			(2)usr_class obj2;
			(2)usr_class obj2 = obj1;
			(3)usr_class obj3 = obj1;

			What is the difference between lines (2) and (3)?
			""",
			"a": """
			In (2) the assignment operator is called.
			In (3) the Copy constructor is called for copying.
			""",
		},
			
	}
}