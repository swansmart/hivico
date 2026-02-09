# Hivico

Hivico is a lightweight HTTP API client library for HiVi speakers.

## Installation

```bash
pip install hivico
```

## Quick start

```python
import asyncio
from hivico import HivicoClient

async def main():
    async with HivicoClient(timeout=5) as client:
        status = await client.get_device_status("192.168.1.100")
        print(status)

asyncio.run(main())
```

## Features

- Query device status and info
- Query / control groups
- Basic playback control and volume settings

## Home Assistant integration

The [HiVi Speaker](https://github.com/swansmart/hivi_speaker) custom integration depends on this library; install `hivico` from PyPI.

## License

Apache License 2.0
