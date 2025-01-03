﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QNALibrary.mappings.CPP
{
    public class ModernCMake : QNABase
    {
        public ModernCMake()
        : base(title: "Rafat Swidzinski's Modern CMake for C++", category: QNACategory.CPP, qnaMapping: qnaMapping_)
        { }

        public override string ToString()
        {
            return "ModernCMake";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>()
        {
            {1, new Dictionary<string, string>() // Chapter 1 - First Steps with CMake
                {
                    { "q", @"
a) What is a modern alternative to 'cmake ..' that you should be implementing?
    Hint: Assume you're in the same directory that you'd be in if you ran 'cmake ..'

b) Why is your answer to (a) a better way of configuring a CMake project?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) 'cmake -B . -S ..'
b) With 'cmake -B . -S ..' you have the opportunity to explicitly specify both your build tree and 
    your source tree.

    This explicitness avoids ambiguity and makes your CMake configuration command self-documenting, particularly
    in scripts or multi-build setups.

    With 'cmake ..' it is implicit that you have to be in the build tree.

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {2, new Dictionary<string, string>()
                {
                    { "q", @"
What is the:
    a) Build tree
    b) Source tree
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Build tree:
    - path of your build output directory

b) Source tree:
    - path at which your source code (including CMakeLists.txt) is located.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {3, new Dictionary<string, string>()
                {
                    { "q", @"
The CMake process has three stages:
    1. Configuration
    2. Generation
    3. Building

Give an overview of the configuration stage.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Summary:
    - reading project details stored in the source tree
    - preparing the output directory, or build tree, for the generation stage

Detail:
    - Reads cached configuration variables from a CMakeCache.txt file if it exists
    - Collects environmental details such as:
        what the architecture is, what compilers are available, what linkers and archivers are installed
    - The CMakeLists.txt project configuration file is parsed and executed
    
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {4, new Dictionary<string, string>()
                {
                    { "q", @"
The CMake process has three stages:
    1. Configuration
    2. Generation
    3. Building

Give an overview of the generation stage.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
After reading the project configuration, CMake will generate a buildsystem for the exact
environment it is working in.

During this stage, CMake applies some final touches to the build configuration by evaluating
generator expressions.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {5, new Dictionary<string, string>()
                {
                    { "q", @"
The CMake process has three stages:
    1. Configuration
    2. Generation
    3. Building

Give an overview of the building stage.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
CMake runs the appropriate build tool to produce target artifacts with:
    - compilers
    - linkers
    - static and dynamic analysis tools
    - test frameworks
    - reporting tools
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {6, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following statement:
    'After reading the project configuration, CMake will generate a buildsystem for the exact environment it is working in.'

What is meant by a 'buildsystem' in this context?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Buildsystems are cut-to-size configuration files for other build tools, for example:
    - Makefiles for GNU Make or Ninja
    - IDE Project files (.sln) for Visual Studio
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {7, new Dictionary<string, string>()
                {
                    { "q", @"
CMake is a family of tools and consists of five executables:
    1) cmake
    2) ctest
    3) cpack
    4) cmake-gui
    5) ccmake

Outline each of them. Additionally, explain the purpose of 'CDash'.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) cmake:
    - the main executable that configures, generates and builds projects
2) ctest:
    - the test driver program used to run and report test results
3) cpack:
    - the packaging program used to generate installers and source packages.
4) cmake-gui:
    - the graphical wrapper around cmake
5) ccmake:
    - console-based GUI wrapper around cmake

CDash is a separate tool which provides advanced oversight over the health of our projects' builds.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {8, new Dictionary<string, string>()
                {
                    { "q", @"
One important feature of CMake is the support for out-of-source builds.

What is meant by 'out-of-source builds'?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
An 'out-of-source build' is a dedicated directory for storing build artifacts. This directory (often named 'build')
is separate from the source tree.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {9, new Dictionary<string, string>()
                {
                    { "q", @"
a) What is a generator and what does a generator do?
b) Give a few examples of CMake generators and what they produce.
c) How can you specify to CMake that you'd like to configure CMakeLists.txt with a particular generator?
d) How can you find the list of available generators to your system?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) A generator is a tool that determines the type of build system or project files CMake generates for your builds.
    When you configure a project with CMake, the generator specifies how CMake translates your CMakeLists.txt into 
    actual build instructions e.g. Makefiles, Ninja, .sln or .vcxproj files.

b) A few examples of CMake generators include:
    1) Unix MakeFiles:
        - generates Makefiles
    2) Visual Studio %version% %year%
        - generates .sln and .vcxproj files
    3) Ninja:
        - generates Ninja build files, optimized for speed and simplicity

c) use the -G option e.g.
    cmake -G ""Visual Studio 17 2022"" -S <source_tree> -B <build_tree> 

d) Type 'cmake --help' for an output of available generators.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {10, new Dictionary<string, string>()
                {
                    { "q", @"
Outline the implications the following possible values for the cache variable CMAKE_BUILD_TYPE:
    1) Debug
    2) Release
    3) RelWithDebInfo
    4) MinSizeRel

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Debug:
    - Enables debugging symbols (e.g. -g on gcc/clang)
