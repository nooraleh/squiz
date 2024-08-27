using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CPP
{
    public partial class DesignPatternsCPP20 : QNABase
    {
        public DesignPatternsCPP20()
        : base(title: "Dmitri Nesteruk's Design Patterns in Modern C++20", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "DesignPatternsCPP20";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>() {
    {1, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			struct Foo : SomeBase<Foo>
			{
			}

		1) What is the basic end-goal of the curiously recurring template pattern (CRTP)?
		2) Give one reason why we would want to use CRTP?"},
        {"a", @"1) In CRTP, an inheritor (in this case Foo) passes itself as a template argument to its
			base class.
		2) In order to be able to access a typed `this` pointer inside a base class implementation.
			- Can be used to create mixins in C++"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {2, new Dictionary<string, string>() {
        {"q", @"In the context of software development, what does it mean for a piece of software
		to be 'feature-complete'?"},
        {"a", @"Feature-complete denotes a version of a piece of software having all the functionality
		intended for a final version but requiring some improvements and fixes before release."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {3, new Dictionary<string, string>() {
        {"q", @"Give an overview of Mixin inheritance in C++ using templates."},
        {"a", @"In C++, we can have a construct as follows:

			template<typename T>
			struct Mixin"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {4, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			class Person
			{
			public:
				Person(int age)
					: _m_age{ age }
				{}

				void set_age(const int& age) { _m_age = age; }
				[[nodiscard]] int get_age() const { return _m_age; }

				__declspec(property(get = get_age, put=set_age)) int m_age;  // (1)
			private:
				int _m_age;
			};

		Explain what is happening on line (1) and give code snippet examples
		of how to take advantage of this."},
        {"a", @"In line (1), we are using a non-standard declarative specified `property` to give
		us getter/setter functionality.

		Note that:
			1) we assign user-defined functions `get_age` and `set_age` to what the declspec
			can work with `get` and `set`
			2) we call the exposed getter/setter m_age and we put a single underscore before
				the private member to emphasize intent of privacy.

		How we can use this:
			Person p(26);
			p.m_age = 23; // invokes the setter `put`
			std::cout << ""turn back the clock "" << p.m_age; // invokes the getter `get` which in turn 
				calls p.get_age();"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {5, new Dictionary<string, string>() {
        {"q", @"Fill in the blank:

		In the Single Responsibility principle, each class has only one responsiblity
		and therefore <BLANK>."},
        {"a", @"BLANK = only one reason to change."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {6, new Dictionary<string, string>() {
        {"q", @"What is an anti-pattern?"},
        {"a", @"An anti-pattern is:
			- design *pattern* that shows up in code often enough is to be recognized globally
			- the opposite of a design pattern in the sense that anti-pattern epitomize bad
				software design"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {7, new Dictionary<string, string>() {
        {"q", @"What is a God Object?"},
        {"a", @"A God Object is:
			- a huge class that tries to handle as many concerns as possible
			- becoming a monolith monstrosity that is very difficult to work with"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {8, new Dictionary<string, string>() {
        {"q", @"In the context of user interface and software design,
		what is the principle of least surprise (alternatively: Principle of least astonishment)?"},
        {"a", @"A proposal that a component of a system should behave in a way that users expect it to
		behave, therefore not ""astonishing"" or ""surprising"" users.

		More formally - if a necessary feature has a high astonishment factor, it may be necessary
		to redesign the feature."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {9, new Dictionary<string, string>() {
        {"q", @"A `weak_ptr` is a non-owning pointer, holding a weak reference
		to the object managed by one or more `shared_ptr`s.

		This means that you cannot access the members of the underlying
		resource via weak_ptr directly.

		a) Which weak_ptr function should you call in order to access
			the underlying resource?
		b) What should you check for when using your answer to (a)"},
        {"a", @"a) std::weak_ptr::lock, which will return a shared_ptr.
		b) That the returned shared_ptr doesn't point to a nullptr.
			You can use a C++17 if-init clause for this:

				auto sp = std::make_shared<MyClass>();
				auto wp = std::weak_ptr<MyClass>\{sp\};

				if (auto observe = wp.lock(); observe != nullptr)
				{
					/.can access via the std::shared_ptr `observe` ./
				}"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {10, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:

			void HTMLBuilder::add_child(const std::string& child_name, const std::string& child_text)
			{
				m_root.m_elements.emplace_back(child_name, child_text);
			}

			// usage
			HTMLBuilder builder{ ""ul"" };
			builder.add_child(""li"", ""hello"");
			builder.add_child(""li"", ""world"");

		a) How can we rewrite `add_child` so that the we have method chaining of the 
		`add_child` calls?
		b) What is your answer to (a) known as?"},
        {"a", @"a) HTMLBuilder& HTMLBuilder::add_child(const std::string& child_name, const std::string& child_text)
			{
				m_root.m_elements.emplace_back(child_name, child_text);
				return *this;
			}
		b) A fluent interface"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {11, new Dictionary<string, string>() {
        {"q", @"In the context of the builder design pattern, how can we
		coerce client code to use a Builder class to construct an object A
		rather than via A directly?"},
        {"a", @"By making the constructors of A protected/private i.e inaccessible
		to clients."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {12, new Dictionary<string, string>() {
        {"q", @"When does the use of the Builder pattern make sense?"},
        {"a", @"When the construction of the object is a non-trivial process,
		and may involve multiple subconstructors for data members of said 
		object."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {13, new Dictionary<string, string>() {
        {"q", @"Consider the following snippet:
			class SolidWall : public Wall
			{
				// ...
				static SolidWall create_main(Point2D start, Point2D end, int elevation, int height)
				{
					return SolidWall{ start, end, elevation, height,  375, Material::aerated_concrete};
				}

				static SolidWall create_partition(Point2D start, Point2D end, int elevation, int height)
				{
					SolidWall{ start, end, elevation, height, 120, Material::brick};
				}
			}

		What kind of methods are `create_partition` and `create_main` called?"},
        {"a", @"Factory methods."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {14, new Dictionary<string, string>() {
        {"q", @"In the context of design patterns, what is commonly understood as
		a `factory`?"},
        {"a", @"A factory is a separate class whose responsibility is to construct
		objects of a particular type."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {15, new Dictionary<string, string>() {
        {"q", @"True or false:
			Copy constructors can be virtual."},
        {"a", @"False"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {16, new Dictionary<string, string>() {
        {"q", @"State a prime candidate for the Singleton pattern?"},
        {"a", @"Since the Singleton pattern grew out of the idea that you should only have one
        instance of a particular component in your application, a prime candidate would be:
        
			A component that loads a database into memory and offers a read-only interface.
			In this case, it doesn't make sense to waste memory storing several identical datasets."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {17, new Dictionary<string, string>() {
        {"q", @"Select the correct option:
			The order of destruction of global static variables is BLANK:
            
        a) deterministic
        b) non-deterministic"},
        {"a", @"b) non-deterministic, this is why using a global static variable v1 in the destructor
			of a another global static variable v2 is not thread-safe."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {18, new Dictionary<string, string>() {
        {"q", @"a) What is understood by ambient context?
        b) What is best way to design an ambient context?"},
        {"a", @"a) Ambient context - a set of states that are meaningful to a certain set of operations
			being undertaken at a particular point in time.
            
        b) as a static construct addressable from within every point in the application, with `final`
			so that it cannot be inherited from."},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
    {19, new Dictionary<string, string>() {
        {"q", @"a) What is the Monostate variation on the Singleton pattern?
        b) What are the pitfalls of using Monostate?"},
        {"a", @"a) A Monostate is a class that behaves like a singleton (all instances have the same underlying
        data due to them being static) which appearing as an ordinary class (since you're allowed to
        instantiate more than one class).
        
        Snippet example:
			class Print
            {
            private:
				static int m_id;
            public:
				int get_id() const {return id;}
                void set_id(int id) {m_id = id;}
			};
            
        b) Disadvantages include:
			1) converting ordinary classes to Monostate is intrusive
            2) the fact that underlying members are static mean that they ALWAYS take
				up memory even when they're not needed"},
        {"snippetQ", @""},
        {"snippetA", @""},
    }},
};
    }
}
