# Notes taken in a QNA style from Joe Fawcett's 'Beginning XML'

qna = {
    1: { # Chapter 1 - Introduction to XML/What is XML?
		'q':  """
		What does XML stand for?
		""",
		'a': """
		Extensible Markup Language.
		""",
	},
    2: {
		'q':  """
		Consider the following snippet:

			<?xml version="1.0" ?>
				<book>
					<title>C# and XML: A Primer</title>
					<author>Jon Hartwell</author>
				</book>

		a) What is the term for '<?xml version="1.0" ?>'?
		b) Why is your answer to (a) necessary?
		""",
		'a': """
		a) XML declaration
		b) It is necessary for certain parsers to be able to identify when
			a document is XML.		
		""",
	},
    3: {
		'q':  """
		Consider the following snippet:

			<?xml version="1.0" ?>
				<book>
					<title>C# and XML: A Primer</title>
					<author>Jon Hartwell</author>
				</book>

		How could you condense the information in this snippet
		using attributes and a single <book> tag.
		""",
		'a': """
		<?xml version="1.0" ?>
		<book title="C# and XML: A Primer" author="Jon Hartwell">
		""",
	},
    4: {
		'q':  """
		Outline the usage difference between XML tags and HTML tags.
		""",
		'a': """
		XML tags:
			- Identify the data and are used to store and organize the data
		HTML tags:
			- Specify how to display data
		""",
	},
    5: {
		'q':  """
		Consider the following snippet:
			<?xml version = "1.0"?>
			<contact-info>
				<name>John Doe</name>
				<company>RandomCompany</company>
				<phone>(011) 123-4567</phone>
			</contact-info>

		Identify all the elements in this snippet.
		""",
		'a': """
		Element 1:
			<contact-info>
				<name>John Doe</name>
				<company>RandomCompany</company>
				<phone>(011) 123-4567</phone>
			</contact-info>

		Element 2:
			<name>John Doe</name>

		Element 3:
			<company>RandomCompany</company>

		Element 4:
			<phone>(011) 123-4567</phone>
		""",
	},
    6: {
		'q':  """
		True or false:

			An XML document can have only one root element.
		""",
		'a': """
		True
		""",
	},
    7: {
		'q':  """
		Are XML elements case-insensitive? I.e would this snippet be well-formed XML:
			<root>
   				<x>...</X>
   				<Y>...</y>
			</Root>
		""",
		'a': """
		No, XML elements are actually case-insensitive so the given snippet is not well-formed
		XML.
		""",
	},
    8: {
		'q':  """
		a) What does an XML attribute represent?
		b) How many attributes can be associated with a given XML element
		""",
		'a': """
		a) An XML attribute of specifies a single property for the element, using a name/value pair.
		b) 0..N
		""",
	},
    9: {
		'q':  """
		Consider the following snippet:

			<elementExample attributeName1="x" attributeName2= "y" attributeName1= "z">....</elementExample>

		Identify and explain what is wrong with this snippet.
		""",
		'a': """
		Attribute 'attributeName1' is specified twice with two different values.
		This is illegal XML.
		""",
	},
    10: {
		'q':  """
		True or false:
			1) Attribute names are defined without quotation marks
			2) Attribute values do not have be defined with quotation marks  
		""",
		'a': """
			1) True
			2) False, attribute values must always be defined with quotation marks.
		""",
	},
	11: {
		'q':  """
		For each of the given characters, state their corresponding entity
		reference:
			a) <
			b) >
			c) &
			d) '
			e) "
		""",
		'a': """
			a) &lt;
			b) &gt;
			c) &amp;
			d) &apos;
			e) &quot;
		""",
	},
	12: {
		'q':  """
		Consider the following XML Prolog:
			<?xml version = "version_number" encoding = "encoding_declaration" standalone = "standalone_status" ?>

		Explain the usage of each of the following attribute names:
			- version
			- encoding
			- standalone
		""",
		'a': """
		Version:
			- Specifies the version of the XML standard to use
			- E.g "1.0"

		Encoding:
			- Defines the character encoding used in the document
			- UTF-8 is the default encoding

		Standalone:
			- Informs the parser whether the document relies on information
			  from an external source for its content
			- E.g Document type definition 'DTD'
			- Default value is set to 'no'
		""",
	},
	13: {
		'q':  """
		What is the formal term for the text that appears between the start and end
		tags?

		E.g:
			<tag>what_am_i</tag>
		""",
		'a': """
		The formal term is 'content'.
		""",
	},
	14: {
		'q':  """
		Consider the following snippet of an element with no content i.e is empty:
				<exampleTag></exampleTag>

		a) Simplify the snippet.
		b) What is the formal term for your answer to (a)?
		""",
		'a': """
		a) <exampleTag />
		b) Empty-element tag
		""",
	},
	15: {
		'q':  """
		What is XPath?
		""",
		'a': """
		XPath is a query language for navigating XML documents.
		""",
	},
	16: {
		'q':  """
		Consider the following snippet:

			<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
			<bookstore>
				<book category="cooking">
					<title lang="en">Everyday Italian</title>
					<author>Giada de Laurentiis</author>
					<year>2005</year>
					<price>30.00</price>
				</book>

				<book category="children">
					<title lang="en">Harry Potter</title>
					<author>J.K. Rowling</author>
					<year>2005</year>
					<price>29.99</price>
				</book>

			</bookstore>

		Extract the text of the 'price' element in the second 'book' element using
		an absolute XPath.
		""",
		'a': r"""
		/bookstore/book[2]/price/text()
		""",
	},
	17: {
		'q':  """
		For each of the following state:
			a) What the acronym stands for
			b) What it is used for

		1) XSL
		2) XSLT
		""",
		'a': """
		1)
			a) Extensible stylesheet language
			b) XSL is a styling language for XML

		2)
			a) Extensible stylesheet language transformations
			b) XSLT is used to transform XML documents into other formats
				like HTML.
		""",
	},
	18: {
		'q':  """
		a) What does XSD stand for?
		b) What are .xsd files used for?
		""",
		'a': """
		a) XML Schema definition
		b) And XSD file is used to define what elements and attributes may appear
		   in an XML document.
		""",
	},
	19: {
		'q':  """
		Consider the following snippet:

			<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
			<bookstore>
				<book category="cooking">
					<title lang="en">Everyday Italian</title>
					<author>Giada de Laurentiis</author>
				</book>
				<book category="children">
					<title lang="en">Harry Potter</title>
					<author>J.K. Rowling</author>
				</book>
				<extraBook>
					<book category="testing double solidus">
						<title lang="en">KSI</title>
						<author>By KSI</author>
					</book>
				</extraBook>
			</bookstore>

		Q: How could I get all 'book' elements (regardless of where they lie in the hierarchy)
		with XPath?
		""",
		'a': """
		//book
		""",
	},
	20: {
		'q':  """
		Consider the following snippet:

			<baseballLeague>
				<team name="Tigers">
					<player name="Joe"/>
				</team>
				<team name="Saints">
					<player name="Steve"/>
				</team>
			</baseballLeague>

		Q: How would you get the 'team' element with attribute name="Tigers"
		using XPath?
		""",
		'a': """
		/baseballLeague/team[@name="Tigers"]
		""",
	},
	21: {
		'q':  """
		What are the two main uses for XML?
		""",
		'a': """
		1) To represent low-level data e.g. configuration files
		2) Add metadata to documents e.g italics, bold
		""",
	},
	22: {
		'q':  """
		What is the term for the way that a file's characters are represented by the 
		underlying data stream?
		""",
		'a': """
		Encoding
		""",
	},
	23: {
		'q':  """
		Outline the pros and cons of text files vs. binary files.
		""",
		'a': """
		Text file pros:
			- Both human-readable and machine-readable (binary only machine-readable)
			- Comparatively easier to parse than binary files

		Binary files pros:
			- Equivalent files are smaller in size than text files
			- Support for metadata (which text files lack)
		""",
	},
	24: {
		'q':  """
		What need drove the development of markup?
		""",
		'a': """
		The need to:
			- Have a human-readable file
			- Which can also be read by a wide range of applications
			- And can carry metada along with its content
		""",
	},
	25: {
		'q':  """
		What is the essence of markup?
		""",
		'a': """
		Markup is the act of surrounding text that conveys information
		about the text.
		""",
	},
	26: {
		'q':  """
		Consider the following (incomplete snippets):

		1)
			<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
			<xsl:template match="/">
				<html>
					<head>
						<title>Application Users Baby!</title>
					</head>
					<body>

		2)
			{for $user in doc(“appUsers.xml”)/applicationUsers/user
				return <tr><td>{data($user/@firstName)}</td>
				<td>{data($user/@lastName)}</td></tr>}

		Which of the two snippets looks like:
			a) XSLT b) XQuery
		""",
		'a': """
		1) XSLT
		2) XQuery
		""",
	},
	27: {
		'q':  """
		Explain the difference between data-centric and document-centric XML.
		""",
		'a': """
		Data-Centric:
			- Used to store pure data, such as configuration files.

		Document-Centric:
			- Used to add metadata to documents, e.g. XHTML
		""",
	},
	28: {
		'q':  """
		Name the four main technologies that rely on XML and explain
		their usage.
		""",
		'a': """
		1) XML Schemas:
			- used to validate that XML documents are in the correct format

		2) XSLT
			- used to convert from one XML format to another (e.g HTML)

		3) XQuery
			- used to query large document collections such as those
			  held in databases

		4) SOAP
			- uses XML to represent the data that is passed to,
			  and returned from, a web service.
		""",
	},
	29: {
		'q':  """
		Why is it that, when designing an XML format for your data,
		it is recommended to choose attributes unless you have a good reason not to?
		""",
		'a': """
		Because the alternative, using elements as children, will need to a larger
		file size for your XML document.

		Bear in mind that data is often transmitted across networks rather than just
		being consumed where it's stored.

		For a small number of users the difference may be negligible, but with a large
		number of users, or if you are transmitting many of these files, this could
		lead to more network traffic, leading to higher costs and reduced efficiency.
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