using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CPP
{
    public partial class CPPConcurrency : QNABase
    {
        public CPPConcurrency()
        : base(title: "Anothony Williams' C++ Concurrency in Action", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "CPPConcurrency";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"What is meant by concurrency in computer systems?"},
        {"a", @"Concurrency in computer systems refers to a single system performing
		multiple independent activities in parallel, as opposed to sequentially."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"In the context of computer systems, what is meant by 'task switching'?"},
        {"a", @"'Task switching' is a phenomenon that occurs when a machine processor can only perform
		one task at a time, but can switch between tasks many times per second. So much so
		that this gives the illusion of concurrency."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"What is hardware concurrency?"},
        {"a", @"Hardware concurrency is when computers with:
			1) multiple processors, or;
			2) multiple cores within a processor; or
			3) both (1) and (2)

		are genuinely capable of running more than one task in parallel
		(i.e not via task switching)."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"Consider:
			- a single core machine
			- this machine has to do two tasks via task switching
			- this machine has to perform a context switch every time it
			  changes from one task to another

		Outline the steps involved in context switching."},
        {"a", @"In order to perform a context switch, the OS has to:
			- save the CPU state and instruction pointer for the currently running
			  task
			- work out which task to switch to
			- then reload the CPU state for the task being switched to
			- then CPU will then (potentially have to) load the memory for the
			  instructions and data for the new task into the cache. Note that
			  this step can prevent the CPU from executing any instructions,
			  causing further delay."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"Consider the following setup:
			- multiple processes
			- each process has a single thread
			- the treads communicate between processes.

		a) Name a few interprocess communication channels available to this setup?
		b) State two downside of such a setup?"},
        {"a", @"a) Standard interprocess communication channels include:
			1) signals
			2) sockets
			3) files
			4) pipes
		
		b)
		Downside 1:
			Communication between processes (as stated in (a)) is often complicated
			to set up, or slow, or both.

		Downside 2:
			There's an inherent overhead in running multiple processes since
			it takes time to start a process, the operating system must devote 
			internal resources to managing the process, and so forth."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"Consider the standard interprocess communication channels:
			1) signals
			2) sockets
			3) files
			4) pipes

		a) Why are these complicated to set up, or slow, or both?
		b) What is one upside to your answer in (a)"},
        {"a", @"a)	Because operating systems typically provide a lot of protection between
			processes to avoid one process accidentally modifying data belonging
			to another process.

		b)	The added protection operating systems provide between processes
			mean that it can be easier to write safe concurrent code with processes
			rather than threads."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"Name an interesting advantage of using separate proceses for concurrency?"},
        {"a", @"You can run the separate processes on distinct machines connected over 
		a network."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"What does 'address space' mean?"},
        {"a", @"An address space is a range of accessible addresses in memory
		that are available for a program or process.

		The memory can be either physical or virtual and is used for
		executing instructions and storing data."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"Outline the difference between concurrency and parallelism from
		a development concern perspective."},
        {"a", @"Parallelism:
			People talk about parallelism when their primary concern is
			taking advantage of the available hardware to increase the performance
			of bulk data processing.

		Concurrency:
			People talk about concurrency when their primary concern is:
				- separation of concerns
				- responsiveness"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"Breifly summarise what is meant by 'throughput'."},
        {"a", @"Throughput is a measure of how many units of information a system can
		process in a given amount of time."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"Briefly outline the difference between:
			1) throughput
			2) bandwidth
			3) latency"},
        {"a", @"1) Throughput:
				Expressed the amount of data that can be processed in a given amount
				of time.

		2) Bandwidth:
				Refers to the capacity of the network for data to be moved
				at one time.

		3) Latency:
				Is an expression of how much time it takes for a data packet
				to get from one designated point to another."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"What is meant by the 'abstraction penalty'?"},
        {"a", @"The abstraction penalty is the cost associated with using high-level
		facilities that wrap low-level facilities, as opposed to using the underlying
		low-level facilities directly."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"Consider the statement:
			Every thread must has an initial function (i.e a callback/function pointer passed in to the thread constructor).
			This initial function is where the new thread of execution begins.

		What is the initial function for the initial thread spawned when an application is run?"},
        {"a", @"`main()`"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

				class BackgroundTask
				{
				public:
					void operator()()
					{
						do_something();
						do_something_else();
					}
				private:
					void do_something() { /* Implementation... */}
					void do_something_else() { /* Implementation... */ }
				};

				int main(void)
				{
					// attempting to spawn a thread
					std::thread myThread(BackgroundTask());   // (1)

					if (myThread.joinable()) myThread.join();
				}

		a) Explain the issue that can arise with line (1)
		b) Outline a few strategy to avoid your answer to (a)"},
        {"a", @"a) This is an example of 'the most vexing parse' and the compiler interprets
			this as a declaration of a function which:
				- takes as a single parameter a function pointer which takes no arguments
				  and returns a `BackgroundTask`
				- ultimate returns a object of type `std::thread`

		b)
		Strategy 1: By using 'uniform initialization syntax' i.e
			std::thread myThread{BackgroundTask()}

		Strategy 2: By using anonymous lambdas i.e
			std::thread myThread2([] {
				do_something();
				do_something_else();
			});"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"Outline the consequences of callig `detach()` on an instance of type `std::thread`?"},
        {"a", @"Calling `detach()` on a `std::thread` object:
			- leaves the thread running in the background with no means of 
			  communicating with it
			- it's no longer possible to wait for the detached thread to be complete
			  i.e it can no longer be `join`'ed
			- detached threads run in the background, ownership and control are passed
			  over to the C++ Runtime Library."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			class X
			{
			public:
				void do_lengthy_work() { std::cout << ""lengthy work?
"";}
			};

			int main(void)
			{
				X x1;

				std::thread t1{ &X::do_lengthy_work, &x1 }; (1)

				if (t1.joinable())
					t1.join();

				return 0;
			}

		Explain how line (1) works"},
        {"a", @"In the thread constructor, we supply as arguments:
		1) The `X::do_lengthy_work` function pointer to be invoked by the new thread
		2) The `this*` of the class.

		As you know, non-static member functions internally
		take `this*` as the first argument in a function."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"Compare `std::unique_ptr` with `std::thread`, with a particular focus on
		ownership semantics."},
        {"a", @"1) Instances of `std::thread` own a resource, while instances of `std::unique_ptr`
		   own a dynamic object.

		2) Both instances of `std::thread` and `std::unique_ptr` are moveable, but not copyable."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"a) What does ABI stand for?
		b) How does an ABI differ from an API?"},
        {"a", @"a) Application binary interface
		b) You may think of the ABI as the compiled version of the API.
			When you write source code, you access the library through the API.
			Once your code is compiled, your application accesses the binary data in the
			library through the ABI."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"State the Standard Library function used to return an indication of the number of
		threads that can truly run concurrently for a given execution of a program?"},
        {"a", @"std::thread::hardware_concurrency()

		NB: This is only a hint."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"In the context of multithreading, what is meant by 'oversubscription'?"},
        {"a", @"Oversubscription is where your program is running more threads than
		the hardware can support."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"State two ways to get an identifier for a thread?"},
        {"a", @"Way 1:
			Calling `std::thread::get_id` on an instance of type `std::thread`.

			NB: If the `std::thread` object doesn't have an associated thread of
			    execution e.g. from being `std::thread::detach`'ed, then `std::thread::get_id`
				will return a default-constructed `std::thread::id` object which indicates
				""not any thread"".

		Way 2:
			Calling `std::this_thread::get_id`."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"What does the C++ Standard define the term 'data race' as?"},
        {"a", @"As per the C++ Standard, a 'data race' is a specific type of race condition
		that arises because of concurrent modification to a single object.

		NB: Data races cause UB."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"True or false:

			Because race conditions are generally timing-sensitive, they can often
			disappear entirely when the application is run under the debugger."},
        {"a", @"True."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"Consider the following strategy to using a mutex:

			1) Create a mutex by calling std::mutex::mutex()
			2) Lock said mutex instance with a call to std::mutex::lock()
			3) Apply business logic to mutex using thread with exclusive write access
			4) Call std::mutex::unlock() when done

		a) Why is (1)-(4) not the recommended practice?
		b) Suggest an alternative to (1)-(4) and explain."},
        {"a", @"a) Because you have to remember to call std::mutex::unlock on every code path
		   out of the function, including those due to exceptions.

		b) An alternative would be the use of the std::lock_guard (or C++17's std::scoped_lock)
		   class template which implements the RAII idiom for a mutex i.e it.
		   	- locks the mutex on construction
			- unlocks the mutex on destruction.
		
		  Ensuring that the mutex is always correctly unlocked."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"What is the main difference between:
			1) pre-C++17's `std::lock_guard`
			2) C++17's `std::scoped_lock`"},
        {"a", @"Both (1) and (2) implement RAII-based mutex management i.e
		locking on construction and unlocking on destruction.

		However, std::scoped_lock can handle multiple mutexes automatically,
		while lock_guard is limited to a single mutex."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"Offer a guideline with respect to the relation between mutexes vs pointers and
		references to protected/private data."},
        {"a", @"Don't pass pointer and references to protected data outside the scope of the lock,
		whether by:
			1) returning them from a function
			2) storing them in externally visible memory, or;
			3) passing them as arguments to user-supplied functions."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"a) Provide the definition for a 'trivial type'
		b) Which <type_traits> function can be used to determine whether a type is trivial?"},
        {"a", @"a) Definition:
				When a class or struct in C++ has either:
					- compiler-provided, or;
					- explicitly default
				special member functions.

		b) std::is_trivial"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"Fill in the blanks:
			Objects with trivial copy constructors, trivial copy assignment operators and
			trivial destructors can be copied with <blank1> or <blank2>.

		BONUS: blank1 and blank2 are defined in which header file?"},
        {"a", @"blank1 = std::memcpy
		blank2 = std::memmove

		BONUS: <cstring>"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {29, new Dictionary<string, string>() {
        {"q", @"Literal types used for constexpr functions must have which special member functions
		trivially defined (i.e via =default or compiler-generated)?"},
        {"a", @"1) constructor
		2) copy constructor
		3) destructor"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {30, new Dictionary<string, string>() {
        {"q", @"a) In C++17, what is meant by an 'aggregate'?
		b) What are the implications of a class or struct being an aggregate?
			Give a code snippet to demonstrate."},
        {"a", @"a) An aggregate is a class or a struct with no user-supplied constructors
		b) The implication is that an aggregate can be initialized with an aggregate
			initializer. 

			Snippet:
				struct Aggregate
				{
				public:
					Aggregate() = default;
					Aggregate(const Aggregate&) = default;
					int a;
					double b;
				};

				int main(void)
				{
					Aggregate x={ 42, 3.14 };
					return 0;
				}

			Note that the above snipper DOES NOT compile in C++20."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {31, new Dictionary<string, string>() {
        {"q", @"What is the key benefit of:
			1) constant expressions, and;
			2) `constexpr` functions involving user-defined types"},
        {"a", @"Key benefit: Objects of a literal type initialized with a constant expression
					are statically initialized, and so their initialization is free
					from race conditions and initialization order issues."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {32, new Dictionary<string, string>() {
        {"q", @"True or false:
			In C++ up to and including 17, constexpr (non-special) member functions can be virtual."},
        {"a", @"False, they cannot be virtual."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {33, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:
			
			template<typename T1, typename T2, typename T3>
			constexpr T1 sum(T2 a, T3 b)
			{
				return a+b;
			}

		a) Under what conditions would the `constexpr` specifier be ignored?
		b) Give concrete examples of a case when:
				i)  The template instance is `constexpr`
				ii) The template instance is not `constexpr`"},
        {"a", @"a) Condition: If at least one of T1, T2, T3 are not literal types, in which case
				a template instantiation under this condition would not be `constexpr`.

		b) 
			i) constexpr int i = sum<int, int, int>(2, 3);

			ii) /*constexpr */ std::string s = sum<std::string, std::string, std::string>(std::string(""hello ""), std::string(""world!"")); // not constexpr as std::string is non-literal type"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {34, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			void foo()
			{
				thread_local std::vector<int> v;
			}

		What are the implications of marking a variable of `thread_local`?"},
        {"a", @"Thread local variables allow you to have a separate instance of each variable for
			each thread in your program. These variables are said to have 'thread storage duration'."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {35, new Dictionary<string, string>() {
        {"q", @"True or false:

			a) The `noexcept` specifier is part of the function type
			b) The `noexcept` specifier can be used for function overloading i.e defining the two `func` functions
					int func(int a, int b, int c) { return a * b * c; }
					int func(int x, int y, int z) noexcept { return x + y + z; }

				is fine."},
        {"a", @"a) True
		b) False, see compiler error: 'C2382'"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {36, new Dictionary<string, string>() {
        {"q", @"State the only functions in C++ that are ""implicitly non-throwing"""},
        {"a", @"The only functions in C++ that are implicitly non-throwing are the six special member functions,
		namely:
			1) the default constructor
			2) the default destructor 
			3) the move constructor
			4) move assignment operator
			5) the copy constructor
			6) copy assignment operator"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {37, new Dictionary<string, string>() {
        {"q", @"Under what condition is a class destructor non-throwing?"},
        {"a", @"Condition: All destructors of the class data members as well as the destructors of the class's base class(es)
					data members must be non-throwing."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {38, new Dictionary<string, string>() {
        {"q", @"1) Fill in the blank:
			`noexcept` can be used as a <BLANK> as well a specifier.

		2) Describe the use-case of <BLANK>"},
        {"a", @"1) BLANK = operator

		2) The `noexcept` operator checks at compile-time if an expression does not throw an exception."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {39, new Dictionary<string, string>() {
        {"q", @"Why is it more favourable to use std::lock(_mutex1, _mutex2) as opposed to _mutex1.lock(), _mutex2.lock()?"},
        {"a", @"Because std::lock locks all the mutexes and ensures that all arguments are locked on return (without producing any deadlocks).
		If the function cannot lock all passed in mutexes, the function first unlocks all objects it successfully has locked (if any)
		before failing."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {40, new Dictionary<string, string>() {
        {"q", @"a) Outline the purpose of <mutex>'s std::lock_guard
		b) Specify a C++17 alternative to std::lock_guard and why it may be better"},
        {"a", @"a)
			std::lock_guard is a mutex wrapper that provides a convenient RAII-style mechanism for owning a mutex
			for the duration of a scoped bock.

			When an std::lock_guard object is created, it attempts to take ownership of the mutex it is given.
			When control leaves the scope in which the std::lock_guard object was created,
			the std::lock_guard instance is destructed and the mutex is released.

		b) std::scoped_lock offers a replacement for std::lock_guard as well as providing the ability to lock
			multiple mutexes using a dealock avoidance algorithm."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {41, new Dictionary<string, string>() {
        {"q", @"In the context of mutex locking, what is the difference between:
			1) .lock
			2) .try_lock
			3) .try_lock_for
			4) .try_lock_until"},
        {"a", @"All of (1)-(4) attempt to take exclusive ownership of the mutex, the
		difference really lies in the behaviour if the mutex is already owned beforehand.

		So in the case that the call is unsuccessful in acquiring the mutex:
			1) .lock will block until it has access and then process
			2) .try_lock will return false (true if success)
			3) .try_lock_for will continue to try for a specified std::chrono::duration
			4) .try_lock_until will block until the specifed std::chrono::time_point has been reached
				or the lock is acquired, whichever comes first. Behaves as std::try_lock after the std::chrono::time_point
				has been reached."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {42, new Dictionary<string, string>() {
        {"q", @"Compare std::mutex with std::timed_mutex"},
        {"a", @"Similar to std::mutex, std::timed_mutex offers exclusive, recursive ownership semantics.
		In addition to that, std::timed_mutex provides the ability to attempt to claim ownership of a std::timed_mutex
		with a timeout via the member functions `std::timed_mutex::try_lock_for`, `std::timed_mutex::try_lock_until`"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {43, new Dictionary<string, string>() {
        {"q", @"a) What is the purpose of std::recursive_mutex
		b) In which coding scenarios would the use of std::recursive_mutex be application"},
        {"a", @"a) And std::recursive mutex is, like std::mutex, Lockable. However, std::recursive_mutex
		   allows the SAME THREAD to acquire multiple (recursive) levels of ownership over the
		   mutex object

		E.g. consider the pseudocode
			std::recursive_mutex __recursive_mutex;

			void recursive_function(int data)
			{
				if (terminal_condition()) return;
				else
				{
					// lock as many times as the recursive depth or
					// internal .lock() limit (this is unspecified as per docs)
					__recursive_mutex.lock();
					// critical section handling
					
					recursive_function(data - 1);

					// By the nature of the recursive function,
					// we unlock as many times as we lock
					__recursive_mutex.unlock();
				}
			}

		If we used a normal std::mutex the second call to .lock() would be blocked
		and we would end up with a deadlock.

		b)
			1) handling critical section with a mutex in a recursive function
			2) handling critical section with a mutex in a for loop"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {44, new Dictionary<string, string>() {
        {"q", @"State and describe the three <mutex> header locking strategy constants."},
        {"a", @"1) std::defer_lock
			- Do not acquire ownership of the mutex
			- i.e wrap but do not lock
			- this leaves the responsibility of wrapper to the client code
		2) std::try_to_lock
			- Try to acquire ownership of the mutex without blocking
		3) std::adopt_lock
			- Assume the calling thread already has ownership of the thread
			- I.e the thread has already called .lock() on mutex before said mutex
			  is passed to std::unique_lock wrapper
			- You'd only ever want to use this if you've already locked the mutex
			  and want a convient RAII-unlocking wrapper afterwards"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {45, new Dictionary<string, string>() {
        {"q", @"<mutex>'s std::unique_lock is a general-purpose mutex wrapper.

		List the functionality that it allows for."},
        {"a", @"1) Deferred locking
		2) Time-constrained attempts at locking
		3) Recursive locking
		4) Transfer of lock ownership (Moveable but not Copyable)
		5) Use with condition variables"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {46, new Dictionary<string, string>() {
        {"q", @"a) What is the purpose of std::call_once?
		b) What arguments do you pass to std::call_once"},
        {"a", @"a) <mutex>'s std::call_once executes a Callable function exactly once,
			even if called concurrently from several threads.

		b) 	First argument: std::once_flag
			Second argument: Callable function
			[third argument, variable]: arguments to the Callable function, 0 if Callable has zero parameters"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {47, new Dictionary<string, string>() {
        {"q", @"Outline the difference between <mutex> header's:	
			1) std::try_lock
			2) std::mutex::try_lock"},
        {"a", @"1) std::try_lock is a:
			- global function which takes 1...N Lockable objects
			- will try to lock each of the given Lockable objects in order of arguments passed
			- if the call fails, no further attempts are made 
			- returns:
				- (-1) returned on success
				- 0-based index of failing Lockable argument returned on failure

		2) std::mutex::try_lock:
			- will attempt to lock the mutex instance once
			- returns
				- `true` on success
				- `false` on failure"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {48, new Dictionary<string, string>() {
        {"q", @"Compare std::lock with std::try_lock"},
        {"a", @"- Both std::lock and std::try_lock take 1...N Lockable objects.
		- std::lock will implement a deadlock available algorithm and try multiple
			orders of the arguments passed and block if no mutex fails
		- std::try_lock will only try once and in the order of the mutexes passed
			and return -1 on success or a 0-based index of the mutex that failed."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {49, new Dictionary<string, string>() {
        {"q", @"Consider the following deadlock avoidance guideline:
			Avoid nested locks

		a) Explain why this is a good guideline
		b) If you need to acquire multiple locks, how should you approach this?"},
        {"a", @"a) Do not acquire a lock if you already hold.
			Sticking to this guideline means that it's impossible to get a deadlock
			from lock usage alone because each thread only ever holds a single lock.
			Mutex locks are a very common cause of deadlocks.

		b) If you need to acquire multiple locks, this should be done as a single
			action with either std::lock or with std::scoped_lock (preferred)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {50, new Dictionary<string, string>() {
        {"q", @"Consider the following deadlock avoidance guideline:
			Acquire locks in a fixed order.

		Explain the importance of this guideline."},
        {"a", @"If you absolutely cannot acquire multiple mutexes in one go either via
		std::lock and std::scoped_lock then you must make sure to acquire each
		lock in order in every thread."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {51, new Dictionary<string, string>() {
        {"q", @"a) State one pro in favour of using std::unique_lock over std::lock_guard
		b) State one pro in favour of using std::lock_guard over std::unique_lock

		BONUS: Explain why your answer to (a) is true."},
        {"a", @"a) std::unique_lock provides more flexibilty of use via the locking strategy constants:
				1) std::defer_lock 2) std::adopt_lock 3) std::try_to_lock

		b) std::lock_guard takes less space and is slightly faster to use than std::unique_lock

		BONUS: Because std::unique_lock must store and update a flag to determine whether
			the std::unique_lock instance owns the mutex, the storage of the flag leads to
			a size increase and the need to update and query said flag leads to a performance penalty."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {52, new Dictionary<string, string>() {
        {"q", @"Explain what is understood by the ""granularity of a lock""."},
        {"a", @"The ""granularity of a lock"" is simply a hand-wavy term to describe the amouunt
		of data protected by a single lock.

		I.e a fine-grained lock protects a small amount of data, and a coarse-grained
		lock protects a large amount of data."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {53, new Dictionary<string, string>() {
        {"q", @"Consider the case where the shared data needs protection only from
		concurrent access while it's being initialized, but after that no
		explicit synchronization is required.

		Which functionality from the C++ Concurrency Support Library would
		be best for this case."},
        {"a", @"std::call_once, std::once_flag"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {54, new Dictionary<string, string>() {
        {"q", @"Consider the case where we want thread-safe initialization of a single global instance.
		What is an alternative to accomplishing via std::call_once?"},
        {"a", @"Since post-C++11 `static` variable initialization is guaranteed to happen on exactly
		once thread, and no other threads will proceed until that initialization is complete,
		declaring a variable as `static` is a viable alternative.

		E.g
			class MyClass { };

			MyClass& get_my_class_instance()
			{
				static MyClass __instance;
				return __instance;
			}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {55, new Dictionary<string, string>() {
        {"q", @"In what circumstances do reader/writer mutexes such as std::shared_mutex
		provide a performance benefit?"},
        {"a", @"Circumstances where readers are overwhelmingly more frequent than writes.

		Concrete example: A cache of DNS entries. DNS entries may be unchanged for years,
			but can happen - so we need to share read access between threads and when
			that rare occasion for write arises, a single thread must have exclusive
			access to write."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {56, new Dictionary<string, string>() {
        {"q", @"What is the main difference between std::shared_mutex and std::mutex?"},
        {"a", @"std::shared_mutex has two levels of access:
			1) shared - several threads can share ownership of the same mutex
			2) exclusive - only one thread can own the mutex

		Note that std::mutex only has functionality for (2) i.e exclusive."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {57, new Dictionary<string, string>() {
        {"q", @"1) What is std::condition_variable used for?
		2) How would you use an instance of std::condition_variable"},
        {"a", @"1) std::condition_variable is used for facilitating inter-thread communication.
		2) pseudo-snippet:
			std::condition_variable __condition_variable;
			__condition_variable(
				<arg1: instance of std::unique_lock>,
				<arg2: lambda returning a bool>
			)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {58, new Dictionary<string, string>() {
        {"q", @"Fill in the blank:
			For an instance of std::condition_variable, we must <BLANK> before
			call std::condition_variable::notify_one/all();"},
        {"a", @"BLANK: manually unlock the mutex"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}
