using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.Software
{
    public partial class NetworkProgramming : QNABase
    {
        public NetworkProgramming()
        : base(title: "Lewis Van Winkles's 'Hand-On Network Programming in C'", category: QNACategory.Software, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "NetworkProgramming";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"What does the acronym OSI stand for ?"},
        {"a", @"Open Systems Interconnection"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Physical layer?"},
        {"a", @"The physical layer concerns the specification of things such as:
			1) the voltage levels on an Ethernet cable
			2) what each pin on a connector is for
			3) the radio frequency of Wi-Fi
			4) the light flashes over an optic fiber"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Data Link layer?"},
        {"a", @"This levels builds on the physical layer.
		
			- It deals with protocols for directly communicating between two nodes.
			- Framing
			- Error detection and correction
			- Flow control"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"What is meant by 'framing'?"},
        {"a", @"Framing defines how a direct message between nodes starts and ends."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Network layer?"},
        {"a", @"The network layer provides the methods to transmit data sequences (called packets)
		between nodes in different networks.

		It provides methods to route packets from one node to another (without
		a direct physical connection) by transferring through many intermediate nodes.

		NB: This is the layer that the Internet protocol is defined on."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Transport layer?"},
        {"a", @"At the Transport layer, we have methods to reliably deliver variable
		length data between hosts.

		These methods deal with:
			1) splitting up data
			2) recombining it
			3) ensuring data arrives in order, etc

		NB: The Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)
		are commonly said to exist on this layer."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Session layer?"},
        {"a", @"The Session layer builds on the transport layer by adding methods to:
			- establish
			- checkpoint
			- suspend
			- resume
			- and terminate
		dialogs."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Presentation layer?"},
        {"a", @"This Presentation layer is the lowest layer at which data structure and presentation
		for an application are defined.

		Concerns such as:
			- data encoding
			- serialization
			- encryption
		Are handled here."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"In the context of the OSI model, what is the concern of the Application layer?"},
        {"a", @"The applications that the user interfaces with (e.g. web browswers and email clients)
		exist in the Application layer. These applications make use of the services provided
		by the six lower layers."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"What is one drawback of the OSI model abstraction?"},
        {"a", @"The OSI model abstraction doesn't fit precisely with the common protocols
		in use today."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"What are the four layers of the TCP/IP model beginning from
		the closest to the physical layer (from the OSI model)?"},
        {"a", @"1) Network access
		2) Internet
		3) Host-to-Host
		3) Process/Application"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"What do the following acronyms stand for?
			1) SMTP
			2) FTP
			3) TCP
			4) UDP
			5) DNS"},
        {"a", @"1) Simple Mail Transfer Protocol
			2) File Transfer Protocol
			3) Transmission Control Protocol
			4) User Datagram Protocol
			5) Domain Name System (DNS)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"In the context of the TCP/IP model, what is the concern of the Network Access layer?"},
        {"a", @"On this layer, physical connections and data framing happen.
		Sending an Ethernet or Wi-Fi packet are examples of layer 1 concerns."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"In the context of the TCP/IP model, what is the concern of the Internet layer?"},
        {"a", @"This layer deals with the concerns of addressing packets and routing them
		over multiple interconnection networks. It's at this layer that an IP
		address is defined."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"In the context of the TCP/IP model, what is the concern of the Host-to-Host layer?"},
        {"a", @"The host-to-host layer provides two protocols, TCP and UDP.
		These protocols address conerns such as data order, data segmentation,
		network congestions, and error correction."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"In the context of the TCP/IP model, what is the concern of the Process/Application layer?"},
        {"a", @"The process/application layer is where protocols such as HTTP, SMTP, and FTP are
		implemented. This layer consumes fucntionality provided by our operating system's
		implementation of the lower layers."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"What is the difference between IPv4 and IPv6 (address size specifically)?"},
        {"a", @"IPv4 uses 32-bit addresses, IPv6 uses 128-bit addresses."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"i)  Why is it important to have network which supports IPv4?
		ii) What is the term for operation system support for both IPv4 and IPv6?"},
        {"a", @"i)  Because you risk a significant portion of your users not being
		able to connect.
		ii) Dual-stack configuration."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"Describe the structure of an IPv4 address."},
        {"a", @"An IPv4 address has the following characteristics:
			- IPv4 addresses are 32 bits long
			- They are commonly divided (dot-delimited) by four 8-bit sections
			- Each section is displayed as a decimal number between 0 and 255
				inclusive.

		Examples include:
			0.0.0.0
			127.0.0.1
			255.255.254.123"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"i)  What is the loopback address?
		ii) Give the IPv4 address representation of what it is reserved for."},
        {"a", @"i)  The loopback address means 'establish a connection to myself'.
		ii) 127.0.0.1"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"TOLEARN: Classless Inter-Domain Routing (CIDR)"},
        {"a", @""},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"Describe the structure of an IPv6 address."},
        {"a", @"- IPv6 addresses are 128 bits long.
		- They are written as eight groups of four hexadecimal characters delineated
			by colons.

		NB: The standard is to use lowercase hexadecimal letters in IPv6 addresses."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"What is the utility command in Windows which lists the routers between
		your system and the destination system?"},
        {"a", @"tracert.

		Usage:
			tracert <website>"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"i)  What are Local Area Networks (LANs)?
		ii) When a packet originates from a device on an LAN, what must
			the packet undergo before being routed on the internet?"},
        {"a", @"i)  Local area networks are IPv4 address ranges reserved for use in
			small local networks (such as households and organizations).

		ii) The packet must undergo Network Address Translation (NAT) before
			being routed on the internet.

			NB: A router that implements NAT remembers which local address a
				connection is established from."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"What does NAT (Network Address Translation) entail?"},
        {"a", @"When an IP packet comes from a local area network (LAN) meant for the
		internet. The Router modifies the source IP address from the original
		private LAN IP address to its own public internet IP address.

		Likewise, when the router receives the return communication, it must
		modify the destination address from its public IP to the private IP
		of the original sender."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"What is meant by:
			1) Unicast addressing
			2) Broadcast addressing
			3) Multicast addressing
			4) Anycast addressing"},
        {"a", @"1) Unicast addressing:
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
				  to handle your request."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"Why would implementing the use of IP multicasting on your local
		network be worthwhile, as opposed to sending the same unicast message
		multiple times?"},
        {"a", @"Because it conserves bandwidth."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"What is a high-level overview of a socket?"},
        {"a", @"A socket is an abstraction that represents one endpoint of a communication link
		between systems."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {29, new Dictionary<string, string>() {
        {"q", @"How is a socket defined?"},
        {"a", @"An open socket is uniquely defined by a 5-tuple consisting of the following:
			1) Local IP address
			2) Local/Ephemeral port
			3) Remote IP address
			4) Remote port
			5) Protocol (UDP or TCP)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {30, new Dictionary<string, string>() {
        {"q", @"What is one difference between Winsock socket and a Berkeley socket?"},
        {"a", @"Winsock requires initialization before use and a cleanup function call when
		we are finished.

		These initialization and cleanup steps are not used with Berkeley sockets.
		Berkley socket API is always ready to use."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {31, new Dictionary<string, string>() {
        {"q", @"i)  What are the two basic socket types?
		ii) Which of TCP or UDP correspond to which type as per your answer to (i)"},
        {"a", @"i)  (1) Connection-oriented  (2) Connectionless
		ii) TCP is a connection-oriented protocol, UDP is a connectionless protocol."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {32, new Dictionary<string, string>() {
        {"q", @"What does a connectionless protocol, such as UDP, entail?"},
        {"a", @"In a connectionless protocol, such as UDP, each data packet is addressed individually.
		From the protocol's perspective, each data packet is completely independent and unrelated
		to any packets coming before or after it."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {33, new Dictionary<string, string>() {
        {"q", @"What does a connection-oriented protocol, such as TCP, entail?"},
        {"a", @"In a connection-oriented protocol we:
			1) Guarantee that data arrives in the same order it is sent.
			2) Prevent duplicate data from arriving twice
			3) Retry sending missing data
			4) Notify when a connection is terminated
			5) Run algorithms to mitigate network congestion"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {34, new Dictionary<string, string>() {
        {"q", @"i)  Name a use case where UDP has an advantage over TCP
		ii) What implications does your answer to (i) have on IP broadcast or multicast."},
        {"a", @"i)  UDP has the advantage in cases where you want to send a message without expecting
			a response from the other end.
		
		ii) This makes it useful when using IP broadcast or multicast. TCP, on the other hand,
			requires bidirectional communication to provide its guarantees and so
			does not work with IP multicast or broadcast."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {35, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) socket()
			2) bind()
			3) listen()"},
        {"a", @"1) socket() - creates and initializes a new socket
			2) bind() - associates a socket with a particular local IP address and port number
			3) listen() - is used on the server to cause a TCP socket to listen for new connections"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {36, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) connect()
			2) accept()
			3) send()
			4) recv()"},
        {"a", @"1) connect() - is used on the client to set the remote address and port.
				In the case of TCP, it also establishes a connection.
			2) accept() - is used on the server to create a new socket for an incoming
				TCP connection.
			3) send() - used to send data with a socket
			4) recv() - sued to receive data with a socket."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {37, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) sento()
			2) recvfrom()"},
        {"a", @"1) sento() -
				is used to send data from sockets without a bound remote address.
			2) recvfrom() - 
				is used to receive data from sockets without a bound remote address."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {38, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) close()
			2) closesocket()
			3) shutdown()"},
        {"a", @"1) close()
				-  applies to Berkeley sockets
			2) closesocket()
				- applies to Winsock sockets.
				
		Both (1) and (2) are used to close a socket. In the case of TCP,
		this also terminates the connection.

			3) shutdown()
				- is used to close one side of a TCP connection. It is useful
				to ensure an orderly connection teardown."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {39, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) select()
			2) getnameinfo()
			3) getaddrinfo()"},
        {"a", @"1) select()
				- is used to wait for an event on one or more sockets.
			2) getnameinfo()
				- provides a protocol-independent manner of working with hostnames
			3) getaddrinfo()
				- provides a protocol-independent manner of working with addresses"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {40, new Dictionary<string, string>() {
        {"q", @"Explain the usage of the following socket functions:
			1) setsockopt()
			2) fcntl()
			3) ioctlsocket()"},
        {"a", @"1) setsockopt()
				- used to set socket options
			2) fcntl()
				- Berkely sockets only
				- used to get and set some options
			3) ioctlsocket()
				- Winsock sockets only
				- used to get and set some options"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {41, new Dictionary<string, string>() {
        {"q", @"When could a TCP client to call `bind()` before `connect`?"},
        {"a", @"If the TCP client is particular about which network interface is
		being used to connect with."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {42, new Dictionary<string, string>() {
        {"q", @"i)  In UNIX, how is a socket descriptor represented?
		ii) What implications does your answer to (i) have on function usage on UNIX sockets?"},
        {"a", @"i)  In UNIX, a socket descriptor is represented by a standard file descriptor.
		ii) This means that, as opposed to Windows, you can use any of the standard UNIX I/O
			functions on sockets."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {43, new Dictionary<string, string>() {
        {"q", @"What are UNIX file descriptors?"},
        {"a", @"All UNIX file descriptors are small, non-negative integers."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {44, new Dictionary<string, string>() {
        {"q", @"What does a call to `socket()` return if it fails in the:
			i)  UNIX platform
			ii) Windows"},
        {"a", @"i)  negative number
			ii) `INVALID_SOCKET`"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {45, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			char request[1024];
			int bytes_received = recv(socket_client, request, 1024, 0);
			printf(""Received %.*s bytes.
"", bytes_received, request);

		Why is important to use the format specifier %.*s instead of for example:
			printf(""Received %s bytes.
"", request);"},
        {"a", @"Because there is no guarantee that the data that's received from `recv()`
		is null terminated.

		In the alternative case, you will likely receive a segmentation fault error
		(or at best garbage output)."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {46, new Dictionary<string, string>() {
        {"q", @"What is 'inetd'?"},
        {"a", @"inetd is a service on UNIX-like systems which can be used to turn
		console-like applications into networked ones.

		You can configure inetd (on /etc/inetd.conf) with your program's:
			1) location
			2) port number
			3) protocol (TCP or UDP)
			4) the user your want it to run as

		inetd will then listen for connections on your desired port."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}
