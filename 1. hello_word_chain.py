


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


information = '''
    Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) 是特斯拉、SpaceX、X（前 Twitter）和政府效率部门（DOGE）的领导者。
    自2021年起他一直是世界首富，截至2025年5月，福布斯估算其净资产为4247亿美元。

    他出生于南非比勒陀利亚的一个富裕家庭，1989年移民加拿大，1997年在宾夕法尼亚大学获得学士学位，随后前往美国加州创业。
    1995年共同创立Zip2，1999年出售后创立X.com，后合并为PayPal。2002年PayPal被eBay收购，同年他成为美国公民。

    2002年创立SpaceX，2004年投资并于2008年担任特斯拉CEO。他还创立了Neuralink、Boring Company，并于2023年将Twitter更名为X。
    2024年他是美国大选最大捐助者，2025年初曾在特朗普政府担任高级顾问并领导DOGE，后因矛盾离开并宣布创建自己的政党“America Party”。
    '''

summary_template = """
    根据以下信息 {information}，为这个人生成内容：
    
    1. 一段简短的中文总结（150字以内）
    2. 两个有趣的事实（用中文）
    
    请直接用中文回复，不要添加多余解释。
    """

summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

llm = ChatOpenAI(
    model='my_local_model',
    base_url='http://127.0.0.1:1234/v1',
    api_key='none_for_need',
)

chain = summary_prompt_template | llm

# 1. invoke直接生成
# result = chain.invoke({'information': information})
# print(f"结果：{result.content}")


# 2. stream流式生成
print("=== 开始生成 ===\n")
for chunk in chain.stream({"information": information}):
    if chunk.content:
        print(chunk.content, end="", flush=True)






