from langchain.prompts import PromptTemplate
from component.embedding import Jinaembedding
from component.databases import Vectordatabase
from openai import OpenAI

class Openai_model:
    def __init__(self,model_name:str='gpt-3.5-turbo',temperature:float=0.9) -> None:
        #初始化大模型
        self.model = OpenAI(api_key="sk-zBYOSwgd6AyAc7OFlVN5igxvPQlyVha3L2H0qPebuHqxMQS9", base_url="https://api.gpts.vin/v1")
        self.model_name=model_name
        self.temperature=temperature

        #加载向量数据库，embedding模型
        self.db=Vectordatabase()
        self.db.load_vector()
        self.embedding_model=Jinaembedding()
        
    #定义chat方法
    def chat(self,question:str):
        #这里利用输入的问题与向量数据库里的相似度来匹配最相关的信息，填充到输入的提示词中
        template="""使用以上下文来回答用户的问题。如果你不知道答案，就说你不知道。总是使用中文回答。
        问题: {question}
        可参考的上下文：
        ···
        {info}
        ···
        如果给定的上下文无法让你做出回答，请回答数据库中没有这个内容，你不知道。
        有用的回答:"""
        info=self.db.query(question,self.embedding_model,3)
        prompt=PromptTemplate(template=template,input_variables=["question","info"]).format(question=question,info=info)
        # print(prompt)
        res = self.model.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            )
        return  res.choices[0].message.content