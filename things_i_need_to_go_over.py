things_i_need_to_go_over = {
	1: "passing multidimensional arrays to functions in c",
	2: "structs, pointers and memory allocation",
	3: "The entire priority of operators in C, you should easily know what ++b.a[2]-- should give, for example.",
	4: "How to malloc for various things inc. an array of structs.",
	5: "An array of functions in C",
	6: "Practice bitwise operations in C - find exercises.",
	7: "Reading/writing streams exercises in C. You should be able to easily do exercises previous of https://edube.org/quiz/c-essentials-part-2/c-essentials-part-2-module-7-quiz",
	8: "Size of common data types in bytes. I.e. when you put in sizeof(data_type)",
	9: "Common file processing functions and their expected parameters",
	9: "values of SEEK_SET, SEEK_CUR, SEEK_END",
	10: "preprocessor directives",
	11: "switch/case statements in C",
	


	# c++
	12: "common c++ manipulators: scientific, fixed etc",
	13: """
	c++ data types:

	This computing environment uses:
	1 bytes for chars
	2 bytes for shorts
	4 bytes for ints
	8 bytes for longs
	4 bytes for floats
	8 bytes for doubles
	1 byte for bools
	8 bytes for pointers
	""",
	14: """
	
	type promotion rules
	
	data of type char or short int will be converted to type int (this is called an integer promotion);
	data of type float undergoes a conversion to type double (floating point promotion);
	if there’s any value of type double in the expression, the other data will be converted to a double;
	if there’s any value of type long int in the expression, the other data will be converted to long int;
	""",
	15: """
	
	string methods
	
	.compare, .substr, .size, .length, .find, .capacity,
	.max_size, .reserve, .resize, .clear, .empty, .append, .push_back, .insert.
	.assign, .erase

	S.compare(substr_start, substr_length, other_string,  other_substr_start, other_substr_length)
	""",
	16: "definitely revise array of arrays: initialization, mem allocation, for looping etc",
	17: "revise type conversions used in binary operations",
	18: "floating points in c++",
	19: """ component visibility rules ---
	1. a static component accesses a static component = always possible
	2. a static component accesses a non-static component = e.g a static function calling a non-static function. This fails.
	3. a non-static component accesses a static component = always possible.
	4. a non-static component accesses a non-static component = always possible.
	
	""",
	20: """ class friendship rules ---
		1. a class may be a friend of many classes
		2. a class may have many friends
		3. a friend’s friend isn’t my friend
		4. friendship isn’t inherited – the subclass has to define its own friendships

		function friendship rules --

		1. a friendship declaration must contain a complete prototype of the friend function (including return type); a function with the same name, but incompatible in the sense of the parameters’ conformance, will not be recognized as a friend
		2. a class may have many friend functions
		3. a function may be a friend of many classes
		4. a class may recognize as friends both global and member functions
	
	""",
	21: """ Dynamic Casting rules ---
		1. dynamic_cast is used at run time to find out the correct down-cast
		2. Needs at least one virtual function in the base class to work.
		3. If dynamic_cast is successful, dynamic_cast returns a value of type new_type
		4. If the cast fails and new_type is a pointer, it returns a null pointer of that type
		5. If the cast fails and new_type is a reference type, is throws an exception that matches a handler of type std::bad_cast.
	""",
	22: """ Static Casting rules ---
		1. static casting a subclass (privately inherited) pointer to a superclass pointer fails at compile time
		2. static_cast can be used for all upcasts, but not for confused down casts
		3. static_cast should be preferred when converting to void* or from void*
	""",
	23: """ Const Casting rules ---
		1. The expression const_case<T>(v) can be used to change the const or v
	""",
	24: """ to revise ---
		Revise public, protected and private inheritance combinations
	""",
	25: """ to revise ---
		Go over the exception class hierarchy from module 3
	""",
	26: """
	quirk to watch out for: 
	"""
}