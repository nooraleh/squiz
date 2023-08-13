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
		a) What is the difference between a serial-based representation of time versus
			a field base representation?

		b) Which of the two representations are more performant?
		""",
		'a': """
		a) A field based representation will have:
			1) time segregation into fields such as year-month-day (e.g. 2023-04-02)
		
		A serial-based representation:	
			- will have one single number (usually the units of duration from a time point 
				such as the epoch) e.g. 18925 days from the epoch

		b) In general, a serial-based representation is more performant.
		""",
	},
	45: {
		'q':  """
		Explain what is meant by SFINAE.
		""",
		'a': """
		SFINAE, or Substitution Failure is not an Error, is a special rule for function
        template overload resolution - it states that:
        
			If a function template overload candidate would cause a compilation error during type
            substitution, it is silently removed from the overload set.
		""",
	},
	46: {
		'q':  """
		Consider the following incomplete snippet:
			template<typename... Ts>
            concept are_all_integral = BLANK1
            
            template<typename... Ts>
            concept at_least_one_integral = BLANK2
            
        Please fill in BLANK1 and BLANK2 to get the desired concepts.
		""",
		'a': """
		Using <type_traits>'s std::conjunction (to perform logical and) and std::disjunction
        (to perform logical or):
        
			template<typename... Ts>
            concept are_all_integral = std::conjunction_v<std::is_integral<Ts>...>;
            
            template<typename... Ts>
            concept at_least_one_integral = std::disjunction_v<std::is_integral<Ts>...>;
		""",
	},
	47: {
		'q':  """
		C++20 introduces modules. What is a module?
		""",
		'a': """
		A module is a modern solution that turns C++ libraries and programs into
		components.

		A module is a set of source code files that are compiled independently of
		the translation units which import them.
		""",
	},
	48: {
		'q':  """
		a) How do precompiled header (PCH) files improve compile time?

		b) State two cons of using PCH?
		""",
		'a': """
		By creating a compiler memory snapshot of a set of header files.
		This is an improvement on repeatedly rebuilding header files.

		b)
			1) PCH files have restrictions that make them more difficult to maintain
				than header files.
			2) As of C++20, they are slower than importing modules
		""",
	},
	49: {
		'q':  """
		Including header units leads to slower compilation times than importing modules.

		Why would you consider header units over modules?s
		""",
		'a': """
		In a legacy codebase that may be reliant on macros and internal implementation (typically
		identified as functions beginning with an underscore and capital letter), you'd want to
		use header units which still expose these as opposed to named modules which do not.
		""",
	},
	50: {
		'q':  """
		State two reasons as to why you would want to use module partitions?
		""",
		'a': """
		1) Reduce compilation times
		2) Separate the interfaces into distinct pieces to unglue certain dependecies.
		""",
	},
	51: {
		'q':  """
		Why does importing a module have a faster compilation time than including
		a header file? 
		""",
		'a': """
		ANS: When a source file imports a module, the compiler reads in the binary
			that contains the contents of the module.

			Reading a binary file is much faster for the compiler than processing
			a header file.

			In addition, the binary is reused by the compiler very time the module
			is imported, saving even more time as opposed to reprocessing multiple
			includes.
		""",
	},
	52: {
		'q':  """
		For every named module, there must be exactly one module interface unit (say A.ixx)
		with no module interface unit with no module partition specified.

		a) What is the term for A.ixx?
		b) What is the purpose of A.ixx?
		""",
		'a': """
		a) Primary module interface unit.
		b) The primary module interface unit is where you declare the:
			1) functions 2) types 3) templates 4) other modules
			5) module partitions

		to expose when source files import the module.
		""",
	},
	53: {
		'q':  """
		Say I have a primary module interface unit file (Shapes.ixx). If I want a module
		interface for a partition called with Rectangle concerns, how would I specify that
		in the first line of Shapes-Rectangle.ixx.
		""",
		'a': """
		export module Shapes:Rectangle;
		""",
	},
	54: {
		'q':  """
		Say you have:
			A.ixx which imports A-partition1.ixx

		How would you import `partition1` in a way that allows importer of A.ixx access
		to the exported contents of `partition1`?
		""",
		'a': """
		In A.ixx simply:
			export import :partition1;

		Think of this as:
			export (import :partition1);

		Where we forward export everthing that we can import from `partition1`.
		""",
	},
	55: {
		'q':  """
		True or false:
			C++20 module require unique names across module since you will get clashes
			similar to header files?
		""",
		'a': """
		False, the same name in multiple modules will not clash since under-the-hood the identiers
		are mangled with the module name.
		""",
	},
	56: {
		'q':  """
		True of false:
			Since C++20 if you want to capture `this` is a lambda, it is not sufficient
			to use =, you will have to explicitly state `this` e.g.

				auto lamb = [=, this](const auto i) { /*do something interesting*/};
		""",
		'a': """
		true;
		""",
	},
	57: {
		'q':  """
		Choose the correct way of templatizing a lambda expression post-C++20:

			a) <typename T>[](T x) { };
			b) []<typename T>(T x) { };
			c) [] (T x) <typename T> { };
		""",
		'a': """
		b) the `<typename T>` should be after the capture clause and before
			the parameter set.
		""",
	},
	58: {
		'q':  """
		In which language standard did we get the following features:
			1) if initializer
			2) switch initializer
			3) ranged-based for loop initializer
		""",
		'a': """
		1) 17 2) 17 3) 20
		""",
	},
	59: {
		'q':  """
		What are the C++20 attributes [[likely]] and [[unlikely]] used for?
		""",
		'a': """
		The [[likely]] and [[unlikely]] attributes are used for giving hints
		to the compiler that certain branches are more likely (or unlikely) to
		be reached to allow the compiler to make optimizations for those branches
		accordingly.

		Snipper:
			switch(value)
			{
				case 1:
					break;
				[[likely]] case 2:
					break;
				[[unlikely]] case 3:
					break;
			}
		""",
	},
	60: {
		'q':  """
		What is profile-guided optimization (PGO)?
		""",
		'a': """
		A.K.A profile-guided feedback, profile-guided optimization is the process of generating a file which logs information
		on branches taken (if/else, switch/case etc) during runtime. This runtime profile information
		is fed into the compiler upon recompilation to "guide" the optimization for the next time it runs.

		E.g if case A it reached much more than case B, the compiler will receive this profile information
		and make necessary optimizations which reflect the probably of these branches.

		Similar to explicity hinting to the compiler that some branches are more likely than others with
		attributes [[likely]] and [[unlikely]].
		""",
	},
	61: {
		'q':  """
		What is the difference between a fixed-sized span (compile-time) and a dynamic-sized span (run-time)?
		""",
		'a': r"""
		A fixed size span has it size specified as a value in the second template argument,
		while a dynamic span omits this - e.g.:

					int data[42];
					std::span<int, 42> a{data};
					std::span<int> b{data};
		""",
	},
	62: {
		'q':  """
		What is the correct way of declaring a read-only span?

			a) const std::span<int>;
			b) std::span<const int>;
		""",
		'a': """
		b)
		""",
	},
	63: {
		'q':  """
		Consider the following:
			__has_cpp_attribute(fallthrough)
			__cpp_binary_literals
			__cpp_char8_t
			__cpp_coroutines

		a) What is the purpose of C++20 feature tests?
		b) Give examples on how you would use these feature tests?
		""",
		'a': """
		a) The purpose of C++20 feature tests is to provide a compile-time
			way of testing if a feature is available to the current compiler.

		b) with attributes you would test like so:
			#if __has_cpp_attribute(fallthrough)
				// ...
			#endif

			with language features you would test against a long value
			represented the year and month the feature was added to the working draft.

			#if __cpp_aggregate_bases >= 201603L
				std::cout << "__cpp_aggregate_bases >= 201603L\n";
			#else
		""",
	},
	64: {
		'q':  """
		a) What are immediate functions in C++20?
		b) Which keyword should you use to create an immediate function?
		""",
		'a': """
		a) An immediate function is a function where every call to the function
			produces a compile-time constant expression.
		b) consteval
		""",
	},
	65: {
		'q':  """
		Consider the snippet:
			enum class CardTypeSuits {Clubs, Diamonds, Hearts, Spades};

			std::string_view get_string(const CardTypeSuits suit_type)
			{
				switch (suit_type)
				{
				case CardTypeSuits::Clubs:
					return "Clubs";
				case CardTypeSuits::Diamonds:
					return "Diamonds";
				case CardTypeSuits::Hearts:
					return "Hearts";
				case CardTypeSuits::Spades:
					return "Spades";
				}
			}

		Use a C++20 feature to reduce the visual pollution in the above. 
		""",
		'a': """
		The C++20 to use is 'using enum' which makes the members of the enum
		unscoped and freely available without having to qualifier it with the
		enum name. 

			std::string_view get_string(const CardTypeSuits suit_type)
			{
				using enum CardTypeSuits;
				switch (suit_type)
				{
				case Clubs:
					return "Clubs";
				case Diamonds:
					return "Diamonds";
				case Hearts:
					return "Hearts";
				case Spades:
					return "Spades";
				}
			}
		""",
	},
	66: {
		'q':  """
		True or false:
			As of C++20, you can now include a reason in the [[nodiscard]] attribute e.g.

				[[nodiscard("Return value expensive the compute, please use return value or don't call function")]]
		""",
		'a': """
		True
		""",
	},
	67: {
		'q':  """
		True or false:

			a) C++20 coroutines are suspendible
			b) C++20 coroutines are resumable functions.
		""",
		'a': """
		a) True b) True
		""",
	},
	68: {
		'q':  """
		a) What is the difference between a stackless and stackful coroutine?
		b) Are C++20 coroutines stackless or stackful?
		""",
		'a': """
		a) Stackful: Data of a coroutine, the coroutine frame, is stored on that stack
		b) Stackless: Data of a coroutine, the coroutine frame, is stored on the heap.
		""",
	},
	69: {
		'q':  """
		In the context of C++20 coroutines, define the following:
			1) task
			2) generator
		""",
		'a': """
		1) task - is a coroutine that does a job without returning a value
		2) generator - a coroutine that does a job AND returns a value (either via `co_yield` or `co_return`)
		""",
	},
	70: {
		'q':  """
		Consider the two coroutine helper types `std::suspend_always` and `std::suspend_never`. What
		is the difference between the two classtypes with respect to their member function:

			constexpr bool await_ready() const noexcept;
		""",
		'a': """
		1) `std::suspend_always` also returns false indicating that an await
			expression always suspends as it waits for its value.

		2) `std::suspend_never` also returns true indicating that an await
			expression never suspends.
		""",
	},
	71: {
		'q':  """
		Brief explain heap ellision?
		""",
		'a': """
		Heap ellision is a way for the compiler to optimize code by
		identifying heap allocations that can be replaced with stack or register
		allocations, without changing the behaviour of the program.
		""",
	},
	72: {
		'q':  """
		Consider the following snippet:

			std::function<int(int)> cb{
				[i = std::make_unique<int>(42)](const int x) {return x + *i; }
			};

		a) Why would the above trigger a compilation error?
		b) Given your answer to (a) se a C++23 alternative that will allow
			this `cb` initialization to be error-free.
		""",
		'a': """
		a) std::function requires a function object that is copyable, since under the
			hood the lambda is a struct-like with the init capture as a member, this
			unique pointer cannot be copied and thus the pre-condition "copyable" fails,
			the compiler compiler raises an error.

		b) Replace 'std::function' with C++23's `std::move_only_function` 
		""",
	},
	73: {
		'q':  """
		C++20 coroutines are stackless. Explain what it means to be stackless in the 
		context of C++20 coroutines?
		""",
		'a': """
		Stackless coroutines suspend execution by returning to the caller and the data that is
		required to resume execution is tores separately from the stack.
		""",
	},
	74: {
		'q':  """
		A function is a coroutine if it contains at least one of 3 expressions. State these
		3 expressions and what they each are used for.
		""",
		'a': """
		1) co_await - to suspend execution until resumed.
		2) co_yield - to suspend execution returning a value
		3) co_return - to complete execution returning a value
		""",
	},
	75: {
		'q':  """
		What are the definition of an aggregate as of C++20?
		""",
		'a': """
		An aggregate is an array or a class with:
			1) no user-declared or inherited constructors
			2) no private or protected non-static data members
			3) no virtual functions
			4) no virtual, private or protected base classes
		""",
	},
	76: {
		'q':  """
		a) What does `constinit` do?

		b) In what situations is C++20's `constinit` specifier useful? 

		""",
		'a': """
		a) `constinit` guarantees that initialization occurs at compile
			time and if it cannot initialize the variable at compile time
			it will be a compilation error.
			
			This resolves the 'static '
		
		b) `constinit` is useful in situations where:

			1) you want to ensure that a variable is initialized, and;
			2) that its value cannot be modified after initialization
			
		""",
	},
	77: {
		'q':  """
		True or false, constinit implies const
		""",
		'a': r"""
		`constinit` does not imply const, for you can initialize a constinit
			variable at compile time and reassign a new literal/compile time expression
			at compile time as well, snippet:

				// static duration constinit int
				static constinit int gs_i{9};

				// declared in global scope so static duration as well
				constinit int g_i{10};

				int main(void)
				{
					gs_i = 1; // reassigning with constant expression, fine
					g_i = 3; // fine here too
					return 0;
				}			
		""",
	},
	78: {
		'q':  """
		Consider the following snippet which attempts to capture
		a structured binding into a lambda:

				auto [a, b] = Widget{1, false};
				auto f = [a]{return a > 0;} // is an error

		Does the above compile?
		""",
		'a': """
		The snippet compiles in C++20, not in C++17.
		""",
	},
	79: {
		'q':  """
		True or false:
			1) As of C++20, lambdas are not allowed in unevaluated contexts
			2) As of C++20, capturesless lambdas are default constructible and assignable.
		""",
		'a': """
			1) False 2) True
		""",
	},
	80: {
		'q':  r"""
		What is the consequence of lambdas being allowed int unevaluated
		contexts e.g.:
			
			decltype([]{}) f;
		""",
		'a': r"""
		You can now have a lambda as a member of a classtype:

			class Widget
			{
				decltype([]{}) f;
			}
		""",
	},
	81: {
		'q':  """
		Explain the meaning of following terms:

			1) Strong structural equality
			2) Weak structural equality
			3) Value equality
			4) Reference equality
		""",
		'a': """
		Strong structural equality:

		""",
	},
	82: {
		'q':  """
		Define strong structural equality and give a concrete code snippet example of it.
		""",
		'a': """
		Types A and B are said to be strong structurally equal if the following holds:

			A == B if and only if &T<A> == &T<B>

		For example:
				template<typename T>
				struct Point
				{
					T x;
					T y;
				};

				Point<int> p1{ 1, 2 };
				Point<int> p2{ 1, 2 };

				bool is_stong_structurally_equal = std::memcmp(std::addressof(p1), std::addressof(p2), sizeof(Point<int>)) == 0; // true

		Note that the fact that Point is strong structurally equal means that we can use it as a template
		argument in C++20 e.g.

				template<Point p>
				class PointyThing
				{};

				int main(void)
				{
					constexpr Point p1{ 0, 1 };
					PointyThing< Point{ 0, 1 }> pt;
					PointyThing < p1 > pt1;
					return 0;
				}

		""",
	},
	83: {
		'q':  """
		Consider the following snippet, with a focus on line (1):

			constexpr int square(int i)
			{
				if (std::is_constant_evaluated()) // (1)
				{
					return i * i;
				}
				else
				{
					return __magic_fast_square(i);
				}
			}

		Why have we opted to `std::is_constant_evaluated()` as opposed to `if constexpr()`?
		"""
		'a': """
		Because `if constexpr` is only evaluated as compile time, meaning the the
		function `square` will only work with compile time arguments. 

		We use `std::is_constant_evaluated()` to evaluated the compile time
		constant arguments for compile time, and then generate the runtime code
		for non-compile time arguments which end up in the else clause.
		""",
	},
	84: {
		'q':  """
		What does the term 'manifestly constant-evaluated expression' mean?
		""",
		'a': """
		A manifestly constant-evaluated expression is an expression that has to be
		evaluted at compile time, and it is a compiler error if a manifestly constant-evaluated
		expression cannot be evaluated at compile time.

		Examples of MCEE's include:
			1) case expressions
			2) array bounds
			3) `if constexpr` conditions
		""",
	},
	85: {
		'q':  """
		In the context of C++20 coroutines, what is the behaviourial difference
		between std::suspend_always and std::suspend_never?
		""",
		'a': """
		std::suspend_always:
			'Pause execution at this point, hand control flow back to the caller'

		std::suspend_never:
			'Do not pause execution at this point (i.e. continue executing within the coroutine)'
		""",
	},
	86: {
		'q':  """
		True or false (C++20 coroutines context):

			1) The `promise_type` provides the hook to control what happens at startup or
				when we return from the coroutine.
			2) The `Awaitable` provides the hooks for determining what happens when we go into
				suspension.
			3) Every `co_await` call suspends.
		""",
		'a': """
		1) True, 2) True
		3) Falls - not every co_await call suspends.
		""",
	},
	87: {
		'q':  """
		a) What is one way to think about std::coroutine_handle ?
		b) What is the difference between using the void specialization std::coroutine_handle<>
			and using std::coroutine_handle<promise_type>? 
		""",
		'a': """
		a) As a raw pointer to the coroutine frame.
		b)
			std::coroutine_handle<>:
				is type erased, can point to any coroutine
			
			std::coroutine_handle<promise_type>:
				- simply more specific, the coroutine handle is constrained
					to point to frames that used the `promise_type` passed in as
					a template argument
		""",
	},
	88: {
		'q':  """
		What is meant by a 'sink argument'?
		""",
		'a': """
		The term 'sink argument' is commonly used in the context of 
		rvalue references and move semantics, particular the move ctor/assign
		special member functions.

		In a broader sense, the term can be used to describe any function argument
		that is intended to consume or take ownership of a value without necessary
		using it directly. Examples include smart pointers and function pointers.
		""",
	},
	89: {
		'q':  """
		Define the three components that make for type erasure.
		""",
		'a': """
		Type erasure is:
			1) a templated constructor; and
			2) a completely non-virtual interface; and
			3) A combination of External Polymorphism + Bridge + Prototype
		""",
	},
	90: {
		'q':  r"""
		a) True or false: 

			You can define a function within another function in C++ e.g.

				int main(void)
				{
					void inner_function()
					{
						std::cout << "do inner function stuff\n";
					}
				}
		""",
		'a': """
		False. Local functions (functions defined within another function) are not permitted,
		but you may declare a function within another function.

		Note: One way of getting around this is to define a local class type and implement
		the call operator. Or you can define a static function within a local class type.
		""",
	},
	91: {
		'q':  """
		a) What does it mean to 'return perfectly' in C++?

		b) Consider the following snippet (with the BLANK)

			template<typename T>
			__BLANK__ call_foo(T&& t)
			{
				return foo(std::forward<T>(t));
			}

		Fill in the __BLANK__ so that the return value in this forwarding function
		returns perfectly.
		""",
		'a': """
		a) Perfect returning means that the value category of the returned value is preserved.
			This means that if:	
				- The return value category inside the function is an lvalue, we return by reference
				- The return value category inside the function is a prvalue, we return by value

		b) #define __BLANK__ decltype(auto) 
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
