# Notes taken in a Q & A style format from various C++ related Youtube videos

qna = {
    1: {
		'q':  """
		In a nutshell, what does the ODR (One Definition Rule) state?
		""",
		'a': """
		The One Definition Rule prescribes that:
			- classes/structs, and
			- non-inline functions
		cannot have more than one definition in the entire program and;

			- templates
			- types
		cannot have more than one definition by translation unit.
		""",
	},
    2: {
		'q':  """
		a) What is an alternative term for translation unit?
		b) What does a translation unit consist of?
		""",
		'a': """
		a) [informal] compilation unit
		b) A translation unit roughly consists of:	
			- a source file (i.e .c/.cpp) after it has been preprocessed

		   From a translation unit, the compiler generates an object file,
		   the object file can be further processed and linked (possible with other
		   object files) to form an executable program.
		""",
	},
    3: {
		'q':  """
		What does ODR-used mean?
		""",
		'a': """
		Informally, an object is ODR used if:
			1) its value has been read (unless it is a compile-time constant i.e via constexpr)
			2) its value has been written
			3) its address is taken
			4) or a reference is bound to it
		""",
	},
    4: {
		'q':  """
		Consider the following line of code:
			const int i = 42;
			const float f = 42.0f;

		True or false:
			1) const variables of integer type are implicitly constexpr
			2) const variables of float type are implicitly constexpr
		""",
		'a': """
			1) true
			2) false
		""",
	},
    5: {
		'q':  """
		True or false:
			1) Since C++11, static object initialization is guaranteed to happen
			exactly once.

			2) Furthermore, this initialization is guaranteed to be thread-safe.
		""",
		'a': """
		1) True
		2) True
		""",
	},
    6: {
		'q':  """
		True or false:
			Is it considered best practice to make single parameter constructors explicit.
		""",
		'a': """
		True
		""",
	},
    7: {
		'q':  """
		For each of the following terms, provide:
			a) A definition
			b) An demonstrative code snippet

		1) Stateless
		2) Stateful

		""",
		'a': """
		1)
			a) Stateless - there is no memory of the past. Every transaction is performed as if it
				were being done for the very first time.

			b)
				int add_one(int n)
				{
					return n + 1; // state is derived by what is passed into the function
				}


		2) 
			a) Stateful - means that there is memory of the past. Previous transactions are remembered and
					may affect the current transaction.

			b)
				int _number = 0;
				
				int add_one()
				{
					++_number;
					return ++_number; // state is maintained by the function and `_number` value dependant on determined by previous calls
				} 
		""",
	},
    8: {
		'q':  """
		True or false:
			Generic lambdas do not support perfect forwarding.
		""",
		'a': """
		False, for consider:

			std::vector<std::string> string_vector;

			auto append_to_string_vector = [&string_vector](auto&& element) {
				string_vector.push_back(std::forward<decltype(element)>(element));
			};

			append_to_string_vector(std::string{ "1" });
			append_to_string_vector(std::string{ "2" });
			append_to_string_vector(std::string{ "3" });
			append_to_string_vector(std::string{ "4" });
		""",
	},
    9: {
		'q':  """
		""",
		'a': """
		""",
	},
    10: {
		'q':  """
		""",
		'a': """
		""",
	},
}