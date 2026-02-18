from datetime import timedelta
from temporalio import workflow

# Import the activity with a safety check for Temporal
with workflow.unsafe.imports_passed_through():
    from activities import check_connectivity

@workflow.defn
class LabTestWorkflow:
    @workflow.run
    async def run(self, ip_to_test: str) -> str:
        return await workflow.execute_activity(
            check_connectivity,
            ip_to_test,
            start_to_close_timeout=timedelta(seconds=20)
        )
