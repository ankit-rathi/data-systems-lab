"""Shared helpers for Data Systems Lab notebooks."""

from __future__ import annotations

import os
import platform
import sys
import time
from pathlib import Path


def environment_report() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "cwd": str(Path.cwd()),
        "pid": os.getpid(),
    }


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def timed(label: str):
    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            return self

        def __exit__(self, *args):
            elapsed = time.perf_counter() - self.start
            print(f"{label}: {elapsed:.4f} s")
    return Timer()
