"""Quick demo: verify hivico library can be imported and run."""
import asyncio
import sys

# Add src to path for direct run
sys.path.insert(0, "src")

from hivico import HivicoClient, DeviceInfo, DeviceStatus, __version__

async def main():
    print("Hivico client demo")
    print("-" * 40)
    print(f"Version: {__version__}")
    async with HivicoClient(timeout=2) as client:
        # Only verify client creation
        print("Client ready; call get_device_status(device_ip) to query a real device")
    print("Library runs OK.")

if __name__ == "__main__":
    asyncio.run(main())
    print("-" * 40)
    print("Done.")