Release:
    - Enables optimization (e.g. -O3) but disables debugging symbols
RelWithDebInfo:
    - Optimized build with debugging symbols (e.g. -O2 -g)
MinSizeRel:
    - Optimized for minimum size (e.g. -0s)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {11, new Dictionary<string, string>()
                {
                    { "q", @"
a) What is the difference between single-configuration vs. multi-configuration generators?
b) How can you determine whether a given generator is single-configuration vs. multi-configuration generators?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Single-configuration generators only support one build configuration per build directory.
    Multi-configuration generators support multiple configurations in the same build directory (build tree)

b) Only single-configuration generators will have the CMAKE_BUILD_TYPE variable present or specified in 
    the CMakeCache.txt file.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {12, new Dictionary<string, string>()
                {
                    { "q", @"
Assume the terminal is in the build tree and this command is run:
    cmake -S .. -B . -D CMAKE_BUILD_TYPE=Debug

Which flag should I add if I want to list out the cache variables to the console?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
The -L flag e.g. 'cmake -L -S .. -B . -D CMAKE_BUILD_TYPE=Debug'

Example output:
    -- Configuring done (0.0s)
    -- Generating done (0.0s)
    -- Build files have been written to: /home/noorudinburaleh/learning/modern_cmake/01ch/01-hello/build_tree
    -- Cache values
    CMAKE_BUILD_TYPE:STRING=Debug
    CMAKE_INSTALL_PREFIX:PATH=/usr/local
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {13, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    (1) cmake -LA -S .. -B . -D CMAKE_BUILD_TYPE=Debug
    (2) cmake -LAH -S .. -B . -D CMAKE_BUILD_TYPE=Debug

a) What does the -A flag do?
b) What does the -H flag do?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) -A (architecture) prints out architecture information to the console
b) -H (help) prints out usage documentation / help
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {14, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    cmake -U <globbing_expression> -S <source_tree> -B <build_tree>

What does the -U flag allow for?

Note: 'globbing_expression' supports the * (wildcard) and ? (any character) symbols. 
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
In this case, -U will remove any cache variables that satisfy the <globbing_expression>.
Note that you should be careful with this as you may erase more variables than intended.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {15, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the folowing:
    cmake -S <source_tree> -B <build_tree>

How can I modify this to use 'trace mode' - which will print out every
executed command with its filename, the line number it is called from, and a list of passed
arguments?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
By using the '--trace' flag, concretely:
    cmake --trace -S <source_tree> -B <build_tree>

Note: The output can be long and is not recommended for everyday use.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {16, new Dictionary<string, string>()
                {
                    { "q", @"
a) What problem do CMake presets solve?
b) In which file can a client user find the available presets?
c) What would you execute on the commandline to list all available presets?
d) What would you execute on the commandline to use one of the available presets?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) CMake presets 'pre set' CMake variables with default values for the convenience of client users of the source code
b) CMakePresets.json
c) cmake --list-presets
d) cmake --preset=<preset> -S <source_tree> -B <build_tree>
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {17, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    cmake -S <source_tree> -B <build_tree>

a) Which flag should we add if we want to wipe out the files in the CMakeFiles/ directory
as well as the CMakeCache.txt file i.e. generate the buildsystem from scratch?

b) Why would we want to do this?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Use --fresh
b) To ensure that we are building with the latest CMakeLists.txt configuration - as sometimes cached variables
in, for example, CMakeCache.txt are not picked up by changes made in CMakeLists.txt between builds.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {18, new Dictionary<string, string>()
                {
                    { "q", @"
Let's say you're in a UNIX-like system and using CMAKE_GENERATOR=""Unix Makefiles""
after you've configured and produced your Makefiles file with:
    'cmake --fresh -S <source_tree> -B <build_tree>'

Is it recommended to use 'make' to produce the artifacts in your system? Why/why not?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Is is not recommended to use a platform-dependent command like 'make' at the build stage.
Instead, it is a preferred to use the platform-independent CMake command:
    'cmake --build <build_tree>' which is generator-independent.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {19, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    cmake --build <build_tree>

a) How would you enhance this by specifying that 4 builders should run in parallel?

b) Why would you want to have the build running in parallel?

c) When would you NOT want the build to run in parallel?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Either of the following:
    1) 'cmake --build <build_tree> --parallel 4'
    2) 'cmake --build <build_tree> -j 4'

