using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CPP
{
    public partial class CPPYouTube : QNABase
    {
        public CPPYouTube()
        : base(title: "Notes Taken From Various C++ Videos", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "CPPYouTube";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"In a nutshell, what does the ODR (One Definition Rule) state?"},
        {"a", @"The One Definition Rule prescribes that:
			- classes/structs, and
			- non-inline functions
		cannot have more than one definition in the entire program and;

			- templates
			- types
		cannot have more than one definition by translation unit."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"a) What is an alternative term for translation unit?
		b) What does a translation unit consist of?"},
        {"a", @"a) [informal] compilation unit
		b) A translation unit roughly consists of:	
			- a source file (i.e .c/.cpp) after it has been preprocessed

		   From a translation unit, the compiler generates an object file,
		   the object file can be further processed and linked (possible with other
		   object files) to form an executable program."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"What does ODR-used mean?"},
        {"a", @"Informally, an object is ODR used if:
			1) its value has been read (unless it is a compile-time constant i.e via constexpr)
			2) its value has been written
			3) its address is taken
			4) or a reference is bound to it"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"Consider the following line of code:
			const int i = 42;
			const float f = 42.0f;

		True or false:
			1) const variables of integer type are implicitly constexpr
			2) const variables of float type are implicitly constexpr"},
        {"a", @"1) true
			2) false"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"True or false:
			1) Since C++11, static object initialization is guaranteed to happen
			exactly once.

			2) Furthermore, this initialization is guaranteed to be thread-safe."},
        {"a", @"1) True
		2) True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"True or false:
			Is it considered best practice to make single parameter constructors explicit."},
        {"a", @"True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"For each of the following terms, provide:
			a) A definition
			b) An demonstrative code snippet

		1) Stateless
		2) Stateful"},
        {"a", @"1)
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
				}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"True or false:
			Generic lambdas do not support perfect forwarding."},
        {"a", @"False, for consider:

			std::vector<std::string> string_vector;

			auto append_to_string_vector = [&string_vector](auto&& element) {
				string_vector.push_back(std::forward<decltype(element)>(element));
			};

			append_to_string_vector(std::string{ ""1"" });
			append_to_string_vector(std::string{ ""2"" });
			append_to_string_vector(std::string{ ""3"" });
			append_to_string_vector(std::string{ ""4"" });"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"Map the following letters with the corresponding numbers:
			1) dynamic polymorphism
			2) static polymorphism

			a) templates
			b) object orientation"},
        {"a", @"1) b)
		2) a)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"What is type erasure?"},
        {"a", @"Type erasure if:
			1) a type-safe GENERIC (i.e templatized) way to provide one interface for different types.
			2) the different types don't need a common base class and are often unrelated."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"a) In a nutshell, what is meant by type safety?
		b) Give an example of a type unsafe statement in C++?"},
        {"a", @"a) Type-safe is the degree to which a language prevents using a value of the wrong type.
		b) Example:
			printf(""Meant to be passing a string: %s"", 42);

			^^ note the above line will give you a warning but not a compiler error"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"Explained with an example showing the special member declarations why you cannot move
		a const object?"},
        {"a", @"For consider:

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
				I.e we do not move, we copy."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"a) What is a constant expression?
		b) What is an integral constant expression?"},
        {"a", @"a) A constant expression is an expression that can be evaluated at compile time
		b) An integral constant expression is an expression that:
			- can be evaluated at compile time
			- whose type is integral or an enumeration"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"Why should you avoid:
			1) using identifiers that contain a double underscore for any use?
			2) using identifiers that begin with and underscore followed by an upperscore letter for any use?
			3) using an identifier that begins with an underscore in the global namespace."},
        {"a", @"According the lex.name section of the C++ draft, cases (1) and (2) are reserved to the implementation for any use.
		Also case (3) is reserved to the implementation for any use.

		Therefore, writing identifiers in any of (1), (2) or (3) will invoke undefined behaviour, as we may be conflicting
		with things that the STL or the compiler has already defined for us.

		Source: https://eel.is/c++draft/lex.name"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"a) State three types which can take a std::in_place in its constructor?
		b) use std::in_place to construct a:
			- std::optional
			- which can optionally take a std::vector of `int`s
			- of size 10, all elements 3"},
        {"a", @"a)	Three types:
				1) std::optional 2) std::any 3) std::variant 

		b) std::optional<std::vector<int>> ov1{ std::in_place, 10, 3 };"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"What is a generally accepted definition of ""const correctness""?"},
        {"a", @"ANS: It simply means the correct usage of `const` wherever applicable
			to prevent objects that are not intended to be modified from being modified.

		Source: https://isocpp.org/wiki/faq/const-correctness"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"In C++, what is the main difference between `static_assert` and `assert`?"},
        {"a", @"`static_assert` is for compile-time checks and compilation will fail if the conditions
		are not met.

		`assert` is for run-time checks, will not trigger compilations errors but will end
		the execution of the program if the condition is false by calling `abort()`."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"Explain with examples the difference (at the language level) of logical vs 
		physical constness."},
        {"a", @"Language level physical constness:
			- simply takes place when you declare an object (i.e not a pointer or reference) as const.
			- from the language's perspective, following objects are physically `const`

				const double d = 5;
				const std::string _str = ""Hello world!"";
				const MyClass mc;

			- note that it doesn't matter whether the above objects are placed in read-only (RO)
				memory or not.
			- any attempts to modify physical const objects will result in undefined behaviour.

		Language level logical constness:
			- related to the constness of the ""access path""
			- access path refers to the access via a reference or a pointer.

			Consider:
				const MyClass* pc;

			Note that whether we assign the address to a const or non-object instance
			of MyClass to `pc`, for the purposes of access via `pc` the underlying
			instance is considered to be const.

				MyClass mc1;
				const MyClass mc2;

				pc = &mc1; // when accessing mc1 via pc it is const
				pc = &mc2; // same is true in this case"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"a) What are fundamental types in C++?
		b) What are the three main categories of built-in types?"},
        {"a", @"a) Fundamental types are also known as built-in types. They have the
		following characteristics:
			1) Specified by the C++ language standard
			2) Built into the compiler
			3) Aren't defined in any header file

		b) 1) integral 2) floating point 3) void"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"Consider the following example:

			// inside example.h
			void increment_n_times(int n, int* obj);

			// inside example.cpp
			#include <example.h>
			void increment_n_times(const int n, int* const obj)
			{ }

		Would the above example cause a compiler error? Why or why not?"},
        {"a", @"The above example would not cause a compiler error because cv-qualifications
		are ignored between declaration and definition."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:
			const int* p = nullptr;
			const int i{};
			const int& i_ref = i;

			auto p_copy = p;			// (1)
			auto i_copy = i;			// (2)
			auto i_ref_copy = i_ref;	// (3)
			auto& i_ref_copy2 = i_ref;	// (4)

		State the types of (1), (2), (3), (4)"},
        {"a", @"(1): const int*
			(2): int
			(3): int
			(4): const int&

		NB: const-ness is auto-deduced for reference and pointers but not for value types."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"Is the following quote true?

			'It makes virtually no sense to use 'constexpr if' outside of a template'
					- Jason Turner"},
        {"a", @"Yes, source: https://youtu.be/AtdlMB_n2pI?t=64"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"a) What is a constant expression?
		b) What is a core constant expression (give an example)?"},
        {"a", @"a) A constant expression is an expression that can be evaluated at compile time.

		b) A core constant expression is any non-volatile integral or enumeration value which is initialized
			with a constant expression."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"In one sentence, what is a C++20 `concept`?"},
        {"a", @"A `concept` is a compile-time predicate which is true if the given
		type(s) meet the requirements."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"When would we ever use std::ranges::unreachable_sentinel ?"},
        {"a", @"When we are using the std::find algorithm, and we're certain that
		what we are looking for is in the container in which we are searching.

		The std::ranges::unreachable_sentinel is more efficient than using .end()/.cend()
		as there is one less comparison (checking if we are at the end) per cycle.

		Recommended to be used in a constexpr context as misuse can be discovered at compile time."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"i) Choose A or B:
			A) a local variable cannot be declared `constinit`
			B) a static variable cannot be declared `constinit`

		ii) constinit assign 42 to an int variable i within `int main()`"},
        {"a", @"i) A
		ii) int main(void)
			{
				constinit static int i = 42;
			}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"State and explained the two properties which each expression has?"},
        {"a", @"1) A type (including const/volatile qualifiers) e.g int*, const volatile unsigned long, etc
		2) A value category. 
			1) glvalue (generalized lvalue)
			2) prvalue (pure rvalues)
			3) lvalue (historically appearing on the LHS)

			NOTE: A value category is a quality of an expression."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"Consider the following:
			int&& ra = 42;

		State the:
			1) type, and;
			2) value category
		of `ra`."},
        {"a", @"1) type: int&&
		2) value category: lvalue"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {29, new Dictionary<string, string>() {
        {"q", @"Consider the follow snippet:

			template<typename T>
			void foo(T&& t) { /*logic*/}

		True or false:
			An r-value reference can only be a forwarding reference in the scope
			of a template function?"},
        {"a", @"True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {30, new Dictionary<string, string>() {
        {"q", @"What does the [[nodiscard]] attribute do?"},
        {"a", @"The [[nodiscard]] attribute instructs the compiler to generate
		a warning if a return value is dropped."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {31, new Dictionary<string, string>() {
        {"q", @"State 4 places where [[nodiscard]] can be used and 
		give an example for each."},
        {"a", @"1) on a function's (return value)
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
			// we are warned when we discard the instance"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {32, new Dictionary<string, string>() {
        {"q", @"[[nodiscard]] should be used extensively. Give examples of places
		where [[nodiscard]] should be applied."},
        {"a", @"Examples include:
			1) getter
			2) accessor
			2) const 
		functions should be [[nodiscard]]"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {33, new Dictionary<string, string>() {
        {"q", @"True or false:
			If an exception is marked `noexcept` and actually does throw an exception,
			std::terminate MUST be called (i.e catching such an exception is futile)."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {34, new Dictionary<string, string>() {
        {"q", @"a) What is understood by 'out-of-band' error reporting.
		b) Why is out-of-band error reporting considered bad practice?"},
        {"a", @"a) Out-of-band error reporting forces the client code to be responsible
		for checking if the logic come from an library API is correct or not.

		E.g forces the client to make their own switch/case function to find the
		error code, or checking if a pointer_v type returned is null or not.

		b)
			1) Will lead to threading issues in a multi-threaded application
			2) User may ignore/forget to make extra function calls, leading to bugs

		source: https://youtu.be/zL-vn_pGGgY?t=2244"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {35, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet, which is intended to be a modernized
		version of <cstdio>'s std::fopen:

			using FilePtr = std::unique_ptr < FILE, decltype([](FILE* f) { std::fclose(f); }) > ;

			[[nodiscard]] FilePtr modern_fopen(const std::filesystem::path& path, std::string_view mode)
			{
				return FilePtr{};
			}

			auto file = modern_fopen(""rw+"", ""/my/file""); (1)

		a) Does the snippet compile successfully?
		b) What is wrong with line (1)
		c) Propose code to prevent line `modern_fopen` being unintentionally misused."},
        {"a", @"a) The snippet does compile successfully
		b) The arguments passes are clearly in the wrong order, the rw+ mode is meant
			to be passed to the second parameter and /my/file clearly a path.

			We have an issue of implicitly conversions allowing the code the compile
			successfully and thus the api being misused.

		c) delete a catch-all for all other template specializations for function `modern_fopen`
			which restricts the compilable usage of the function to explicit arguments
			passed in.

			snippet:
				void modern_fopen(const auto&, const auto&) = delete;"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {36, new Dictionary<string, string>() {
        {"q", @"What are the three semantics categories in C++?"},
        {"a", @"1) Value semantics (copy semantics)
		2) Move semantics
		3) Reference semantics (pointer semantics)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {37, new Dictionary<string, string>() {
        {"q", @"In C++, what is a class-type?"},
        {"a", @"A class-type is an object which is encapsulated either by:
			1) a class
			2) a struct, or;
			3) a union"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {38, new Dictionary<string, string>() {
        {"q", @"Consider the following statement:

			You should use a class as opposed to a struct when the underlying
			data is invariant.

		Explain what 'invariant' means in this context and give an example
		of a struct and a class to demonstrate."},
        {"a", @"`Invariant` in this context means that the values are constrained by a notion of
		""validity"" as a subset of the domain of the type(s) being used to represent them.

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
		constructor."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {39, new Dictionary<string, string>() {
        {"q", @"True or false:

			As a core guideline, you should make single parameter
			constructors (including conversion constructors) and conversion
			operators explicit."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {40, new Dictionary<string, string>() {
        {"q", @"True or false:

			A base class should either be:
				1) public and virtual, or;
				2) protected and non-virtual"},
        {"a", @"True on both accounts."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {41, new Dictionary<string, string>() {
        {"q", @"True or false:
			For scope enums, you may specify 'enum struct' as well as 
			'enum class'."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {42, new Dictionary<string, string>() {
        {"q", @"In dynamic polymorphism you have to make a choice between two things.
		What are they?"},
        {"a", @"Choice 1) Designing for the addition of types (to avoid having to make
			switch/case statements and static_casting the values to call a method)
		Choice 2) Designing for the addition of operations (you make want to avoid
			lots of virtual functions in a base class which many inheritors
			may not want to/need to implement)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {43, new Dictionary<string, string>() {
        {"q", @"When would be want to turn to the prototype pattern?"},
        {"a", @"When we are in a situation where:
			1) an object is far more expensive to create than copy
			2) objects have an initial common state
			3) we want to hide the complexity of creating new instances from the user
			4) the ""customizations"" of an object is specified at runtime."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {44, new Dictionary<string, string>() {
        {"q", @"a) What is the difference between a serial-based representation of time versus
			a field base representation?

		b) Which of the two representations are more performant?"},
        {"a", @"a) A field based representation will have:
			1) time segregation into fields such as year-month-day (e.g. 2023-04-02)
		
		A serial-based representation:	
			- will have one single number (usually the units of duration from a time point 
				such as the epoch) e.g. 18925 days from the epoch

		b) In general, a serial-based representation is more performant."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {45, new Dictionary<string, string>() {
        {"q", @"Explain what is meant by SFINAE."},
        {"a", @"SFINAE, or Substitution Failure is not an Error, is a special rule for function
        template overload resolution - it states that:
        
			If a function template overload candidate would cause a compilation error during type
            substitution, it is silently removed from the overload set."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {46, new Dictionary<string, string>() {
        {"q", @"Consider the following incomplete snippet:
			template<typename... Ts>
            concept are_all_integral = BLANK1
            
            template<typename... Ts>
            concept at_least_one_integral = BLANK2
            
        Please fill in BLANK1 and BLANK2 to get the desired concepts."},
        {"a", @"Using <type_traits>'s std::conjunction (to perform logical and) and std::disjunction
        (to perform logical or):
        
			template<typename... Ts>
            concept are_all_integral = std::conjunction_v<std::is_integral<Ts>...>;
            
            template<typename... Ts>
            concept at_least_one_integral = std::disjunction_v<std::is_integral<Ts>...>;"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {47, new Dictionary<string, string>() {
        {"q", @"C++20 introduces modules. What is a module?"},
        {"a", @"A module is a modern solution that turns C++ libraries and programs into
		components.

		A module is a set of source code files that are compiled independently of
		the translation units which import them."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {48, new Dictionary<string, string>() {
        {"q", @"a) How do precompiled header (PCH) files improve compile time?

		b) State two cons of using PCH?"},
        {"a", @"By creating a compiler memory snapshot of a set of header files.
		This is an improvement on repeatedly rebuilding header files.

		b)
			1) PCH files have restrictions that make them more difficult to maintain
				than header files.
			2) As of C++20, they are slower than importing modules"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {49, new Dictionary<string, string>() {
        {"q", @"Including header units leads to slower compilation times than importing modules.

		Why would you consider header units over modules?s"},
        {"a", @"In a legacy codebase that may be reliant on macros and internal implementation (typically
		identified as functions beginning with an underscore and capital letter), you'd want to
		use header units which still expose these as opposed to named modules which do not."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {50, new Dictionary<string, string>() {
        {"q", @"State two reasons as to why you would want to use module partitions?"},
        {"a", @"1) Reduce compilation times
		2) Separate the interfaces into distinct pieces to unglue certain dependecies."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {51, new Dictionary<string, string>() {
        {"q", @"Why does importing a module have a faster compilation time than including
		a header file?"},
        {"a", @"ANS: When a source file imports a module, the compiler reads in the binary
			that contains the contents of the module.

			Reading a binary file is much faster for the compiler than processing
			a header file.

			In addition, the binary is reused by the compiler very time the module
			is imported, saving even more time as opposed to reprocessing multiple
			includes."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {52, new Dictionary<string, string>() {
        {"q", @"For every named module, there must be exactly one module interface unit (say A.ixx)
		with no module interface unit with no module partition specified.

		a) What is the term for A.ixx?
		b) What is the purpose of A.ixx?"},
        {"a", @"a) Primary module interface unit.
		b) The primary module interface unit is where you declare the:
			1) functions 2) types 3) templates 4) other modules
			5) module partitions

		to expose when source files import the module."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {53, new Dictionary<string, string>() {
        {"q", @"Say I have a primary module interface unit file (Shapes.ixx). If I want a module
		interface for a partition called with Rectangle concerns, how would I specify that
		in the first line of Shapes-Rectangle.ixx."},
        {"a", @"export module Shapes:Rectangle;"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {54, new Dictionary<string, string>() {
        {"q", @"Say you have:
			A.ixx which imports A-partition1.ixx

		How would you import `partition1` in a way that allows importer of A.ixx access
		to the exported contents of `partition1`?"},
        {"a", @"In A.ixx simply:
			export import :partition1;

		Think of this as:
			export (import :partition1);

		Where we forward export everthing that we can import from `partition1`."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {55, new Dictionary<string, string>() {
        {"q", @"True or false:
			C++20 module require unique names across module since you will get clashes
			similar to header files?"},
        {"a", @"False, the same name in multiple modules will not clash since under-the-hood the identiers
		are mangled with the module name."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {56, new Dictionary<string, string>() {
        {"q", @"True of false:
			Since C++20 if you want to capture `this` is a lambda, it is not sufficient
			to use =, you will have to explicitly state `this` e.g.

				auto lamb = [=, this](const auto i) { /*do something interesting*/};"},
        {"a", @"true;"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {57, new Dictionary<string, string>() {
        {"q", @"Choose the correct way of templatizing a lambda expression post-C++20:

			a) <typename T>[](T x) { };
			b) []<typename T>(T x) { };
			c) [] (T x) <typename T> { };"},
        {"a", @"b) the `<typename T>` should be after the capture clause and before
			the parameter set."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {58, new Dictionary<string, string>() {
        {"q", @"In which language standard did we get the following features:
			1) if initializer
			2) switch initializer
			3) ranged-based for loop initializer"},
        {"a", @"1) 17 2) 17 3) 20"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {59, new Dictionary<string, string>() {
        {"q", @"What are the C++20 attributes [[likely]] and [[unlikely]] used for?"},
        {"a", @"The [[likely]] and [[unlikely]] attributes are used for giving hints
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
			}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {60, new Dictionary<string, string>() {
        {"q", @"What is profile-guided optimization (PGO)?"},
        {"a", @"A.K.A profile-guided feedback, profile-guided optimization is the process of generating a file which logs information
		on branches taken (if/else, switch/case etc) during runtime. This runtime profile information
		is fed into the compiler upon recompilation to ""guide"" the optimization for the next time it runs.

		E.g if case A it reached much more than case B, the compiler will receive this profile information
		and make necessary optimizations which reflect the probably of these branches.

		Similar to explicity hinting to the compiler that some branches are more likely than others with
		attributes [[likely]] and [[unlikely]]."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {61, new Dictionary<string, string>() {
        {"q", @"What is the difference between a fixed-sized span (compile-time) and a dynamic-sized span (run-time)?"},
        {"a", @"A fixed size span has it size specified as a value in the second template argument,
		while a dynamic span omits this - e.g.:

					int data[42];
					std::span<int, 42> a{data};
					std::span<int> b{data};"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {62, new Dictionary<string, string>() {
        {"q", @"What is the correct way of declaring a read-only span?

			a) const std::span<int>;
			b) std::span<const int>;"},
        {"a", @"b)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {63, new Dictionary<string, string>() {
        {"q", @"Consider the following:
			__has_cpp_attribute(fallthrough)
			__cpp_binary_literals
			__cpp_char8_t
			__cpp_coroutines

		a) What is the purpose of C++20 feature tests?
		b) Give examples on how you would use these feature tests?"},
        {"a", @"a) The purpose of C++20 feature tests is to provide a compile-time
			way of testing if a feature is available to the current compiler.

		b) with attributes you would test like so:
			#if __has_cpp_attribute(fallthrough)
				// ...
			#endif

			with language features you would test against a long value
			represented the year and month the feature was added to the working draft.

			#if __cpp_aggregate_bases >= 201603L
				std::cout << ""__cpp_aggregate_bases >= 201603L
"";
			#else"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {64, new Dictionary<string, string>() {
        {"q", @"a) What are immediate functions in C++20?
		b) Which keyword should you use to create an immediate function?"},
        {"a", @"a) An immediate function is a function where every call to the function
			produces a compile-time constant expression.
		b) consteval"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {65, new Dictionary<string, string>() {
        {"q", @"Consider the snippet:
			enum class CardTypeSuits {Clubs, Diamonds, Hearts, Spades};

			std::string_view get_string(const CardTypeSuits suit_type)
			{
				switch (suit_type)
				{
				case CardTypeSuits::Clubs:
					return ""Clubs"";
				case CardTypeSuits::Diamonds:
					return ""Diamonds"";
				case CardTypeSuits::Hearts:
					return ""Hearts"";
				case CardTypeSuits::Spades:
					return ""Spades"";
				}
			}

		Use a C++20 feature to reduce the visual pollution in the above."},
        {"a", @"The C++20 to use is 'using enum' which makes the members of the enum
		unscoped and freely available without having to qualifier it with the
		enum name. 

			std::string_view get_string(const CardTypeSuits suit_type)
			{
				using enum CardTypeSuits;
				switch (suit_type)
				{
				case Clubs:
					return ""Clubs"";
				case Diamonds:
					return ""Diamonds"";
				case Hearts:
					return ""Hearts"";
				case Spades:
					return ""Spades"";
				}
			}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {66, new Dictionary<string, string>() {
        {"q", @"True or false:
			As of C++20, you can now include a reason in the [[nodiscard]] attribute e.g.

				[[nodiscard(""Return value expensive the compute, please use return value or don't call function"")]]"},
        {"a", @"True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {67, new Dictionary<string, string>() {
        {"q", @"True or false:

			a) C++20 coroutines are suspendible
			b) C++20 coroutines are resumable functions."},
        {"a", @"a) True b) True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {68, new Dictionary<string, string>() {
        {"q", @"a) What is the difference between a stackless and stackful coroutine?
		b) Are C++20 coroutines stackless or stackful?"},
        {"a", @"a) Stackful: Data of a coroutine, the coroutine frame, is stored on that stack
		b) Stackless: Data of a coroutine, the coroutine frame, is stored on the heap."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {69, new Dictionary<string, string>() {
        {"q", @"In the context of C++20 coroutines, define the following:
			1) task
			2) generator"},
        {"a", @"1) task - is a coroutine that does a job without returning a value
		2) generator - a coroutine that does a job AND returns a value (either via `co_yield` or `co_return`)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {70, new Dictionary<string, string>() {
        {"q", @"Consider the two coroutine helper types `std::suspend_always` and `std::suspend_never`. What
		is the difference between the two classtypes with respect to their member function:

			constexpr bool await_ready() const noexcept;"},
        {"a", @"1) `std::suspend_always` also returns false indicating that an await
			expression always suspends as it waits for its value.

		2) `std::suspend_never` also returns true indicating that an await
			expression never suspends."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {71, new Dictionary<string, string>() {
        {"q", @"Brief explain heap ellision?"},
        {"a", @"Heap ellision is a way for the compiler to optimize code by
		identifying heap allocations that can be replaced with stack or register
		allocations, without changing the behaviour of the program."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {72, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			std::function<int(int)> cb{
				[i = std::make_unique<int>(42)](const int x) {return x + *i; }
			};

		a) Why would the above trigger a compilation error?
		b) Given your answer to (a) se a C++23 alternative that will allow
			this `cb` initialization to be error-free."},
        {"a", @"a) std::function requires a function object that is copyable, since under the
			hood the lambda is a struct-like with the init capture as a member, this
			unique pointer cannot be copied and thus the pre-condition ""copyable"" fails,
			the compiler compiler raises an error.

		b) Replace 'std::function' with C++23's `std::move_only_function`"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {73, new Dictionary<string, string>() {
        {"q", @"C++20 coroutines are stackless. Explain what it means to be stackless in the 
		context of C++20 coroutines?"},
        {"a", @"Stackless coroutines suspend execution by returning to the caller and the data that is
		required to resume execution is tores separately from the stack."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {74, new Dictionary<string, string>() {
        {"q", @"A function is a coroutine if it contains at least one of 3 expressions. State these
		3 expressions and what they each are used for."},
        {"a", @"1) co_await - to suspend execution until resumed.
		2) co_yield - to suspend execution returning a value
		3) co_return - to complete execution returning a value"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {75, new Dictionary<string, string>() {
        {"q", @"What are the definition of an aggregate as of C++20?"},
        {"a", @"An aggregate is an array or a class with:
			1) no user-declared or inherited constructors
			2) no private or protected non-static data members
			3) no virtual functions
			4) no virtual, private or protected base classes"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {76, new Dictionary<string, string>() {
        {"q", @"a) What does `constinit` do?

		b) In what situations is C++20's `constinit` specifier useful?"},
        {"a", @"a) `constinit` guarantees that initialization occurs at compile
			time and if it cannot initialize the variable at compile time
			it will be a compilation error.
			
			This resolves the 'static '
		
		b) `constinit` is useful in situations where:

			1) you want to ensure that a variable is initialized, and;
			2) that its value cannot be modified after initialization"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {77, new Dictionary<string, string>() {
        {"q", @"True or false, constinit implies const"},
        {"a", @"`constinit` does not imply const, for you can initialize a constinit
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
				}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {78, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet which attempts to capture
		a structured binding into a lambda:

				auto [a, b] = Widget{1, false};
				auto f = [a]{return a > 0;} // is an error

		Does the above compile?"},
        {"a", @"The snippet compiles in C++20, not in C++17."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {79, new Dictionary<string, string>() {
        {"q", @"True or false:
			1) As of C++20, lambdas are not allowed in unevaluated contexts
			2) As of C++20, capturesless lambdas are default constructible and assignable."},
        {"a", @"1) False 2) True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {80, new Dictionary<string, string>() {
        {"q", @"What is the consequence of lambdas being allowed int unevaluated
		contexts e.g.:
			
			decltype([]{}) f;"},
        {"a", @"You can now have a lambda as a member of a classtype:

			class Widget
			{
				decltype([]{}) f;
			}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {81, new Dictionary<string, string>() {
        {"q", @"Explain the meaning of following terms:

			1) Strong structural equality
			2) Weak structural equality
			3) Value equality
			4) Reference equality"},
        {"a", @"Strong structural equality:"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {82, new Dictionary<string, string>() {
        {"q", @"Define strong structural equality and give a concrete code snippet example of it."},
        {"a", @"Types A and B are said to be strong structurally equal if the following holds:

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
				}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {83, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet, with a focus on line (1):

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

		Why have we opted to `std::is_constant_evaluated()` as opposed to `if constexpr()`?"},
        {"a", @"Because `if constexpr` is only evaluated as compile time, meaning the the
		function `square` will only work with compile time arguments. 

		We use `std::is_constant_evaluated()` to evaluated the compile time
		constant arguments for compile time, and then generate the runtime code
		for non-compile time arguments which end up in the else clause."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {84, new Dictionary<string, string>() {
        {"q", @"What does the term 'manifestly constant-evaluated expression' mean?"},
        {"a", @"A manifestly constant-evaluated expression is an expression that has to be
		evaluted at compile time, and it is a compiler error if a manifestly constant-evaluated
		expression cannot be evaluated at compile time.

		Examples of MCEE's include:
			1) case expressions
			2) array bounds
			3) `if constexpr` conditions"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {85, new Dictionary<string, string>() {
        {"q", @"In the context of C++20 coroutines, what is the behaviourial difference
		between std::suspend_always and std::suspend_never?"},
        {"a", @"std::suspend_always:
			'Pause execution at this point, hand control flow back to the caller'

		std::suspend_never:
			'Do not pause execution at this point (i.e. continue executing within the coroutine)'"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {86, new Dictionary<string, string>() {
        {"q", @"True or false (C++20 coroutines context):

			1) The `promise_type` provides the hook to control what happens at startup or
				when we return from the coroutine.
			2) The `Awaitable` provides the hooks for determining what happens when we go into
				suspension.
			3) Every `co_await` call suspends."},
        {"a", @"1) True, 2) True
		3) Falls - not every co_await call suspends."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {87, new Dictionary<string, string>() {
        {"q", @"a) What is one way to think about std::coroutine_handle ?
		b) What is the difference between using the void specialization std::coroutine_handle<>
			and using std::coroutine_handle<promise_type>?"},
        {"a", @"a) As a raw pointer to the coroutine frame.
		b)
			std::coroutine_handle<>:
				is type erased, can point to any coroutine
			
			std::coroutine_handle<promise_type>:
				- simply more specific, the coroutine handle is constrained
					to point to frames that used the `promise_type` passed in as
					a template argument"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {88, new Dictionary<string, string>() {
        {"q", @"What is meant by a 'sink argument'?"},
        {"a", @"The term 'sink argument' is commonly used in the context of 
		rvalue references and move semantics, particular the move ctor/assign
		special member functions.

		In a broader sense, the term can be used to describe any function argument
		that is intended to consume or take ownership of a value without necessary
		using it directly. Examples include smart pointers and function pointers."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {89, new Dictionary<string, string>() {
        {"q", @"Define the three components that make for type erasure."},
        {"a", @"Type erasure is:
			1) a templated constructor; and
			2) a completely non-virtual interface; and
			3) A combination of External Polymorphism + Bridge + Prototype"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {90, new Dictionary<string, string>() {
        {"q", @"a) True or false: 

			You can define a function within another function in C++ e.g.

				int main(void)
				{
					void inner_function()
					{
						std::cout << ""do inner function stuff\n"";
					}
				}"},
        {"a", @"False. Local functions (functions defined within another function) are not permitted,
		but you may declare a function within another function.

		Note: One way of getting around this is to define a local class type and implement
		the call operator. Or you can define a static function within a local class type."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {91, new Dictionary<string, string>() {
        {"q", @"a) What does it mean to 'return perfectly' in C++?

		b) Consider the following snippet (with the BLANK)

			template<typename T>
			__BLANK__ call_foo(T&& t)
			{
				return foo(std::forward<T>(t));
			}

		Fill in the __BLANK__ so that the return value in this forwarding function
		returns perfectly."},
        {"a", @"a) Perfect returning means that the value category of the returned value is preserved.
			This means that if:	
				- The return value category inside the function is an lvalue, we return by reference
				- The return value category inside the function is a prvalue, we return by value

		b) #define __BLANK__ decltype(auto)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {92, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

True or false:
    Non-static constexpr data members are not valid. I.e lines (1) and (2)
    will not compile if the 'static' is removed.
"                   },
                    {"snippetQ", @"
struct MyStruct
{
public:
	static constexpr char who[] = ""John Doe""; // (1)
	static_assert(who[0] == 'J', ""pass"");
	static constexpr const char* o = &who[1]; // (2)
	static_assert(*o == 'o', ""pass"");
};
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {93, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

True or false:
    Casting away the const of a `constexpr` value leads to undefined behaviour.
"                   },
                    {"snippetQ", @"
constexpr int my_constrxpr_value = 100;

void for_main() try
{
	int& ref = const_cast<int&>(my_constrxpr_value);

	ref = 200; // (1)

	std::println(""{}"", my_constrxpr_value);
	std::println(""{}"", ref);
}
catch (std::exception e)
{
	std::println(""{}"",e.what());
}
"},
                    { "a", @"
True - the snippet example leads to a segmentation fault (access violation) at line (1).
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {94, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

Why would we prefer to throw an exception within a constexpr function
as opposed to using a static_assert to validate the pre-conditions?
"                   },
                    {"snippetQ", @"
#include <cmath>
#include <stdexcept>


constexpr double constexpr_pow_int(double base, int exp)
{
	return (exp > 100) || (exp < -100) ?
		throw std::range_error(""abs(exp) exceeds 100"") :
		exp >= 0 ? std::pow(base, exp) : std::pow(base, -exp);
}
"},
                    { "a", @"
The throw idiom for constexpr errors has the benefit of evaluating at both:
    - compile-time (will be a compiler error for compile time-evaluated calls)
    - run-time (will throw std::range_error for runtime-evaluated calls)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {95, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

Which is preferable `use_value_A` or `use_value_B`?
"                   },
                    {"snippetQ", @"
std::string get_value()
{
	return std::string{ ""get_value"" };
}

void use_value_A(int count)
{
	std::string value;
	for (int i = 0; i < count; ++i)
	{
		value = get_value();
	}
}

void use_value_B(int count)
{
	for (int i = 0; i < count; ++i)
	{
		std::string value = get_value();
	}
}

"},
                    { "a", @"
use_value_B is preferable due to:
    a) `value` variable being contained within the for loop (if it is not needed outside)
    b) Reasons outlined in snippet comments
"
                    },
                    {"snippetA", @"
std::string get_value()
{
	return std::string{ ""get_value"" };
}

void use_value_A(int count)
{
	std::string value;                    // default ctor
	for (int i = 0; i < count; ++i)
	{
		value = get_value();              // copy/move assignment
	}
}

void use_value_B(int count)
{
	for (int i = 0; i < count; ++i)
	{
		std::string value = get_value();  // direct-init/RVO
	}
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {96, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet::

a) What does std::remove_all_extents do?
b) State the expected output types passed into the `info` function calls.
"                   },
                    {"snippetQ", @"
#include <iostream>
#include <type_traits>
#include <typeinfo>
 
template<class A>
void info(const A&)
{
    typedef typename std::remove_all_extents<A>::type Type;
    std::cout << ""underlying type: "" << typeid(Type).name() << '\n';
}
 
int main()
{
    float a0;
    float a1[1][2][3];
    float a2[1][1][1][1][2];
    float* a3;
    int a4[3][2];
    double a5[2][3];
    struct X { int m; } x0[3][3];
 
    info(a0); // (A)
    info(a1); // (B)
    info(a2); // (C)
    info(a3); // (D)
    info(a4); // (E)
    info(a5); // (F)
    info(x0); // (G)
}
"},
                    { "a", @"
a) For std::remove_all_extents<T>:
    If T is a multidimension C-style array of type X, then the `typedef type` member is equal to X
    Else:
        T

b)  1) float
    2) float
    3) float
    4) float*
    5) int
    6) double
    7) main::X (although compiler-dependent due to `typeid(T).name`)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {97, new Dictionary<string, string>()
                {
                    { "q", @"
When should you prefer allocating data on the:
    1) Stack
    2) Heap
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) Stack when:
    - The data is small
    - The data doesn't need to persist beyond the scope within which the data is allocated
    - You want speed

2) Heap when:
    - The data is large
    - The data needs to persist beyond the scope within which the data is allocated
    - The data is required to be flexible (i.e. resizing)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {98, new Dictionary<string, string>()
                {
                    { "q", @"
If I have an instance of std::vector, where the capacity is far greater than the size, which member
function should I call to suggest the capacity to be reduced to the size?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::vector::shrink_to_fit

NOTE: That this is a non-binding request (meaning it is a suggestion, not an obligation, to the C++ STL implementors)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {99, new Dictionary<string, string>()
                {
                    { "q", @"
a) What is the C++ symbol table? 
b) What is the C++ symbol table used for?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) The C++ symbol table is:
    - a key component in the compiler's semantic analysis phase
    - a multi-level (hierarchical) data structure:
        - global (scope) symbol table
        - local (scope) symbol table
        - class/namespace (scope) symbol table

b) The C++ symbol table is a key component in the compiler's semantic analysis phase.
    The C++ symbol table is also used for:
    - keeping track of storage details (name, data type, scope, linkage (internal/external), memory location)
    - handling overloading and templates
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {100, new Dictionary<string, string>()
                {
                    { "q", @"
a) True or false:
    If you put a class into a namespace, you should put all adjacent entities:
        - free functions that are supplied with an instance of a class
        - other entities that reference/make user of the class

    Into that same namespace

b) BONUS: What is the above guideline called and who invented it?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) True
b) Interface principle, Herb Sutter
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {101, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

a) What gets printed on line (1)?
b) What gets printed on line (2)?
"                   },
                    {"snippetQ", @"
#include <cstring>
#include <print>

// function template
template<typename T>
const T& max(const T& a, const T& b)
{
	// implementation
	std::println(""1"");
	return (a > b) ? a : b;
}

// non-template free function
char const* max(const char* a, const char* b)
{
	std::println(""2"");
	return std::strcmp(a, b) ? a : b;
}


// template specialization
template <>
const char* const& max(const char* const& a, const char* const& b)
{
	std::println(""3"");
	return (std::strcmp(a, b) > 0) ? a : b;
}


void for_main()
{
	const char* a = ""a"";
	const char* b = ""b"";
	auto c = max(a, b);					// line (1)
	auto d = max<const char *>(a, b);	// line (2)
}
"},
                    { "a", @"
a) 2
b) 3
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {102, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the snippet:

Which of (1) or (2) is cheap/expensive to call? Why?
"                   },
                    {"snippetQ", @"
void for_main()
{
	std::vector<int> vec{ 0, 8, 15, 47, 11, 42 };
	auto view1 = vec | std::views::drop(100);
	auto pos = view1.begin();			// (1) - lazily evaluated .begin()

	std::list<int> list{ 0, 8, 15, 47, 11, 42 };
	auto view2 = list | std::views::drop(100);
	auto pos2 = view2.begin();			// (2) - lazily evaluated .begin()
}
"},
                    { "a", @"
(1) Cheap:
    - std::vector is a random-access ranges (satisfies std::ranges::random_access_range)
    - Calling begin after the drop of 100 is equivalent to .begin() + 100

(2) Expensive:
    - std::list is a linked list
    - Calling .begin() after the drop of 100 is equivalent to calling .begin() then ++ 100 times
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {103, new Dictionary<string, string>()
                {
                    { "q", @"
Which of the following C++20 views cache begin?

    a) filter
    b) drop_while
    c) split
    d) drop
    e) reverse
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) always
b) always
c) always
d) sometimes (e.g. std::vector no, std::list yes)
e) sometimes
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {104, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet with an emphasis on line (1)

Example why line (1) causes a compiler error.
"                   },
                    {"snippetQ", @"
#include <vector>
#include <ranges>
#include <iostream>
#include <list>

void print(const std::ranges::input_range auto range)
{
	for (const auto& element : range)
	{
		std::cout << element << ' ';
	}
	std::cout << '\n';
}

void for_main()
{
	std::vector<int> vector{ 0, 8, 1, 47, 11, 42, 2 };
	std::list<int> list{ 0, 8, 1, 47, 11, 42, 2 };

	print(vector);
	print(list);

	print(vector | std::views::take(3));
	print(list | std::views::take(3));

	print(vector | std::views::drop(3));
	print(list | std::views::drop(3));     // line (1)

	print(vector | std::views::reverse);
	print(list | std::views::reverse);
}
"},
                    { "a", @"
The drop view on std::list is expensive, calling ++ n times given std::views::drop(n).

Since this call is expensive, under-the-hood the begin() value is cached to prevent the
traversal happening again.

This caching modifies the view - and since the print function was declared const it cannot
compile.

Not that caching logic happens within the for loop since views are lazily evaluated.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {105, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    std::ranges::subrange is a view that stores/caches .begin() on 
    initialization.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {106, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

a) What is the key difference between a 'ref_view' and an 'owning_view'?
b) What is the consequence of this difference in C++20 (believe this is fixed in C++23)?
"                   },
                    {"snippetQ", @"
#include <vector>
#include <ranges>

std::vector<int> get_vector()
{
	return { 1, 2, 3, 4, 5 };
}

void for_main()
{
	auto greater_than_9 = [](auto element) {return element > 9; };

	std::vector<int> collection = get_vector();


	// typeid(ref_view).name() == std::ranges::filter_view<std::ranges::ref_view<std::vector<int>>>
	auto ref_view = collection | std::ranges::views::filter(greater_than_9);

	// typeid(owning_view).name() == std::ranges::filter_view<std::ranges::owning_view<std::vector<int>>>
	auto owning_view = get_vector() | std::views::filter(greater_than_9);
}
"},
                    { "a", @"
a)
    A ref_view has the underlying range to which the view refers to outside of the scope of
    the view.

    An owning view contains the underlying range as a member.

b) ref_view does NOT propogate const, while owning_view does propagate const
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {107, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

True or false:
    1) `big_class_type_0` subsumes the concepts `big_type`
    2) `big_class_type_1` subsumes the concepts `big_type`
"                   },
                    {"snippetQ", @"
#include <type_traits>

template<typename T>
concept big_type = sizeof(T) > 8;

template<typename T>
concept big_class_type_0 = sizeof(T) > 8 && std::is_class_v<T>;

template<typename T>
concept big_class_type_1 = big_type<T> && std::is_class_v<T>;
"},
                    { "a", @"
1) False - only concept constraints are checked for subsumption
2) True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {108, new Dictionary<string, string>()
                {
                    { "q", @"
Why is the c-style 'std::printf' not recommended (vs. C++20's std::format)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::printf is not recommended as it is:
    - not type safe
    - not extensible (only supports a fixed number of types)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {109, new Dictionary<string, string>()
                {
                    { "q", @"
State at least 5 calendrical types in <chrono>.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Any 5 of:
    1) std::chrono::day
    2) std::chrono::month
    3) std::chrono::year
    4) std::chrono::month_day
    5) std::chrono::weekday
    6) std::chrono::weekday_indexed
    7) std::chrono::year_month_day
    8) std::chrono::year_month_day_last
    9) std::chrono::year_month_weekday_last
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {110, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

True or false:

Both 0 and 7 are valid for initializing calendrical type std::chrono::weekday
to Sunday.
"                   },
                    {"snippetQ", @"
void for_main()
{
	std::chrono::weekday sunday1{ 0 };
	std::chrono::weekday sunday1{ 7 };
}
"},
                    { "a", @"
True - looks like we simply check for 7 in the ctor initializer list (see snippet).
"
                    },
                    {"snippetA", @"
_EXPORT_STD class weekday {
public:
	weekday() = default;
	constexpr explicit weekday(unsigned int _Val) noexcept
		: _Weekday{ static_cast<unsigned char>(_Val == 7 ? 0 : _Val) } {
	}

	// ....
};

"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {111, new Dictionary<string, string>()
                {
                    { "q", @"
What does the calendrical type std::chrono::weekday_indexed represent?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::chrono::weekday_indexed represents a combination of:
    1) a weekday i.e. a day of the week in the Gregorian calendar
    2) an index range [1, 5] representing the weekday of the month (1st, .., 4th and so on)

See the snippet
"
                    },
                    {"snippetA", @"
void for_main2()
{
	// represents the first Monday of the month
	constexpr auto wdi = std::chrono::weekday_indexed{ std::chrono::Monday, 1 };
	// represents the third Wednesday of the month
	constexpr auto wdi2 = std::chrono::weekday_indexed{ std::chrono::Wednesday, 3 };
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {112, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

Enhance this snippet to bring in the chrono suffix literals (e.g. 'd' and 'y')
without exposing the entire std::chrono:: namespace.
"                   },
                    {"snippetQ", @"
#include <chrono>
#include <iostream>

void for_main()
{
	std::chrono::year_month_day ymd1{ std::chrono::October / 28d / 2021y };
}
"},
                    { "a", @"
See snippet
"
                    },
                    {"snippetA", @"
#include <chrono>
#include <iostream>

void for_main()
{
	using namespace std::chrono_literals; // brings in literals 'd' and 'y'
	std::chrono::year_month_day ymd1{ std::chrono::October / 28d / 2021y };
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {113, new Dictionary<string, string>()
                {
                    { "q", @"
Fun one:

For a type T to qualify as a Clock, it must satisfy each of the following conditions:

The following qualified-ids must be value and denote a type:
    1) T::rep
    2) T::period
    3) T::duration
    4) T::time_point

The following expressions must be well-form when treated as an unevaluated operand:
    5) T::is_steady
    6) T::now()

Write up the above requirements into a 'clock_concept' concept
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
See snippet (pretty much what MSVC implemented for 'is_clock_v')
"
                    },
                    {"snippetA", @"
template<typename T>
concept clock_concept = requires
{
   typename T::rep;
   typename T::period;
   typename T::duration;
   typename T::time_point;

   T::is_steady;
   T::now();
};
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {114, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

What is C++23's 'auto(x)' and when shoud you use it.
"                   },
                    {"snippetQ", @"
#pragma once
#include <concepts>
#include <print>

void for_main1()
{
    // auto(x) decays arrays to pointers
 	int arr[] = { 1, 2, 3 };
	auto decayed_arr = auto(arr);  // line (1)

    static_assert(std::same_as<decltype(decayed_arr), int*>);
}

void for_main2()
{
    auto value = auto(generate());  // line (2)
    std::println(""{}"", value);
}


void for_main() {for_main2();}
"},
                    { "a", @"
auto(x) is a concise syntax for creating decayed prvalue copies of objects
in C++23.

You should use it when you need a type-decayed version of an object or expression.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {115, new Dictionary<string, string>()
                {
                    { "q", @"
What is variable shadowing?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Variable shadowing is when a variable in an inner scope is declared and initialized
while a variable in an outerscope with the same name already exists.

See snippet.
"
                    },
                    {"snippetA", @"
int func(int param)
{
    int i{param};
    int sum{0};

    for(
        int i = param; // variable `i` shadowed, lifetime is for the entire duration of loop 
        i > 0;
        --i)
    {
        int sum{5}; // variable `sum` shadowed, lifetime is per-iteration of the loop
        sum += i;
    }

    return sum;
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {116, new Dictionary<string, string>()
                {
                    { "q", @"
What is lock-free programming?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Lock-free programming is a way of designing concurrent programs without using
traditional locking mechanisms (e.g. std::mutex) to coordinate access to shared data.

Instead, it relies on atomic operations that guarantee consistency and correctness
without blocking threads.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {117, new Dictionary<string, string>()
                {
                    { "q", @"
Consider and outline the key characteristics of lock-free programming:

1) No blocking
2) Atomicity
3) No deadlocks
4) Better performance
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) No blocking:
    - Threads never wait on a lock, they can always make progress independently
2) Atomicity
    - Operations on shared data are performed atomically
3) No deadlocks
    - Because there are no locks, deadlocks (when threads are waiting on each other)
        cannot occur.
4) Better performance
    - often faster in high concurrency scenarios, as threads are not stalled by waiting for locks.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {118, new Dictionary<string, string>()
                {
                    { "q", @"
What is a reentrant function?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
A reentrant function is one which can be interrupted during execution of a
1st call and be able to be called a 2nd time before the 1st call completes.

This interruption might be a:
    1) hardware interrupt
    2) signal - such as a segfault
    3) an exception
    4) another any mechanism which transfers control without the 1st call completing.

The 1st function call must resume (from its interruption point) with correct execution.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {119, new Dictionary<string, string>()
                {
                    { "q", @"
State which mutex wrapper you would reach for in the following use-case scenarios:

1) Need simple, scope-based locking when no additional flexibility is required
2) Need more control over locking and unlocking, or when integrating synchronization
    primitives like std::condition_variable.
3) Need to lock multiple mutexes safely and efficiently
4) Need non-blocking attempts to lock one or more mutexes
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) std::lock_guard
2) std::unique_lock
3) std::scoped_lock
4) std::try_lock
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {120, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet?

Explain what is going on with respect to line (1) i.e. the initialization
of the static 'ComplicatedObject' instance:
    a) which thread will construct the object?
    b) what is the other thread doing while that is going on?
"                   },
                    {"snippetQ", @"
#include <thread>
#include <print>
#include <string>

struct ComplicatedObject
{
	std::string x;
	std::string y;
};

void foo()
{
	static ComplicatedObject obj{ ""some"", ""data"" };     // line (1)
	std::println(""{}: Hello from foo! obj.x={}, obj.y={}"", std::this_thread::get_id(), obj.x, obj.y);
}

void for_main()
{
	// which thread initializes 'obj'??
	std::thread t1{ foo }, t2{ foo };

	t1.join(); t2.join();
}
"},
                    { "a", @"
The core C++ language is aware of threads (core-language-threading).

a) The first thread to arrive will start initializing the static instance
b) Any additional threads to arrive at line (1) will BLOCK AND WAIT until
    the first thread either:
    1) succeeds - unblocking them all
    2) fails with an exception - unblocking one of them.

This process is known as thread-safe static initialization.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {121, new Dictionary<string, string>()
                {
                    { "q", @"
C++20 provides std::stop_source and std::stop_token to handle cooperative
cancellation.

True or false:
    If the target task to be stopped doesn't check for a stop from the stop source
    thread, nothing happens.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True - that is the essence of cooperative cancellation.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {122, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    Starting a std::jthread does not implicitly create a std::stop_source object.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
False - starting a std::jthread DOES implicitly create a std::stop_source object.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {123, new Dictionary<string, string>()
                {
                    { "q", @"
What is a definition of a data race?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Unsynchronised access to a memory location from more than one thread, where at
least one thread is writing.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {124, new Dictionary<string, string>()
                {
                    { "q", @"
Which STL synchronisation primitive matches the following description:

- single-use counter that allows threads to wait for the count to reach 0
- is constructed with a non-zero count
- one or more threads may decrease the count
- other threads may wait for this primitive to be signalled
- when the count reaches 0 it is permanently signalled and all waiting threads
    are awoken.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::latch
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {125, new Dictionary<string, string>()
                {
                    { "q", @"
Which STL synchronisation primitive (SP) matches the following description:

Synchronization is done in phases:

- construct this SP with a non-zero count and a completion function
- one or more threads arrive at this SP
- some of these threads wait for the SP to be signalled
- when the count reaches zero:
    1) the SP is signalled
    2) the completion function is called
    3) the count is reset
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::barrier<>
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {126, new Dictionary<string, string>()
                {
                    { "q", @"
State two differences between std::barrier and std::latch.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1. std::barrier, unlike std::latch, is reusable
    i.e. once the group of arriving threads are unblocked, the barrier can be reused.

2. std::barrier, unlike std::latch, executes a possibly empty callable 'completion function'
    before unblocking threads.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {127, new Dictionary<string, string>()
                {
                    { "q", @"
Which part of the following, if at all, is false?

    std::barrier<COMPLETION_FUNCTION> is great for loop synchronisation between
    parallel tasks. The COMPLETION_FUNCTION allows you to do something between loops e.g.:
        1) pass the result on to another step
        2) write to a file

    The COMPLETION_FUNCTION is run on one of the participating threads.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
No part of the excerpt is false.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {128, new Dictionary<string, string>()
                {
                    { "q", @"
What does std::shared_future allow for?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
std::shared_future allows multiple threads to receive the same result (see snippet).
"
                    },
                    {"snippetA", @"
#include <chrono>
#include <print>
#include <future>
#include <thread>

void do_stuff(int i)
{
	std::println(""{}: do_stuff({})"", std::this_thread::get_id(), i);
}

void for_main()
{
	std::promise<int> int_promise;
	std::shared_future int_shared_future = int_promise.get_future().share();

	std::jthread jt0{
		[int_promise = std::move(int_promise)]() mutable {int_promise.set_value(42); }
	};

	std::jthread jt1{ [int_shared_future] {do_stuff(int_shared_future.get());  } };
	std::jthread jt2{ [int_shared_future] {do_stuff(int_shared_future.get());  } };
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {129, new Dictionary<string, string>()
                {
                    { "q", @"
Consider std::counting_semaphore<MAX_COUNT>.

True or false:
    std::binary_sempahore is an alias for std::counting_semaphore<2>.
    
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
False.

std::counting_semaphore<2> implies that the semaphore can be acquired up to two times
while std::binary_semaphore can only be acquired once at any given time. See snippet
for the MSVC alias.
"
                    },
                    {"snippetA", @"
_EXPORT_STD using binary_semaphore = counting_semaphore<1>;
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {130, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

True or false:
    The initial count of the semaphore must match the maximum count specified
    in the non-type template parameter
"                   },
                    {"snippetQ", @"
#include <semaphore>

void for_main()
{
	// non-type template parameter = 5 = max count 
	// constructor argument passed = 5 = initial count of the semaphore
	std::counting_semaphore<5> slots{ 5 };
}
"},
                    { "a", @"
False.

The constraint is: INITIAL_COUNT <= MAX_COUNT

It is a runtime error to have INITIAL_COUNT > MAX_COUNT (see snippet)
"
                    },
                    {"snippetA", @"
#include <semaphore>

void for_main()
{
	// initial count exceed max specified in the NTTP - runtime error!
	std::counting_semaphore<5> slots{ 6 };
}
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {131, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {132, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {133, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {134, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {135, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {136, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {137, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {138, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {139, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {140, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {141, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {142, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {143, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {144, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {145, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {146, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {147, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {148, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {149, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {150, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {151, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {152, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {153, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {154, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {155, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {156, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {157, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {158, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {159, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {160, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {161, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {162, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {163, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {164, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {165, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {166, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {167, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {168, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {169, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {170, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {171, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {172, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {173, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {174, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {175, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {176, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {177, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {178, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {179, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {180, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {181, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {182, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {183, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {184, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {185, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {186, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {187, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {188, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {189, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {190, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {191, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {192, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {193, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {194, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {195, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {196, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {197, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {198, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {199, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {200, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
};
    }
}
