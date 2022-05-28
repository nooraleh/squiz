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
		When C++ is given a choice between converting a float to an:
			1) int
			2) double

		Which conversion does C++ prefer?
		""",
		'a': """
		ANS: (2) i.e double
		""",
	},
	20: {
		'q':  """
		True or false:

		When is comes to pointers of type `void*`:

			1) there is no way to dereference them
			2) there is no way to increment them
			3) there is no way to decrement them
		""",
		'a': """
		All three statements are false.
		""",
	},
	21: {
		'q':  """
		True or false:

			It is possible to give a member function template specialization
			a different access level from that of the main template.

		I.e

			class Widget
			{
			public:
				template<typename T>
				void example(T* param) {}

			private:
				template<>
				void example<int>(int* param) {}
			};
		""",
		'a': """
		False. This is because template specialization must be
		written at namespace scope, not class scope.
		""",
	},
	22: {
		'q':  """
		Let's talk class member function reference qualifiers.
		Consider the snippet:
			class Widget
			{
			public:
				void do_work()&;  // (1)

				void do_work()&&; // (2)
			};

		Explain the significant of lines (1) and (2).
		""",
		'a': """
		(1) this version of do_work() is called only
			when *this is an lvalue
		(2) this version of do_work() is called only
			when *this is an rvalue
		""",
	},
	23: {
		'q':  """
		Describe the object code ramifications of declaring a function `noexcept`?
		""",
		'a': """
		In a `noexcept` marked function:

			1) optimizers need not keep the runtime stack in an unwindable
				state if an exception would propagate out of the function
			2) optimizers need not ensure that objects in a `noexcept` function
				are destroyed in reverse order of construction should an exception
				leave the function.
		""",
	},
	24: {
		'q':  """
		In the context of library interface design, what is meant by:
		a)
			i)  A function with a wide contract
			ii) A function with a narrow contract

		b) Which of (i) or (ii) is marked `noexcep`
		""",
		'a': """
		a)
			i) A function with a wide contract:

				1) has no preconditions
				2) may be called regardless of the state of the program
				3) imposes no constraints on the arguments that callers pass it
				4) never exhibit undefined behaviour

			ii) Narrow contracts - functions without a wide contract

		b) Functions with wide contracts
		""",
	},
	25: {
		'q':  """
		Which of `std::atomic` or `std::mutex` is more appropriate for the following scenarios:

			1) A single variable or memory location requiring synchronization
			2) Two or more variables or memory locations that requires manipulation as a unit
		""",
		'a': """
			1) std::atomic
			2) Mutex
		""",
	},
	26: {
		'q':  """
		What is the difference in code generation between:
			1) copy construction/assignment, AND;
			2) move construction/assignment
		""",
		'a': """
		The copy construction/assignment operations are independent.
		Declaring one doesn't prevent compilers from generating the other.

		The move construction/assignment operations, however, are not independent.
		If you declare either, that prevents compilers from generating the other.
		""",
	},
	27: {
		'q':  """
		i) True or false:

			Move operations will be generated for any class that
			explicitly declares a copy.

		ii) State the justification to your answer to (i)
		""",
		'a': """
		i) False, move operations will not be generated in that case.

		ii) The justification is that declaring a copy operation (construction
			or assignment) indicates that the normal approach to copying an object
			(memberwise copy) isn't appropriate for that particular class.

			Therefore, compilers figure that if memberwise copy isn't appropriate
			for the copy operations, memberwise move probably isn't appropriate
			and so move operations will NOT be generated by the compiler.
		""",
	},
	28: {
		'q':  """
		True or false:

			Declaring at least one move operation (construction or assignment)
			in a class causes compilers to disable the copy operations
			(via implicitly deleting them).
		""",
		'a': """
		True.
		""",
	},
	29: {
		'q':  """
		In C++11, move operations are (implicitly compiler) generated for
		classes only if what three things are true?
		""",
		'a': """
			1) No copy operations are declared in the class
			2) No move operations are declared in the class
			3) No destructor is declared in the class
		""",
	},
	30: {
		'q':  """
		Why do polymorphic base classes normally have virtual destructors?
		""",
		'a': """
		Because if they don't, some operations (e.g the use of `delete`
		or `typeid` on a derived class object through a base class pointer
		or reference) yield undefined or misleading results.
		""",
	},
	31: {
		'q':  """
		What is a common use case for std::unique_ptr ?
		""",
		'a': """
		A common use for std::unique_ptr is as a factory function return type
		for objects in a hierarchy.
		""",
	},
	32: {
		'q':  """
		Consider the following statements about the existence of the 
		reference (i.e use of std::shared_ptr):

			1) std::shared_ptr are twice the size of a raw pointer
			2) Memory for the reference count must be dynamically allocated
			3) Increments and decrements of the reference count must be atomic

		Explain the performance implication(s) of each statement.
		""",
		'a': """
			1) Because they internally contain a raw pointer to the resource
				as well as a raw pointer to the resource's reference count.
			2) Conceptually, the reference count is associated with the object
				being pointed to, but in reality pointed-to objects know nothing
				about the reference count.

				The pointed-to objects thus have no place to store a reference count.
				NB: The cost of dynamic allocated is avoided when the std::shared_ptr
				is created via std::make_shared.

			3) This is because there can be simulataneous readers and writers
				in different threads.

				For example, in one thread, we could be executing std::shared_ptr's
				destructor, hence decrementing the reference count. While in 
				another thread, we may be calling the constructor, hence incrementing.
				Since this operators may be simulatenous we must protect against
				read/write with std::atomic.

				Atomic operations are typically slower than non-atomic operation,
				so we would see a performance hit in multithreaded environments.

		""",
	},
	33: {
		'q':  """
		Which of the following smart pointers:

			1) std::shared_ptr
			2) std::unique_ptr

		Specifies a custom deleter as point of it's type?

		In other words, which of lines (1) or (2) is valid?
			auto custom_deleter = [](T* pt)
			{
				// do custom stuff
				delete pt;
			};

			1) std::shared_ptr<T, decltype(custom_deleter)> // ...instantiate
			2) std::unique_ptr<T, decltype(custom_deleter)> // ...instantiate
		""",
		'a': """

		ANS: (2) std::unique_ptr i.e line (2) is correct
		""",
	},
	34: {
		'q':  """
		In the context of smart pointer memory management, what is the
		control block?
		""",
		'a': """
		The control block is a heap-allocated data structure that exists for each
		object managed by std::shared_ptrs.

		The control block contains the following data:

			1) reference count
			2) weak count
			3) custom deleter (if specified)
			3) custom allocators (if specified)
		""",
	},
	35: {
		'q':  """
		Why would constructing (not via make_shared) more than one
		std::shared_ptr from a single raw pointer lead to undefined behaviour?

		Illustrative snippet:

			auto pw = new Widget;
			std::shared_ptr<Widget> spw1(pw);
			std::shared_ptr<Widget> spw2(pw);
		""",
		'a': """
		Because
			- the pointed-to object will have multiple control blocks.
			- multiple control blocks means multiple reference counts
			- multiple reference counts mean the object will be destroyed
				multiple times.
		""",
	},
	36: {
		'q':  """
		i)  What would you use if you want a class managed by std::shared_ptrs
			to be able to safely create a std::shared_ptr from a `this` pointer?
		ii)	Write a code snippet to demonstrate its usage.
		""",
		'a': """
		i) Use <memory>'s base class template `std::enable_shared_from_this<T>`

		ii)

			class Widget : public std::enable_shared_from_this<Widget>
			{
			/* members .... */
			}

		Now Widget instances have access to a `shared_from_this()` member
		function which can be used inside the class in move operations e.g

			void Widget::process()
			{
				m_process_widgets.emplace_back(shared_from_this());
			}
		""",
	},
	37: {
		'q':  """
		i)  What does CRTP stand for?
		ii) Which base class template is most commonly associated with CRTP?
		""",
		'a': """
		i)  Curiously recurring template pattern - CRTP
		ii) <memory>'s std::enable_shared_from_this
		""",
	},
	38: {
		'q':  """
		Out of:

			1) std::shared_ptr
			2) std::unique_ptr

		Which one can work with C-style arrays?
		""",
		'a': """
		std::unique_ptr can work with C-style arrays, std::shared_ptr
		cannot.

		I.e. you cannot have std::shared_ptr<T[]>
		""",
	},
	39: {
		'q':  """
		True or false:

		In C++11:
			1) std::weak_ptr's can be dereferenced
			2) std::weak_ptr's cannot be tested for nullness
		""",
		'a': """
			1) false
			2) true
		""",
	},
	40: {
		'q':  """
		Which member function can you use to tests
		if a weak point no longer points to an object?
		""",
		'a': """
		std::weak_ptr::expired
		""",
	},
	41: {
		'q':  """
		Consider the following snippet:

			class Widget {};
			int compute_priority() {/*runtime computation of priority*/}

			void process_widget(
				std::shared_ptr<Widget>(new Widget),
				compute_priority()
			);

		i) In what circumstance can the above snippet lead to a resource leak?
		ii) How would you rewrite the invocation of `process_widget` to
			ensure against resource leaks?
		""",
		'a': """
		i) At runtime, the arguments for a function must be evaluated before
		the function can be invoked.

		However, compilers are new required to generate code that executes
		the evaluation of arguments in order.

		I.e we may get this order:

			1. perform "new Widget"
			2. execute `compute_priority`
			3. call std::shared_ptr constructor

		If step 2. throws an exception - then the dynamically allocated
		Widget from step 1. will be leaks, as the exception means that step 3.
		will not occur.

		ii) void process_widget(
				std::make_shared<Widget>(),
				compute_priority()
			);
		""",
	},
	42: {
		'q':  """
		Despite the overwhelming arguments of using std::make_*
		instead of directly using the constructor for smart pointers,
		give two usage cases where using the smart pointer constructor would be
		favourable.
		""",
		'a': """
		1) std::make_* doesn't permit for custom deleters - so if you were
		required to develop and use a custom deleter - then you'd have
		to pass it as an argument to the constructor.

		2) Passing braced initializers - however you can still use std::make_*
			if you assign the braced initializer to a variable.
		""",
	},
	43: {
		'q':  """
		i)  What does Pimpl stand for?
		ii) When using the Pimpl idiom, where should you define the special
			member functions?
		iii) What benefits do Pimpl idiom enjoy?
		""",
		'a': """
		i)  Pointer to implementation
		ii) In the implementation file (i.e the .cpp).
		iii) Benefit: reduces compilation dependencies between a class's
				implementation and the class's clients.
		""",
	},
	44: {
		'q':  """
		What does the Pimpl (pointer to implementation) idiom entail?
		
		""",
		'a': """
		The Pimpl idiom is a technique whereby you replace the data members
		of a class with a pointer to an implementation class (or struct),
		put the data members that used to be in the primary class into the
		implementation class, and access those data members indirectly
		through the pointer.
		""",
	},
	45: {
		'q':  """
		What do we call a type that has been declared, but not defined?
		""",
		'a': """
		We call this type an 'incomplete type'.
		""",
	},
	46: {
		'q':  """
		Give a brief description of what the functions
			i)  std::move
			ii) std::forward
		Do in essence.
		""",
		'a': """

			i)  std::move unconditionally casts its argument to an rvalue
			ii) std::forward conditionally casts its argument to an rvalue 
				if the argument was initialized with an rvalue.
		""",
	},
	47: {
		'q':  """
		Why should you not declare objects `const` if you want to
		be able to move from them?
		""",
		'a': """
		Because move requests on `const` objects are silently transformed
		into copy operations.

		For consider the prototypes of copy and move ctors, respectively:

			Widget(const Widget& src); // copy
			Widget(Widget&& src);      // move

		An rvalue reference const object does not match the parameter list
		of the move ctor.

		However, lvalue references to const are permitting to bind to
		rvalue references to const, and so copy construction will occur.
		""",
	},
	48: {
		'q':  """
		In which two context does using two &&'s lead an identifier being
		associated with a universal/forwarding reference -
		and not just an rvalue reference?
		""",
		'a': """
		Context 1: With template parameters 

		E.g. 
			template<typename T>
			void f(T&& param);

		Context 2: With auto

		E.g.
			auto&& var2 = var1;

		NB: Both these context have the element of type deduction.
		""",
	},
	49: {
		'q':  """
		Consider the following snippet which allows `param` to be a 
		universal/forwarding reference:

			template<typename T>
			void f(T&& param);

		Give two snippet rewrites to showcase the way that we can disqualifiy
		the `param` from being forwarding reference to an rvalue reference.
		""",
		'a': """
		1) Wrapping `T` in a sequential container:

			template<typename T>
			void f(std::vector<T>&& param);

		This is because `param`s type deduction will now be std::vector<T>&&
		and not T&&. 

		2) Const qualification e.g.

			template<typename T>
			void f(const T&& param);
		""",
	},
	50: {
		'q':  """
		Which of:
			1) std::move 2) std::forward

		Should be used on:
			i)  universal/forwarding references
			ii) rvalue references
		""",
		'a': """
		ANS:
			a) std::move should be used on rvalue references
			b) std::forward should be used on universal references
		""",
	},
	51: {
		'q':  """
		Consider the following snippet:

			Widget make_widget()
			{
				Widget w;
				return w;
			}

		i) What are the two conditions required for return value optimization
			(RVO) to take place?

		ii) What alternative to RVO does the Standard require if RVO does not take place?
			Use the snippet as a guide to answering (ii)
		""",
		'a': """
		i)	1) the type of the local object is the same as that returned by the
				function.
			2) the local object is what's being returned.

		ii) Implicit move i.e if we do not get copy elision then compilers must treat
			the function as if it were written like this:

				Widget make_widget()
				{
					Widget w;
					return std::move(w);
				}
		""",
	},
	52: {
		'q':  """
		Why is overloading a function that takes a universal/forwarding reference
		a bad idea?

		Visual snippet:

			template<typename T>
			void f(T&& param()
			{ /* function body ...*/ }

			void f(int param)
			{ /* different function body ...*/ }
		""",
		'a': """
		Because the universal reference function will instantiate far more
		argument types (leading to exact matches - and hence be chosen candidate).

		Then the developer may expect. In the visual snippet if a client
		were to call f(arg) with argument of type:

			1) unsigned int
			2) long int
			3) long int
			4) std::size_t

		All of (1) - (4) would be called by the forwarding reference function.
		""",
	},
	53: {
		'q':  """
		Explain what the following type traits do:

			1) std::is_integral
			2) std::remove_reference_t

		3) Use both (1) and (2) in tandem to determine whether a type T
			is integral or not, irrespective of whether the T is deduced from
			an lvalue or an rvalue.
		""",
		'a': """
		1) Determines whether a type is integral (e.g. std::size_t, int, long unsigned <- True)
		2) Removes any reference qualifiers from a type

		3) std::is_integral<std::remove_reference_t<T>>()
		""",
	},
	54: {
		'q':  """
		i) Name a strategy for getting around overloading perfect forwarding
			functions.

		ii) Explain the approach to this strategy.
		""",
		'a': """
		i)  Tag dispatch

		ii) This essentially entails for an overloaded function `f` to call
			and `f_impl` which leverages type_traits to determine which implementation
			to dispatch to. (see item27 p.204/334 for a refresher)
		""",
	},
	55: {
		'q':  """
		What is the purpose of std::enable_if?
		""",
		'a': """
		std::enable_if:

			- a template using std::enable_if is enabled only if the condition
				specified by std::enable_if is satisfied
			- potential templates that do not satisfy these conditions are 
				said to be disabled
		""",
	},
	56: {
		'q':  """
		In C++14, which type trait can we use to remove any references and CV-qualifiers?
		""",
		'a': """
		std::decay_t<T>
		""",
	},
	57: {
		'q':  """
		Consider <type_trait>'s std::is_base_of and complete the following sentence.

		std::is_base_of<A, B>::value is true if .....
		""",
		'a': """
		.... if B is derived from A (or A is a base of B)
		""",
	},
	58: {
		'q':  """
		i) Which <type_trait> can we use to determine whether a type A is constructible
			from a type B?

		ii) Write a templatized function that returns a true or false depending on whether
			an std::string can be constructed from an object of type T.
		""",
		'a': """
		i) std::is_constructible

		ii) Something like:

			template<typename T>
			bool is_string_constructible_from_t(T candidate)
			{
				return std::is_constructible<std::string, T>();
			}
		""",
	},
	59: {
		'q':  """
		In the context of lambda expressions, what is:
	   
			i) a closure?
			ii) a closure class?
		""",
		'a': """
		i)  A closure is a runtime object created by a lambda.
		ii) - A closure class is a class from which a closure is instantiated.
		    - Each lambda causes compilers to generate a unique closure class.
		""",
	},
	60: {
		'q':  """
		State whether the following exist during compilation or during runtime:

			1) lambdas
			2) closure classes
			3) closures
		""",
		'a': """
			1) compilation time
			2) compilation time
			3) runtime
		""",
	},
	61: {
		'q':  """
		Consider the following snippet and (i) determine what is wrong with (1):

			using FILTER_CONTAINER = std::vector<std::function<bool(int)>>;
			FILTER_CONTAINER filters;

			void add_divisor_filter()
			{	
				auto divisor = 2;

				filters.emplace_back(
					[&](int value) {return value % divisor == 0; }  // (1)
				);
			}

		(ii) What could we do to line (1) to prevent the issue you raised
			in (i)

		(iii) What could go wrong with (ii)?
		""",
		'a': """
		(1) uses the default-by-reference capture mode.
		The problem is that if the lifetime of the closure generated exceeds
		the lifetime of the local variable `divisor`, the reference in the closure will
		dangle.

		(ii) Replace default-capture-by-reference with default-capture-by-value i.e:
				[=](int value) {return value % divisor == 0; }

		(iii) If you're default-capture-by-value'ing a raw pointer, and that pointer
			gets `delete`ed, then you end up with a dangling pointer.
		""",
	},
	62: {
		'q':  """
		i) What are init captures used for?
		ii) Give a code snippet exhibiting init capture usage.
		""",
		'a': """
		i) Init captures are used for moving objects into closures.
		ii) Code snippet (anything like this is fine):

			class MyMessage
			{
			public:
				MyMessage(const std::string& message)
					: m_message(message)
				{}

				void print_message()
				{
					std::cout << m_message << std::endl;
				}

			private:
				std::string m_message;
			};

			void usage()
			{
				auto up_my_message = std::make_unique<MyMessage>("hey yall");

				auto func = [pw = std::move(up_my_message)]
				{
					return pw->print_message();
				};

				func();
			}
		""",
	},
	63: {
		'q':  """
		Consider the following:

			auto func = [lhs_pw = std::move(rhs_pw)]{/**/};

		Express in words what the capture clause represents.
		""",
		'a': """
		ANS:
			Create a data member of `lhs_pw` in the closure class,
			and intialize that data member the result of applying std::move
			to the local variable `pw`.
		""",
	},
	64: {
		'q':  """
		What's another name for C++14's init capture?
		""",
		'a': """
		Generalized lambda capture.
		""",
	},
	65: {
		'q':  """
		What is a C++14 generic lambda?
		""",
		'a': """
		""",
	},
	66: {
		'q':  """
		What is a good rule to remember with regards to reference
		collapsing?
		""",
		'a': """
		If either reference is an lvalue reference:
			then the result is an lvalue reference
		Else (if both are rvalue references):
			the result is an rvalue reference.
		""",
	},
	67: {
		'q':  """
		State the four context in which reference collapsing
		occurs?
		""",
		'a': """
		1) Template instantiation
		2) `auto` type generation
		3) creation and use of `typedef`s and alias declarations
		4) decltype usage
		""",
	},
	68: {
		'q':  """
		i)   What does SSO stand for?
		ii)  What does SSO entail?
		iii) What implications does your answer to (ii) have on moving
			vs. copying performance?
		""",
		'a': """
		i)   Small string optimization
		ii)  "small" strings (defined as having a capacity of no more than 
				15 characters) are stored in a buffer within the `std::string`
				objects, i.e. no heap-allocated storage is used.
		iii) Moving small strings that use an SSO-based implementation is
			no faster than copying them, because the copy-only-a-pointer
			trick that generally underlists the performance advantage of
			moves over copies isn't applicable.
		""",
	},
	69: {
		'q':  """
		Consider the snippet:

			template<typename T>
			void fwd(T&& param)
			{
				f(std::forward<T>(param));
			}

		Write `fwd` in variadic templace form to allow it to
		accept any number of arguments.
		""",
		'a': """
		template<typename... Ts>
		void fwd(Ts&&... params)                // accept any argument
		{
			f(std::forward<Ts>(params)...);     // forward them to `f`
		}
		""",
	},
	70: {
		'q':  """
		What makes is possible for emplacement functions to outperform
		insertion functions?
		""",
		'a': """
		Essence:
			Insertion functions take objects to be inserted.
			Emplace functions take constructor arguments for objects to be inserted.

		This difference permits emplacement functions to avoid the creation and
		destruction of temporary objects that insertion functions can necessitate.
		""",
	},
	71: {
		'q':  """
		Consider the following snippet:

			int x = 1;
			std::vector<int> vi;

			vi.push_back(x);    (1)
			vi.emplace_back(x); (2)

		True or false:
		Lines (1) and (2) have the same net effect on the constructor.
		""",
		'a': """
		True.

		Both take the lvalue `x` and copy-construct at the end of `vi`.
		""",
	},
}