b) To leverage modern multi-processors and save client users' time.

c) For debugging, you would want to force a single-threaded build to output the --trace
    sequentially.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {20, new Dictionary<string, string>()
                {
                    { "q", @"
a) What is meant by a 'target' in the CMake context?
b) Give a few examples of targets
c) Consider the snippet of a CMakeLists.txt and consider the following build command:
    'cmake --build <build_tree>'
  
    How can we enhance this so that the above command applies to the target 'Hello'?
"                   },
                    {"snippetQ", @"
// # CMakeLists.txt file
cmake_minimum_required(VERSION 3.26)
project(Hello)
add_executable(Hello hello.cpp)
"},
                    { "a", @"
a) A target represents an entity that CMake manages and builds.
   
b) Examples of targets include:
    - an executable defined with 'add_executable'
    - a library defined with 'add_library'
    - a custom build step defined with 'add_custom_target'

c) 'cmake --build . --target Hello'

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {21, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following command:
    'cmake -build <build_tree> -t clean'

a) What does the above command do?
b) Offer the command to execute if you want to clean first and then build.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) The above commands removed any build artifacts from the <build_tree> location
    - this is the generator-independent equivalent of 'make clean' when using CMAKE_GENERATOR=""Unix Makefiles""

b) 'cmake --build <build_tree> --clean-first'.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {22, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following command:
    'cmake --build <build_tree>'

What would you add to the above to get details logs of the build process?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Either of the following, which are equivalent:
    (1) cmake --build <build_tree> --verbose
    (2) cmake --build <build_tree> -v
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {23, new Dictionary<string, string>()
                {
                    { "q", @"
a) What are workflow presets?
b) Offer the command you would execute to:
    i)  list out the available workflow presets
    ii) executing a particular workflow with the name 'name'
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Workflow presets automate and unify the steps of configure, build and test
    in a single command. They are define in CMakePresets.json
b) 
    i)  'cmake --workflow --list-presets'
    ii) 'cmake --workflow --preset  name'
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {24, new Dictionary<string, string>()
                {
                    { "q", @"
State two alternative names for the build tree?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) Build root
2) Binary tree
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {25, new Dictionary<string, string>()
                {
                    { "q", @"
a) What are files that contain the CMake language called?
b) State three ways that your answer to (a) can include one in another?
c) By convention, what is the file extension to your answer to (a)?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) listfiles
    Note: Due to historical reasons, the CMake project configuration file has 'CMakeLists.txt'
