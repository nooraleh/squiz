# Notes taken in a Q & A style format from Wisnu Anggoro's 'Boost.Asio C++ Network Programming, Second Edition'
# Also... notes taken in a Q & A style format from Dmytro Radchuk's 'Boost.Asio C++ Network Programming Cookbook'
qna = {
    1: {
		'q':  """
		What is the core object of the boost::asio namespace?
		""",
		'a': """
		The `io_service` object
		""",
	},
    2: {
		'q':  """
		In the context of boost.asio, what is the I/O service?
		""",
		'a': """
		The I/O service is a channel that is used to:

			1) access operating system resources
			2) establish communication between our program and the
				operating system that performs I/O requests
		""",
	},
    3: {
		'q':  """
		boost.asio context, what is understood as an `event`?
		""",
		'a': """
		An `event` is an action or occurrence detected by a program,
		which will be handled by the program using the `event handler` object.

		Note that the `io_service` object has oen or more instances where events
		are handled, which is the `event processing loop`.
		""",
	},
    4: {
		'q':  """
		What is the `boost::asio::io_service::work` object responsible for?
		""",
		'a': """
		It is responsible for telling the boost::asio::io_service object when the work
		starts and when the work has finished.
		""",
	},
    5: {
		'q':  """
		a) What is the boost::asio::io_service::poll member function used for?
		b) What is the difference between io_service::run() and io_service::poll()
		""",
		'a': """
		a) The poll() member function is used to run ready handlers until there are no
		more ready handlers remaining or until the boost::asio::io_service object
		has been stopped.

		b) poll() will not block the program, run() will
		""",
	},
    6: {
		'q':  """
		a) What is the difference between the functionality of:

			1) boost::asio::io_service::post, and;
			2) boost::asio::io_service::dispatch

		b) True or false:
			The member functions referenced in part (a) are deprecated in favour
			of free functions `boost::asio::post` and `boost::asio::dispatch`
		""",
		'a': """
		a)
			Both `post` and `dispatch` are used to post a function or task to an
			`io_service` object for asynchronous execution, and both are thread-safe, however:

			post:
				- posts the given function or task to the `io_service` object's queue and returns
				immediately.
				- the function/task posted is guaranteed to be executed by the `io_service` object
				thread(s) in the future
				- the caller of `post` does not wait for the function or task to complete

			dispatch:
				- also posts the given function or task to the `io_service` object's queue
				- guarantees that the function or task will be executed immediately by the 
					`io_service` object's thread BEFORE dispatch returns
				- this means that the caller of `dispatch` may wait for the function or
					task to complete before executing

			Summary:
				`boost::asio::post` is non-blocking, while `boost::asio::dispatch` is blocking.

		b) True
		""",
	},
    7: {
		'q':  """
		a) Define a `strand`?
		b) Based on your answer to (a), give an example of an implicit strand and an
			explicit strand.
		""",
		'a': """
		a) A strand is defined as:
			- a strictly sequential invocation of event handlers (i.e no concurrent invocation)
			- note that use of strands allows sequential execution of code in a
				multithreaded program without the need for explicit locking (e.g. mutexes)

		b) 
		Implicit strand:
			- calling boost::asio::io_context::run from only one thread meands that all
				event handlers assoicated with said instance of io_context will execute in
				and implicit strand.
			- this is due to boost::asio::io_context's guarantee that event handlers are only
				invoked inside run.

		Explicit strand:
			- is an instance of boost::asio::strand<> or boost::asio::io_context::strand
			
		""",
	},
    8: {
		'q':  """
		What is understood as an 'event handler' in boost.asio?
		""",
		'a': """
		An 'event handler' is a function that is called when a particular event occurs on an
		I/O object 'i.e a boost::asio::io_context'.

		An event handler is registered with an I/O object by calling one of the `async_*()`
		functions provided by the boost.asio library.
		""",
	},
    9: {
		'q':  """
		What is an executor?
		""",
		'a': """
		An executor repesents an object that can execute functions or tasks.
		In boost.asio, an executor allows us to separate the scheduling of the work
		from the work itself.
		""",
	},
    10: {
		'q':  r"""
		boost::asio::io_context::work is deprecated, consider the following
		snippet and replace it with the preferred calling code:

			boost::asio::io_context io_context;
			boost::asio::io_context::work work_guard{io_context};
		""",
		'a': r"""
		boost::asio::io_context::work is deprecated in favour of boost::asio::executor_work_guard
		so we would rewrite the snippet as follows:

			boost::asio::io_context io_context;
			auto work_guard{boost::make_work_guard(io_context.get_executor())};
		""",
	},
	11: {
		'q':  """
		`boost::asio::io_context::run` has an overload which takes no parameters.
			std::size_t boost::asio::io_context::run();

		What is the other overload and what is the other overload used for?
		""",
		'a': """
		The other overload of `boost::asio::io_context::run` takes a boost::system::error_code&
		this is so that it can be modified and if there is an issue it can be checkout within
		the calling code:

		E.g.
			boost::system::error_code ec;
			boost::asio::io_context io_context;

			io_context->run(ec);

			if (ec) // something went run if we are in this block
			{

			}
		""",
	},
	12: {
		'q':  """
		What is the difference between:
			1) boost::asio::work_guard, and;
			2) boost::asio::io_context::stop member function?
		""",
		'a': """
		boost::asio::work_guard:
			- is used to keep the `boost::asio::io_context` object running even if
				there is no active work

		boost::asio::io_context::stop:
			- is used to immediately stop the `boost::asio::io_context` and abandon any
				unfinished work.
		""",
	},
	13: {
		'q':  """
		What is the difference between a:
			1) Physical address
			2) Logical address
		""",
		'a': """
		Physical address (also known as MAC [media access control] address):
			- is a unique identifier assigned to a NIC (network interface controller)
				by its manufacturer.
			- is a hardware address
			- used in the data link layer of the networking stack
			- typically 48 bits long are represented in hexadecimal notation

		Logical address (AKA IP address)
			- software address assigned by a network administrator or automatically
				through a protocol such as DHCP
			- used in the network layer of the networking stack
			- are 32 to 128 bits long and are represented in decimal notation

		""",
	},
	14: {
		'q':  """
		What is the difference between a) shutting down a socket b) closing a socket?
		""",
		'a': """
		Socket shut down:
			- a way of terminating the sending or receiving of data (or both) on a socket
				WHILE leaving a socket open.
			- when a socket is shut down, it can no longer send of receive data, but the
				socket remains open and can still be used for other operations.

		Socket close:
			- terminating a socket and freeing up the system resources associated with it
			- upon closing, all data sent or received is discarded and the socket is closed
				for futher use
		""",
	},
	15: {
		'q':  """
		a) What is the purpose of `boost::asio::ip::tcp::resolver` ?
		b) Give a concrete code example of your answer given in (a)
		""",
		'a': """
		a) The `boost::asio::ip::tcp::resolver` class is used to resolve
			hostnames to their corresponding IP address.

		b) Snippet:
			boost::asio::ip::tcp::resolver resolver{ *p_io_context };
			boost::asio::ip::tcp::resolver::query query{ "www.packtpub.com", boost::lexical_cast<std::string>(80) };
			auto iterator = resolver.resolve(query);
			boost::asio::ip::tcp::endpoint endpoint = *iterator;
			std::cout << "connecting to: " << endpoint << '\n';

		As you can see, we have passed a `query` class which has the human-readable
		hostname and in the last line we print out the IP address.
		""",
	},
	16: {
		'q':  """
		What is the purpose of boost::asio::ip::tcp::acceptor::reuse_address ?
		""",
		'a': """
		`reuse_address` is a socket option to allow the socket in question to be bound
		to an address that is already in use.
		""",
	},
	17: {
		'q':  """
		What is `boost::asio::ip::tcp::socket::shutdown_both` used for?
		""",
		'a': """
		It is an option flag for shutting down both send and receive on
		the socket upon calling boost::asio::ip::tcp:socket::shutdown on an
		instant of boost::asio::ip::tcp::socket.
		""",
	},
	18: {
		'q':  """
		What is a:
			1) passive socket (also known as acceptor socket)
			2) active socket

		""",
		'a': """
		Passive socket:
			- socket used by a server program to listen for incoming
				requests from client programs
		
		Active socket:
			- socket used for communication with a specific client that
				has connected to the server
			- is created by the passive socket when the passive socket
				receives the connection request, the created active socket
				will then be responsible for communication with the client

		""",
	},
	19: {
		'q':  """
		What is a distributed application?
		""",
		'a': """
		A distributed application is one that:
			- consists of two or more parts
			- each part runs on a separate computing device
			- communicates with other parts over a computer network
		""",
	},
	20: {
		'q':  """
		a) What is the 'point-to-point communication model'?
		b) Which of protocols 1) TCP or 2) UDP assume the point-to-point communication model?
		""",
		'a': """
		a)  Point-to-point communication model:
				Only two applications can communicate over a single connection.
				I.e. no multicast messaging is supported.
		b) TCP
		""",
	},
	21: {
		'q':  """
		What is an endpoint?
		""",
		'a': """
		An endpoint is a pair of values consisting of:
			 1) and IP address, and;
			 2) a protocol port number
		that uniquely identifies a particular application running on a particular
		host in a computer network.
		""",
	},
	22: {
		'q':  """
		Endpoints serve a goal for the client application as well as the server application.
		State the two.
		""",
		'a': """
		Client application:
			- uses an endpoint to designate a particular server application is wants to communicate 
				with.

		Server application:
			- uses an endpoint to specify a local IP address and port number on which it wants
				to receive incoming messages from clients.
		""",
	},
	23: {
		'q':  """
		True or false:
			For a server application, if there is more than one IP address on the host,
			the server application will want to create a special endpoint representing
			all IP addresses at once.

		b) if true, how would you go about achieving this with boost::asio?
		""",
		'a': """
		a) True.

		NOTE that this means that server applications tend to only need to obtain a port
		number on which to listen.

		b) Instantiate a cass boost::asio::ip::address with one of the following:
			1) boost::asio::ip::address_v4::any(), or;
			2) boost::asio::ip::address_v6::any()
		""",
	},
	24: {
		'q':  """
		True or false:
			An instance of type boost::asio::ip::address represents an IPv4 address
			by default.
		""",
		'a': """
		False, boost::asio::ip::address is an IP-protocol-version-agnostic class which can
		represent both IPv4 and IPv6.

		""",
	},
	25: {
		'q':  """
		Describe and distinguish the following terms in the context of the process of establishing
		a network connection:
			1) Creating a socket
			2) Opening a socket
		""",
		'a': """
		Creating a socket:
			- involves allocating resources in the operating system to create a socket object
			- this socket object is used for send and receiving data over a network

		Opening a socket:
			- involves binding the socket to a specific network address and port number
			- then putting the socket ni a listening state to accept incoming connections
				or initiating a connection to a remote network endpoint.
		""",
	},
	26: {
		'q':  """
		In boost.asio, what does it mean to open a socket? I.e calling one of:
			1) boost::asio::ip::tcp::socket::open or
			2) boost::asio::ip::udp::socket::open ?
		""",
		'a': """
		In boost.asio, 'opening' a socket means associate the `socket` object with
		a full set of parameters describing a specific protocol over which the socket
		is intended to be communicating.

		When the boost.asio `socket` instance is provided with these parameters, it has
		enough information to allocate a real socket object of the underlying operating system.
		""",
	},
	27: {
		'q':  """
		Consider the statement:
			A passive (also acceptor) socket is a type of socket that is used
			to wait for connection establishments requests from remote applications.

		Explain why an acceptor socket is not available under the boost::asio::ip::udp namespace.
		""",
		'a': """
		Because the udp protocol is connectionless (i.e does not establish connections),
		and since the passive socket by definition is used to wait for connection requests there is 
		no need for such a udp acceptor socket object.
		""",
	},
	28: {
		'q':  """
		Consider the following snippet:
			boost::asio::io_context io_context; 									(1)
			boost::asio::ip::tcp protocol_tcp_ipv4{ boost::asio::ip::tcp::v4() }; 	(2)
			boost::asio::ip::tcp::acceptor acceptor{ io_context }; 					(3)
			boost::system::error_code ec; 
			acceptor.open(protocol_tcp_ipv4, ec);  								  	(4)

		On which line is the operating system socket object associated with the `acceptor`
		class instance allocated?
		""",
		'a': """
		Line (4)
		""",
	},
	29: {
		'q':  """
		a) What is the purpose of `boost::asio::ip::tcp::resolver::query`?
		b) What are the constructor arguments?
		""",
		'a': """
		a) The `query` class abstracts a query to the DNS (domain name system).
		
		b) Constructor arguments contain:
			1) a DNS name to resolve
			2) a port number
			3) [optionally] a flag to control some aspects of the resolution process e.g.
				`boost::asio::ip::tcp::resolver::query::numeric_service`.
		""",
	},
	30: {
		'q':  """
		Consider the following snippet:

			std::string host{ "www.google.com" };
			std::string port_num{ "3333" };

			boost::asio::io_context io_context;

			boost::asio::ip::tcp::resolver::query resolver_query{
				host, port_num, boost::asio::ip::tcp::resolver::query::numeric_service };

			boost::asio::ip::tcp::resolver resolver{ io_context };

			boost::system::error_code ec;
			auto iterator = resolver.resolve(resolver_query, ec); (1)

		Q: How would I go about iterating all possible IP address resolutions that have been found
			in line (1)
		""",
		'a': """
		Model answer:

			// default constructed object represents the end iterator
			boost::asio::ip::tcp::resolver::iterator end_iterator{};

			for (; iterator != end_iterator; ++iterator)
			{
				// calling `endpoint` more explicit than dereferencing the iterator
				auto current_endpoint = iterator->endpoint();
			}
		""",
	},
	31: {
		'q':  """
		What is the name of the process of associating a socket with a particular endpoint?
		""",
		'a': """
		Name: Binding.
		""",
	},
	32: {
		'q':  """
		In the context of the point-to-point communication model, what are the implications
		of a socket A being connected to a socket B?
		""",
		'a': """
		Implications:
			1) both socket A and socket B can communicate with each other
			2) neither socket A nor socket B can communicate with any other socket C
		""",
	},
	33: {
		'q':  """
		True or false:

			The acceptor socket doesn't connect itself to the client application while processing
			a connection request. Instead, it opens and connects another active socket, which is then
			used for communication with the client application. The acceptor socket only listens for
			and processes (accepts) incoming connection requests.
		""",
		'a': """
		True
		""",
	},
	34: {  ## ---------------------
		'q':  """
		Consider the statement:
			Like any other type of I/O, the network I/O involves using memory buffers.

		What are memory buffers?
		""",
		'a': """
		Memory buffers are contiguous blocks of memory allocated in the process's address space
		used to store the data.
		""",
	},
	35: {
		'q':  """
		boost.asio supports two types of I/O operations:
			1) synchronous 2) asynchronous

		Outline the distiction in behaviour for synchronous and asynchronous i/o operations.
		""",
		'a': """
		Synchronous operations:
			- block the thread of execution invoking them and unblock only when the
				operation is finished.

		Asynchronous operation:
			- when initiated, is associated with a callback function or functor
			- this callback is invoked by the boost.asio library when the operation is finished
		""",
	},
	36: {
		'q':  """
		Why is the ability to cancel a previously initiated asynchronous operation important?
		""",
		'a': """
		It allows the application to state that the previously initiated operation is not relevant
		anymore, which may save the application's resources (both CPU and memory), that otherwise
		would be unavoidably wasted.
		""",
	},
	37: {
		'q':  """
		In boost.asio, a fixed-length buffer is represented by either of two classes,
		state them.

		""",
		'a': """
		1) boost::asio::mutable_buffer
			- writable-buffer
			- used to receive the output of an operation
			- e.g. the `receive` operation of a socket

		2) boost::asio::const_buffer
			- read-only-buffer
			- used as input to an operation
			- e.g. `send` operation of a socket
		""",
	},
	38: {
		'q':  """
		Consider the following snippet:
			const std::size_t BUFFER_SIZE{20};
			auto p_buffer = std::make_unique<char[]>(BUFFER_SIZE);
			std::unique_ptr<char[]> p_alt{ new char[BUFFER_SIZE] };
			auto mutable_buffer = boost::asio::buffer(
				static_cast<void*>(p_buffer.get()), BUFFER_SIZE
			);

		True or false:
			All classes in boost.asio that represent buffers, i.e.
				1) boost::asio::mutable_buffer
				2) boost::asio::const_buffer
				3) boost::asio::mutable_buffers_1 (adapter for sequences)
				4) boost::asio::const_buffers_1 (adapter for sequences)

			Take ownership of the underlying resource (i.e they are responsible)
			for their lifetimes.
		""",
		'a': """
		False. They do not take ownership or control the underlying buffer resource
		lifetime - it is up to you as the client of this code to control the lifetime
		of the resources that you allocate and pass as an argument into the boost.asio 
		library.
		""",
	},
	39: {
		'q':  """
		a) What are extensible buffers?
		b) What is the purpose of extensible buffers?
		c) Which class in the boost.asio library represents an extensible buffer?
		""",
		'a': """
		a) Extensible buffers are those buffers that dynamically increase
			in size when new data is written to them.
		b) They are usually used to read data from sockets when the size of the 
			incoming message is unknown.
		c) boost::asio::streambuf
		""",
	},
	40: {
		'q':  """
		Writing to a TCP is an output operation that is used to send data to the
		remote application connected to this socket.

		What is the most basic way to write to the socket in the boost.asio library?
		""",
		'a': """
		Using member function `boost::asio::ip::tcp::socket::write_some`
		""",
	},
	41: {
		'q':  """
		a) Which free function in the boost.asio library should you turn to in order
		to read from a socket until a particular pattern is found?

		b) What should the client developer bear in mind when using the answer to (a)
		""",
		'a': """
		a)  boost::asio::read_until, consider one of the overloads:

			template <typename SyncReadStream, typename Allocator>
			inline std::size_t read_until(SyncReadStream& s,
				boost::asio::basic_streambuf<Allocator>& b, char delim)
			{
			  return read_until(s, basic_streambuf_ref<Allocator>(b), delim);
			}

		b) boost::asio::read_until is guaranteed to contain at least one delimiter 
			symbol but it may contain more. Therefore it is the developers responsibility
			to parse the data in the buffer and handle the situation where it contains data
			after the delimiter symbols.
		""",
	},
	42: {
		'q':  """
		True or false:
			One of the benefits of asynchronous operations provided by the boost.asio library
			is that they can be canceled at any moment after the initiation.
		""",
		'a': """
		True
		""",
	},
	43: {
		'q':  """
		What is the purpose of member function `boost::asio::ip::tcp::socket::cancel`?
		""",
		'a': """
		The purpose is to cancel all asynchronous operations (cancel, send and/or receive)
		associated with the instance of `boost::asio::ip::tcp::socket`.
		""",
	},
	44: {
		'q':  """
		Do the `boost::asio::ip::tcp::socket` class implement the RAII idiom? Explain.
		""",
		'a': """
		Since the boost::asio::ip::tcp::socket class calls it's `close` member in the destructor,
		and since the `close` member function is responsibily for returning the owned resource back
		to the operating system - yes `socket` does use RAII.
		""",
	},
	45: {
		'q':  """
		Consider the snippet:
			
			boost::asio::ip::tcp::socket active_socket(io_context);
			// ...
			active_socket.shutdown(boost::asio::socket_base::shutdown_send); (1)

		True or false:
			Once writing to a socket has been disabled (as in line (1)) it is possible
			to restore the socket state to make it writable again.
		""",
		'a': """
		False. It is not posssible to restore the socket state to make it writable again.
		""",
	},
	46: {
		'q':  """
		A synchronous approach has some functional limitations which can make it unacceptable.
		State a few of these limitations that a synchronous approach would have that an asynchronous
		one would not.
		""",
		'a': """
		Limitations:
			1) The inability to cancel a synchronous operation after it has started.
			2) Inability to assign the synchronous operation a timeout so that it gets interrupted
				if it is running longer than a certain amount of time.
		""",
	},
	47: {
		'q':  """
		What is the term for hybrid server applications that provide their services through both TCP
		and UDP?
		""",
		'a': """
		Multiprotocol servers.
		""",
	},
	48: {
		'q':  """
		Give a brief summary of the following terms:
			1) iterative server
			2) parallel server

		And outline the pros and cons of using them
		""",
		'a': """
		Iterative server:
			- serves clients in a one-by-one fashion
			- it does not start serving the next client before it
				completes serving the one it is currently serving.
			- pro:
				- relatively simple to implement
				- ideal for low request rates

		Parallel server:
			- can serve multiple clients in parallel
			- pro:
				- ideal for higher request rates
			- con:
				- not as simply to implement
		""",
	},
	49: {
		'q':  """
		Consider the following typedef's in the boost.asio library:
			1) typedef basic_waitable_timer<chrono::system_clock> system_timer;
			2) typedef basic_waitable_timer<chrono::steady_clock> steady_timer;
			3) typedef basic_waitable_timer<chrono::high_resolution_clock> high_resolution_timer;

		Which of (1), (2) or (3) is best suited for:
			a) cases when high precision in time management is required
			b) cases when we need to set up a timer that will notify us when a certain absolute
				timepoint is reached (e.g. 13h:15m:45s)
			c) cases when we need to measure intervals between timepoints
		""",
		'a': """
		a) (3)
		b) (1) as system_timer is influenced by external changes of the current system time.
		c) (2) since:
			- steady_clock not influenced by system clock changes
			- system_clock is influenced by system clock shifts which may result in the timer
				expiring sooner or later than expected.
		""",
	},
	50: {
		'q':  """
		True or false:
			Because a steady timer is not influenced by the system clock shifts,
			it is the best fit to implement the timeout mechanism.
		""",
		'a': """
		True
		""",
	}
}