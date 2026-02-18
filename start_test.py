import asyncio
from temporalio.client import Client
from workflows import LabTestWorkflow

async def main():
    print(f"starting start_test.py script")

    client = await Client.connect("localhost:7233")
    print("client connected to serveur")
    # Start the workflow (we test connectivity to client1)
    result = await client.execute_workflow(
        LabTestWorkflow.run,
        "172.80.80.31",
        id="test-lab-connectivity_first",
        task_queue="lab-test-queue",
    )
    
    print(f"Workflow Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