b) By using `include()`, `find_package()` or indirectly via `add_subdirectory()`
c) .cmake
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {26, new Dictionary<string, string>()
                {
                    { "q", @"
When the configure stage is run for the first time, the cache variables generated
from the listfiles are stored to which file?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
CMakeCache.txt
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {27, new Dictionary<string, string>()
                {
                    { "q", @"
State the two files that store CMake presets and explain their individual purpose. 
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) CMakePresets.json:
    - meant for project authors to provide official presets.
2) CMakeUserPresets.json:
    - dedicated to individual users who want to customize the project configuration to their liking
    - should be added to .gitignore, any presets meant to be shared should be in CMakePresets.json
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {28, new Dictionary<string, string>()
                {
                    { "q", @"
Besides the primary focus of building projects and producing artifacts that get
consumed by other systems, what two other concepts can be implemented via CMake?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) CMake scripts:
    Run with 'cmake -P my_script.cmake'

2) Modules:
    - external modules which enhance the functionality of CMake projects
    - examples include: CPack, Ctest
    - use the 'include(<MODULE>)' command in a listfile to include them.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {29, new Dictionary<string, string>() // Chapter 2 - The CMake Language
                {
                    { "q", @"
True or false:
    Everything in a CMake listfile is either a comment or a command invocation.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {30, new Dictionary<string, string>()
                {
                    { "q", @"
Provide an example of a nested multiline comment in a .cmake listfile.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
#[=[
    #[[
        nested comment
    #]]
#]=]
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {31, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the snippet of a .cmake listfile and determine if the statement is true or false:
    Command names (e.g. `message`) are case-sensitive, so the call (1) is not necessarily the same
    as call (2).
"                   },
                    {"snippetQ", @"
cmake_minimum_required(VERSION 3.28)

message(""hello"" world) (1)
MESSAGE(""hello"" world) (2)
"},
                    { "a", @"
False. In .cmake list files command invocations aren't case-sensitive, so (1) and (2)
will yield the same behaviour.

Note: the convention is to prefer snake_case
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {32, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    In .cmake listfiles, each line of source code can only contain one command.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {33, new Dictionary<string, string>()
                {
                    { "q", @"
CMake commands can be categorized into two groups:
    1) Scripting commands
    2) Project commands

For each category of the command state the:
    a) scope
    b) purpose
    c) Give a few examples
    d) impact on the build (direct or indirect?)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) Scripting commands:
    a) scope:  always available (inside or outside a project)
    b) purpose: control flow, variable manipulation and file handling
    c) `set`, `if`, `foreach`, `file`, `include`
    d) indirect impact (e.g., setting variables or manipulating files)

2) Project commands:
    a) scope: only relevant in the context of a project
        (i.e. in a scope where 'project' command has been invoked already)
    b) purpose: define and manage build targets, dependencies and tools
    c) `project`, `add_executable`, `add_library`, `install`
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {34, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

How many arguments are being passed in:
    1) line (1)
    2) line (2)
"                   },
                    {"snippetQ", @"
cmake_minimum_required(VERSION 3.28)

message(argu\ end\;1) # (1)
message(arg;ume nts)  # (2)
"},
                    { "a", @"
1) 1
2) 3
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {35, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    'project(myProject VERSION 1.2.3)'

True or false:
    Keywords in CMake are case-insensitive, i.e the above is equivalent to:
    'project(myProject version 1.2.3)'
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
False - keywords such as 'VERSION' are case-sensitive.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {36, new Dictionary<string, string>()
                {
                    { "q", @"
What is meant by the phrase 'CMake run(s)'?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
A 'CMake run' refers to the configuration step of the CMake process:
    'cmake -S <source_tree> -B <build_tree>'

This is when CMake reads the CMakeLists.txt file(s) and generates the buildsystem files
in the specified build tree.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {37, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    a) CMake variable names are case-sensitive and can include almost any character
    b) All CMake variables are stored internally as strings, even if some commands can interpret them
        as values of other data types (even lists!)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) true
b) true
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {38, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the  snippet from a .cmake listfile.

What would be printed on line:
    a) 1
    b) 2
    c) 3
    d) 4
"                   },
                    {"snippetQ", @"
cmake_minimum_required(VERSION 3.28)
set(MyString1 ""Text1"")
set(Text1 ""Hello2"")

message(${MyString1}) # (1)
message(${Text1})     # (2)

set(${MyString1} ""Changed"")
message(${MyString1}) # (3)
message(${Text1})     # (4)

"},
                    { "a", @"
a) Text1
b) Hello2
c) Text1
d) Changed
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {39, new Dictionary<string, string>()
                {
                    { "q", @"
Provide the syntax used to REFERENCE:
    a) normal or cache variables
    b) environment variables
    c) strictly cache variables
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) ${}
b) $ENV{}
c) $CACHE{}
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {40, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following documentation on how to set cache variables:
    'set(<variable> <value> CACHE <type> <docstring> FORCE)'

What does the FORCE option do?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
The FORCE option forces the cmake configuration process to override any values that may already be
in the CMakeCache.txt.

Without the FORCE option, variables that have already been set in CMakeCache will not change.

Alternatively, you can use
    'cmake -D<variable>=""<new_value>"" -L -S <source_tree> -B <build_tree>'

To override a cache value, and -L for listing the values to the console during configuration.

NOTE that the above was no affect when a cache variable is set to FORCE.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {41, new Dictionary<string, string>()
                {
                    { "q", @"
CMake has two kinds of variable scopes, state and outline them.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
CMake variable scopes:
    1) File:
        - used when blocks and custom functions are executed within a file.

    2) Directory:
        - used when the `add_subdirectory()` command is called to execute another
            CMakeLists.txt listfile in a nested directory.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {42, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    Conditional blocks, loop blocks and macros don't create separate
    scopes in CMake.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {43, new Dictionary<string, string>()
                {
                    { "q", @"
State the two command pairs that open a 'file variable scope' in CMake.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) block() and endblock()
2) function() and endfunction()
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {44, new Dictionary<string, string>()
                {
                    { "q", @"
For each of the following, give the if clause to check if the variable type if defined:
    1) normal variable
    2) cache variable
    3) environment variable
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) 'if(DEFINED <name>)'
2) 'if(DEFINED CACHE{<name>})'
3) 'if(DEFINED ENV{<name>})'
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {45, new Dictionary<string, string>()
                {
                    { "q", @"
You can define your own command with either of the following commands:
    1) macro()/endmacro()
    2) function()/endfunction()

State the difference between these two.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) macro() / endmacro()
    - analagous to C-style preprocessor macros
    - works more like find-and-replace than actual subroutine
    - calling return() from a macro will return to the calling statement one level higher than the callee's

2) function() / endfunction()
    - analagous to actual C++ function
    - creates a local scope for its variable, unlike macro() / endmacro()
    - calling return() returns to the calling statement of the callee
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {46, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    You should prefer function() / endfunction() where possible over macro() / endmacro()
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {47, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following of the modes of the `message()`, indicating some kind of deficiency
to the user - give an overview of each:
    1) FATAL_ERROR
    2) SEND_ERROR
    3) WARNING
    4) AUTHOR_WARNING
    5) DEPRECATION
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) FATAL_ERROR:
    - stops processing and buildsystem generation
