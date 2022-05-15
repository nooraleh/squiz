# Notes taken in a QNA style from Scott Meyer's 'Effective Modern C++'

qna = {
    1: {
		'q':  """
		In the context of exception safety, what is meant when a function is said 
		to offer:

			i)  the basic exception guarantee
			ii) the strong exception guarantee
		""",
		'a': """

		i) Basic guarantee - Assures function callers that even if an exception
			is thrown, program invariants remain intact i.e no data structure corruption,
			no resource leaks.

		ii) Strong guarantee - assures callers that if an exception arises, the state of
			the program remains as it was prior to the call.
		""",
	},
    2: {
		'q':  """
		In the context of design-by-contract, what is meant by a program invariant?
		""",
		'a': """
		A program invariant is condition that must be satisfied during the whole execution
		of the function or method.
		""",
	},
    3: {
		'q':  """
		Consider the following snippet:

			template<typename T>
			void f(T& param);

		State the deduced type of i) `T` and ii) `param`
		in the following cases:


		1) int x = 27; f(x);
		2) const int cx = x; f(cx);
		3) const int& rx = x; f(rx);


		""",
		'a': """
		
		1) T is `int`, param's type is `int&`
		2) T is `const int`, param's type is `const int&`
		3) T is `const int`, param's type is `const int&`

		""",
	},
    4: {
		'q':  """
		Consider the following snippet:

			template<typename T>
			void f(const T& param);

		State the deduced type of i) `T` and ii) `param`
		in the following cases:

		1) int x = 27; f(x);
		2) const int cx = x; f(cx);
		3) const int& rx = x; f(rx);

		""",
		'a': """
		1) T is `int`, param's type is `const int&`
		2) T is `int`, param's type is `const int&`
		3) T is `int`, param's type is `const int&`

		""",
	},
    5: {
		'q':  """
		Consider the following snippet:

			template<typename T>
			void f(T&& param);

			int x = 27;
			const int cx = x;
			const int& rx = x;

		State the deduced types for (i) `T` (ii) `param`
		in the following cases:

			1) f(x);
			2) f(cx);
			3) f(rx);
			4) f(27);
		""",
		'a': """

			1) x is lvalue, so: (i) T is int& (ii) param's type also int&
			2) cx is lvalue, so: (i) T is const int& ii) param's type is const int&
			3) rx is lvalue, so: (i) T is const int& ii) param's type is const int&
			4) 27 is rvalue, so: (i) T is int, ii) param's type is int&&
		""",
	},
    6: {
		'q':  """
		Fill in the blank in the following statement:

			`const` and `volatile` qualifiers are ignored only for by-<_____> parameters
		""",
		'a': """
		ANS: value (pass-by-value parameters)
		""",
	},
    7: {
		'q':  """
		State:
		
			i) the two things that may decay to pointers upon being passed as an
				argument to a function,
			ii) the caveat for this decomposition
		""",
		'a': """

			i)  (1) array names (2) function names
			ii) unless they're used to initializze references
		""",
	},
    8: {
		'q':  """
		i) In C++11, what is the only way in which `auto` type deduction and template
			type deduction differ. 
			
		ii) Give a concrete example of your answer to (i)
		""",
		'a': """
		i)  In the treatment of std::initializer_list

		ii) 
			auto x = {11, 23, 9}; // x's type: std::initializer_list<int> //success

			template<typename T>
			void f(T param);

			f({11, 23, 9});  // error - cannot deduce type for T
		""",
	},
    9: {
		'q':  """
		Consider the following snippet:

			auto create_init_list()
			{
				return {1, 2, 3};
			}

		i) Does the snippet compile?
		ii) Why? Why not?
		""",
		'a': """
		i)  It does not compile
		ii) The `auto` in this case employs template type deduction rules
			not `auto` type deduction. There braced initializaers won't compile.
				
		Compilation error excerpt:
			C2440 'return': cannot convert from 'initializer list' to 'auto'
		""",
	},
    10: {
		'q':  """
		Consider the following snippet:

			std::vector<int> v;
			auto reset_V = [&v](const auto& new_value) {; };

			reset_V({1, 2, 3});

		----------
		i) Does the above code compile in C++14?
		ii) Why? Why not?

		""",
		'a': """
		i)  No.
		ii) C++14 lambda auto params use template type deduction rules,
			and therefore cannot handle brace initialized arguments.
		""",
	},
	11: {
		'q':  """
		Consider the following snippets:

			decltype(auto) f1()
			{
				int x = 0;
				return x;
			}

			decltype(auto) f2()
			{
				int x = 0;
				return (x);
			}

		What is the return type for:

			1) f1
			2) f2
		""",
		'a': """

			1) int
			2) int&
		""",
	},
	12: {
		'q':  """
		What is the main benefit (difference) of using <functional>'s std::function
		over employing function pointers?
		""",
		'a': """
		Function pointers can only point to functions. However, std::function
		objects can refer to any callable object.
		""",
	},
	13: {
		'q':  """
		std::vector<T>::operator[] (assuming access is valid)
		returns a reference to an element of type T for all T except for which
		data type?
		""",
		'a': """
		Except for bool. std::vector<bool> returns std::vector<bool>::reference
		because std::vector<bool> is specified to represent its `bool`s in packed form
		i.e one bit per bool.
		""",
	},
	14: {
		'q':  """
		i)  What is a proxy class?
		ii) Give a concrete example of a proxy class?
		""",
		'a': """
		i) A proxy class is a class that exists for the purpose of emulating
		and augmenting the behaviour of some other type.

		ii) Options include
			1) std::vector<bool>::reference, exists to offer the illusion that
			operator[] for std::vector<bool> returns a reference to a bit.

			2) smart points as proxy classes for raw pointers
		""",
	},
	15: { # chapter 3: Moving to Modern C++
		'q':  """
		Consider the following snippet:

			class Widget
			{
			private:
				int x{ 0 };   (1)
				int y = 0;    (2)
				int z(0);     (3)
			};
		
		i)  What types of initialization are (1), (2) and (3) known as?
		ii) Which line triggers a compiler error?
		""",
		'a': """
		i)
			(1) - Uniform initialization
			(2) - copy initialization
			(3) - direct intialization

		""",
	},
	16: {
		'q':  """
		Consider the following snippet:

			double x, y, z;

			int sum1{ x + y + z }; (1)
			int sum2(x + y + z);   (2)
			int sum = x + y + z;   (3)

		i)  What type of conversion would implicitly take place in all three lines?
		ii) Given your answer to (i), which lines give compiler errors and which warnings? 
		""",
		'a': """
		i) Implicit narrowing conversion
		ii) (1) gives a compiler error, (2) and (3) give warnings
		""",
	},
	17: {
		'q':  """
		What is the output of the following snippet:

			class Widget
			{
			public:
				Widget() {
					std::cout << "parameterless constructor" << std::endl;
				}

				template<typename T>
				Widget(std::initializer_list<T> il)
				{
					std::cout << "initializer list constructor" << std::endl;
				}
			};

			int main(void)
			{
				Widget{};
				return 0;
			}
		""",
		'a': """
		ANS: parameterless constructor
		NB: This is an odd edge case as uniform unitialized objects tend
			to dispatch to constructors with initializer_list parameters.
		""",
	},
	18: {
		'q':  """
		What is a compelling technical reason for preferring 'using' aliases
		declarations over `typedef`s?
		""",
		'a': """
		In C++11, alias declarations may be templatized (alias templates) while
		`typedef`s cannot.
		""",
	},
	19: {
		'q':  """

		""",
		'a': """
		
		""",
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
	29: {
		'q':  """
		""",
		'a': """
		""",
	},
	30: {
		'q':  """
		""",
		'a': """
		""",
	},
	31: {
		'q':  """
		""",
		'a': """
		""",
	},
	32: {
		'q':  """
		""",
		'a': """
		""",
	},
	33: {
		'q':  """
		""",
		'a': """
		""",
	},
	34: {
		'q':  """
		""",
		'a': """
		""",
	},
	35: {
		'q':  """
		""",
		'a': """
		""",
	},
	36: {
		'q':  """
		""",
		'a': """
		""",
	},
	37: {
		'q':  """
		""",
		'a': """
		""",
	},
	38: {
		'q':  """
		""",
		'a': """
		""",
	},
	39: {
		'q':  """
		""",
		'a': """
		""",
	},
	40: {
		'q':  """
		""",
		'a': """
		""",
	},
	41: {
		'q':  """
		""",
		'a': """
		""",
	},
	42: {
		'q':  """
		""",
		'a': """
		""",
	},
	43: {
		'q':  """
		""",
		'a': """
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
}
