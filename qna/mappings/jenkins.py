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
}