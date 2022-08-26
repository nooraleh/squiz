# Notes taken in a QNA style from John Paul Mueller's 'C# All-in-One for Dummies'

qna = {
    1: { # Chapter 8: Delegating those events
		'q':  """
		You can divide delegates used specifically as function pointers
        into three types using three special keywords.

            1) What are these three keywords
            2) Outline an overview of each delegate type in your answer to (1)
		""",
		'a': """
            1) Action:
                i) Has one or more input parameters and no output parameters
            2) Func:
                - Has zero or more input parameters and one return parameter
            3) Predicate
                - Defines a specific set of criteria and determines whether the input
                    object meets those criteria.
                - Returns True when the conditions are met and False otherwise.
		""",
	},
    2: {
		'q':  """
		Consider the snippet (Form1.cs):
            public partial class Form1 : Form 

        What does the keyword `partial` mean?
		""",
		'a': """
		The partial keyword indicates that this file is only part of the full class.
        The rest can be found in, for example, a file called 'Form1.Designer.cs'
		""",
	},
    3: {
		'q':  """
		Consider the following snippet:
            delegate void UpdateProgressCallback();
            UpdateProgressCallback anon = delegate ()
            {
                // progressBar1.PerformStep();
            };
            if (anon != null) anon();

        i) What are the hidden costs of using an anonymous function?
        ii) Which keyword can you use to prevent these costs and why?
		""",
		'a': """
        i)
            1) Overhead for the delegate invocation
            2) Heap allocations for each of the argument
            3) Heap allocations for the enclosing method created by the lambda expression
        ii)
            - Since C# 9.0 onwards allows the use of static keywords
            - which disallows the capture of locals or instane state from containing scope
            - we can, therefore, reduce or eliminate any unintended allocations functions.
		""",
	},
    4: {
		'q':  """
		Consider the following two lines:
            var handler = (object Obj, EventArgs Args) => ShowDialog(); (1)
            var handler = (object _, EventArgs _) => ShowDialog(); (2)

        i)  What is the term for the underscores in (2)
        ii) What does you answer to (i) indicate to the compiler and readers?
		""",
		'a': """
		i)  Discard parameters
        ii) That you don't intend on using those parameters
		""",
	},
    5: {
		'q':  """
		In C#, when you have a class on which interesting events arise, how can you advertise
        the availability of notifications to any classes that may have an interest in knowing
        about such events?
		""",
		'a': """
		By providing a delegate and a coresponding event.
		""",
	},
    6: {
		'q':  """
		What are the two event-related delegate types for .NET handles for you?
		""",
		'a': """
            1) EventHandler
            2) EventHandler<TEventArgs>
		""",
	},
    7: {
		'q':  """
		When should you use each of the following:
            1) Events
            2) Delegates
            3) Lambdas
		""",
		'a': """
        1) Events:
            - When you have multiple subscribers, or;
            - When communicating with client software that uses your classes.

        2) Delegates:
            - Use delegates or anonymous functions when you need a 
              callback or need to customize an operation.

        3) Lambdas:
            - Can be used instead of anomymous methods
            - Lambdas are simply a short way to specify the method you're passing 
              to a delegate.
		""",
	},
    8: { # Chapter 9: Can I use your namespace in the library?
		'q':  """
		i)  What is a project file?
        ii) What are the extensions for 
            a) C# project files
            b) C++ project files
        iii) What is the term for a set of project files?
		""",
		'a': """
		i)  A project file contains the instructions about which files 
            should be used together and how they're combined.
        ii)
            a) .csproj
            b) .vcxproj

        iii) A solution (.sln)
		""",
	},
    9: {
		'q':  """
		i)  C# 10.0 introduced the `global using` statement. Outline its usage.
        ii) Other than C# 10.0, what other requirements are they to enable the usage of
            `global using`?
		""",
		'a': """
        i)
            The idea is that you place these `global using` statements into a 
            separate file, where they're easy to find and manage, and that they
            affect your entire project.
        ii)
            1) .NET core application.
            2) select .NET 6.0 as the application. 
		""",
	},
    10: {
		'q':  """
		Fill in the blank:
            In visual studio and other .NET languages, one project equals one compile
            module otherwise known as an <_____> in .NET.
		""",
		'a': """
		Assembly

        NB: The words 'assembly' and 'module' have different technical meanings,
            despite being used interchangeable in software parlance.
		""",
	},
	11: {
		'q':  """
		What are the two basic assembly types that c# can produce?
		""",
		'a': """
		1) Executable (.exe)
        2) Class library (.dll)
		""",
	},
	12: {
		'q':  """
		i)  What does CLR stand for?
        ii) What the CLR do?
		""",
		'a': """
		i)  Common language runtime
        ii) 
        The common language runtime:
            - runs c# programs
            - loads library assemblies (.dll's) into memory as needed
		""",
	},
	13: {
		'q':  """
		i)  Before becoming a .dll or a .exe, what does C# compile your source into?
        iI) What is one benefit of your answer to (i)
		""",
		'a': """
		i)  C# compiles your source code into Common Intermediate Language (also [C]IL)
        ii) CIL can be used to interact with other programming languages, for example C++.
		""",
	},
	14: {
		'q':  """
		Consider an executable with takes arguments such as files from the command line.
        What is an alternative approach to running an .exe via the command line?
		""",
		'a': """
		Simply drag the file into the .exe from Windows File Explorer.
		""",
	},
	15: {
		'q':  """
		If you have a Visual Studio solution which contains more than .exe project,
        what must you do?
		""",
		'a': """
		You must specify to Visual Studio which .exe project is the 'startup project' i.e
        the one which runs from the Debug menu.
		""",
	},
	16: {
		'q':  """
		What distinguishing a project that compiles to a .exe (executable) or to
        a .dll (class library)?
		""",
		'a': """
		The presence of a `Main()` method.
		""",
	},
	17: {
		'q':  """
		What is the most private access modifier that you should use
        when the intent is to access the code from outside the assembly?
		""",
		'a': """
		public
		""",
	},
	18: {
		'q':  """
		i)  How should you approach exceptions in class library code.
        ii) Explain the reasoning behind your answer to (i)
		""",
		'a': """
        i)
            Normally, you shouldn't try to catch exceptions.
            Allow them to bubble up from the library to the client code that's
            calling the library.

        ii)
            Rationale: Clients need to know about the exceptions and handle
            them in their own ways.
		""",
	},
	19: {
		'q':  """
		State two benefits of using namespaces?
		""",
		'a': """
		1) Putting related classes in one scope.
        2) Reducing collision between names and used in different places.
		""",
	},
	20: {
		'q':  """
		True or false:
            A namespace cannot span multiple assemblies.
		""",
		'a': """
		False. A namespace CAN multiple assemblies.
		""",
	},
	21: {
		'q':  """
		What happens if your classes are not wrapped in a namespace?
		""",
		'a': """
		C# puts the in the 'global namespace', which is the base (unnamed)
        namespace for all other namespaces.
		""",
	},
	22: {
		'q':  """
		Fill in the blank:

            Namespaces are implicitly <access_specifier_here>
		""",
		'a': """
		public
		""",
	},
	23: {
		'q':  """
		Besides classes, state four other types that namspaces can contain.
		""",
		'a': """
        1) delegate
        2) enum
        3) interface
        4) struct
		""",
	},
	24: {
		'q':  """
		True or false:
            Prefixing all namespaces in a program with your company name is conventional.
            E.g. MyCompany.MathRoutines (<- this is a single (dotted ) namespace name, not a
            nested namespace).
		""",
		'a': """
		True
		""",
	},
	25: {
		'q':  """
		Consider the following snippet:

            namespace NotFileScopeNameSpace
            {
                class Program
                {
                    static void Main(string[] args)
                    {
                        // ....
                    }
                }
            }

        i)  Rewrite the snippet using C# 10.0's new 'file-scoped' namespace syntax. 

        ii) What is one benefit of using file-scoped namespace syntax?
		""",
		'a': """
        i) 
            namespace FileScopeNameSpace;
            class Program
            {
                static void Main(string[] args)
                {
                    // ....
                }
            }

        N.B: FileScopeNameSpace now applies to the entire file.

        ii) Reduction of horizontal waste.
		""",
	},
	26: {
		'q':  """
		i)  What does the `new` modifier keyword do?
        ii) Give a snippet example to illustrate your answer to (i)
		""",
		'a': """
		i)  The `new` keyword explicitly hides a member that is inherited
            from a base class.
        ii)
        Snippet:
                public class Base
                {
                    public void Invoke() { }
                }

                public class Derived : Base
                {
                    new public void Invoke() { }
                }
		""",
	},
	27: {
		'q':  """
		What does a partial method do?
		""",
		'a': """
		A partial method allows you to split a method into a signature part
        and potentially an implementation part.
		""",
	},
	28: { # Chapter 10 - Improving Productivity with Named and Optional Parameters
		'q':  """
		i)  What are optional parameters in C#?
        ii) Let:
                - `func` be a public static method which returns void
                - `param1` be a non-optional parameter of type string
                - `param2` be an optional parameter of type int

            Use the above information to outline to usage of optional parameters
		""",
		'a': """
		i)  Optional parameters are parameters that have a default value right in
            the method signature.

        ii) Snippet:
                public static void func(string param1, int param2 = 2) { /*...*/ }
		""",
	},
	29: {
		'q':  """
		What is the `sealed` modifier keyword used for?
		""",
		'a': """
		The `sealed` keyword is used to stop inheriting the particular class from
		other classes. It is essentially `final` in C++. 
		""",
	},
	30: {
		'q':  """
		What does the `in` parameter modifier do?
		""",
		'a': """
		The `in` keyword:
			- causes arguments to be passed in by reference but ensures the
			  argument is not modified.
		""",
	},
	31: {
		'q':  """
		Consider the following snippet:

			public static int addit(int z, int y, int x = 0, int w = 0, int v = 0)
			{
				return z + y + x + w + v;
			}

		In the context of named parameters, call the function `addit` with:
			1) parameter z being passed an argument of 3
			2) parameter y being passed an argument of 7
			3) parameter v being passed an argument of 4
		""",
		'a': """
		int answer = addit(z: 3, y: 7, v: 4);
		""",
	},
	32: {
		'q':  """
		i)  What are output parameters?
		ii) Which parameter modifier do we use to specify output parameters?
		""",
		'a': """
		i)  Output parameters are parameters in the method signature that actually
			change the value of the variable that is passed into them by the user.
		ii) `out`
		""",
	},
	33: {
		'q':  """
		i)  What does the `nameof` expression do?
		ii) Give a simple example of its usage.
		""",
		'a': """
		i)  The nameof expression produces the name of a variable, type, or member
			as a string constant.
		ii)
		Snippet:
			int p = 2;
			Console.WriteLine(nameof(p)); // output will be: p
		""",
	},
	34: {
		'q':  """
		i)   State the character used for the verbatim identifier.
		ii)  State three ways the verbatim identifier can be uses.
		""",
		'a': """
		i)  @
		ii) 
		Usage:
			1) To enable C# keywords to be used as identifiers.
				e.g 'string[] @for = {"Jack", "Jill"}' 
			2) To enable a string to be interpreted verbatim, similar to a raw string
				in other languages where special characters are escaped.
			3) To enable the compiler to distinguish between attributes in cases
				of naming conflict.
		""",
	},
	35: {
		'q':  """
		Give the:
			a) syntax
			b) usage
			c) C# version in which it was/will be released
		For the:
			1) The 'null-forgiving' operator
			2) 'Parameter null checking'
		""",
		'a': """
		1)
			a) !
			b)
				public static void Main()
				{
					Person? p = Find("John");
					if (IsValid(p))
					{
						Console.WriteLine($"Found {p!.Name}");
					}
				}
			c) 10.0

		2)
			a) !!
			b) 
				static void SayHello(String name!!)
				{
					Console.WriteLine($"Hello {Name}!");
				}
			c) 11.0
		""",
	},
	36: { # Chapter 11 - Interacting with Structures
		'q':  """
		What is the keyword used to create a structure?
		""",
		'a': """
		struct
		""",
	},
	37: {
		'q':  """
		State which of the following are reference types or value types:

			1) classes
			2) structures
		""",
		'a': """
			1) reference type
			2) value type
		""",
	},
	38: {
		'q':  """
		True or false:
			a) Structures can inherit from other structures or classes.
			b) Structures can have constructors
			c) Structures can have destructors
			d) Can be defined as abstract
			e) Cannot be defined as virtual
			f) Cannot be protected
		""",
		'a': """
		a) False
		b) True
		c) False
		d) False
		e) True
		f) True
		""",
	},
	39: {
		'q':  """
		Why does an array of references incur a larger penalty in resource use/
		allocation time/deallocation time than an array of values?
		""",
		'a': """
		Because an array of references contains just pointers to the individual objects.
		To access the object, the application must then look for it on the heap.

		Values types undergo deterministic destruction at the moment they go out of scope.
		Waiting for C# to garbage-collect reference types means that you can't be sure
		how memory is used in your application.
		""",
	},
	40: {
		'q':  """
		What is a best practice for structure members? Explain the rationale.
		""",
		'a': """
		Best practice: Keep structures limited to other value types such as `int` and `double` where possible,
		Rationale: Reference members reduce the impact of any resources and time savings that a structure can
					provide (as they'll need to be garbage-collected).
		""",
	},
	41: {
		'q':  """
		Consider the following struct:
				public struct Message2
				{
					public Message2(int msgID, int productId = 22, int quantity = 5)
					{
						MsgID = msgID;
						ProductID = productId;
						Quantity = quantity;

						if (ProductID == 22)
							Price = CalculatePrice(5.99, Quantity);     <-- line of interest (1)
						else
							Price = CalculatePrice(6.99, Quantity);
					}

					public int MsgID; public int ProductID; public int Quantity; public double Price;

					public static double CalculatePrice(double singlePrice, int quantity) <-- line of interest (2)
					{
						return singlePrice * quantity;
					}
				}

		Question: Why must the signature in (2) be declared static?		
		""",
		'a': """
		The compiler error would be:
			The 'this' object cannot be used before all of its fields are assigned to

		All the fields in a struct have to be assigned by the constructor before the constructor
		can call an instance method, which essentially is a method which takes the argument `this`
		under-the-hood.

		We need a method which isn't bound to the instance i.e. a static method.
		""",
	},
	42: {
		'q':  """
		What are two benefits of using read-only structures?
		""",
		'a': """
		1)  Performance
		2)  Thread safety
		""",
	},
	43: {
		'q':  """
		Consider the following snippet:

			public readonly struct ReadOnlyData
			{
				public readonly int Value { get; } // (1)

				public ReadOnlyData(int n)
				{
					Value = n;
				}
			}

		Q: Modify line (1) and initialize an `ReadOnlyData` with C# 9.0's
		'init accessor', assigning `Value` to 12.
		""",
		'a': """
			public readonly struct ReadOnlyData
			{
				public readonly int Value { get; init;} // <- modification

				public ReadOnlyData(int n)
				{
					Value = n;
				}
			}

			public static void Main(string[] args)
			{
				ReadOnlyData rod = new ReadOnlyData
				{
					Value = 12;
				}
			}
		""",
	},
	44: {
		'q':  """
		State as many limitations of using a reference structure as you can.
		""",
		'a': """
		1) No array element support
		2) Unable to declare it as a type of a field of a class or a non-ref struct
		3) No interface implementation
		4) No boxing to System.ValueType or System.Object
		5) Unable to use it as a type argument
		6) Ineligible for capture by a lambda expression or a local function
		7) Inaccessible in an async method
		8) No iterator support
		""",
	},
	45: {
		'q':  """
		What is the main readon to work with structures in most cases?
		""",
		'a': """
		To create records that contain custom data. You use these
		custom data records to hold complex information and pass it around
		as needed within your application.
		""",
	},
	46: {
		'q':  """
		True or false:

			It's always better to restriction groupings of data records encapsulated
			in structures to arrays (as opposed to C# collections) in your application when
			speed is the most important concern.
		""",
		'a': """
		True
		""",
	},
	47: {
		'q':  """
		Outline some of the features of the `record` type.
		""",
		'a': """
		1) Ability to define immutable properties
		2) Use of value equality i.e to records residing in distinct memory
			locations yet have the same properties are considered equal.
		3) Non-destructive mutation (using the `with` keyword)
		4) Human-readable 'ToString' method
		""",
	},
	48: {
		'q':  """
		Consider the following snippet:

			public record NamedPoint(string Name, int X, int Y); // positional declaration
			var p1 = new NamedPoint("A", 0, 0);

		Write a line to instantiate a `NamedPoint` called `p2` with:
			- `Name` assigned a value of "C",
			- `Y` assigned a value of 4

		""",
		'a': """
		p2 = p1 with
			{
				Name = "C",
				Y = 4
			};
		""",
	},
	49: {
		'q':  """
		As you know, `record` types use value equality as opposed to reference equality.
		Let:
			- record1 be a record type
			- record2 be the same record type
			- record1 == record2 yields true

		Use a function to determine whether record1 and record2 are equal in reference.
		I.e. the two objects point to the same location in memory.
		""",
		'a': """
		ReferenceEquals(record1, record2);		
		""",
	},
	50: {
		'q':  """
		a) What is a backing field (a.k.a backing store)?
		b) Give an example of its usage
		""",
		'a': """
		a) A backing field is a private field that stores the data exposed
			by a public property.

		b) Anything only the lines of:

				private int m_Capacity;

				public int Capacity
				{
					get { return m_Capacity > 0 ? m_Capacity : -666; }
					set { m_Capacity = value; }
				}
		""",
	},
	51: {
		'q':  """
		Consider the following snippet:

			public class record Person
			{
				// ...
				private string department; // (backing field) (1)
				public string Department {get {return department;}; set {department = value.ToUpper();}}
			}

		Use C# 10.0 `field` keyword to eliminate the use of the backing field in (1).		
		""",
		'a': """
			public class record Person
			{
				// ...
				public string Department {get; set => field = value.ToUpper();}
			}
		""",
	}, # Book 3: Designing for C#
	52: { # Chapter 1: Writing Secure Code
		'q':  """
		Give a brief outline of the meaning of the terms:
			1) authentication
			2) authorisation
		""",
		'a': """
		Authentication:
			- Making sure the user is authentic
		Authorisation:
			- the act of ensure that a user has the authority to perform
				specific tasks.
		""",
	},
	53: {
		'q':  """
		In the context of threat modelling:
			What does the acronym STRIDE stand for?
		""",
		'a': """
		S: Spoofing data
			- users pretend to be someone they are not
		T: Tampering with data or files
			- users edit something that shouldn't be edited
		R: Repudiation of action
			- users have the opportunity to say they didn't do something that they actually did do
		I: Information disclosure
			- users see something that shouldn't be seen
		D: Denial of service
			- users prevent legitimate users from accessing the system
		E: Elevation of privilege
			- users get access to something that they shouldn't have access to
		""",
	},
	54: { # Book 3, Chapter 2: Accessing Data
		'q':  """
		What is the primary role of the System.Data namespace?
		""",
		'a': """
		Getting information out of and into a database.
		""",
	},
	55: {
		'q':  """
		i)  What does LINQ stand for?
		ii) What does LINQ enable you to do?
		""",
		'a': """
		i)  LINQ stands for 'language integrated query'
		ii) Enables you to get data out of the data containers in a less complicated
			way than object-oriented language.
		""",
	},
	56: {
		'q':  """
		What is the black box problem?
		""",
		'a': """
		The black box problem is that of having a development environment
		do some things for you over which you have no control.
		""",
	},
	57: {
		'q':  """
		Give a brief overview of the following C# data containers:
			1) DataSet
			2) DataTable
			3) DataRow
			4) DataView
			5) DataReader
		""",
		'a': """
		1) DataSet:
			- the in-memory representation of an entire database
		2) DataTable
			- a single table of data stored in memory
			- `DataSet` containers are composed of `DataTable` containers
		3) DataRow
			- a row in a `DataTable` container
		4) DataView
			- a copy of a `DataTable` that you can use to sort and filter data
			  for viewing purposes
		5) DataReader
			- A read-only, forward-only stream of data used for one-time processes.
		""",
	},
	58: {
		'q':  """
		There are two SQL Server database files, for each:
			a) Name the extension and name
			b) State the purpose of the file
		""",
		'a': """
			1)
				a) .mdf, 'master database file'
				b) Contains the schema and the data

			2) 
				a) .ldf, 'log database file'
				b) Contains the logs (of db transactions, DDL, changed made by stored procs etc)
		""",
	},
	59: {
		'q':  """
		True or false:
			Enterprise customers define a specific data code format and expect their
			software developers to use that, rather than visual tools which is purposely generic
			in order to support anything that anyone might want to do it.
		""",
		'a': """
		True.
		""",
	},
	60: { # Book 3, Chapter 3: Fishing the File Stream
		'q':  """
		What are the two kinds of output that programs can generate?
		""",
		'a': """
		1) Binary
		2) Text-based
		""",
	},
	61: {
		'q':  """
		Explain the purpose of the following file modes:

			1) FileMode.CreateNew
			2) FileMode.Append
			3) FileMode.Create
		""",
		'a': """
			1) FileMode.CreateNew
				- Create a file if it doesn't exist or throw an exception if the file exists

			2) FileMode.Append
				- Append to an existing file or create a new file if it doesn't exist

			3) FileMode.Create
				- Create a new file or truncate an existing file
		""",
	},
	62: {
		'q':  """
		State the three FileAccess possibilities:
		""",
		'a': """
		1) FileAccess.Read
		2) FileAccess.Write
		3) FileAccess.ReadWrite
		""",
	},
	63: {
		'q':  """
		1) True or false:
				It's good programming practice to null a reference after it becomes
				invalid so that you won't try to use it again.
		
		2) What could happen if you do not follow this guideline?

		3) Give an example of the reference 'invalidation' described in (1)

		""",
		'a': """
		1) True
		2) Runtime exception
		3) Examples include:
				1) Calling .Close() on a Stream/FileWriter
		""",
	},
	64: {
		'q':  """
		1) What is the usual way to do stream writing in C#

			Hint: The answer has parallels with Python's `with` context manager.
		""",
		'a': """
		1) The usual way is with a `using` statement.

			E.g.

				using (StreamWriter sw = new StreamWriter(fs))
				{
					// use the resource
				}
		""",
	},
	65: {
		'q':  """
		Consider the following template for `using` resource management idiom:
				using (<initial_some_resource_or_resources>)
				{
					// use the resource
				}

		True or False:
			The resources acquired in the parenthesis can be of different types.

		""",
		'a': """
		False
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