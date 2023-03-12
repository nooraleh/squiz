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
		Map the following letters with the corresponding numbers:
			1) dynamic polymorphism
			2) static polymorphism

			a) templates
			b) object orientation
		""",
		'a': """
		1) b)
		2) a)
		""",
	},
    10: {
		'q':  """
		What is type erasure?
		""",
		'a': """
		Type erasure if:
			1) a type-safe GENERIC (i.e templatized) way to provide one interface for different types.
			2) the different types don't need a common base class and are often unrelated.
		""",
	},
	11: {
		'q':  """
		a) In a nutshell, what is meant by type safety?
		b) Give an example of a type unsafe statement in C++?
		""",
		'a': r"""
		a) Type-safe is the degree to which a language prevents using a value of the wrong type.
		b) Example:
			printf("Meant to be passing a string: %s", 42);

			^^ note the above line will give you a warning but not a compiler error
		""",
	},
	12: {
		'q':  """
		Explained with an example showing the special member declarations why you cannot move
		a const object?
		""",
		'a': """
		For consider:

			struct S
			{
				S() = default;						// ctor
				S(S&&) = default;					// move ctor  (1)
				S(const S&);						// copy ctor (2)
				S& operator=(S&&) = default;		// move assignment operator
				S& operator=(const S&) = default;	// copy assignment operator
				~S() = default;
			};

		and the code:

			int main(void)
			{
					const S s;                (3)
					S s2{ std::move(s) };     (4)
			}

		Explanation: Since line (3) makes a const instance and the move ctor (1) cannot accept
				const-qualified arguments, the overload dispatches to the copy ctor (2).
				I.e we do not move, we copy.
		""",
	},
	13: {
		'q':  """
		a) What is a constant expression?
		b) What is an integral constant expression?
		""",
		'a': """
		a) A constant expression is an expression that can be evaluated at compile time
		b) An integral constant expression is an expression that:
			- can be evaluated at compile time
			- whose type is integral or an enumeration
		""",
	},
	14: {
		'q':  """
		Why should you avoid:
			1) using identifiers that contain a double underscore for any use?
			2) using identifiers that begin with and underscore followed by an upperscore letter for any use?
			3) using an identifier that begins with an underscore in the global namespace.
		""",
		'a': """
		According the lex.name section of the C++ draft, cases (1) and (2) are reserved to the implementation for any use.
		Also case (3) is reserved to the implementation for any use.

		Therefore, writing identifiers in any of (1), (2) or (3) will invoke undefined behaviour, as we may be conflicting
		with things that the STL or the compiler has already defined for us.

		Source: https://eel.is/c++draft/lex.name
		""",
	},
	15: {
		'q':  """
		a) State three types which can take a std::in_place in its constructor?
		b) use std::in_place to construct a:
			- std::optional
			- which can optionally take a std::vector of `int`s
			- of size 10, all elements 3
		""",
		'a': """
		a)	Three types:
				1) std::optional 2) std::any 3) std::variant 

		b) std::optional<std::vector<int>> ov1{ std::in_place, 10, 3 };
		""",
	},
	16: {
		'q':  """
		What is a generally accepted definition of "const correctness"?
		""",
		'a': r"""
		ANS: It simply means the correct usage of `const` wherever applicable
			to prevent objects that are not intended to be modified from being modified.

		Source: https://isocpp.org/wiki/faq/const-correctness
		""",
	},
	17: {
		'q':  """
		In C++, what is the main difference between `static_assert` and `assert`?
		""",
		'a': """
		`static_assert` is for compile-time checks and compilation will fail if the conditions
		are not met.

		`assert` is for run-time checks, will not trigger compilations errors but will end
		the execution of the program if the condition is false by calling `abort()`.
		""",
	},
	18: {
		'q':  """
		Explain with examples the difference (at the language level) of logical vs 
		physical constness.
		""",
		'a': """
		Language level physical constness:
			- simply takes place when you declare an object (i.e not a pointer or reference) as const.
			- from the language's perspective, following objects are physically `const`

				const double d = 5;
				const std::string _str = "Hello world!";
				const MyClass mc;

			- note that it doesn't matter whether the above objects are placed in read-only (RO)
				memory or not.
			- any attempts to modify physical const objects will result in undefined behaviour.

		Language level logical constness:
			- related to the constness of the "access path"
			- access path refers to the access via a reference or a pointer.

			Consider:
				const MyClass* pc;

			Note that whether we assign the address to a const or non-object instance
			of MyClass to `pc`, for the purposes of access via `pc` the underlying
			instance is considered to be const.

				MyClass mc1;
				const MyClass mc2;

				pc = &mc1; // when accessing mc1 via pc it is const
				pc = &mc2; // same is true in this case
		""",
	},
	19: {
		'q':  """
		a) What are fundamental types in C++?
		b) What are the three main categories of built-in types?
		""",
		'a': """
		a) Fundamental types are also known as built-in types. They have the
		following characteristics:
			1) Specified by the C++ language standard
			2) Built into the compiler
			3) Aren't defined in any header file

		b) 1) integral 2) floating point 3) void
		""",
	},
	20: {
		'q':  """
		Consider the following example:

			// inside example.h
			void increment_n_times(int n, int* obj);

			// inside example.cpp
			#include <example.h>
			void increment_n_times(const int n, int* const obj)
			{ }

		Would the above example cause a compiler error? Why or why not?
		""",
		'a': """
		The above example would not cause a compiler error because cv-qualifications
		are ignored between declaration and definition.		
		""",
	},
	21: {
		'q':  """
		Consider the following snippet:
			const int* p = nullptr;
			const int i{};
			const int& i_ref = i;

			auto p_copy = p;			// (1)
			auto i_copy = i;			// (2)
			auto i_ref_copy = i_ref;	// (3)
			auto& i_ref_copy2 = i_ref;	// (4)

		State the types of (1), (2), (3), (4)
		""",
		'a': """
			(1): const int*
			(2): int
			(3): int
			(4): const int&

		NB: const-ness is auto-deduced for reference and pointers but not for value types.
		""",
	},
	22: {
		'q':  """
		Is the following quote true?

			'It makes virtually no sense to use 'constexpr if' outside of a template'
					- Jason Turner
		""",
		'a': """
		Yes, source: https://youtu.be/AtdlMB_n2pI?t=64
		""",
	},
	23: {
		'q':  """
		a) What is a constant expression?
		b) What is a core constant expression (give an example)?
		""",
		'a': """
		a) A constant expression is an expression that can be evaluated at compile time.

		b) A core constant expression is any non-volatile integral or enumeration value which is initialized
			with a constant expression.
		""",
	},
	24: {
		'q':  """
		In one sentence, what is a C++20 `concept`?
		""",
		'a': """
		A `concept` is a compile-time predicate which is true if the given
		type(s) meet the requirements.
		""",
	},
	25: {
		'q':  """
		When would we ever use std::ranges::unreachable_sentinel ?
		""",
		'a': """
		When we are using the std::find algorithm, and we're certain that
		what we are looking for is in the container in which we are searching.

		The std::ranges::unreachable_sentinel is more efficient than using .end()/.cend()
		as there is one less comparison (checking if we are at the end) per cycle.

		Recommended to be used in a constexpr context as misuse can be discovered at compile time.
		""",
	},
	26: {
		'q':  """
		i) Choose A or B:
			A) a local variable cannot be declared `constinit`
			B) a static variable cannot be declared `constinit`

		ii) constinit assign 42 to an int variable i within `int main()` 
		""",
		'a': """
		i) A
		ii) int main(void)
			{
				constinit static int i = 42;
			}
		""",
	},
	27: {
		'q':  """
		State and explained the two properties which each expression has?
		""",
		'a': """
		1) A type (including const/volatile qualifiers) e.g int*, const volatile unsigned long, etc
		2) A value category. 
			1) glvalue (generalized lvalue)
			2) prvalue (pure rvalues)
			3) lvalue (historically appearing on the LHS)

			NOTE: A value category is a quality of an expression.
		""",
	},
	28: {
		'q':  """
		Consider the following:
			int&& ra = 42;

		State the:
			1) type, and;
			2) value category
		of `ra`.
		""",
		'a': """
		1) type: int&&
		2) value category: lvalue
		""",
	},
	29: {
		'q':  """
		Consider the follow snippet:

			template<typename T>
			void foo(T&& t) { /*logic*/}

		True or false:
			An r-value reference can only be a forwarding reference in the scope
			of a template function?
		""",
		'a': """
		True
		""",
	},
	30: {
		'q':  """
		What does the [[nodiscard]] attribute do?
		""",
		'a': """
		The [[nodiscard]] attribute instructs the compiler to generate
		a warning if a return value is dropped.
		""",
	},
	31: {
		'q':  """
		State 4 places where [[nodiscard]] can be used and 
		give an example for each.
		""",
		'a': """
		1) on a function's (return value)
			e.g [[nodiscard]] bool is_empty() const;

		2) On the type itself:
				struct [[nodiscard]] NDStruct {/*members*/};

		3) On a lambda (C++23)
			auto lamb = []() [[nodiscard]] constexpr {return 42;}
			// now the return value of lamb() is no discard.

		4) on a constructor of a class/struct (C++20)
			
			struct FDHolder
			{
				[[nodiscard]] explicit FDHolder(int FD);
				FDHolder();
			};

			// now when we call the ctor overload which takes an int
			// we are warned when we discard the instance
		""",
	},
	32: {
		'q':  """
		[[nodiscard]] should be used extensively. Give examples of places
		where [[nodiscard]] should be applied.
 		""",
		'a': """
		Examples include:
			1) getter
			2) accessor
			2) const 
		functions should be [[nodiscard]]
		""",
	},
	33: {
		'q':  """
		True or false:
			If an exception is marked `noexcept` and actually does throw an exception,
			std::terminate MUST be called (i.e catching such an exception is futile).
		""",
		'a': """
		True.
		""",
	},
	34: {
		'q':  """
		a) What is understood by 'out-of-band' error reporting.
		b) Why is out-of-band error reporting considered bad practice?
		""",
		'a': """
		a) Out-of-band error reporting forces the client code to be responsible
		for checking if the logic come from an library API is correct or not.

		E.g forces the client to make their own switch/case function to find the
		error code, or checking if a pointer_v type returned is null or not.

		b)
			1) Will lead to threading issues in a multi-threaded application
			2) User may ignore/forget to make extra function calls, leading to bugs

		source: https://youtu.be/zL-vn_pGGgY?t=2244
		""",
	},
	35: {
		'q': r"""
		Consider the following snippet, which is intended to be a modernized
		version of <cstdio>'s std::fopen:

			using FilePtr = std::unique_ptr < FILE, decltype([](FILE* f) { std::fclose(f); }) > ;

			[[nodiscard]] FilePtr modern_fopen(const std::filesystem::path& path, std::string_view mode)
			{
				return FilePtr{};
			}

			auto file = modern_fopen("rw+", "/my/file"); (1)

		a) Does the snippet compile successfully?
		b) What is wrong with line (1)
		c) Propose code to prevent line `modern_fopen` being unintentionally misused.

		""",
		'a': r"""
		a) The snippet does compile successfully
		b) The arguments passes are clearly in the wrong order, the rw+ mode is meant
			to be passed to the second parameter and /my/file clearly a path.

			We have an issue of implicitly conversions allowing the code the compile
			successfully and thus the api being misused.

		c) delete a catch-all for all other template specializations for function `modern_fopen`
			which restricts the compilable usage of the function to explicit arguments
			passed in.

			snippet:
				void modern_fopen(const auto&, const auto&) = delete;
		""",
	},
	36: {
		'q':  """
		What are the three semantics categories in C++?
		""",
		'a': """
		1) Value semantics (copy semantics)
		2) Move semantics
		3) Reference semantics (pointer semantics)
		""",
	},
	37: {
		'q':  """
		In C++, what is a class-type?
		""",
		'a': """
		A class-type is an object which is encapsulated either by:
			1) a class
			2) a struct, or;
			3) a union
		""",
	},
	38: {
		'q':  """
		Consider the following statement:

			You should use a class as opposed to a struct when the underlying
			data is invariant.

		Explain what 'invariant' means in this context and give an example
		of a struct and a class to demonstrate.
		""",
		'a': """
		`Invariant` in this context means that the values are constrained by a notion of
		"validity" as a subset of the domain of the type(s) being used to represent them.

		For example, for a struct `Point`

			struct Point
			{
			public:
				int x;
				int y;
			} 

		There is a no constaint on a point position, we could have negative
		and position values, small and large etc to represent the notion of a point.

		However, for a class `Date`:

			class Date
			{
			public:
				Date(unsigned int year, unsigned int month, unsigned int day)
			
			// private members
			}

		Note that there isn't a universally accepted notion of a 0 month, which
		this allowed. Or a 35th day of a month, or a 13th, 14th month etc.

		In this case the class is invariant, and we establish the invariant in the
		constructor.
		""",
	},
	39: {
		'q':  """
		True or false:

			As a core guideline, you should make single parameter
			constructors (including conversion constructors) and conversion
			operators explicit.
		""",
		'a': """
		True.
		""",
	},
	40: {
		'q':  """
		True or false:

			A base class should either be:
				1) public and virtual, or;
				2) protected and non-virtual
		""",
		'a': """
		True on both accounts.
		""",
	},
	41: {
		'q':  """
		True or false:
			For scope enums, you may specify 'enum struct' as well as 
			'enum class'.
		""",
		'a': """
		True.
		""",
	},
	42: {
		'q':  """
		In dynamic polymorphism you have to make a choice between two things.
		What are they?
		""",
		'a': """
		Choice 1) Designing for the addition of types (to avoid having to make
			switch/case statements and static_casting the values to call a method)
		Choice 2) Designing for the addition of operations (you make want to avoid
			lots of virtual functions in a base class which many inheritors
			may not want to/need to implement)
		""",
	},
	43: {
		'q':  """
		When would be want to turn to the prototype pattern?
		""",
		'a': """
		When we are in a situation where:
			1) an object is far more expensive to create than copy
			2) objects have an initial common state
			3) we want to hide the complexity of creating new instances from the user
			4) the "customizations" of an object is specified at runtime.
		""",
	},
	44: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	45: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	46: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	47: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	48: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	49: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	50: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	51: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	52: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	53: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	54: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	55: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	56: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	57: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	58: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	59: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	60: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	61: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	62: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	63: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	64: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	65: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	66: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	67: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	68: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	69: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	70: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	71: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	72: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	73: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	74: {
		'q':  """
		
		""",
		'a': """
		
		""",
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
	89: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	90: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	91: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	92: {
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
    106: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    107: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    108: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
    109: {
		'q':  """
		
		""",
		'a': """
		
		""",
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
	151: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	152: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	153: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	154: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	155: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	156: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	157: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	158: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	159: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	160: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	161: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	162: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	163: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	164: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	165: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	166: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	167: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	168: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	169: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	170: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	171: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	172: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	173: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	174: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	175: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	176: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	177: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	178: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	179: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	180: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	181: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	182: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	183: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	184: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	185: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	186: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	187: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	188: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	189: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	190: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	191: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	192: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	193: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	194: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	195: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	196: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	197: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	198: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	199: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	200: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
}