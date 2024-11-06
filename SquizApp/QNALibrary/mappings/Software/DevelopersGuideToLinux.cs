namespace QNALibrary.mappings.Software
{
    public partial class DevelopersGuideToLinux : QNABase
    {
        public DevelopersGuideToLinux()
        : base(title: "David Cohen's 'Software Developer's Guide to Linux'", category: QNACategory.Software, qnaMapping: qnaMapping_)
        { }


        public override string ToString()
        {
            return "DevelopersGuideToLinux";
        }

        static Dictionary<int, Dictionary<string, string>> qnaMapping_ = new Dictionary<int, Dictionary<string, string>>()
        {
            {1, new Dictionary<string, string>() // Chapter 1 - How the Command Line Works
                {
                    { "q", @"
What is a command-line interface?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
A command-line interface is a text-based environment for interacting with your computer that:
    1) Reads some input from you
    2) Evaluates (or processes) that input
    3) prints some output to the screen in response, and then
    4) Loops back to (1) to repeat that process.

Steps (1) - (4) are known as REPL
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
True or false:
    In the context of the command-line, some programs might accept short and long versions
    of a parameter, usually denoted by single- vs. double-hyphenation,

    E.g -l and --long might do the same thing.
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
            {3, new Dictionary<string, string>()
                {
                    { "q", @"
Outline the difference between:
    1) The command line environment
    2) The shell
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Command line environment:
    - Any text-based environment that acts as a kind of REPL, specifically for interacting
        with the operating system
The shell:
    - specific program that implements this command-line environment and lets you give it
        text commands
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
State two commands which can be used to find the location/origin of a command e.g `ls`?
"                   },
                    {"snippetQ", @"
1) which ls
2) command -v ls
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
            {5, new Dictionary<string, string>()
                {
                    { "q", @"
a) What does POSIX stand for?
b) What is POSIX
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) POSIX = the portable operating system interface
b) Practically speaking, POSIX is an attempt at defining some common standards between Unix systems
    e.g. 'every POSIX-compatible OS should have a list command called ls'
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
Consider the 'ls' command, what happens when you:
    a) Run 'ls' without any arguments?
    b) Run 'ls' with a path (absolute or relate) passed in as an argument (e.g. 'ls /var/logs')?
    c) Run 'ls' with -l?
    d) Run 'ls' with -h?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) List the files and directories in your current directory
b) List the files and directories in the directory that you passed in
c) Same as (a) and (b) but will show a detailed view of permissions, modification dates etc
h) Will be listed in human-readable format
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
Consider the file permissions '-rw-r--r--' - the first character '-' corresponds to the file type:
State the file types represented by the following characters:

a) '-'
b) 'd'
c) 'l'
d) 'b'
e) 'c'
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) A regular file
b) Directory
c) Symbolic link
d) Block device
e) Character device
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
Breakdown and interpret the following file permissions sequence:
    -rwxr-xr-x
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
The first char '-' is the file type - and the '-' indicates that it is a regular file.

Next three chars 'rwx' repesent the 'owner' permissions, in this case they can
read, write and execute the file.

The following three chars 'r-x' represent the 'group' permissions, in this case they can
read, not write, but execute the file.

The final three chars represent 'others' permissions, they too can
read, not write, but execute the file.
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
Consider the following, which is an extract of the output of running 'ls -l' in bash:
    -rwxrwxrwx 1 noorudinburaleh noorudinburaleh  282 Apr  6  2023  desktop.ini

Breakdown what each of the columns represent.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Column 1:
    - File permissions
    - first char is the file type
    - next three chars are the owner permissions
    - following three chars are the group permissions
    - final three chars are the 'others' permissions

Column 2:
    - Number of references (hard links) to the file
    - In this case it is 1 which indiciates there's only one instance of this file
    
