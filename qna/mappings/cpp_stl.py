qna = {
    1: { # <any>
		'q':  """
		Which type_trait must a class satisfy in order for an instance
		of said class to be containable in an std::any class?
		""",
		'a': """
		std::is_copy_constructible
		""",
	},
    2: { # <cmath>
		'q':  """ 
		a) State the standalone function used for Euler exponentiation?
		b) Use your answer to (a) as well as other code to represent:
			 e** i * pi
		""",
		'a': """
		a) std::exp() - so std::exp(1) is e**1
		b)
		Snippet:
			#include <numbers> // for pi, C++20 only
			#include <complex> // for i
			#include <cmath>   // for the std::exp

			void ans()
			{
				using namespace std::complex_literals;

				auto answer = std::exp(std::numbers::pi * 1i);

				// NB: Note that the output of `answer` will be -1 with E-16 epsilon tolerance
			}
		""",
	},
    3: {
		'q':  """
		What is std::reference_wrapper<T> in a nutshell?
		""",
		'a': """
		A std::reference_wrapper<T> is an object that:
			1) wraps a pointer (T*) and has the semantics of a reference (T&)
			2) It is assignable and copyable

		Due to (1) & (2), it can rebind to another object like a pointer.
		""",
	},
    4: {
		'q':  """
		a) What does std::enable_shared_from_this allow for
		b) What is a pre-requisite to using std::enable_shared_from_this
		""",
		'a': """
		a) It enables you to get a valid std::shared_ptr instance to this,
			when all you have is `this`

		b) Pre-requisite:
			If you want this functionality inside a class, say Y, then you must:
				- publically inherit std::enable_shared_from_this

			e.g.:
				class Y : public std::enable_shared_from_this<T>
				{ };
		""",
	},
    5: {
		'q':  """
		 Consider the following snippet:
			
				std::variant<int, std::string> __variant = std::string{"abc"};
				
		a) Identify the alternative types in variant `__variant`
		b) Write code to determine whether `__variant` is currently holding an `int`
		""",
		'a': r"""
		a) int, std::string
		b) Snippet:
				std::cout << std::boolalpha << std::holds_alternative<int>(__variant) << '\n';
		""",
	},
    6: {
		'q':  """
		What does std::variant<T...>::index return?
		""",
		'a': r"""
		A zero-based index of the alternative that is currently held by the variant.

		E.g. consider:
			std::variant<T1, T2, T3> __variant = T3{};

			assert(__variant.index() == 2); // as T3 is at index 2
		""",
	},
    7: {
		'q':  """
		State two cases in which you'd want to use <variant>'s std::monostate?
		""",
		'a': """
		1)	For use in a variant of non-default-constructible types.

			For consider:
				std::variant<T1, T2, T3> __variant; // compiler error

			If none of T1, T2 or T3 are default constructible, then this line of code
			will trigger a compiler error.

			So you would have to add std::monostate at the start
				std::variant<std::monostate, T1, T2, T3> __variant; 

		2) To represent the idea of "empty", as std::monotone have their comparison
			operators overloaded.

		""",
	},
    8: {
		'q':  """
		a) What is the purpose of std::variant<T...>::valueless_by_exception() ?
		b) What is the purpose of <variant>'s std::variant_npos?
		""",
		'a': """
		a) std::variant<T...>::valueless_by_exception returns false if and only if the
			variant holds a value.

			NB: A variant may not hold a value when in an exception is thrown during various
				initialization/assignment steps to a variant.
		
		b) std::variant_npos is returned if and only if std::variant<T...>::valueless_by_exception()
			returns true;
		""",
	},
    9: {
		'q':  """
		True or false:
			An std::variant is never permitted to allocate dynamic memory.
		""",
		'a': """
		True	
		""",
	},
    10: {
		'q':  """
		Say we have:

				std::variant<int, std::string, float> __variant;
				// ... various allowable assignments to variant

		Write the line of code which will determine whether or not `__variant`
		is currently holding an std::string.
		""",
		'a': """
		auto holding_string = std::holds_alternative<std::string>(__variant);
		""",
	},
	11: {
		'q':  """
		a) What is the purpose of std::visit?
		b) State any constraints there may be on std::visit?
		""",
		'a': """
		a) The purpose of std::visit is to pass a callback to be invoke on the underlying
		item within an std::variant.

		Used as followed:
			std::visit($<CALLBACK>, $<std::variant INSTANCE>)

		b) Constraints include the callback being compatible with all data types specified in the variant.
			Specifically, for variant:
				std::variant<T1, T2, ..., TN>

			The passed callback has to be invokable with any of T1, T2, ..., TN

			NOTE: You can get around this with a generic lambda of by specifying a custom
				visitor struct that call inherit from multiple lambdas and adapt to each type.
		""",
	},
	12: {
		'q':  """
		When would we favour <utility>'s std::as_const over const_cast?
		""",
		'a': """
		When you want to access the const member functions of an object, and
		not accidentally remove const if the object is already const.
		""",
	},
	13: {
		'q':  """
		a) Which C++20 class provides information regarding source code, including file names, line numbers,
		the calling function etc..
		b) In which header file can I find your answer to (a)
		""",
		'a': """
		a) std::source_location
		b) <source_location>
		""",
	},
	14: {
		'q':  """
		Consider the following example:

			if (<BLANK>)
			{
				// do some compile time logic
			}
			else
			{
				// we know we're in runtime, so do some runtime based logic e.g.
				// dynamic memory, manage runtime variables, perhaps throw exception.
			}

		Which function/construct BLANK would be used to differentiation between whether we're in
		compile time or runtime when we are in:
			a) C++20
			b) C++23
		""",
		'a': """
		a) <type_trait>'s std::is_constant_evaluated
		b) Using 'if consteval' e.g.:

			if consteval
			{ // if logic}
			else
			{  // else logic}

		Note that 'if consteval' doesn't use parenthesis.
		""",
	},
	15: {
		'q':  """
		Consider the following function:
			auto some_function()
			{
				return 1;
			}

		Using C++20's concepts, constrain the function to only return
		integral values.
		""",
		'a': """
		#include <concepts>

		std::integral auto some_function()
		{
			return 1;
		}
		""",
	},
	16: {
		'q':  """
		Explain the motivation behind std::span (particular what it intends to replace)
		as well as any other benefits of using std::span.
		""",
		'a': """
		Explanation:
			Consider the following old-fashioned way of passing an array to a function,
			you need to also pass along a parameter specifying its size so the for loop
			knows when do stop.

				void process_array(const int arr[], const int array_size)
				{
					for(int i = 0; i < array_size; ++i)
					{
						// processing logic
					}
				}

			You can accomplish the same thing with std::span, for example:
				void process_span(std::span<int> my_span)
				{
					for (auto i : my_span)
					{
						// processing logic
					}
				}

			It's essentially a cleaner, less error-prone way of processing continguous blocks
			of data:
				1) more lightweight than using a container such as std::vector
				2) access to methods/idioms such as range-based for, find_if etc
		""",
	},
	17: {
		'q':  """
		What is the formal definition of an std::ranges::view ?
		""",
		'a': """
		A `view` is a range which:
			1) is default constructible 
			2) has O(1) move and destruction operations
			3) (if std::is_copyable_v is true) has O(1) copy operations
		""",
	},
	18: {
		'q':  """
		What is <functional>'s std::identity used for?
		""",
		'a': """
		std::identity is simply a function object type whose `operator()` returns
		its argument unchanges.
		""",
	},
	19: {
		'q':  """
		What does the concept `std::semiregular` specify?
		""",
		'a': """
		The concept `std::semiregular` specifies a type T that is both:
			1) copyable and;
			2) default initialization

		I.e. an implementation would look like this

		template<typename T>
		concept semiregualar = std::copyable<T> && std::default_initializable<T>
		""",
	},
	20: {
		'q':  """
		What is the purpose/use case of std::declval?
		""",
		'a': """
		Converts any type T into a reference type, making it possible to use member functions
		in decltype expressions without the need to go through constructors.

		NOTE: std::declval can only be used in unevaluated contexts (like `decltype`, `sizeof` etc).
		""",
	},
	21: {
		'q':  """
		In what scenario would you prefer using <memory>'s `std::addressof` as opposed to
		simple calling `&` on a (non-rvalue) object?
		""",
		'a': """
		When you're using user-defined types/third-party libraries and are unsure if the 
		operator& has been overloaded incorrectly.
		""",
	},
	22: {
		'q':  """
		True or false:
			ADL (Argument dependent lookup)/Koenig lookup only
			applies to namespaces.
		""",
		'a': """
		True.
		""",
	},
	23: {
		'q':  """
		a) What function would you use to determine if a given floating-point number
			is negative?

		b) In which header does it reside?
		""",
		'a': """
		a) std::signbit
		b) <cmath>
		""",
	},
	24: {
		'q':  """
		True or false:
		a)	It is valid to make a pointer from a reference, that is you can have:
				pointer to T&

		b) Considering you're answer to (a) why would you want to
			use <type_trait>'s std::add_pointer_t?
		""",
		'a': """
		a) false

		b) Since it is NOT valid to make a pointer from a reference, it would
			be preferably to use std::add_pointer<T> to represent T* withou
			worrying about T being deduced as a reference (add_pointer removes the reference).
		""",
	},
	25: {
		'q':  """
		1) Express a duration instance as:
			a) 10 minutes as 10 units of duration with a tick size of 60 seconds
			b) 14 seconds as 14 units of duration with a ticket size of 1 second

		2) What is the default duration tick size? 
		""",
		'a': """
		1)
			#include <chrono>
			#include <ratio>

			a) std::chrono::duration<long, std::ratio<60>> a = 10;
			b) std::chrono::duration<long, std::ratio<1>>  b = 1;

		2) The default duration tick size is 1, so we could've written answer (b) as
			std::chrono::duration<long> b = 1;
		""",
	},
	26: {
		'q':  """
		Give a brief explanation as to the purpose of <chrono>'s std::time_point?
		""",
		'a': """
		A std::time_point is:
			1) Associated with a clock
			2) Represents a point in time as a std::duration relative to the epoch
		""",
	},
	27: {
		'q':  """
		a) Which header file should I turn to to get implementation-dependent information
		about the C++ Standard Library that I am using?

		b) Give a few examples of the type of information that you can get?
		""",
		'a': """
		a) C++20's <version>.
		b) Version number, release date, copyright notice, select library feature
			test macros like __cpp_lib_any
		""",
	},
	28: {
		'q':  """
		What is the difference between <cstdint>'s:
			1) std::uint8_t, and;
			2) std::uint_fast8_t ?

		When would I prefer one over the other?
		""",
		'a': """
		Difference:
			std::uint8_t guarantees that the type will be exactly 8 bits,
			while std::uint_fast8_t will be AT LEAST 8 bits, but the actual
			width may be larger for performance reasons.

		Use std::uint8_t when the size of the type is critical, e.g. when
		working with hardware registers that expect a certain data width.

		Use sd::uint_fast8_t when performance is a higher priority than the 
		actual size of the data.
		""",
	},
	29: {
		'q':  """
		a) What is the purpose of C++23's `std::out_ptr` and `std::inout_ptr`? 
		b) When should you use `std::out_ptr` and when should you turn to `std::inout_ptr`?
		""",
		'a': """
		a) std::out_ptr and std::inout_ptr exist for compatibility between C++ smart pointers
		and C APIs. Commonly used to pass smart pointer in order to pass in the resultant 
		std::out_ptr_t or std::inout_ptr_t to the C function.

		Consider the C api from winsqlite3.h

			SQLITE_API int SQLITE_APICALL sqlite3_open(
			const char *filename,   /* Database filename (UTF-8) */
			sqlite3 **ppDb          /* OUT: SQLite db handle */
			);

		in the second parameter we would like to pass a std::out_ptr(std::unique_ptr instance).

		b) 
			std::out_ptr use case:
				When a function expects a raw pointer as an output parameter and takes ownership
				of (is responsible for freeing the underlying resource) the pointed-to-resource.

			std::inout_ptr use case:
				When a function expects a raw pointer to an input/output parameter and modifies the
				pointed-to-resource without taking ownership.
		""",
	},
	30: {
		'q':  """
		What does `std::thread::hardware_concurrency` return?
		""",
		'a': """
		It returns the number of threads supported by the current
		implementation's hardware can suport.
		""",
	},
	31: {
		'q':  """
		In the <concepts> context, when constraining a type T with `requires`.
		Which helper templates should you reach for when:

			a) You want to constrain for an exact match with std::string
			b) You want to constrain for implicit conversions from T to std::string to be allowed
			c) You want to constrain for explicit conversions to std::string with T as a constructor argument
		""",
		'a': """
			a)
				template<typename T>
				requires std::same_as<std::remove_cvref_t<T>, std::string>

			b)
				template<typename T>
				requires std::convertible_to<T, std::string>

			c)
				template<typename T>
				requires std::constructible_from<std::string, T>
		""",
	},
}