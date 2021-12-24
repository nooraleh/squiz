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
}