source for network lab : https://github.com/naveenachyuta/naf-temporal-2025/tree/main

# Step by step summary
1) Set up a lab on a Linux VM following: https://github.com/naveenachyuta/naf-temporal-2025/tree/main

2) Install Temporal with python extension : https://docs.temporal.io/develop/python/set-up-your-local-python , (bc python used for the POC)

Check that the temporal server can be launched : `temporal server start-dev`

3) Create a workflow and an activity : 
- workflow : defines the sequence of activities and handles the state. Workflows are  deterministic (no variables, all external interactions must go through activities).

- activity : on node of the workflow : coded function that performs a single&specific task (like configuring a router, sending an API call, or querying a DB). They are designed to be retried automatically if they fail.

4) Run the POC by creating a worker : process that polls the Temporal Server for tasks and executes your code.
- Start the Worker by creating a `run_worker.py` script to register your Workflows/Activities.
- Trigger the Workflow: Use a `start_workflow.py` script or the Temporal CLI to start the process.

To have temporalio : 
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install temporalio`

To use ansible in the activity : 
- `source env/bin/activate` 
`pip install ansible-runner`

To run the test : 
- start the server `temporal server start-dev`
- `source env/bin/activate`
`python3 run_worker.py`
- `source env/bin/activate`
`python3 start_test.py`


Notes : 
temporal is available with a wide range of languages  python, ruby, java, php … as long as the correct extension is installed

![Structure](Temporal-schéma.drawio (1).png)

