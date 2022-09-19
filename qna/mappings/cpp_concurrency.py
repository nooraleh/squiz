qna = { # Notes taken in a QNA style from Anothony Williams' 'C++ Concurrency in Action'
    1: { # Chapter 1: Hello, world of concurrency in C++!
		'q':  """
		What is meant by concurrency in computer systems?
		""",
		'a': """
		Concurrency in computer systems refers to a single system performing
		multiple independent activities in parallel, as opposed to sequentially.
		""",
	},
    2: {
		'q':  """
		In the context of computer systems, what is meant by 'task switching'?
		""",
		'a': """
		'Task switching' is a phenomenon that occurs when a machine processor can only perform
		one task at a time, but can switch between tasks many times per second. So much so
		that this gives the illusion of concurrency.
		""",
	},
    3: {
		'q':  """
		What is hardware concurrency?
		""",
		'a': """
		Hardware concurrency is when computers with:
			1) multiple processors, or;
			2) multiple cores within a processor; or
			3) both (1) and (2)

		are genuinely capable of running more than one task in parallel
		(i.e not via task switching).
		""",
	},
    4: {
		'q':  """
		Consider:
			- a single core machine
			- this machine has to do two tasks via task switching
			- this machine has to perform a context switch every time it
			  changes from one task to another

		Outline the steps involved in context switching.
		""",
		'a': """
		In order to perform a context switch, the OS has to:
			- save the CPU state and instruction pointer for the currently running
			  task
			- work out which task to switch to
			- then reload the CPU state for the task being switched to
			- then CPU will then (potentially have to) load the memory for the
			  instructions and data for the new task into the cache. Note that
			  this step can prevent the CPU from executing any instructions,
			  causing further delay. 
		""",
	},
    5: {
		'q':  """
		Consider the following setup:
			- multiple processes
			- each process has a single thread
			- the treads communicate between processes.

		a) Name a few interprocess communication channels available to this setup?
		b) State two downside of such a setup?
		""",
		'a': """
		a) Standard interprocess communication channels include:
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
			internal resources to managing the process, and so forth. 
		""",
	},
    6: {
		'q':  """
		Consider the standard interprocess communication channels:
			1) signals
			2) sockets
			3) files
			4) pipes

		a) Why are these complicated to set up, or slow, or both?
		b) What is one upside to your answer in (a)
		""",
		'a': """
		a)	Because operating systems typically provide a lot of protection between
			processes to avoid one process accidentally modifying data belonging
			to another process.

		b)	The added protection operating systems provide between processes
			mean that it can be easier to write safe concurrent code with processes
			rather than threads. 
		""",
	},
    7: {
		'q':  """
		Name an interesting advantage of using separate proceses for concurrency?
		""",
		'a': """
		You can run the separate processes on distinct machines connected over 
		a network.
		""",
	},
    8: {
		'q':  """
		What does 'address space' mean?
		""",
		'a': """
		An address space is a range of accessible addresses in memory
		that are available for a program or process.

		The memory can be either physical or virtual and is used for
		executing instructions and storing data.
		""",
	},
    9: {
		'q':  """
		Outline the difference between concurrency and parallelism from
		a development concern perspective.
		""",
		'a': """
		Parallelism:
			People talk about parallelism when their primary concern is
			taking advantage of the available hardware to increase the performance
			of bulk data processing.

		Concurrency:
			People talk about concurrency when their primary concern is:
				- separation of concerns
				- responsiveness
		""",
	},
    10: {
		'q':  """
		Breifly summarise what is meant by 'throughput'.
		""",
		'a': """
		Throughput is a measure of how many units of information a system can
		process in a given amount of time.
		""",
	},
	11: {
		'q':  """
		Briefly outline the difference between:
			1) throughput
			2) bandwidth
			3) latency
		""",
		'a': """
		1) Throughput:
				Expressed the amount of data that can be processed in a given amount
				of time.

		2) Bandwidth:
				Refers to the capacity of the network for data to be moved
				at one time.

		3) Latency:
				Is an expression of how much time it takes for a data packet
				to get from one designated point to another.
		""",
	},
	12: {
		'q':  """
		What is meant by the 'abstraction penalty'?
		""",
		'a': """
		The abstraction penalty is the cost associated with using high-level
		facilities that wrap low-level facilities, as opposed to using the underlying
		low-level facilities directly.
		""",
	},
	13: {
		'q':  """
		Consider the statement:
			Every thread must has an initial function (i.e a callback/function pointer passed in to the thread constructor).
			This initial function is where the new thread of execution begins.

		What is the initial function for the initial thread spawned when an application is run?
		""",
		'a': """
		`main()`
		""",
	},
	14: { # Chapter 2 - Managing Threads
		'q':  """
		Consider the following snippet:

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
		b) Outline a few strategy to avoid your answer to (a)
		""",
		'a': """
		a) This is an example of 'the most vexing parse' and the compiler interprets
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
			});

		""",
	},
	15: {
		'q':  """
		Outline the consequences of callig `detach()` on an instance of type `std::thread`?
		""",
		'a': """
		Calling `detach()` on a `std::thread` object:
			- leaves the thread running in the background with no means of 
			  communicating with it
			- it's no longer possible to wait for the detached thread to be complete
			  i.e it can no longer be `join`'ed
			- detached threads run in the background, ownership and control are passed
			  over to the C++ Runtime Library.
		""",
	},
	16: {
		'q':  """
		Consider the following snippet:

			class X
			{
			public:
				void do_lengthy_work() { std::cout << "lengthy work?\n";}
			};

			int main(void)
			{
				X x1;

				std::thread t1{ &X::do_lengthy_work, &x1 }; (1)

				if (t1.joinable())
					t1.join();

				return 0;
			}

		Explain how line (1) works
		""",
		'a': """
		In the thread constructor, we supply as arguments:
		1) The `X::do_lengthy_work` function pointer to be invoked by the new thread
		2) The `this*` of the class.

		As you know, non-static member functions internally
		take `this*` as the first argument in a function.
		""",
	},
	17: {
		'q':  """
		Compare `std::unique_ptr` with `std::thread`, with a particular focus on
		ownership semantics.
		""",
		'a': """
		1) Instances of `std::thread` own a resource, while instances of `std::unique_ptr`
		   own a dynamic object.

		2) Both instances of `std::thread` and `std::unique_ptr` are moveable, but not copyable.
		""",
	},
	18: {
		'q':  """
		a) What does ABI stand for?
		b) How does an ABI differ from an API?
		""",
		'a': """
		a) Application binary interface
		b) You may think of the ABI as the compiled version of the API.
			When you write source code, you access the library through the API.
			Once your code is compiled, your application accesses the binary data in the
			library through the ABI.
		""",
	},
	19: {
		'q':  """
		State the Standard Library function used to return an indication of the number of
		threads that can truly run concurrently for a given execution of a program?
		""",
		'a': """
		std::thread::hardware_concurrency()

		NB: This is only a hint.
		""",
	},
	20: {
		'q':  """
		In the context of multithreading, what is meant by 'oversubscription'?
		""",
		'a': """
		Oversubscription is where your program is running more threads than
		the hardware can support.
		""",
	},
	21: {
		'q':  """
		State two ways to get an identifier for a thread?
		""",
		'a': """
		Way 1:
			Calling `std::thread::get_id` on an instance of type `std::thread`.

			NB: If the `std::thread` object doesn't have an associated thread of
			    execution e.g. from being `std::thread::detach`'ed, then `std::thread::get_id`
				will return a default-constructed `std::thread::id` object which indicates
				"not any thread".

		Way 2:
			Calling `std::this_thread::get_id`.
		""",
	},
	22: { # Chapter 3 - Sharing Data between Threads
		'q':  """
		What does the C++ Standard define the term 'data race' as?
		""",
		'a': """
		As per the C++ Standard, a 'data race' is a specific type of race condition
		that arises because of concurrent modification to a single object.

		NB: Data races cause UB.
		""",
	},
	23: {
		'q':  """
		True or false:

			Because race conditions are generally timing-sensitive, they can often
			disappear entirely when the application is run under the debugger.
		""",
		'a': """
		True.
		""",
	},
	24: {
		'q':  """
		Consider the following strategy to using a mutex:

			1) Create a mutex by calling std::mutex::mutex()
			2) Lock said mutex instance with a call to std::mutex::lock()
			3) Apply business logic to mutex using thread with exclusive write access
			4) Call std::mutex::unlock() when done

		a) Why is (1)-(4) not the recommended practice?
		b) Suggest an alternative to (1)-(4) and explain.
		""",
		'a': """
		a) Because you have to remember to call std::mutex::unlock on every code path
		   out of the function, including those due to exceptions.

		b) An alternative would be the use of the std::lock_guard (or C++17's std::scoped_lock)
		   class template which implements the RAII idiom for a mutex i.e it.
		   	- locks the mutex on construction
			- unlocks the mutex on destruction.
		
		  Ensuring that the mutex is always correctly unlocked. 
		""",
	},
	25: {
		'q':  """
		What is the main difference between:
			1) pre-C++17's `std::lock_guard`
			2) C++17's `std::scoped_lock`
		""",
		'a': """
		Both (1) and (2) implement RAII-based mutex management i.e
		locking on construction and unlocking on destruction.

		However, std::scoped_lock can handle multiple mutexes automatically,
		while lock_guard is limited to a single mutex. 
		""",
	},
	26: {
		'q':  """
		Offer a guideline with respect to the relation between mutexes vs pointers and
		references to protected/private data.
		""",
		'a': """
		Don't pass pointer and references to protected data outside the scope of the lock,
		whether by:
			1) returning them from a function
			2) storing them in externally visible memory, or;
			3) passing them as arguments to user-supplied functions.
		""",
	},
	27: {
		'q':  """
		a) Provide the definition for a 'trivial type'
		b) Which <type_traits> function can be used to determine whether a type is trivial?
		""",
		'a': """
		a) Definition:
				When a class or struct in C++ has either:
					- compiler-provided, or;
					- explicitly default
				special member functions.

		b) std::is_trivial

		""",
	},
	28: {
		'q':  """
		Fill in the blanks:
			Objects with trivial copy constructors, trivial copy assignment operators and
			trivial destructors can be copied with <blank1> or <blank2>.

		BONUS: blank1 and blank2 are defined in which header file?
		""",
		'a': """
		blank1 = std::memcpy
		blank2 = std::memmove

		BONUS: <cstring>
		""",
	},
	29: {
		'q':  """
		Literal types used for constexpr functions must have which special member functions
		trivially defined (i.e via =default or compiler-generated)?
		""",
		'a': """
		1) constructor
		2) copy constructor
		3) destructor
		""",
	},
	30: {
		'q':  """
		a) In C++17, what is meant by an 'aggregate'?
		b) What are the implications of a class or struct being an aggregate?
			Give a code snippet to demonstrate.
		""",
		'a': """
		a) An aggregate is a class or a struct with no user-supplied constructors
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

			Note that the above snipper DOES NOT compile in C++20.
		""",
	},
	31: {
		'q':  """
		What is the key benefit of:
			1) constant expressions, and;
			2) `constexpr` functions involving user-defined types
		""",
		'a': """
		Key benefit: Objects of a literal type initialized with a constant expression
					are statically initialized, and so their initialization is free
					from race conditions and initialization order issues.
		""",
	},
	32: {
		'q':  """
		True or false:
			In C++ up to and including 17, constexpr (non-special) member functions can be virtual.
		""",
		'a': """
		False, they cannot be virtual.
		""",
	},
	33: {
		'q':  """
		Consider the following snippet:
			
			template<typename T1, typename T2, typename T3>
			constexpr T1 sum(T2 a, T3 b)
			{
				return a+b;
			}

		a) Under what conditions would the `constexpr` specifier be ignored?
		b) Give concrete examples of a case when:
				i)  The template instance is `constexpr`
				ii) The template instance is not `constexpr`
		""",
		'a': """
		a) Condition: If at least one of T1, T2, T3 are not literal types, in which case
				a template instantiation under this condition would not be `constexpr`.

		b) 
			i) constexpr int i = sum<int, int, int>(2, 3);

			ii) /*constexpr */ std::string s = sum<std::string, std::string, std::string>(std::string("hello "), std::string("world!")); // not constexpr as std::string is non-literal type
		""",
	},
	34: {
		'q':  """
		Consider the following snippet:

			void foo()
			{
				thread_local std::vector<int> v;
			}

		What are the implications of marking a variable of `thread_local`?
		""",
		'a': """
		Thread local variables allow you to have a separate instance of each variable for
			each thread in your program. These variables are said to have 'thread storage duration'.
		""",
	},
	35: {
		'q':  """
		True or false:

			a) The `noexcept` specifier is part of the function type
			b) The `noexcept` specifier can be used for function overloading i.e defining the two `func` functions
					int func(int a, int b, int c) { return a * b * c; }
					int func(int x, int y, int z) noexcept { return x + y + z; }

				is fine.

		""",
		'a': """
		a) True
		b) False, see compiler error: 'C2382'
		""",
	},
	36: {
		'q':  """
		State the only functions in C++ that are "implicitly non-throwing"
		""",
		'a': """
		The only functions in C++ that are implicitly non-throwing are the six special member functions,
		namely:
			1) the default constructor
			2) the default destructor 
			3) the move constructor
			4) move assignment operator
			5) the copy constructor
			6) copy assignment operator
		""",
	},
	37: {
		'q':  """
		Under what condition is a class destructor non-throwing?
		""",
		'a': """
		Condition: All destructors of the class data members as well as the destructors of the class's base class(es)
					data members must be non-throwing.
		""",
	},
	38: {
		'q':  """
		1) Fill in the blank:
			`noexcept` can be used as a <BLANK> as well a specifier.

		2) Describe the use-case of <BLANK>
		""",
		'a': """
		1) BLANK = operator

		2) The `noexcept` operator checks at compile-time if an expression does not throw an exception.
		""",
	},
	39: {
		'q':  """
		Why is it more favourable to use std::lock(_mutex1, _mutex2) as opposed to _mutex1.lock(), _mutex2.lock()?
		""",
		'a': """
		Because std::lock locks all the mutexes and ensures that all arguments are locked on return (without producing any deadlocks).
		If the function cannot lock all passed in mutexes, the function first unlocks all objects it successfully has locked (if any)
		before failing.
		""",
	},
	40: {
		'q':  """
		a) Outline the purpose of <mutex>'s std::lock_guard
		b) Specify a C++17 alternative to std::lock_guard and why it may be better
		""",
		'a': """
		a)
			std::lock_guard is a mutex wrapper that provides a convenient RAII-style mechanism for owning a mutex
			for the duration of a scoped bock.

			When an std::lock_guard object is created, it attempts to take ownership of the mutex it is given.
			When control leaves the scope in which the std::lock_guard object was created,
			the std::lock_guard instance is destructed and the mutex is released.

		b) std::scoped_lock offers a replacement for std::lock_guard as well as providing the ability to lock
			multiple mutexes using a dealock avoidance algorithm.
		""",
	},
	41: {
		'q':  """
		In the context of mutex locking, what is the difference between:
			1) .lock
			2) .try_lock
			3) .try_lock_for
			4) .try_lock_until
		""",
		'a': """
		All of (1)-(4) attempt to take exclusive ownership of the mutex, the
		difference really lies in the behaviour if the mutex is already owned beforehand.

		So in the case that the call is unsuccessful in acquiring the mutex:
			1) .lock will block until it has access and then process
			2) .try_lock will return false (true if success)
			3) .try_lock_for will continue to try for a specified std::chrono::duration
			4) .try_lock_until will block until the specifed std::chrono::time_point has been reached
				or the lock is acquired, whichever comes first. Behaves as std::try_lock after the std::chrono::time_point
				has been reached.
		""",
	},
	42: {
		'q':  """
		Compare std::mutex with std::timed_mutex
		""",
		'a': """
		Similar to std::mutex, std::timed_mutex offers exclusive, recursive ownership semantics.
		In addition to that, std::timed_mutex provides the ability to attempt to claim ownership of a std::timed_mutex
		with a timeout via the member functions `std::timed_mutex::try_lock_for`, `std::timed_mutex::try_lock_until`
		""",
	},
	43: {
		'q':  """
		a) What is the purpose of std::recursive_mutex
		b) In which coding scenarios would the use of std::recursive_mutex be application 
		""",
		'a': """
		a) And std::recursive mutex is, like std::mutex, Lockable. However, std::recursive_mutex
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
			2) handling critical section with a mutex in a for loop
		""",
	},
	44: {
		'q':  """
		State and describe the three <mutex> header locking strategy constants.
		""",
		'a': """
		1) std::defer_lock
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
			  and want a convient RAII-unlocking wrapper afterwards
		""",
	},
	45: {
		'q':  """
		<mutex>'s std::unique_lock is a general-purpose mutex wrapper.

		List the functionality that it allows for.
		""",
		'a': """
		1) Deferred locking
		2) Time-constrained attempts at locking
		3) Recursive locking
		4) Transfer of lock ownership (Moveable but not Copyable)
		5) Use with condition variables
		""",
	},
	46: {
		'q':  """
		a) What is the purpose of std::call_once?
		b) What arguments do you pass to std::call_once
		""",
		'a': """
		a) <mutex>'s std::call_once executes a Callable function exactly once,
			even if called concurrently from several threads.

		b) 	First argument: std::once_flag
			Second argument: Callable function
			[third argument, variable]: arguments to the Callable function, 0 if Callable has zero parameters
		""",
	},
	47: {
		'q':  """
		Outline the difference between <mutex> header's:	
			1) std::try_lock
			2) std::mutex::try_lock
		""",
		'a': """
		1) std::try_lock is a:
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
				- `false` on failure
		""",
	},
	48: {
		'q':  """
		Compare std::lock with std::try_lock
		""",
		'a': """
		- Both std::lock and std::try_lock take 1...N Lockable objects.
		- std::lock will implement a deadlock available algorithm and try multiple
			orders of the arguments passed and block if no mutex fails
		- std::try_lock will only try once and in the order of the mutexes passed
			and return -1 on success or a 0-based index of the mutex that failed.
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