2) SEND_ERROR:
    - continues processing but skips generation
3) WARNING
    - continues processing
4) AUTHOR_WARNING:
    - A CMake warning, continues processing
5) DEPRECATION:
    - works accordingly if CMAKE_ERROR_DEPRECATED or CMAKE_WARN_DEPRECATED is enabled.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {48, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following of the modes of the `message()`,
indicating some kind of logging severity to the user - give an overview of each:
    1) NOTICE
    2) STATUS
    3) VERBOSE
    4) DEBUG
    5) TRACE
    
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) NOTICE:
    - the default
    - prints a message to stderr to attract the user's attention
2) STATUS:
    - continues processing
    - recommended for main messages to users
3) VERBOSE:
    - continues processing
    - should be used for more detailed information that usually isn't very necessary
4) DEBUG:
    - continues processing
    - contains fine details that might be helpful when there's an issue with a project
5) TRACE:
    - continues processing
    - recommended to print TRACE messages during project development
    - these sorts of messages should be removed before publishing the project
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {49, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet of 'message_context.cmake':

What do I need to add to 'cmake -P message_context.cmake' to get the output
below?
"                   },
                    {"snippetQ", @"
cmake_minimum_required(VERSION 3.28)

function(foo)
    list(APPEND CMAKE_MESSAGE_CONTEXT ${CMAKE_CURRENT_FUNCTION})
    message(""foo message"")
endfunction()

list(APPEND CMAKE_MESSAGE_CONTEXT ""global"")
message(""before foo"")
foo()
message(""after foo"")

output:
# [global] before foo
# [global.foo] foo message
# [global] after foo
"},
                    { "a", @"
cmake -P message_context.cmake --log-context
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {50, new Dictionary<string, string>()
                {
                    { "q", @"
When we include files that have side effects, we may want to restrict them
so that they're only included once, state the command for:
    a) when we want to include the .cmake listfile once per directory
    b) when we want to include the .cmake listfile once per project
    c) when we want to include a particular .cmake file, say utilities.cmake, once
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) include_guard() or include_guard(DIRECTORY)
b) include_guard(GLOBAL)
c) include_guard(utilities.cmake)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {51, new Dictionary<string, string>() // Chapter 3 - Using CMake in Popular IDEs
                {
                    { "q", @"
a) What does cross-compilation involve?
b) How does remote development differ from cross-compilation?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Cross-compilation involves using a specialized toolchain that allows a compiler
running on one platform (like Windows) to produce artifacts for another platform (like Linux).

b) In remote development, you sesnd your code to the target machine and build it there using the
local toolchain.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {52, new Dictionary<string, string>() // Chapter 4 - Setting Up Your First CMake Project
                {
                    { "q", @"
True or false:
    The call to `cmake_minimum_required(VERSION <version>)` implicitly triggers
    another command, cmake_policy(VERSION) - which specifies the policies to be used
    for the project.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {53, new Dictionary<string, string>()
                {
                    { "q", @"
What is the primary purpose of CMake policies?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
To manage backward-incompatible changes - each policy enables the new behaviour
associated with that backward-incompatible change.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {54, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    It is recommended to put the `project()` command immeditately after `cmake_minimum_required()`.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True as doing so will ensure we have the right policies when configuring the project.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {55, new Dictionary<string, string>()
                {
                    { "q", @"
What is the difference between CMAKE_PROJECT_NAME and PROJECT_NAME?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
CMAKE_PROJECT_NAME only applies to the project name of the top-level CMakeLists.txt
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {56, new Dictionary<string, string>()
                {
                    { "q", @"
Consider: 
    'project(hello_world)'

a) By default, which lanauges are enabled for a project in CMake?
b) How can you enhance the above to only look for C++ compilers?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) C and C++
b) You can specify C++ as the only language for the project by setting the LANGUAGES keyword:
    'project(hello_world LANGUAGES CXX)'
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {57, new Dictionary<string, string>()
                {
                    { "q", @"
Breakdown the following comman:
    'add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])'
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) add_subdirectory adds the 'source_dir' to our builds
2) [binary_dir] is the optional location for a path that build files will be written to
3) [EXCLUDE_FROM_ALL] keyword will disable the automatic building of targets defined in the subdirectory
    (useful for separating parts of the project that aren't needed for the core functionality)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {58, new Dictionary<string, string>()
                {
                    { "q", @"
State a few pros of using add_subdirectory
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) Variables are isolated to the nested scope
2) The nested artifacts can be configured independently
3) Modifying the nested CMakeLists.txt that is referenced in add_subdirectory
    doesn't require building unrelated targets.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {59, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the add_library command:
    'add_library(<name> [<type>] [EXCLUDE_FROM_ALL] <sources>...)'

For each of the following add_library <type> options, state the output (if any)
and the purpose of the option:

1) STATIC
2) SHARED
3) MODULE
4) INTERFACE
5) OBJECT
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) STATIC: 
    output: static library (.a or .lib)
    purpose: reusable, statically linked code
2) SHARED:
    output: shared library (.so, .dll)
    purpose: dynamically linked, reusable code
3) MODULE:
    output: shared library for runtime (also .so, .dll)
    purpose: plugins or dynamically loaded libraries
4) INTERFACE:
    output: no compiled output
    purpose: for header-only or property-based library
