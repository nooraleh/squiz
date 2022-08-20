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