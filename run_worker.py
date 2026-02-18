import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflows import LabTestWorkflow
from activities import check_connectivity

async def main():
    # Connect to the Temporal server
    client = await Client.connect("localhost:7233")
    print("run_worker.py connected to temporal server ... Creating the worker") 
    # Run the worker for a specific task queue
    worker = Worker(
        client,
        task_queue="lab-test-queue",
        workflows=[LabTestWorkflow],
        activities=[check_connectivity],
    )
    print("Worker is created, running and listening for tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