5) OBJECT:
    output: object files (.o, .obj)
    purpose: to share compiled object files across targets
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {60, new Dictionary<string, string>()
                {
                    { "q", @"
Which CMAKE_* variable would you turn to in order to support multiple target
operating systems with a single CMake script.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
CMAKE_SYSTEM_NAME - see snippet
"
                    },
                    {"snippetA", @"
if(CMAKE_SYSTEM_NAME STREQUAL ""Linux"")
# 1> [CMake] -- CURRENTLY USING CMAKE_SYSTEM_NAME = Linux
	message_cmake_system_name(CMAKE_SYSTEM_NAME)
elseif(CMAKE_SYSTEM_NAME STREQUAL ""Darwin"")
	message_cmake_system_name(CMAKE_SYSTEM_NAME)
elseif(CMAKE_SYSTEM_NAME STREQUAL ""Windows"")
# 1> [CMake] -- CURRENTLY USING CMAKE_SYSTEM_NAME = Windows
	message_cmake_system_name(CMAKE_SYSTEM_NAME)
elseif(CMAKE_SYSTEM_NAME STREQUAL ""AIX"")
	message_cmake_system_name(CMAKE_SYSTEM_NAME)
else()
	message(FATAL_ERROR ""UNHANDLED CASE CMAKE_SYSTEM_NAME: ${CMAKE_SYSTEM_NAME}"")
endif()
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {61, new Dictionary<string, string>()
                {
                    { "q", @"
True or false:
    In 64-bit architecture, memory addresses, processor registers, processor instructions,
    address buses, and data buses are 64 bits wide.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {62, new Dictionary<string, string>()
                {
                    { "q", @"
Say you are dealing with a project with the topmost CMakeLists.txt having:
    'set(CMAKE_CXX_STANDARD 23)'

a) Will this standard propagate to all downstream targets?
b) If you have a downstream target (named <target>) which must compile with C++14, state the command
    you would offer to achieve this.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) yes
b) set_property(TARGET <target> PROPERTY CXX_STANDARD 14)

Note: We override with 'CXX_STANDARD' and not 'CMAKE_CXX_STANDARD'
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {63, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following snippet:

a) Explain what is going on?
b) Outline the significance, pros and cons adding lines (1)-(4) to a CMakeLists.txt cmake listfile?
"                   },
                    {"snippetQ", @"
cmake_minimum_required(VERSION 3.26)
project(Structure CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(CheckIPOSupported)                               # (1)
check_ipo_supported(RESULT ipo_supported)                # (2)
message(STATUS ""IPO supported: ${ipo_supported}"")        # (3)
set(CMAKE_INTERPROCEDURAL_OPTIMIZATION ${ipo_supported}) # (4)

add_subdirectory(src bin)

"},
                    { "a", @"
a) (1) - include the .cmake logic to bring the check_ipo_supported in
   (2) - setting the result of whether IPO is supported to variable `ipo_supported`
   (3) - message for enduser purposes
   (4) - setting the ipo option on depending on whether IPO is actually supported

b) significance:
    - interprocedural optimization at link time, a.k.a link-time optimization
    - allows all compilation units to be optimized as a unified module

   pro:
    - in principle will achieve better (optimization) results

   cons:
    - slower builds, more memory consumption
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {64, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the snippet from a topmost CMakeLists.txt file:

What is being guarding against exactly?
"                   },
                    {"snippetQ", @"
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)

    mesage(FATAL_ERROR ""Can't do this"")
endif()
"},
                    { "a", @"
In-source builds
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {65, new Dictionary<string, string>() // Chapter 5 - Working with Targets
                {
                    { "q", @"
In software engineering, two components are said to be connascent if...?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Two components are said to be connascent if a change in one would require
the other to be modified in order to maintain the overall correctness of the system.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {66, new Dictionary<string, string>()
                {
                    { "q", @"
a) What does a CMake target represent?
b) True or false:
    Targets can have dependencies on other targets, and their construction follows a 
    declarative approach.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Logical unit that focuses on a specific object
b) True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {67, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    'target_sources(<target> [PRIVATE | PUBLIC | INTERFACE] <source1> [<source2> ...])'

What is the purpose of 'target_sources'?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
`target_sources` allows you to explicitly manage the files associated with a target
in a modular and flexible way.

E.g. adding Windows-specific files to the target if(CMAKE_SYSTEM_NAME == ""Windows"") / endif()
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {68, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    'add_executable(<target_name> [WIN32] [MACOSX_BUNDLE] [EXCLUDE_FROM_ALL] [source1] [source2 ...])'

What is the consequence of specifying the 'EXCLUDE_FROM_ALL' keyword?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
The 'EXCLUDE_FROM_ALL' keyword when specified, will prevent the executable target
from being built in a regular, default build. Such a target will have to be explicitly called with
    'cmake --build -t <target_name>'
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {69, new Dictionary<string, string>()
                {
                    { "q", @"
What's the difference (in intention) between:
    1) `target_link_libraries()`
    2) `add_dependencies()`
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) `target_link_libraries()`:
    - intended to be used with actual libraries
    - allows you also to control property propagation

2) `add_dependencies()`:
    - meant to be used only with top-level targets to set their build order
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {70, new Dictionary<string, string>()
                {
                    { "q", @"
a) Offer the command you would run to generate a .dot file to visualize
the DAG dependency created in a CMake project.

b) True or false:
    custom targets are not visible by default

c) If (b) is true, offer the property you would set to allow for custom targets
    to be visualized.

d) What would you use this link for? https://dreampuf.github.io/GraphvizOnline/?engine=dot
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) cmake --graphviz=test.dot <source_tree>

b) True

c) set(GRAPHVIZ_CUSTOM_TARGETS ON)

d) Pop in the contents of your .dot file into that location to visualize the dependencies in your CMake project
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {71, new Dictionary<string, string>()
                {
                    { "q", @"
a) What is a pseudo target?
b) State the three pseudo targets.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) pseudo targets:
    - represent inputs such external dependencies, aliases or other non-build artifacts
    - do not represent outputs of the buildsystem and are not represented in the generated buildsystem
b)
    1) imported targets
    2) aliases
    3) interface libraries
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {72, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the following:
    'add_executable(<alias_name> ALIAS <existing_target>)
    add_library(<alias_name> ALIAS <existing_target>)'

True or false:
    a) Properties of alias targets are read only
    b) You cannot install aliases
    c) You can export aliases
    d) Aliases are visible in the generated buildsystem
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) True
b) True
c) False - you cannot export (build) aliases
d) False - aliases are not visible in the generated buildsystem
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {73, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {74, new Dictionary<string, string>()
                {
                    { "q", @"
a) What are the two primary uses of interface libraries?
b) Which command would we use to achieve both purposes?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a)
    1) To represent header-only libraries
    2) To bundle propagated properties into a single logical unit

