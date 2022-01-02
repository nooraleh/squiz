# Notes taken in a Q & A style format from Cisco Academy's 'Advanced C++'
qna = {
	1: { # module 1: STL Sequential Containers
		'q':  """
		What are boost libraries?""",
		'a': """
		Boost libraries are free and peer-reviewed portable C++ source libraries?""",
	},
    2: {
		'q':  """
		i) What are iterators?
        ii) Give 5 types of iterators""",
		'a': """
		i) Generalizations of pointers which allow for access to the elements of a collection.
        ii)
            1) input iterator
            2) output iterator
            3) forward iterator
            4) bidirectional iterator
            5) random access iterator""",
	},
    3: {
		'q':  """
		Consider the definition of std::vector:
        
            template<class T, class Allocator = std::allocator<T>>class vector;
            
        What is the `Allocator` responsible for?""",
		'a': """
		The `Allocator` is responsible for providing a memory model for the container
        elements.
        
        The default is std::allocator<T> but it's possible to supply a different one.""",
	},
    4: {
		'q':  """
		Consider:
               int a1[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        construct a vector v1 from a1 taking in all the elements from a1.
        """,
		'a': """
		std::vector<int> v1 (a1, a1+10);
        """,
	},
    5: {
		'q':  """
		Consider:
            int a1[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
            std::vector<int> v1 (a1, a1+10);
            
        Is the second argument to the std::vector constructor (i.e a1+10)
        inclusive or exclusive.
            """,
		'a': """
		Exclusive - the value at a1+10 will not be included.""",
	},
    6: {
		'q':  """
		Consider the destructor of an instance of std::vector<T>. 
        If the destructor is called, under what condition will the sub-elements
        of type T be called as well?""",
		'a': """
		If the sub elements of type T are static (i.e not pointers). If elements of T
        are pointers, the user is responsible for adding logic for their destruction (deallocation).
        """,
	},
    7: {
		'q':  """
		Which data structure is an std::list an implementation of?""",
		'a': """
		std::list is an implementation of the double-linked list principle.""",
	},
    8: {
		'q':  """
		Which access method does std::list lack?""",
		'a': """
		std::list lacks the random access mechanism, namely operator[].""",
	},
    9: {
		'q':  """
		Consider:
		
			std::vector, std::deque, std::list
			
		Which container(s) return:
		
			i) Random access iterators
			ii) Bidirectional iterators""",
		'a': """
		i) std::vector, std::deque
		ii) std::list
		""",
	},
    10: {
		'q':  """
		Why is it preferable to call .empty() on an std::list instead of
		.size()?""",
		'a': """
		Because calling .size() for a list might result in linear time
		performance instead of the more desirable constant time.""",
	},
    11: {
		'q':  """
		Consider:
			std::vector, std::deque, std::list

		Which one(s) may have operator[] overloaded? Why?

		BONUS: What related method is only available to that/those sequential containers?
		""",
		'a': """
		std::vector, std::deque may have operator[] overloaded.
		This is because they support random access iterators.
		
		BONUS: .at() which performs bounds checking and is preferable.
		""",
	},
    12: {
		'q':  """
		Consider the .pop_back() method for STL sequential containers,
		is the popped value returned?""",
		'a': """
		The value is not returned. Use .back() if you want the last element.""",
	},
    13: {
		'q':  """
		What does <iterator>'s std::advance do?""",
		'a': """
		std::advance(iterator, n) advances `iterator` by `n` element positions.""",
	},
    14: {
		'q':  """
		i) What is a containter adapter (STL terminology)
		ii) Name three container adapters that the STL provides""",
		'a': """
		i) A container adaptor is a class which uses an STL container
		to provide other functionality
		ii) 1) stack 2) queue 3) priority_queue""",
	},
    15: {
		'q':  """
		What STL sequential containers are valid underlying containers
		for std::priority_queue?""",
		'a': """
		std::vector, std::deque. Since the containers must satisfy:
		
			1) the elements being accessible via random access iterator
			2) .front() implementation
			3) .push_back() implementation
			4) .pop_back() implementation""",
	},
    16: {
		'q':  """
		i) How does std::priority_queue maintain its order?
		ii) Explain how your answer to (i) works.""",
		'a': """
		i) By using a comparator
		ii) The comparator is a function which takes two parameters
		and returns `true` if the first parameter is "lower" than the second.""",
	},
    17: { # module 2: Associative containers
		'q':  """
		What are the four types of associative containers in the STL?""",
		'a': """
		
			1) set
			2) multiset
			3) map
			4) multimap
		""",
	},
    18: {
		'q':  """
		Consider <numeric>'s std::iota signature:
			
			constexpr void iota( ForwardIt first, ForwardIt last, T value );

		What does it do?
		""",
		'a': """
		std::iota fills in the range [first, last) with sequentially increasing
		values, starting with `value` and repetitively evaluating `++value`
		""",
	},
    19: {
		'q':  """
		Consider (as of C++20) <vector>'s std::erase and std::erase_if.
		
		i) What do both of these functions require as the first or first and second args?
		ii) What does erase_if return?""",
		'a': """
		i) Either:
			1) a starting point (iterator or pointer) to traverse the container
			2) A starting and exclusive end point (usually .begin() and .end())
			
		ii) std::erase_if returns the count of erased elements.
		""",
	},
    20: {
		'q':  """
		What methods are available for getting:
		
		i) The const iterators of a container
		ii) The const reverse iterators of a container""",
		'a': """
		i) .cbegin(), .cend()
		ii) .crbegin(), .crend()""",
	},
    21: {
		'q':  """
		Is there a difference between .cbegin() and .begin() for std::set's and std::multisets?""",
		'a': """
		No, there is no difference. Both iterator return values are const and this is 
		related Key invariability property of their elements.""",
	},
    22: {
		'q':  """
		Consider the .find(value) method for STL associative containers, what is returned?""",
		'a': """
		If `value` is found:
			an iterator to the found element is returns
		else:
			.find returns std::end() <- the one-past-the-end iterator.""",
	},
    23: { # module 4: non-modifying containers
		'q':  """
		What's the main difference between std::vector::swap and std::vector::iter_swap?""",
		'a': """
		std::vector::swap takes referenes as arguments, while std::vector::iter_swap
		takes iterators as arguments.""",
	},
    24: {
		'q':  """
		What's one quirk of std::remove that you should be aware of?""",
		'a': """
		It cannot alter the size of an array or a container.""",
	},
    25: {
		'q':  """
		What using std::partition with a predicate function `pred`,
		what is the partitioning order?""",
		'a': """
		Values which `pred` return true come before values which `pred`
		returns false.""",
	},
    26: {
		'q':  """
		What do the *_copy suffix do to algorithms in the STL?""",
		'a': """
		Does the same operation as *, but copies the result into a separate
		container and preserves the state of the original.
		
		E.g std::copy_unique applied std::copy to the input container and stores
		the result into an output container.""",
	},
    27: {
		'q':  """
		Which STL containers are compatible with std::random_shuffle?""",
		'a': """
		std::vector, std::deque, std::array.""",
	},
    28: { # 05 module: STL sorting algorithms
		'q':  """
		What STL containers are compatible with std::sort, std::stable_sort""",
		'a': """
		std::vector, std::deque, std::array""",
	},
    29: { # 06 module: merging stl algorithms
		'q':  """
		What's important to remember when using std::merge on two containers?""",
		'a': """
		Both containers must be sorted beforehand (using the same comparators e.g std::less)""",
	},
    30: { # 07 module: utilities and functional tools STL
		'q':  """
		i) What does <functional>'s std::ptr_fun do?
		ii) What is this functionality useful in combination with?""",
		'a': """
		i) Converts an input function into it's equivalent function object.
		ii) std::bind1st and std::bind2nd""",
	},
    31: { # 08 module: Advanced I/O
		'q':  """
		Define a stream?""",
		'a': """
		A stream can be defined as some kind of channel through which bytes are transmitted.""",
	},
    32: {
		'q':  """
		Name the three families of stream classes that STL I/O library
		provides functionality for?""",
		'a': """
		1) console/terminal streams
		2) file streams
		3) string streams""",
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
	}, # 09 module: templates
    37: {
		'q':  """
		What does RTTI stand for?""",
		'a': """
		Run time type information.""",
	},
    38: {
		'q':  """
		What's one notable limitation of templates?""",
		'a': """
		They have to be defined inside one file. I.e you cannot separate
		the declaration and the implementation in separate files.
		
		Templates are usually declared and defined inside a header file.""",
	},
    39: {
		'q':  """
		When is a template verified to be valid for a given type?""",
		'a': """
		When it is used to create and actual class or function.""",
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
}