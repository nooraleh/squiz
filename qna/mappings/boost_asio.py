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