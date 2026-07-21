from typing import Annotated, TypedDict
import operator
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send, RetryPolicy

# ---------- 1. State 定义 ----------
class OverallState(TypedDict):
    topic: str
    subtopics: list[str]
    summaries: Annotated[list[dict], operator.add]  # 并行结果用 reducer 累加
    final_report: str

class SubtopicState(TypedDict):
    # Send 分发给每个 summarize_node 的局部 state（节点模板的输入）
    topic: str
    subtopic: str
    index: int

# ---------- 2. 规划节点 ----------
def plan_node(state: OverallState) -> dict:
    topic = state["topic"]
    # 实际项目中应调用 LLM 生成子主题，这里用示例代替
    subtopics = [f"{topic}的历史", f"{topic}的现状", f"{topic}的未来趋势"]
    return {"subtopics": subtopics}

# ---------- 3. 分发控制函数 ----------
MAX_PARALLEL = 5

def dispatch_to_summarize(state: OverallState):
    subtopics = state["subtopics"][:MAX_PARALLEL]      # 数量控制
    subtopics = list(dict.fromkeys(subtopics))          # 去重
    if not subtopics:
        return []  # 为空则不分发（需注意此时图会在此终止）
    return [
        Send("summarize_node", {
            "topic": state["topic"],
            "subtopic": s,
            "index": i,
        })
        for i, s in enumerate(subtopics)
    ]

# ---------- 4. 节点模板：summarize_node ----------
def summarize_node(state: SubtopicState) -> dict:
    """只依赖 Send 传入的最小字段，内部做错误隔离"""
    try:
        subtopic = state["subtopic"]
        # 实际项目：调用 LLM 做摘要，这里用示例代替
        content = f"关于「{subtopic}」的摘要内容（示例）"
        result = {"index": state["index"], "subtopic": subtopic,
                   "content": content, "status": "ok"}
    except Exception as e:
        result = {"index": state.get("index", -1), "subtopic": state.get("subtopic", "unknown"),
                   "content": None, "status": f"error: {e}"}
    return {"summaries": [result]}

# ---------- 5. 汇总节点 ----------
def aggregate_node(state: OverallState) -> dict:
    summaries = sorted(state["summaries"], key=lambda x: x["index"])
    ok = [s for s in summaries if s["status"] == "ok"]
    failed = [s for s in summaries if s["status"] != "ok"]
    body = "\n\n".join(f"## {s['subtopic']}\n{s['content']}" for s in ok)
    report = f"# {state['topic']} 综合报告\n\n{body}"
    if failed:
        report += f"\n\n（{len(failed)} 个子任务失败）"
    return {"final_report": report}

# ---------- 6. 构建图 ----------
builder = StateGraph(OverallState)
builder.add_node("plan", plan_node)
builder.add_node("summarize_node", summarize_node, retry_policy=RetryPolicy(max_attempts=3))
builder.add_node("aggregate", aggregate_node)

builder.add_edge(START, "plan")
builder.add_conditional_edges("plan", dispatch_to_summarize)
builder.add_edge("summarize_node", "aggregate")
builder.add_edge("aggregate", END)

graph = builder.compile()

result = graph.invoke({
    "topic": "人工智能",
    "subtopics": [],
    "summaries": [],
    "final_report": ""
})
print(result["final_report"])