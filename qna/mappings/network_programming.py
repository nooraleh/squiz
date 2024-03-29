# Notes taken in a QNA style from Lewis Van Winkles's 'Hand-On Network Programming in C'

qna = {
    1: { # Chapter 1: Introducing Networks and Protocols
		'q':  """
		What does the acronym OSI stand for ?
		""",
		'a': """
		Open Systems Interconnection
		""",
	},
    2: {
		'q':  """
		In the context of the OSI model, what is the concern of the Physical layer?
		""",
		'a': """
		The physical layer concerns the specification of things such as:
			1) the voltage levels on an Ethernet cable
			2) what each pin on a connector is for
			3) the radio frequency of Wi-Fi
			4) the light flashes over an optic fiber
		""",
	},
    3: {
		'q':  """
		In the context of the OSI model, what is the concern of the Data Link layer?
		""",
		'a': """
		This levels builds on the physical layer.
		
			- It deals with protocols for directly communicating between two nodes.
			- Framing
			- Error detection and correction
			- Flow control
		""",
	},
    4: {
		'q':  """
		What is meant by 'framing'?
		""",
		'a': """
		Framing defines how a direct message between nodes starts and ends.
		""",
	},
    5: {
		'q':  """
		In the context of the OSI model, what is the concern of the Network layer?
		""",
		'a': """
		The network layer provides the methods to transmit data sequences (called packets)
		between nodes in different networks.

		It provides methods to route packets from one node to another (without
		a direct physical connection) by transferring through many intermediate nodes.

		NB: This is the layer that the Internet protocol is defined on.
		""",
	},
    6: {
		'q':  """
		In the context of the OSI model, what is the concern of the Transport layer?
		""",
		'a': """
		At the Transport layer, we have methods to reliably deliver variable
		length data between hosts.

		These methods deal with:
			1) splitting up data
			2) recombining it
			3) ensuring data arrives in order, etc

		NB: The Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)
		are commonly said to exist on this layer.
		""",
	},
    7: {
		'q':  """
		In the context of the OSI model, what is the concern of the Session layer?
		""",
		'a': """
		The Session layer builds on the transport layer by adding methods to:
			- establish
			- checkpoint
			- suspend
			- resume
			- and terminate
		dialogs.
		""",
	},
    8: {
		'q':  """
		In the context of the OSI model, what is the concern of the Presentation layer?
		""",
		'a': """
		This Presentation layer is the lowest layer at which data structure and presentation
		for an application are defined.

		Concerns such as:
			- data encoding
			- serialization
			- encryption
		Are handled here.
		""",
	},
    9: {
		'q':  """
		In the context of the OSI model, what is the concern of the Application layer?
		""",
		'a': """
		The applications that the user interfaces with (e.g. web browswers and email clients)
		exist in the Application layer. These applications make use of the services provided
		by the six lower layers.
		""",
	},
    10: {
		'q':  """
		What is one drawback of the OSI model abstraction?
		""",
		'a': """
		The OSI model abstraction doesn't fit precisely with the common protocols
		in use today.
		""",
	},
	11: {
		'q':  """
		What are the four layers of the TCP/IP model beginning from
		the closest to the physical layer (from the OSI model)?
		""",
		'a': """
		1) Network access
		2) Internet
		3) Host-to-Host
		3) Process/Application
		""",
	},
	12: {
		'q':  """
		What do the following acronyms stand for?
			1) SMTP
			2) FTP
			3) TCP
			4) UDP
			5) DNS
		""",
		'a': """
			1) Simple Mail Transfer Protocol
			2) File Transfer Protocol
			3) Transmission Control Protocol
			4) User Datagram Protocol
			5) Domain Name System (DNS)
		""",
	},
	13: {
		'q':  """
		In the context of the TCP/IP model, what is the concern of the Network Access layer?
		""",
		'a': """
		On this layer, physical connections and data framing happen.
		Sending an Ethernet or Wi-Fi packet are examples of layer 1 concerns.
		""",
	},
	14: {
		'q':  """
		In the context of the TCP/IP model, what is the concern of the Internet layer?
		""",
		'a': """
		This layer deals with the concerns of addressing packets and routing them
		over multiple interconnection networks. It's at this layer that an IP
		address is defined.
		""",
	},
	15: {
		'q':  """
		In the context of the TCP/IP model, what is the concern of the Host-to-Host layer?
		""",
		'a': """
		The host-to-host layer provides two protocols, TCP and UDP.
		These protocols address conerns such as data order, data segmentation,
		network congestions, and error correction.
		""",
	},
	16: {
		'q':  """
		In the context of the TCP/IP model, what is the concern of the Process/Application layer?
		""",
		'a': """
		The process/application layer is where protocols such as HTTP, SMTP, and FTP are
		implemented. This layer consumes fucntionality provided by our operating system's
		implementation of the lower layers.
		""",
	},
	17: {
		'q':  """
		What is the difference between IPv4 and IPv6 (address size specifically)?
		""",
		'a': """
		IPv4 uses 32-bit addresses, IPv6 uses 128-bit addresses.
		""",
	},
	18: {
		'q':  """
		i)  Why is it important to have network which supports IPv4?
		ii) What is the term for operation system support for both IPv4 and IPv6?
		
		""",
		'a': """
		i)  Because you risk a significant portion of your users not being
		able to connect.
		ii) Dual-stack configuration.
		""",
	},
	19: {
		'q':  """
		Describe the structure of an IPv4 address.
		""",
		'a': """
		An IPv4 address has the following characteristics:
			- IPv4 addresses are 32 bits long
			- They are commonly divided (dot-delimited) by four 8-bit sections
			- Each section is displayed as a decimal number between 0 and 255
				inclusive.

		Examples include:
			0.0.0.0
			127.0.0.1
			255.255.254.123
		""",
	},
	20: {
		'q':  """
		i)  What is the loopback address?
		ii) Give the IPv4 address representation of what it is reserved for. 
		""",
		'a': """
		i)  The loopback address means 'establish a connection to myself'.
		ii) 127.0.0.1
		""",
	},
	21: {
		'q':  """
		TOLEARN: Classless Inter-Domain Routing (CIDR)
		""",
		'a': """
		
		""",
	},
	22: {
		'q':  """
		Describe the structure of an IPv6 address.
		""",
		'a': """
		- IPv6 addresses are 128 bits long.
		- They are written as eight groups of four hexadecimal characters delineated
			by colons.

		NB: The standard is to use lowercase hexadecimal letters in IPv6 addresses.
		""",
	},
	23: {
		'q':  """
		What is the utility command in Windows which lists the routers between
		your system and the destination system?
		""",
		'a': """
		tracert.

		Usage:
			tracert <website>
		""",
	},
	24: {
		'q':  """
		i)  What are Local Area Networks (LANs)?
		ii) When a packet originates from a device on an LAN, what must
			the packet undergo before being routed on the internet?
		""",
		'a': """
		i)  Local area networks are IPv4 address ranges reserved for use in
			small local networks (such as households and organizations).

		ii) The packet must undergo Network Address Translation (NAT) before
			being routed on the internet.

			NB: A router that implements NAT remembers which local address a
				connection is established from.
		""",
	},
	25: {
		'q':  """
		What does NAT (Network Address Translation) entail?
		""",
		'a': """
		When an IP packet comes from a local area network (LAN) meant for the
		internet. The Router modifies the source IP address from the original
		private LAN IP address to its own public internet IP address.

		Likewise, when the router receives the return communication, it must
		modify the destination address from its public IP to the private IP
		of the original sender.
		""",
	},
	26: {
		'q':  """
		What is meant by:
			1) Unicast addressing
			2) Broadcast addressing
			3) Multicast addressing
			4) Anycast addressing
		""",
		'a': """
		1) Unicast addressing:
				- When a packet is routed from one sender to one receiver.
		2) Broadcast addressing:
				- Allows a single sender to address a packet to all recipients
				  simultaneously. Typically used to deliver a packet to every
				  receiver on an entire subnet.
		3) Multicast addressing:
				- If broadcast is one-to-all, multicast is one-to-many.
				- Multicast involves group management, and a message is addressed
				  and delivered to members of a group.
		4) Anycast addressing:
				- Used to deliver a message to one recipient when you don't care who
				  that recipient is.
				- Useful for when you have several servers that provide the same
				  functionality, and you simply want one of them (you don't care which)
				  to handle your request.
		""",
	},
	27: {
		'q':  """
		Why would implementing the use of IP multicasting on your local
		network be worthwhile, as opposed to sending the same unicast message
		multiple times?
		""",
		'a': """
		Because it conserves bandwidth.
		""",
	},
	28: {
		'q':  """
		What is a high-level overview of a socket?
		""",
		'a': """
		A socket is an abstraction that represents one endpoint of a communication link
		between systems.
		""",
	},
	29: {
		'q':  """
		How is a socket defined?
		""",
		'a': """
		An open socket is uniquely defined by a 5-tuple consisting of the following:
			1) Local IP address
			2) Local/Ephemeral port
			3) Remote IP address
			4) Remote port
			5) Protocol (UDP or TCP)
		""",
	},
	30: { # Chapter 2: Getting to Grips with Socket APIs
		'q':  """
		What is one difference between Winsock socket and a Berkeley socket?
		""",
		'a': """
		Winsock requires initialization before use and a cleanup function call when
		we are finished.

		These initialization and cleanup steps are not used with Berkeley sockets.
		Berkley socket API is always ready to use.
		""",
	},
	31: {
		'q':  """
		i)  What are the two basic socket types?
		ii) Which of TCP or UDP correspond to which type as per your answer to (i)
		""",
		'a': """
		i)  (1) Connection-oriented  (2) Connectionless
		ii) TCP is a connection-oriented protocol, UDP is a connectionless protocol.
		""",
	},
	32: {
		'q':  """
		What does a connectionless protocol, such as UDP, entail?
		""",
		'a': """
		In a connectionless protocol, such as UDP, each data packet is addressed individually.
		From the protocol's perspective, each data packet is completely independent and unrelated
		to any packets coming before or after it.
		""",
	},
	33: {
		'q':  """
		What does a connection-oriented protocol, such as TCP, entail?
		""",
		'a': """
		In a connection-oriented protocol we:
			1) Guarantee that data arrives in the same order it is sent.
			2) Prevent duplicate data from arriving twice
			3) Retry sending missing data
			4) Notify when a connection is terminated
			5) Run algorithms to mitigate network congestion
		""",
	},
	34: {
		'q':  """
		i)  Name a use case where UDP has an advantage over TCP
		ii) What implications does your answer to (i) have on IP broadcast or multicast.
		""",
		'a': """
		i)  UDP has the advantage in cases where you want to send a message without expecting
			a response from the other end.
		
		ii) This makes it useful when using IP broadcast or multicast. TCP, on the other hand,
			requires bidirectional communication to provide its guarantees and so
			does not work with IP multicast or broadcast.
		""",
	},
	35: {
		'q':  """
		Explain the usage of the following socket functions:
			1) socket()
			2) bind()
			3) listen()
		""",
		'a': """
			1) socket() - creates and initializes a new socket
			2) bind() - associates a socket with a particular local IP address and port number
			3) listen() - is used on the server to cause a TCP socket to listen for new connections
		""",
	},
	36: {
		'q':  """
		Explain the usage of the following socket functions:
			1) connect()
			2) accept()
			3) send()
			4) recv()
		""",
		'a': """
			1) connect() - is used on the client to set the remote address and port.
				In the case of TCP, it also establishes a connection.
			2) accept() - is used on the server to create a new socket for an incoming
				TCP connection.
			3) send() - used to send data with a socket
			4) recv() - sued to receive data with a socket.
		""",
	},
	37: {
		'q':  """
		Explain the usage of the following socket functions:
			1) sento()
			2) recvfrom()
		""",
		'a': """
			1) sento() -
				is used to send data from sockets without a bound remote address.
			2) recvfrom() - 
				is used to receive data from sockets without a bound remote address.
		""",
	},
	38: {
		'q':  """
		Explain the usage of the following socket functions:
			1) close()
			2) closesocket()
			3) shutdown()
		""",
		'a': """
			1) close()
				-  applies to Berkeley sockets
			2) closesocket()
				- applies to Winsock sockets.
				
		Both (1) and (2) are used to close a socket. In the case of TCP,
		this also terminates the connection.

			3) shutdown()
				- is used to close one side of a TCP connection. It is useful
				to ensure an orderly connection teardown.
		""",
	},
	39: {
		'q':  """
		Explain the usage of the following socket functions:
			1) select()
			2) getnameinfo()
			3) getaddrinfo()
		""",
		'a': """
			1) select()
				- is used to wait for an event on one or more sockets.
			2) getnameinfo()
				- provides a protocol-independent manner of working with hostnames
			3) getaddrinfo()
				- provides a protocol-independent manner of working with addresses
		""",
	},
	40: {
		'q':  """
		Explain the usage of the following socket functions:
			1) setsockopt()
			2) fcntl()
			3) ioctlsocket()
		""",
		'a': """
			1) setsockopt()
				- used to set socket options
			2) fcntl()
				- Berkely sockets only
				- used to get and set some options
			3) ioctlsocket()
				- Winsock sockets only
				- used to get and set some options
		""",
	},
	41: {
		'q':  """
		When could a TCP client to call `bind()` before `connect`?
		""",
		'a': """
		If the TCP client is particular about which network interface is
		being used to connect with.
		""",
	},
	42: {
		'q':  """
		i)  In UNIX, how is a socket descriptor represented?
		ii) What implications does your answer to (i) have on function usage on UNIX sockets?
		""",
		'a': """
		i)  In UNIX, a socket descriptor is represented by a standard file descriptor.
		ii) This means that, as opposed to Windows, you can use any of the standard UNIX I/O
			functions on sockets.
		""",
	},
	43: {
		'q':  """
		What are UNIX file descriptors?
		""",
		'a': """
		All UNIX file descriptors are small, non-negative integers.
		""",
	},
	44: {
		'q':  """
		What does a call to `socket()` return if it fails in the:
			i)  UNIX platform
			ii) Windows
		""",
		'a': """
			i)  negative number
			ii) `INVALID_SOCKET`
		""",
	},
	45: {
		'q':  """
		Consider the following snippet:

			char request[1024];
			int bytes_received = recv(socket_client, request, 1024, 0);
			printf("Received %.*s bytes.\n", bytes_received, request);

		Why is important to use the format specifier %.*s instead of for example:
			printf("Received %s bytes.\n", request);
		""",
		'a': """
		Because there is no guarantee that the data that's received from `recv()`
		is null terminated.

		In the alternative case, you will likely receive a segmentation fault error
		(or at best garbage output).
		""",
	},
	46: {
		'q':  """
		What is 'inetd'?
		""",
		'a': """
		inetd is a service on UNIX-like systems which can be used to turn
		console-like applications into networked ones.

		You can configure inetd (on /etc/inetd.conf) with your program's:
			1) location
			2) port number
			3) protocol (TCP or UDP)
			4) the user your want it to run as

		inetd will then listen for connections on your desired port.
		""",
	},
	47: { # Chapter 3: An In-Depth Overview of TCP Connections
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
