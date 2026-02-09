"""Hivico device API client."""

from .client import (
    HivicoClient,
    HivicoClientSync,
    HivicoError,
    ConnectionError,
    DeviceInfo,
    DeviceStatus,
    discover_devices,
)

__all__ = [
    "HivicoClient",
    "HivicoClientSync",
    "HivicoError",
    "ConnectionError",
    "DeviceInfo",
    "DeviceStatus",
    "discover_devices",
]

__version__ = "0.1.0"
