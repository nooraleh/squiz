using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CSharp
{
    public partial class DotNetMaui : QNABase
    {
        public DotNetMaui()
        : base(title: "Jesse Liberty's .NET MAUI for C# Developers", category: QNACategory.CSharp, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "DotNetMaui";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"Which of the following platform refer to 'apps' and which refer to 'applications'?
			a) iOS and Android
			b) Windows and Mac"},
        {"a", @"a) apps
		b) applications"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"Consider a file named ""MainPage.xaml"". What would be the name for the 'code-behind' file?"},
        {"a", @"The format for code-behind files is <PageName>.xaml.cs - so in the case it would be
		MainPage.xaml.cs"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"In a .NET MAUI project, what does the 'Resources' folder contain?"},
        {"a", @"The 'Resources' folder contains all the resources for all the platforms."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"In a .NET MAUI project, what does the 'Platforms' folder contain?"},
        {"a", @"The 'Platforms' folder contains everything that is needed on a per-platform
		basis."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @".NET MAUI programs are (typically) written in two languages. What are these two languages
		and what is the purpose of each language?"},
        {"a", @"1) XAML
			- used for the layout and creation of controls
		2) C#
			- used for all the logic"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"True or false:
			In .NET MAUI, all UI classes are marked `partial`"},
        {"a", @"True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"What is the significance of using a <ScrollView> layout element?"},
        {"a", @"All the children elements contained within <ScrollView> are scrollable."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"What is the purpose of the <VerticalStackLayout> element?"},
        {"a", @"This layout element holds things stacked one on top of another."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"a) What does DIP stand for?
		b) What is DIP used for?"},
        {"a", @"a) DIP stands for device-independent units
		b) Using DIPs means that you can define the size for one device, and in theory
			get a proportional size on another device."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"What is the 'SemanticProperties.Description' property used for in the <Image> elements?"},
        {"a", @"It's used for entering a text-based description to assist those who use screen readers e.g.
		people with visual difficulties."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"True or false:

			a) Each <ContentPage> can have only one layout
			b) The layout element of <ContentPage> can itself contain other layout elements
				(e.g <Image>, <Label>)"},
        {"a", @"a) True
		b) True"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet, take from a 'code-behind' file:

			    public partial class MainPage : ContentPage
				{
					int count = 0;

					public MainPage()
					{
						InitializeComponent();
					}
				}

		What is the job of `InitializeComponent`?"},
        {"a", @"The job of `InitializeComponent` is to initialize all of the elements of the page
		as defined in the corresponding .xaml file."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"In a sentence, what is an event handler?"},
        {"a", @"An event handler is a method that is registered to an event in the UI."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"What is the <Entry> element used for in .xaml files?"},
        {"a", @"<Entry> elements are primarily used for text entries."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"State one benefit of following the Model-View-ViewModel (MVVM) architecture
		in .NET MAUI?"},
        {"a", @"The MVVM architecture facilitates unit testing."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"a) What is a .NET MAUI control?
		b) Give a concrete example of a .NET MAUI Control?"},
        {"a", @"a) A .NET MAUI Control is an object that maps to native controls on each
			targets platform.

		b) E.g a .NET MAUI Button object maps to an iOS, Android, Macintosh, and
			Windows native Button."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"What is the principal element to use in order to display text in XAML?"},
        {"a", @"<Label>"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"a) What is a best practice for coding XAML element properties?
		b) What tool can you use to ensure your answer to (a) is done for you?"},
        {"a", @"a) The properties should be alphabetically sorted by name e.g.

			<Label  BackgroundColor=""Red""
					FontAttributes=""Bold""
					FontSize=""Small""
					HorizontalOptions=""Center""
					HorizontalTextAlignment=""Center""
					LineBreakMode=""WordWrap""
					Margin=""20""
					MaxLines=""5""
					Padding=""10""
					Text=""Welcome to Forget Me Not""
					TextColor=""Yellow""
					VerticalTextAlignment=""Center""/>

		b) You can use an XAML styler."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"Why should all binding (e.g. in ViewModel class files) be done with public partial
		classes?"},
        {"a", @"Because the `partial` keyword allows for the generation of other partial classes
		generated by the .NET MAUI framework."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {20, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:
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
		invoking `InitializeComponent`?"},
        {"a", @"Option A as it is generally considered good practice."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {21, new Dictionary<string, string>() {
        {"q", @"a) What are the two principal XAML elements for obtaining text from the user?
		b) What is the different between the two elements in your answer to (a)"},
        {"a", @"a) 1) <Entry> 2) <Editor>
		b) <Entry>
				- used for entering a line of text
			<Editor>
				- used for entering multiple lines of text"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {22, new Dictionary<string, string>() {
        {"q", @"What is the difference between OneWay and TwoWay binding?"},
        {"a", @"OneWay
			- control gets its value from the data source (e.g. C# property in ViewModel)

		TwoWay
			- control gets its value from the data source (e.g. C# property in ViewModel)
			- but can also write a value back into the data source"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {23, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet
			<Editor IsTextPredictionEnabled=""True"" />

		a) What does the `IsTextPredictionEnabled` property allow for?
		b) Is `IsTextPredictionEnabled` ""True"" or ""False"" by default?"},
        {"a", @"a) `IsTextPredictionEnabled` allows your <Editor> to offer user text to
			complete their sentence.
		b) `IsTextPredictionEnabled` is ""True"" by default"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {24, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:
			<Editor>
				<Editor.Behaviors>
					<behaviors:EventToCommandBehavior
					EventName=""Completed""
					Command=""{Binding EditorCompletedCommand}"" />
				</Editor.Behaviors>
			</Editor>

		In the context of .NET MAUI, what do 'behaviours' allow you to do?"},
        {"a", @"Behaviours:
			- let you add funcitonality to your controls (e.g. <Editor>) without
				having to create subclasses (e.g. inheriting from <Editor> and extended the child)
			- in the snippet, EventToCommandBehavior, for example, allows you to transform an event
				(which would be handled in the code-behind file) into a command, which can be handled
				in ViewModel"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {25, new Dictionary<string, string>() {
        {"q", @"a) What do we call a UI that offers a series of choices to the user?
		b) Which asynchronous .NET MAUI function can we use to program your answer to (a)"},
        {"a", @"a) A wizard
		b) DisplayActionSheet (.cs function)"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {26, new Dictionary<string, string>() {
        {"q", @"In .NET MAUI, you can fill in the colour of any number of controls using a brush.
		There are three types of brushes, what are they?"},
        {"a", @"1) Solid
		2) Linear Gradient
		3) Radial Gradient"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {27, new Dictionary<string, string>() {
        {"q", @"One key feature of a well-designed UX is that when something is going to take
		more than a second or so, you let the user know that the app is working on it.

		Explain why this is a good feature."},
        {"a", @"It's a good feature because implementing this ensures that it doesn't look like
		your app froze."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {28, new Dictionary<string, string>() {
        {"q", @"State and explain the two ways to let the user know that your application
		is working on something time-consuming."},
        {"a", @"1) ActivityIndicator
			- says 'I'm working on it, but I don't know how long it'll take'
		
		2) ProgressBar
			- says 'I'm working on it and I'm (for example) about halfway done'"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}
