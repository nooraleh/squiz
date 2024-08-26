# Notes taken in a Q & A style format from Stefan Bjornander's 'Microsoft Visual C++ Windows Applications by Examples'
qna = {
    1: {
		'q':  """
		Consider the following snippet:

			int n = 1;
			int main(void)
			{
				int n = 2;
				<BLANK>
				return 0;
			}

		Fill in the blank to cout the global variable `n` as well as
		the local variable `n`
		""",
		'a': """
		ANS:
			std::cout << std::format("global: { }, local: { }", ::n, n);

		Note the use of the scope resolution operator for the global variable.
		""",
	},
    2: {
		'q':  """
		Consider the following snippet:

			void KeepCount()
			{
				static int iCount = 0; // line of interest
				++iCount;
				cout << "This function has been called " << iCount
				<< "times." << endl;
			}

		Select the true statement:
			1) A static local variable is initialized when the function is called
			2) A static local variable is initialized when the execution of the program starts
		""",
		'a': """
			2) Is the true statement
		""",
	},
    3: { # Chapter 3: Windows development
		'q':  """
		What is the purpose of an Application Wizard?
		""",
		'a': """
		An Application Wizard designs the skeleton application code for use to
		then add our application-specific code on to.
		""",
	},
    4: {
		'q':  """
		What can we do with the Win32 API?
		""",
		'a': """
		With the Win32 API, it is possible to totally control the Windows
		operating system.
		""",
	},
    5: {
		'q':  """
		What is main reason for the existence of Microsoft Foundation Classes (MFC)?
		""",
		'a': """
		MFC is a large C++ class library containing many classes encapsulating
		the functionality of Win32 API.
		""",
	},
    6: {
		'q':  """
		What is `CWnd`?
		""",
		'a': """
		`CWnd` is the Windows main class.
		""",
	},
    7: {
		'q':  """
		In an MFC environment, the function `main` is embedded in
		the framework.

		Example how an MFC application is launched?
		""",
		'a': """
		In an MFC environment, there is the object `theApp` - which
		is an instance of the application class. The application is
		launched by the constructor of `theApp`.
		""",
	},
    8: {
		'q':  """
		BOOL with the values of TRUE or FALSE was introduced before
		there was a standard logical type in C++.

		True or false:
			We must continue to use BOOL when dealing with MFC method
			calls despite standard `bool` currently existing.
		""",
		'a': """
		True
		""",
	},
    9: {
		'q':  """
		True or false:

		1) All generated framework classes have a capital C at the beginning
			of the name.
		2) As a best practice, therefore, the classes we write ourselves
			should have a capital C as well.
		""",
		'a': """
		1) True
		2) False
		""",
	},
    10: {
		'q':  """
		By default, the MFC Application Wizard creates an application
		skeleton with two classes:
			1) State these two classes
			2) Explain each of the classes' purpose
		""",
		'a': """
			1) Document class, View class

			2) Document class:
				a) Stores the data
				b) Manages printing the data
				c) Coordinates updating multiple views of the data
			
			  View class:
			  	a) Displays the data
				b) Manages user interaction with the data - including selection and editing
		""",
	},
	11: {
		'q':  """
		Give a detailed reason as to why the document/view model should be followed?
		""",
		'a': """
		A good reason is when you need multiple views of the same document, such as
		both a spreadsheet and a chart view (of the same data).

		The document/view model would allow in this case:
			1) a dedicated view object to handle the spreadsheet
			2) a dedicated view object to handle the chart
			
		While code common to all views (e.g. a calculation engine) may reside
		in the document object. The document takes on the task of updating all views
		when the underling data changes.
		""",
	},
	12: {
		'q':  """
		Select the correct statement:

		In an MFC application, there is:

			1) Exactly one document object, but there may be one or 
				more view objects, or none at all.
			2) Exactly one view object, but there may be one or 
				more view objects, or none at all.
		""",
		'a': """
		
		""",
	},
}