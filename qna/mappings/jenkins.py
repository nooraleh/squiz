# Notes taken in a QNA style from Nikhil Pathania's
# 'Learning Continuous Integration with Jenkins, 2nd Edition'

qna = {
    1: {
		'q':  """
		What is a Jenkins 'freestyle job'?
		""",
		'a': """
		A Jenkins freestyle job is:
			- the classic way of creating a pipeline
			- each CI stage is represented using a Jenkins job
			- is web-based, GUI-propelled configuration
		""",
	},
    2: {
		'q':  """
		Outline some of the advantage of 'Pipeline as Code' for Jenkins
		pipeline creation?
		""",
		'a': """
		1) It's programmable
		2) All of your CI/CD pipeline configurations can be described using
			just a single file (Jenkinsfile)
		3) It's version controllable
		4) Option to use 'Declarative Pipeline' syntax
		""",
	},
    3: {
		'q':  """
		What is a Declarative Pipeline typically composed of?
		""",
		'a': """
		1) `node` blocks (node)
		2) `stage` blocks (stages)
		3) directives
		4) steps

		NB: A single `node` block can have multiple `stage` blocks,
			and vice versa.
		""",
	},
    4: {
		'q':  """
		i)  What does the `node` block define?
		ii) Write a brief template of what the `node` block should look like?
		""",
		'a': """
		i)  The `node` block defines the Jenkins agent wherein its 
			constituents (stage blocks, directives and steps) should run.
		ii) node ('<paramter>') {<constituents>}
		""",
	},
    5: {
		'q':  """
		i)  What does the 'stage' block define?
		ii) Write a brief template of the `stage` block structure.
		""",
		'a': """
		i)  The `stage` block is a collection of closely related steps
			and directives that have a common objective.
		ii) stage ('<parameter>') {<constituents>}
		""",
	},
    6: {
		'q':  """
		In the context of the Declarative Pipeline, what is the main purpose of directives?
		""",
		'a': """
		The main purpose of directives is to assist the:
			- `node` block
			- `stage` block
			- and steps
		by providing them with any of the following elements:
			- environments
			- options
			- parameters
			- triggers
			- tools
		""",
	},
    7: {
		'q':  """
		Consider the following snippet:
			
			node ('master') {
				// contents...
			}

		Explain the meaning of the preceding code.
		""",
		'a': """
		The string 'master' is a parameter (`label`) that tells Jenkins
		to use the Jenkins master for running the contents of the `node`
		block.
		""",
	},
    8: {
		'q':  """
		The built-in node has been rename from 'master node' to ...?
		""",
		'a': """
		'built-in node'
		""",
	},
    9: {
		'q':  """
		What does a Multibranch pipeline allow for?
		""",
		'a': """
		A Multibranch pipeline allows you to automatically create a 
		pipeline for each branch on your source control repository.
		""",
	},
    10: {
		'q':  """
		Outline the three stages of the automated deployment pipeline?
		""",
		'a': """
		1) Continuous integration
		2) Automated acceptance testing
		3) Configuration management
		""",
	},
	11: {
		'q':  """
		Explain what the following terms entail:
			1) Automated acceptance testing
			2) Configuration management
		""",
		'a': """
		1) Automated acceptance testing - this checks if the client's requirements have
			been met by the developers implementing the features. This testing replaces the
			manual QA phase.

		2) Configuration management - This replaces the manual operations phase; it
			configures the environment and deploys the software.
		""",
	},
	12: {
		'q':  """
		What is meant by:

			i)  Exploratory testing
			ii) Non-functional testing

		And state whether each of the preceding are manual or automated.
		""",
		'a': """
			i)  Exploratory testing - is the manual black-box testing phase, which
					tries to break or improve the system. Manual.
			ii) Non-functional testing - tests that represent system properties related
					to performance, scalability, security and so on. Automated.
		""",
	},
	13: {
		'q':  """
		Briefly outline what is meant by Infrastructure as Code (IaC).
		""",
		'a': """
		IaC - if you use the cloud instead of bare-metal servers, then tools such as
			Terraform or AWS CloudFormation let you store the description of your
			infrastructure in the version control system.
		""",
	},
	14: {
		'q':  """
		What is the difference between continuous delivery and continuous deployment?
		""",
		'a': """
		Continous delivery:
			Less strict and means that each commit ends up with a release candidate,
			so it allows the last step (from release to production) to be manual.
		Continuous deployment:
			Means each commit to the repository is automatically released to production.
		""",
	},
	15: {
		'q':  """
		i)  What is meant by 'trunk-based development'?
		ii) What software development implications are there in the absence of trunk-based
			development.
		""",
		'a': """
		i)  Developers must check changes into one centralized main branch regularly.
		ii) Otherwise, if everyone develops in their branches, integration is rare,
			which means that releases are rare, which is exactly the opposite of the
			ideal continous delivery approach.
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