# Notes taken in a QNA style from Jesse Liberty's '.NET MAUI for C# Developers'
qna = {
    1: {
		'q':  """
		Which of the following platform refer to 'apps' and which refer to 'applications'?
			a) iOS and Android
			b) Windows and Mac
		""",
		'a': """
		a) apps
		b) applications
		""",
	},
    2: {
		'q':  """
		Consider a file named "MainPage.xaml". What would be the name for the 'code-behind' file?
		""",
		'a': """
		The format for code-behind files is <PageName>.xaml.cs - so in the case it would be
		MainPage.xaml.cs
		""",
	},
    3: {
		'q':  """
		In a .NET MAUI project, what does the 'Resources' folder contain?
		""",
		'a': """
		The 'Resources' folder contains all the resources for all the platforms.
		""",
	},
    4: {
		'q':  """
		In a .NET MAUI project, what does the 'Platforms' folder contain?
		""",
		'a': """
		The 'Platforms' folder contains everything that is needed on a per-platform
		basis.
		""",
	},
    5: {
		'q':  """
		.NET MAUI programs are (typically) written in two languages. What are these two languages
		and what is the purpose of each language?
		""",
		'a': """
		1) XAML
			- used for the layout and creation of controls
		2) C#
			- used for all the logic
		""",
	},
    6: {
		'q':  """
		True or false:
			In .NET MAUI, all UI classes are marked `partial`
		""",
		'a': """
		True
		""",
	},
    7: {
		'q':  """
		What is the significance of using a <ScrollView> layout element?
		""",
		'a': """
		All the children elements contained within <ScrollView> are scrollable.
		""",
	},
    8: {
		'q':  """
		What is the purpose of the <VerticalStackLayout> element?
		""",
		'a': """
		This layout element holds things stacked one on top of another.
		""",
	},
    9: {
		'q':  """
		a) What does DIP stand for?
		b) What is DIP used for?
		""",
		'a': """
		a) DIP stands for device-independent units
		b) Using DIPs means that you can define the size for one device, and in theory
			get a proportional size on another device.
		""",
	},
    10: {
		'q':  """
		What is the 'SemanticProperties.Description' property used for in the <Image> elements?
		""",
		'a': """
		It's used for entering a text-based description to assist those who use screen readers e.g.
		people with visual difficulties.
		""",
	},
	11: {
		'q':  """
		True or false:

			a) Each <ContentPage> can have only one layout
			b) The layout element of <ContentPage> can itself contain other layout elements
				(e.g <Image>, <Label>)
		""",
		'a': """
		a) True
		b) True
		""",
	},
	12: {
		'q':  """
		Consider the following snippet, take from a 'code-behind' file:

			    public partial class MainPage : ContentPage
				{
					int count = 0;

					public MainPage()
					{
						InitializeComponent();
					}
				}

		What is the job of `InitializeComponent`?
		""",
		'a': """
		The job of `InitializeComponent` is to initialize all of the elements of the page
		as defined in the corresponding .xaml file.
		""",
	},
	13: {
		'q':  """
		In a sentence, what is an event handler?
		""",
		'a': """
		An event handler is a method that is registered to an event in the UI.
		""",
	},
	14: {
		'q':  """
		What is the <Entry> element used for in .xaml files?
		""",
		'a': """
		<Entry> elements are primarily used for text entries.
		""",
	},
	15: {
		'q':  """
		State one benefit of following the Model-View-ViewModel (MVVM) architecture
		in .NET MAUI?
		""",
		'a': """
		The MVVM architecture facilitates unit testing.
		""",
	},
	16: {
		'q':  """
		a) What is a .NET MAUI control?
		b) Give a concrete example of a .NET MAUI Control?
		""",
		'a': """
		a) A .NET MAUI Control is an object that maps to native controls on each
			targets platform.

		b) E.g a .NET MAUI Button object maps to an iOS, Android, Macintosh, and
			Windows native Button.
		""",
	},
	17: {
		'q':  """
		What is the principal element to use in order to display text in XAML?
		""",
		'a': """
		<Label>
		""",
	},
	18: {
		'q':  """
		a) What is a best practice for coding XAML element properties?
		b) What tool can you use to ensure your answer to (a) is done for you?
		""",
		'a': """
		a) The properties should be alphabetically sorted by name e.g.

			<Label  BackgroundColor="Red"
					FontAttributes="Bold"
					FontSize="Small"
					HorizontalOptions="Center"
					HorizontalTextAlignment="Center"
					LineBreakMode="WordWrap"
					Margin="20"
					MaxLines="5"
					Padding="10"
					Text="Welcome to Forget Me Not"
					TextColor="Yellow"
					VerticalTextAlignment="Center"/>

		b) You can use an XAML styler.
		""",
	},
	19: {
		'q':  """
		Why should all binding (e.g. in ViewModel class files) be done with public partial
		classes?
		""",
		'a': """
		Because the `partial` keyword allows for the generation of other partial classes
		generated by the .NET MAUI framework.
		""",
	},
	20: {
		'q':  """
		Consider the following snippet:
			public partial class MainPage : ContentPage
			{
				private MainViewModel vm = new MainViewModel();
				public MainPage()
				{
					BindingContext = vm;         (A)
					InitializeComponent();
					// BindingContext = vm;      (B)
			}

		Should you prefere setting the `BindingContext` before (A) or after (B)
		invoking `InitializeComponent`?
		""",
		'a': """
		Option A as it is generally considered good practice.
		""",
	},
	21: {
		'q':  """
		a) What are the two principal XAML elements for obtaining text from the user?
		b) What is the different between the two elements in your answer to (a)
		""",
		'a': """
		a) 1) <Entry> 2) <Editor>
		b) <Entry>
				- used for entering a line of text
			<Editor>
				- used for entering multiple lines of text

		""",
	},
	22: {
		'q':  """
		What is the difference between OneWay and TwoWay binding?
		""",
		'a': """
		OneWay
			- control gets its value from the data source (e.g. C# property in ViewModel)

		TwoWay
			- control gets its value from the data source (e.g. C# property in ViewModel)
			- but can also write a value back into the data source
		""",
	},
	23: {
		'q':  """
		Consider the following snippet
			<Editor IsTextPredictionEnabled="True" />

		a) What does the `IsTextPredictionEnabled` property allow for?
		b) Is `IsTextPredictionEnabled` "True" or "False" by default?
		""",
		'a': """
		a) `IsTextPredictionEnabled` allows your <Editor> to offer user text to
			complete their sentence.
		b) `IsTextPredictionEnabled` is "True" by default
		""",
	},
	24: {
		'q':  """
		Consider the following snippet:
			<Editor>
				<Editor.Behaviors>
					<behaviors:EventToCommandBehavior
					EventName="Completed"
					Command="{Binding EditorCompletedCommand}" />
				</Editor.Behaviors>
			</Editor>

		In the context of .NET MAUI, what do 'behaviours' allow you to do?
		""",
		'a': """
		Behaviours:
			- let you add funcitonality to your controls (e.g. <Editor>) without
				having to create subclasses (e.g. inheriting from <Editor> and extended the child)
			- in the snippet, EventToCommandBehavior, for example, allows you to transform an event
				(which would be handled in the code-behind file) into a command, which can be handled
				in ViewModel 
		""",
	},
	25: {
		'q':  """
		a) What do we call a UI that offers a series of choices to the user?
		b) Which asynchronous .NET MAUI function can we use to program your answer to (a)
		""",
		'a': """
		a) A wizard
		b) DisplayActionSheet (.cs function)
		""",
	},
	26: {
		'q':  """
		In .NET MAUI, you can fill in the colour of any number of controls using a brush.
		There are three types of brushes, what are they?
		""",
		'a': """
		1) Solid
		2) Linear Gradient
		3) Radial Gradient
		""",
	},
	27: {
		'q':  """
		One key feature of a well-designed UX is that when something is going to take
		more than a second or so, you let the user know that the app is working on it.

		Explain why this is a good feature.
		""",
		'a': """
		It's a good feature because implementing this ensures that it doesn't look like
		your app froze.
		""",
	},
	28: {
		'q':  """
		State and explain the two ways to let the user know that your application
		is working on something time-consuming.
		""",
		'a': """
		1) ActivityIndicator
			- says 'I'm working on it, but I don't know how long it'll take'
		
		2) ProgressBar
			- says 'I'm working on it and I'm (for example) about halfway done'
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