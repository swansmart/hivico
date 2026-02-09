"""Call get_device_status: query HiVi device status by IP."""
import asyncio
import sys

# Add src to path for direct run
sys.path.insert(0, "src")

from hivico import HivicoClient

async def main():
    # Device IP: from command line if given, else default (change to your speaker IP)
    ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.100"
    print(f"Querying device status: {ip}")
    print("-" * 40)
    async with HivicoClient(timeout=5) as client:
        status = await client.get_device_status(ip)
    if status is not None:
        print("Device status:", status)
    else:
        print("No status (timeout or not a HiVi device).")

if __name__ == "__main__":
    asyncio.run(main())
