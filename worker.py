import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflows import LabTestWorkflow
from activities import check_connectivity

async def main():
    # Connect to your Temporal server (use the VM IP if remote)
    client = await Client.connect("localhost:7233")
    
    # Run the worker for a specific task queue
    worker = Worker(
        client,
        task_queue="lab-test-queue",
        workflows=[LabTestWorkflow],
        activities=[check_connectivity],
    )
    print("Worker is running and listening for tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
