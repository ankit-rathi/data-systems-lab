"""Run the deterministic Agent Workbench demonstration."""
from __future__ import annotations

import json
from pathlib import Path

from tools.tool_gateway import ToolRequest, authorize
from graders.grade_trace import grade

ROOT = Path(__file__).resolve().parent
trace = json.loads((ROOT / "traces" / "example_trace.json").read_text())

print("TRACE GRADE")
print(json.dumps(grade(trace), indent=2))
print("\nTOOL AUTHORIZATION")
for request in [
    ToolRequest("inspect_fixture", {}, 2),
    ToolRequest("sandbox_write", {}, 2),
    ToolRequest("deploy_with_approval", {}, 6, False),
    ToolRequest("deploy_with_approval", {}, 6, True),
]:
    print(request.name, "->", authorize(request))
