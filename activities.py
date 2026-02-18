import subprocess
from temporalio import activity

@activity.defn
async def check_connectivity(target_ip: str) -> str:
    """Simple activity to ping a client in the lab."""
    try:
        # Pinging the client1 mgmt IP as a test
        result = subprocess.run(
            ["ping", "-c", "3", target_ip],
            capture_output=True,
            text=True,
            check=True
        )
        return f"Connectivity OK for {target_ip}: {result.stdout.splitlines()[-1]}"
    except subprocess.CalledProcessError as e:
        return f"Connectivity FAILED for {target_ip}: {e.stderr}"
