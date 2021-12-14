# Notes taken in a Q & A style format from Edube's C++ Essentials - Parts 1 & 2 courses

qna = {
    1: {
        "q": """What are the i) << ii) >> operators called?""",
        "a": """ i) The insertion operator, commonly used with cout. ii) the extraction operator, commonly used with cin""",
    },
    2: {
        "q": """Consider the for loop:
            for(intializor; conditional; modifier)

            if the initializor, conditional and modifier is empty, what is presumed to be there instead?
        """,
        "a": """Presumed to have 1, this edge case will lead to an infinite loop."""
    },
    3: {
        "q": """What's one limitation to passing by reference e.g int &bval?""",
        "a": """The actual parameter passed must be a variable, not a literal.""",
    },
    4: {
        "q": """Name the mechanism which allows us to have more than one function of the same name?""",
        "a": """Overloading""",
    },
    5: {
        "q": """What keyword is used to request the creation of a new memory block?""",
        "a": """`new`""",
    },
    6: {
        "q": """What keyword is used to free/release a memory block we no longer need?""",
        "a": """`delete`. delete[] for arrays""",
    },
    7: {
        "q": """Give two ways of initializing the variable `pet_name` to the string Lassie""",
        "a": """
        i) string pet_name = "Lassie";, <- assignment style
        
        ii) string pet_name("Lassie"); <- functional style
        """,
    },
    8: {
        "q": """Name one important limitation of string concatenation?""",
        "a": """String concatenation cannot concatenate literals""",
    },
    9: {
        "q": """What is the name space in one sentence?""",
        "a": """The name space is a space in which a particular name has an unambiguous and clear meaning.""",
    },
    10: {
        "q": """What's the official name for ::?""",
        "a": """Scope resolution operator""",
    },
    11: {
        "q": """What's an anonymous namespace""",
        "a": """A namespace defined like so:
        
        namespace <missing_name> {
            int troll = 1;
        }

        This kind of namespace is implicitly and automatically used in a source file where it's visible.
        """,
    },
    12: {
        "q": """i) What is encapsulation? ii) How would you implement encapsulation in C++?""",
        "a": """
        i) The ability to hide selected values against unauthorized accessed.
        ii) private:
        """,
    },
    13: {
        "q": """Let Class1 be a pre-define class and Class2 be a proposed child class. How would you code this in C++?""",
        "a": """
        class Class2:Class1 {

        };
        """,
    },
    14: {
        "q": """Are class components (methods and attributes) public or private by default?""",
        "a": """C++ class components are private by default.""",
    },
    15: {
        "q": """How do we specify class constructors in C++?""",
        "a": """We define a function with a name identical to its home class. Do not specify a return type.""",
    },
    16: {
        "q": """Explain the concept of memory leaks in C++?""",
        "a": """Memory leaks occur when unused (but still allocated) memory grows in size, affecting system performance.""",
    },
    17: {
        "q": """Where are entities created by the `new` keyword stored?""",
        "a": """In a specific memory region called a heap.""",
    },
    18: {
        "q": """Are constructors from inner objects invoked before or after constructors from outer objects?""",
        "a": """Before""",
    },
    19: {
        "q": """
        Let A be a class and X, Y, Z be proposed subclasses. How would you define:
        i) X as a subclass of A
        ii) X, Y, Z as superclasses of A""",
        "a": """
        i) class X: {<visibility_specifier>} X {...};
        ii) class A: X, Y, Z {...};

        """,
    },
    20: {
        "q": """Explain private inheritance?""",
        "a": """
        When a visibility specifier isn't specified for an inherited subclass,
        private inheritance means that all public superclass components turn into private access,
        and private superclass components won't be accessible at all.""",
    },
    21: {
        "q": """What does the keyword access specifier `protected` do?""",
        "a": """
        `protected` means that any component marked with it behaves like a
        public component when used by any of the subclasses and looks
        like a private component to the rest of the world.
        This only applies to publicly inherited classes.""",
    },
    22: {
        "q": """
        i) Must you declare const in constant pointers before or after the *?
        ii) Do variables qualified with const have to be initialized?""",
        "a": """
        i) After.
        ii) They do.""",
    },
    23: {
        "q": """Outline the syntactic difference between constant pointers,
        pointers to constants and constant pointers to constants.""",
        "a": """
        i) constant pointers e.g.: int * const ptr = &val;
        ii) pointers to constants: const int *ptr = &val;
        iii) const pointers to const: const int * const ptr = &val;""",
    },
    24: {
        "q": """How would you declare a const member function?""",
        "a": """
        <type> <function_name>(<params>) const {<body>}.
        Note the placement of const between the parameter list and function body.""",
    },
    25: {
        "q": """What is a friend of a class able to do?""",
        "a": """
        A friend of a class can access or use private and protect and protected components of the class.""",
    },
    26: {
        "q": """What does the volatile keyword qualifier do?""",
        "a": """
        It indicates that a variable can be changed by a background process/routine.
        Every reference to the volatile variable will reload the content from main memory.
        It will not use the copy of the variable which can be present in the register.
        Compiler optimizations are not applied on the volatile variable.""",
    },
    27: {
        "q": """
        i) What is an EOF state? ii) Name two ways this can be brought about""",
        "a": """
        i) The event in which there is no more data to process
        ii) ctrl+D in linux, the actual end of a disk file containing data.
        """,
    },
    28: {
        "q": """A function which throws an exceptions,
        may but doesn't have to specify the types of the entities being throws.
        Let int func(void)  be a function. 
        i) Give the form if func throws a string
        ii) The form if func throws a class named Class
        iii) The generalised from if func throws x1, x2, ... ,xn params
        iv) if func throws no exceptions at all""",
        "a": """
        i) int func(void) throw (string) {}
        ii) int func(void) throw (Class) {}
        iii) int func(void) throw (x1, x2, ..., xn) {}
        iv ) int func(void) throw () {}
        """,
    },
    29: {
        "q": """What are unexpected exceptions?""",
        "a": """Exceptions incompatible with the specification made.""",
    },
    30: {
        "q": """What does the explicit keyword do?""",
        "a": """It protects the constructor from being used in any context requiring the use of implicit conversions.""",
    },
    31: {
        "q": """
        Describe the purpose of:
        i) logic_error: 
        ii) domain_error:
        iii) bad_exception
        """,
        "a": """
        i) logic_error: Designed to represent all the exceptions caused by a violation of the rules imposed by the logic of the algorithm/program.
        ii) domain_error: designed to represent all exceptions caused by the data exceeding the permissible range.
        iii) bad_exception: is thrown when a function tries to throw an exception not specified inside its throw specification.
        """,
    },
    32: {
        "q": """
        i) Give the specialized form of the catch statement that's able to catch all passing exceptions
        ii) What is one drawback to this?""",
        "a": """
        i) catch(...) {<exception_handling_logic>}
        iii) This form that neither identify the exception object, nor make any use of it.""",
    },
    33: {
        "q": """What is the purpose of virtual functions?""",
        "a": """To enable the ability of ruuntime polymorphism.""",
    },
    34: {
        "q": """
        i) What do pure virtual functions do?
        ii) Let void make_sound() be a method in a class, specify make_sound as a pure virtual function""",
        "a": """
        i) The enforce subclasses to implement the function, cause the class with a
            pure virtual function to be an 'abstract class'.
        ii) virtual void make_sound() = 0;
            """,
    },
    35: {
        "q": """What is the formal definition of an abstract class in C++?""",
        "a": """A class which has at least one pure virtual function.""",
    },
    36: {
        "q": """
        i) What are smart pointers?
        ii) What are the three types of smart pointer in C++""",
        "a": """
        i) A container or a wrapper for a raw pointer.
        Unlike raw pointers, they deallocate memory automatically.
        ii) std::unique_ptr, std::shared_ptr, std::weak_ptr""",
    },
    37: {
        "q": """What is a function template?""",
        "a": """
        A function template is a generalization of an algorithm. It's a single
        declaration that can generate declarations for similar, but distinct functions
        Each generated function implements the algorithm for operands of different types.
        A function template is not an actual function. It's a recipe for generating functions.""",
    },
    38: {
        "q": """What is an infix operator?""",
        "a": """Operators place in between their arguments""",
    },
    39: {
        "q": """What are the four non-overloadable operators?""",
        "a": """
        i) ?:
        ii) .
        iii) ::
        iv) sizeof
        """,
    },
    40: {
        "q": """
        Consider the following code:
        usr_class obj1;
        (2)usr_class obj2;
        (2)usr_class obj2 = obj1;
        (3)usr_class obj3 = obj1;

        What is the difference between lines (2) and (3)?
        """,
        "a": """
        In (2) the assignment operator is called.
        In (3) the Copy constructor is called for copying.
        """,
    },
}