from agent_lab.tools.tool_gateway import ToolRequest, authorize
from agent_lab.graders.grade_trace import grade


def test_low_permission_cannot_write():
    assert authorize(ToolRequest("sandbox_write", {}, 2))["allowed"] is False


def test_deploy_requires_approval():
    assert authorize(ToolRequest("deploy_with_approval", {}, 6, False))["allowed"] is False
    assert authorize(ToolRequest("deploy_with_approval", {}, 6, True))["allowed"] is True


def test_trace_requires_independent_verification():
    trace={"goal":"x","context":[],"proposal":"y","verification":["test"],"decision":"revise","human_approval":False}
    assert grade(trace)["passed"] is True
