# Notes taken in a Q & A style format from various C++ related Youtube videos

qna = {
    1: {
		'q':  """
		In a nutshell, what does the ODR (One Definition Rule) state?
		""",
		'a': """
		The One Definition Rule prescribes that:
			- classes/structs, and
			- non-inline functions
		cannot have more than one definition in the entire program and;

			- templates
			- types
		cannot have more than one definition by translation unit.
		""",
	},
    2: {
		'q':  """
		a) What is an alternative term for translation unit?
		b) What does a translation unit consist of?
		""",
		'a': """
		a) [informal] compilation unit
		b) A translation unit roughly consists of:	
			- a source file (i.e .c/.cpp) after it has been preprocessed

		   From a translation unit, the compiler generates an object file,
		   the object file can be further processed and linked (possible with other
		   object files) to form an executable program.
		""",
	},
    3: {
		'q':  """
		What does ODR-used mean?
		""",
		'a': """
		Informally, an object is ODR used if:
			1) its value has been read (unless it is a compile-time constant i.e via constexpr)
			2) its value has been written
			3) its address is taken
			4) or a reference is bound to it
		""",
	},
    4: {
		'q':  """
		Consider the following line of code:
			const int i = 42;
			const float f = 42.0f;

		True or false:
			1) const variables of integer type are implicitly constexpr
			2) const variables of float type are implicitly constexpr
		""",
		'a': """
			1) true
			2) false
		""",
	},
    5: {
		'q':  """
		True or false:
			1) Since C++11, static object initialization is guaranteed to happen
			exactly once.

			2) Furthermore, this initialization is guaranteed to be thread-safe.
		""",
		'a': """
		1) True
		2) True
		""",
	},
    6: {
		'q':  """
		True or false:
			Is it considered best practice to make single parameter constructors explicit.
		""",
		'a': """
		True
		""",
	},
    7: {
		'q':  """
		For each of the following terms, provide:
			a) A definition
			b) An demonstrative code snippet

		1) Stateless
		2) Stateful

		""",
		'a': """
		1)
			a) Stateless - there is no memory of the past. Every transaction is performed as if it
				were being done for the very first time.

			b)
				int add_one(int n)
				{
					return n + 1; // state is derived by what is passed into the function
				}


		2) 
			a) Stateful - means that there is memory of the past. Previous transactions are remembered and
					may affect the current transaction.

			b)
				int _number = 0;
				
				int add_one()
				{
					++_number;
					return ++_number; // state is maintained by the function and `_number` value dependant on determined by previous calls
				} 
		""",
	},
    8: {
		'q':  """
		True or false:
			Generic lambdas do not support perfect forwarding.
		""",
		'a': """
		False, for consider:

			std::vector<std::string> string_vector;

			auto append_to_string_vector = [&string_vector](auto&& element) {
				string_vector.push_back(std::forward<decltype(element)>(element));
			};

			append_to_string_vector(std::string{ "1" });
			append_to_string_vector(std::string{ "2" });
			append_to_string_vector(std::string{ "3" });
			append_to_string_vector(std::string{ "4" });
		""",
	},
    9: {
		'q':  """
		Map the following letters with the corresponding numbers:
			1) dynamic polymorphism
			2) static polymorphism

			a) templates
			b) object orientation
		""",
		'a': """
		1) b)
		2) a)
		""",
	},
    10: {
		'q':  """
		What is type erasure?
		""",
		'a': """
		Type erasure if:
			1) a type-safe GENERIC (i.e templatized) way to provide one interface for different types.
			2) the different types don't need a common base class and are often unrelated.
		""",
	},
	11: {
		'q':  """
		a) In a nutshell, what is meant by type safety?
		b) Give an example of a type unsafe statement in C++?
		""",
		'a': r"""
		a) Type-safe is the degree to which a language prevents using a value of the wrong type.
		b) Example:
			printf("Meant to be passing a string: %s", 42);

			^^ note the above line will give you a warning but not a compiler error
		""",
	},
	12: {
		'q':  """
		Explained with an example showing the special member declarations why you cannot move
		a const object?
		""",
		'a': """
		For consider:

			struct S
			{
				S() = default;						// ctor
				S(S&&) = default;					// move ctor  (1)
				S(const S&);						// copy ctor (2)
				S& operator=(S&&) = default;		// move assignment operator
				S& operator=(const S&) = default;	// copy assignment operator
				~S() = default;
			};

		and the code:

			int main(void)
			{
					const S s;                (3)
					S s2{ std::move(s) };     (4)
			}

		Explanation: Since line (3) makes a const instance and the move ctor (1) cannot accept
				const-qualified arguments, the overload dispatches to the copy ctor (2).
				I.e we do not move, we copy.
		""",
	},
	13: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	14: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	15: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	16: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	17: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	18: {
		'q':  """
		
		""",
		'a': """
		
		""",
	},
	19: {
		'q':  """
		
		""",
		'a': """
		
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