b) add_library
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {75, new Dictionary<string, string>()
                {
                    { "q", @"
Which buildsystem target does CMake generate by default to contain all top-level listfile
targets, such as executeables and libraries (not necessarily custom targets)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
ALL. <- this is run when we run the standard 'cmake --build <build_tree>'

Note that (1) and (2) are equivalent:
    'cmake --build <build_tree>' (1)
    'cmake --build <build_tree> --target all' (2, note lowercase)
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {76, new Dictionary<string, string>()
                {
                    { "q", @"
Consider the 'add_custom_target' command.

True or false:
    a) By default, targets created with 'add_custom_target' are excluded from the ALL target
    unless you explicitly add them with a ALL keyword.
    b) In order for the `clean` target to work correctly, you need to manually specify any
        files that your custom targets create as BYPRODUCTS.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) True
b) True
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {77, new Dictionary<string, string>() // Chapter 6 - Using Generator Expressions
                {
                    { "q", @"
As you know, CMake has three stages:
    1) Configuration
    2) Generation
    3) Building

At which stage are generator expressions / 'genexes' evaluated?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
You guessed it, (2) the generation stage.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {78, new Dictionary<string, string>()
                {
                    { "q", @"
What problem do generator expressions solve?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Generator expressions solve the ""chicken and egg"" paradox where data
required in the configuration stage of CMake is only made available once the configuration
stage is complete and the buildsystem is generated.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {79, new Dictionary<string, string>()
                {
                    { "q", @"
Outline what the following generator expressions return:
    a) $<CONFIG>
    b) $<CONFIG:config>
    c) $<PLATFORM_ID>
    d) $<PLATFORM_ID:platform>
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

a) Returns the current configuration as a string i.e. 'Debug', 'Release'
b) Returns true if `configs` contains the current build configuration (case-insensitive comparison)
c) Returns the current platform ID as a string, 'Linux', 'Windows' or 'Darwin' for macOS
d) Returns true if `platform` contains the current platform ID.
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {80, new Dictionary<string, string>()
                {
                    { "q", @"
Outline what the following generator expressions return:
    a) $<CXX_COMPILER_ID>
    b) $<CXX_COMPILER_VERSION>
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Returns CMake's compiler ID of the C++ compiler used
b) Returns CMake's compiler version of the C++ compiler used
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {81, new Dictionary<string, string>()
                {
                    { "q", @"
What is the difference between:
    a) 'target_link_libraries(libA PRIVATE libB)'
    b) 'target_link_libraries(libA PRIVATE $<LINK_ONLY:libB>)'
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a)
    - Directly links libB to libA as a private dependency.
    - All of libB's usage requirements (include directories, compile definitions) 
      are propagated to libA