Column 3:
    - owner (username of the file's owner)

Column 4:
    - group (group that owns the file)

Column 5:
    - file size in bytes

Column 6:
    - Last modification date

Column 7:
    - File name
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
Breakdown the following commands:
    a) find . -type f -name tutorial.yml
    b) find . -type d -name learning
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Find in this current working directory (and any subdirectories) a file with the name 'tutorial.yml'
b) Find in this current working directory (and any subdirectories) a directory with the name 'learning'
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
State the command that allows you to read a file, one 'page'
(based on the size of your terminal window) at a time. 
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
less ${filename}
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
Fill in the blanks - all blanks refer to keyboard input.

    Running `less` will open the file and allow you to scroll through it, one line (__1___)
    or one page (___2___) at a time.

    To search inside the file type ___3___, followed by your search string, and hit ___4____.
    Navigate matchings with ___5___ (for next) and ___6___ (previous).
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) up/down arrow keys
2) spacebar
3) /
4) Enter
5) n
6) shift+n

BONUS: 'b' will do the opposite of spacebar i.e. take you one page back.
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
Assume your pwd is in ~.

Give the command for making the '/var/log/myapp/error' directory.
Assume '/var/log/myapp' parent directory does not exist.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
mkdir -p /var/log/myapp/error
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
Consider the command:
    rm –rf /path/to/directory

Explain what each of the following flags do:
    1) -r
    2) -f
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) -r 
    - 'recursive'
    - applies removals recursively (i.e. to all directories contained by the one 
        you're deleting).

2) -f
    - 'force'
    - forces deletion without a confirmation for each file and directory.
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
            {15, new Dictionary<string, string>() // Chapter 2: Working with Processes
                {
                    { "q", @"
What does the term 'process' refer to in linux?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
The term 'process' in linux refers to the operating system's internal model of what exactly 
a running program is.

It is a ge
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
Which command can you run to get a listing of all system processes that your user is allowed to see?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
ps aux
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
True or false:
    All processes (except the init process, PID=1) are spawned by a parent.
    If the parent process dies while the child is alive, the child becomes an 'orphan'.
    Orphaned processes are re-parented to init (PID=1).
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
            {18, new Dictionary<string, string>()
                {
                    { "q", @"
Each process has a current working directory. How can you get the current working directory of a given process.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Step 1:
    - get the process id out from the output of e.g. 'ps aux'
Step 2:
    - Once you have the process id, run 'pwdx $PROCESS_ID'
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
Consider the ps command which shows processes on the system. Which flags should you use if
    1) You want to show thread information for the processes
    2) You want to see the relationships between parent and child processes visually
        (chldren are indented under their parents)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) ps -eLf
2) ps -ejH
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
State the command you would run if you would like:
    1) An interactive program that polls all processes (once a second by default)
       and outputs a sorted list of resource usage (by default).

    2) An interactive program that polls all processes and sorts for disk I/O.
       This program is useful for finding IO-hungry processes.

    3) Like (1),but for network I/O
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) top
2) sudo iotop (requires 'sudo apt install iotop')
3) sudo nethogs (requires 'sudo apt install nethogs')
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
In the context of Unix and Linux, what is a 'signal'?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Signals are numerical messages that can be sent between programs. They're a way
for processes to communicate with each other and with the operating system, allowing processes
to send and receive specific messages.
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
If the process you'd like to terminate has PID 2600, what would you run?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
kill 2600
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
What does the following signal represent:
    SIGHUP (1)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
SIGHUP (1):
    - 'hangup'
    - interpreted by many applications as 're-read your configuration because I've made changes to it'
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
What does the following signal represent:
    SIGINT (2)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
SIGINT (2):
    - 'interrupt'
    - equivalent to 'CTRL+c'
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
What does the following signal represent:
    SIGTERM (15)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
SIGTERM (15):
    - 'terminate'
    - nicely asks a process to shutdown
    - this is the default signal when 'kill $PID' is called without a signal specified.
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
What do the following signals represent:
    - SIGUSR1 (30)
    - SIGUSR2 (31)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
These signals are sometimes used for application-defined messaging.

