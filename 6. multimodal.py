"""
多模态模型（Vision LLM）中把图片转成 Base64 的核心原因是：
API 请求通常是基于文本（JSON）的，而图片是二进制数据，必须先转换成文本形式才能安全地塞进请求体里。
"""
import base64
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.messages import HumanMessage

def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)
agent = create_agent(llm, tools = [])

image_path = 'resource/耄耋.jpg'
image_64 = encode_image_to_base64(image_path)
multimodal_message = HumanMessage(content=[
    {'type': 'text', 'text': '请描述这张图片'},
    {'type': 'image_url', 'image_url': {
        'url': f'data:image/jpeg;base64,{image_64}',
    }}
])

response = agent.invoke({'messages': [multimodal_message]})
print(response['messages'][-1].content)