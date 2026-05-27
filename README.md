# Hands-On-AI-Agents（坚持更新中2016-5-27）

用于演示与学习基于 LangChain/LangGraph 自定义工具的 AI agent 的示例集合。

本教程使用的所有模型均为本地部署，但使用AI供应商API同样适用。

由于本教程将随着我个人的学习而更新以及重新组织，所以有不足的地方请大家多多包涵。
也欢迎指出你认为我没有涉及到但很重要的知识，以及志同道合的朋友帮助我一同完善教程。

持续更新，喜欢的请⭐⭐⭐

本人承诺所有收益将用于偿还课程贷款（以及购买斐济悲）

## why this

Langchain框架的变动和更新速度非常快，导致很多教程和示例很快就过时了。
这个仓库旨在提供一个持续更新的、基于最新版本Langchain的AI agent示例集合，帮助大家更好地理解和使用这个框架。

个人来说，不推荐任何市面上的教程，因为你很可能在`form ... import ...`就遭遇报错，那实在是过于挫败了。
所以，索性自己做一个教程。

说实话，我就是被过时的教程与图书给折磨疯了，才会动手制作这个教程。
甚至Github上搜索的教程的大多过时了，要是langchain官方文档更像人类的话，我想我也不用费这个力气了。

## What's next

- MCP的详细教程
- ML Studio本地部署大模型
- 基础部分讲解（主要在做，现在存放于part_1_concept文件中，只是草稿，希望有个文笔好的朋友来帮助我；/(ㄒoㄒ)/~~）
- langgraph教程
- Agent理论部分知识
- 更清晰的圆头耄耋
- 把现有的教程变更为jupyter notebook形式(还在学习notebook的使用方法，主要是不会快捷键，相信会很快完成这一部分)
- 制作示例用的文件（.pdf, .csv等）

## 项目结构（部分）

- `hello_word_chain.py`
- `2.agent structured output.py`
- `3. tool usage.py`
- `4. web_search.py`
- `5. short-term memory.py`
- `6. multimodal.py`
- `7. mcp.py`
- `8. custome context.py`
- `resource/`（包含示例图片等资源）
- `README.md`
- `LICENSE`（请在仓库根目录添加此文件）

## 要求

- Windows（已在 Windows 环境下测试）
- Python 3.10+
- 建议使用虚拟环境

## 安装与配置

- 若仓库包含 `requirements.txt`，请使用该文件安装依赖；否则按需安装常见依赖（例如 `langchain`、`openai` 等）。
- 如使用外部 API（OpenAI 或本地 LLM 服务），请通过环境变量或配置文件设置相应的 `api_key` / `base_url`。

## 注意事项

- 确保虚拟环境已激活且依赖已正确安装。
- 文件名若包含空格，在命令行中请用引号或重命名以避免问题。
- 若使用本地模型或服务，检查服务地址、端口与防火墙设置。

## 赞助（Sponsorship）

如果该项目对你有帮助，欢迎通过以下方式支持：

- Buy Me a Coffee：
  <img src="resource/e3978777806a36a51cd901795f3805b1.jpg" width="200" alt="Buy Me a Coffee QR Code">

## 许可证

本仓库采用 MIT 许可证。

## 贡献

欢迎通过 PR 改进文档、添加 `LICENSE` 文件或补充信息。

## 参考资源

(sorry, i'm too lazy to put all resources with the link. I'll fill it(maybe, i hope so))

- [LangChain Academy](https://academy.langchain.com/)
- deeplearning.ai
- Udemy
- Coursera
- Langchain Doc
- some book