E.g. SIGUSR1 asks nginx to re-open the log files it's writing to.
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
What does the following signal represent:
    SIGKILL (9)
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
SIGKILL (9):
    - cannot be trapped and handled by processes.
    - if this signal is sent to a program, the operating system will kill that program immediately.
    - any cleanup code, like flushing writes or safe shutdown is not performed
    - considered a last resort, since it could lead to data corruption
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
            {29, new Dictionary<string, string>()
                {
                    { "q", @"
What command would I run if I want a list of files that a process (say 1589) has open?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
lsof -p 1589
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
            {30, new Dictionary<string, string>() // Chapter 3 - Service Management with systemd
                {
                    { "q", @"
a) What are services (also frequently called daemons)?
b) Give a few examples of services/daemons.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) Services/daemons are long-running processes that run in the background.
b) Examples of services/daemons include:
    1) Databases
    2) Web servers
    3) Network manager
    
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
How are services/daemons typically started and controlled?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Via an init system such as systemd
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
What is an `init` system?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
An `init` system refers to the first process your operating system kernel starts, and it is the 
job of this process to take care of starting any other processes.
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
What is `systemctl`?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
`systemctl` is a commandline utility for:
    - controlling systemd services.
    - e.g. start/stop/restart a service that's been misbehaving or to reload one
        whose configuration has changed.

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
Outline the two tools you'll use to interact with systemd.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
1) systemctl:
    - controls services (called 'units' in systemd nomenclature)
2) journalctl:
    - lets you work with systems logs. 
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
In the context of service management, what is meant by a 'unit file'?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
Sservices are defined by a unit file, which specifies exactly how the service should be managed
by systemd.
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
Let a systemd service be called <service> - how would you use systemd to:
    1) Start the service
    2) Stop the service
    3) Restart the service
    4) Display the current status of the service
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"

    systemctl start <service>
    systemctl stop <service>
    systemctl restart <service>
    systemctl status <service>
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
Let's talk about the common `init` term in Linux:
    a) What is the process ID of init
    b) What is init responsible for?
    c) Aside from systemd, what other init systems exist?
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
a) PID 1
b) init is responsible for:
    - managing the boot process
    - starting all other processes and services that have been configured to run on the system
    - re-parenting orphaned processes (i.e. processes whose original parents have died) and keeping
      them as its own children
c) Other init systems:
    - SysV
    - OpenTC
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
'A service adds convenient features to how a program (and the resulting process spawned by that program)
is handled by the system'.

Give a few examples of this.
"                   },
                    {"snippetQ", @"
"},
                    { "a", @"
For example, a service:
    - lets you define dependencies between different processes
    - control startup order
    - add environment variables for the process to start with
    - limit resource usage
    - control permissions
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
            {40, new Dictionary<string, string>()
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
            {41, new Dictionary<string, string>()
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
            {42, new Dictionary<string, string>()
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
            {43, new Dictionary<string, string>()
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
            {44, new Dictionary<string, string>()
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
            {45, new Dictionary<string, string>()
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
            {46, new Dictionary<string, string>()
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
            {47, new Dictionary<string, string>()
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
            {48, new Dictionary<string, string>()
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
            {49, new Dictionary<string, string>()
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
            {50, new Dictionary<string, string>()
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
            {51, new Dictionary<string, string>()
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
            {52, new Dictionary<string, string>()
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
            {53, new Dictionary<string, string>()
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
            {54, new Dictionary<string, string>()
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
            {55, new Dictionary<string, string>()
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
            {56, new Dictionary<string, string>()
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
            {57, new Dictionary<string, string>()
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
            {58, new Dictionary<string, string>()
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
            {59, new Dictionary<string, string>()
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
            {60, new Dictionary<string, string>()
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
            {61, new Dictionary<string, string>()
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
            {62, new Dictionary<string, string>()
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
            {63, new Dictionary<string, string>()
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
            {64, new Dictionary<string, string>()
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
            {65, new Dictionary<string, string>()
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
            {66, new Dictionary<string, string>()
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
            {67, new Dictionary<string, string>()
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
            {68, new Dictionary<string, string>()
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
            {69, new Dictionary<string, string>()
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
            {70, new Dictionary<string, string>()
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
            {71, new Dictionary<string, string>()
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
            {72, new Dictionary<string, string>()
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
            {75, new Dictionary<string, string>()
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
            {76, new Dictionary<string, string>()
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
            {77, new Dictionary<string, string>()
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
            {78, new Dictionary<string, string>()
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
            {79, new Dictionary<string, string>()
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
            {80, new Dictionary<string, string>()
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
            {81, new Dictionary<string, string>()
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
            {82, new Dictionary<string, string>()
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
