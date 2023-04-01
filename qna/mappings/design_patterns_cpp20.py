# Notes taken in a Q & A style format from Dmitri Nesteruk's 'Design Patterns in Modern C++20'
qna = {
    1: {
		'q':  """
		Consider the following snippet:

			struct Foo : SomeBase<Foo>
			{
			}

		1) What is the basic end-goal of the curiously recurring template pattern (CRTP)?
		2) Give one reason why we would want to use CRTP?
		""",
		'a': """
		1) In CRTP, an inheritor (in this case Foo) passes itself as a template argument to its
			base class.
		2) In order to be able to access a typed `this` pointer inside a base class implementation.
			- Can be used to create mixins in C++
		""",
	},
    2: {
		'q':  """
		In the context of software development, what does it mean for a piece of software
		to be 'feature-complete'?
		""",
		'a': """
		Feature-complete denotes a version of a piece of software having all the functionality
		intended for a final version but requiring some improvements and fixes before release.
		""",
	},
    3: {
		'q':  """
		Give an overview of Mixin inheritance in C++ using templates.
		""",
		'a': """
		In C++, we can have a construct as follows:

			template<typename T>
			struct Mixin
		""",
	},
    4: {
		'q':  """
		Consider the following snippet:

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
		of how to take advantage of this.
		""",
		'a': """
		In line (1), we are using a non-standard declarative specified `property` to give
		us getter/setter functionality.

		Note that:
			1) we assign user-defined functions `get_age` and `set_age` to what the declspec
			can work with `get` and `set`
			2) we call the exposed getter/setter m_age and we put a single underscore before
				the private member to emphasize intent of privacy.

		How we can use this:
			Person p(26);
			p.m_age = 23; // invokes the setter `put`
			std::cout << "turn back the clock " << p.m_age; // invokes the getter `get` which in turn 
				calls p.get_age();
		""",
	},
    5: {
		'q':  """
		Fill in the blank:

		In the Single Responsibility principle, each class has only one responsiblity
		and therefore <BLANK>.
		""",
		'a': """
		BLANK = only one reason to change.
		""",
	},
    6: {
		'q':  """
		What is an anti-pattern?
		""",
		'a': """
		An anti-pattern is:
			- design *pattern* that shows up in code often enough is to be recognized globally
			- the opposite of a design pattern in the sense that anti-pattern epitomize bad
				software design
		""",
	},
    7: {
		'q':  """
		What is a God Object?
		""",
		'a': """
		A God Object is:
			- a huge class that tries to handle as many concerns as possible
			- becoming a monolith monstrosity that is very difficult to work with
		""",
	},
    8: {
		'q':  """
		In the context of user interface and software design,
		what is the principle of least surprise (alternatively: Principle of least astonishment)?
		""",
		'a': """
		A proposal that a component of a system should behave in a way that users expect it to
		behave, therefore not "astonishing" or "surprising" users.

		More formally - if a necessary feature has a high astonishment factor, it may be necessary
		to redesign the feature.
		""",
	},
    9: {
		'q':  """
		A `weak_ptr` is a non-owning pointer, holding a weak reference
		to the object managed by one or more `shared_ptr`s.

		This means that you cannot access the members of the underlying
		resource via weak_ptr directly.

		a) Which weak_ptr function should you call in order to access
			the underlying resource?
		b) What should you check for when using your answer to (a)
		""",
		'a': """
		a) std::weak_ptr::lock, which will return a shared_ptr.
		b) That the returned shared_ptr doesn't point to a nullptr.
			You can use a C++17 if-init clause for this:

				auto sp = std::make_shared<MyClass>();
				auto wp = std::weak_ptr<MyClass>\{sp\};

				if (auto observe = wp.lock(); observe != nullptr)
				{
					/.can access via the std::shared_ptr `observe` ./
				}
		""",
	},
    10: {
		'q':  """
		Consider the following snippet:

			void HTMLBuilder::add_child(const std::string& child_name, const std::string& child_text)
			{
				m_root.m_elements.emplace_back(child_name, child_text);
			}

			// usage
			HTMLBuilder builder{ "ul" };
			builder.add_child("li", "hello");
			builder.add_child("li", "world");

		a) How can we rewrite `add_child` so that the we have method chaining of the 
		`add_child` calls?
		b) What is your answer to (a) known as?
		""",
		'a': """
		a) HTMLBuilder& HTMLBuilder::add_child(const std::string& child_name, const std::string& child_text)
			{
				m_root.m_elements.emplace_back(child_name, child_text);
				return *this;
			}
		b) A fluent interface
		""",
	},
	11: {
		'q':  """
		In the context of the builder design pattern, how can we
		coerce client code to use a Builder class to construct an object A
		rather than via A directly?
		""",
		'a': """
		By making the constructors of A protected/private i.e inaccessible
		to clients.
		""",
	},
	12: {
		'q':  """
		When does the use of the Builder pattern make sense?
		""",
		'a': """
		When the construction of the object is a non-trivial process,
		and may involve multiple subconstructors for data members of said 
		object.
		""",
	},
	13: {
		'q':  """
		Consider the following snippet:
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

		What kind of methods are `create_partition` and `create_main` called?
		""",
		'a': """
		Factory methods.
		""",
	},
	14: {
		'q':  """
		In the context of design patterns, what is commonly understood as
		a `factory`?
		""",
		'a': """
		A factory is a separate class whose responsibility is to construct
		objects of a particular type.
		""",
	},
	15: {
		'q':  """
		True or false:
			Copy constructors can be virtual.
		""",
		'a': """
		False
		""",
	},
	16: {
		'q':  """
		State a prime candidate for the Singleton pattern?
		""",
		'a': """
        Since the Singleton pattern grew out of the idea that you should only have one
        instance of a particular component in your application, a prime candidate would be:
        
			A component that loads a database into memory and offers a read-only interface.
			In this case, it doesn't make sense to waste memory storing several identical datasets.
		""",
	},
	17: {
		'q':  """
		Select the correct option:
			The order of destruction of global static variables is BLANK:
            
        a) deterministic
        b) non-deterministic
		""",
		'a': """
		b) non-deterministic, this is why using a global static variable v1 in the destructor
			of a another global static variable v2 is not thread-safe.
		""",
	},
	18: {
		'q':  """
		a) What is understood by ambient context?
        b) What is best way to design an ambient context?
		""",
		'a': """
		a) Ambient context - a set of states that are meaningful to a certain set of operations
			being undertaken at a particular point in time.
            
        b) as a static construct addressable from within every point in the application, with `final`
			so that it cannot be inherited from.
		""",
	},
	19: {
		'q':  """
		a) What is the Monostate variation on the Singleton pattern?
        b) What are the pitfalls of using Monostate?
		""",
		'a': """
		a) A Monostate is a class that behaves like a singleton (all instances have the same underlying
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
				up memory even when they're not needed
		""",
	},
	20: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	21: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	22: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	23: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	24: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	25: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	26: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	27: {
		'q':  """
		
		""",
		'a': """
		
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