b)  - libA has ability to resolve symbol references with libB
    - libB's usage requirements (include directories, compile definitions) 
      are NOT propagated to libA 
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {82, new Dictionary<string, string>()
                {
                    { "q", @"
Offer the target query generator expression for the following cases:
    a) returns true if the target exists
    b) returns the target name if the target exists and an empty string otherwise
    c) return the `prop` property value for the target
    d) returns a list of object files for an object library target
    
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) $<TARGET_EXISTS:target>
b) $<TARGET_NAME_IF_EXISTS:target>
c) $<TARGET_PROPERTY:target,prop>
d) $<TARGET_OBJECTS:target>
"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {83, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {84, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {85, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {86, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {87, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {88, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {89, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {90, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {91, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {92, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {93, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {94, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {95, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {96, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {97, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {98, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {99, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {100, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {101, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {102, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {103, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {104, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {105, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {106, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {107, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {108, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {109, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {110, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {111, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {112, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {113, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {114, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {115, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {116, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {117, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {118, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {119, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {120, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {121, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {122, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {123, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {124, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {125, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {126, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {127, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {128, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {129, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {130, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {131, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {132, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {133, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {134, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {135, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {136, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {137, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {138, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {139, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {140, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {141, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {142, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {143, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {144, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {145, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {146, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {147, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {148, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {149, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {150, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {151, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {152, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {153, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {154, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {155, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {156, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {157, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {158, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {159, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {160, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {161, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {162, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {163, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {164, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {165, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {166, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {167, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {168, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {169, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {170, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {171, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {172, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {173, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {174, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {175, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {176, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {177, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {178, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {179, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {180, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {181, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {182, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {183, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {184, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {185, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {186, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {187, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {188, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {189, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {190, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {191, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {192, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {193, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {194, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {195, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {196, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {197, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {198, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {199, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },
            {200, new Dictionary<string, string>()
                {
                    { "q", @"

"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

"
                    },
                    {"snippetA", @"
"
                    },
                    {"imgQ", @"
"
                    },
                    {"imgA", @"
"
                    },
                }
            },

        };

    }
}
