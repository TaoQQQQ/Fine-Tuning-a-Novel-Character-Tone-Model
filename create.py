from openai import OpenAI
import re

def load_segments_from_file(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        segments = re.split(r'《段落\d+》', content)
        # 移除可能存在的空字符串
        segments = [seg.strip() for seg in segments]
    return segments

def chat(input_content):
    prompt = "我现在想制作小说特定角色萧薰儿（别名熏儿，薰儿）语气的训练集，制作成我需要的对话数据集的格式，也就是常见的问答数据语料，请不要用第三视角制作数据集。需要你阅读文本，把其中有关萧炎和萧薰儿的对话内容提取出来，如萧炎问:我现在还有资格让你怎么叫么？萧熏儿答:萧炎哥哥，以前你曾经与薰儿说过，要能放下，才能拿起，提放自如，是自在人！参考我给的例子，理解上下文的语义和角色，以问答的格式输出，请注意，萧炎是提问人，萧熏儿是回答的人，不需要不符合条件的问答。\n 参考格式：问:xxxxxx\n答:xxxxxxxx\n 这样的格式制作数据集。最后，下面是原文："
    message = [
    {
        "role": "system",
        "content": prompt
    },
    {"role": "user", "content": input_content}]

    # 例子用的是智谱，Qwen也是一个调用格式，改下apikey和url就行
    try:
        response = client.chat.completions.create(
            model = "glm-4.5",
            messages = message,
            top_p = 0.7,
            temperature = 0.5
        )
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        print(f"处理问题出错：错误信息：{e}")

def chat_with_llm(segments_list, output_file):

    with open(output_file, 'a+', encoding='utf-8') as file:
        for i,question in enumerate(segments_list):
            answer = chat(question)
            print(f"第{str(i + 1)},段： {answer}\n")
            file.write(f"{answer}\n\n")

if __name__ == "__main__":
    # 使用OpenAI格式进行对话，一般大模型供应商会提供这种格式的调用
    client = OpenAI(
        api_key = "",
        base_url = ""
    )
    # 假设的文件路径，请替换为您的实际文件路径
    file_path = "./split.content.txt"
    # 输出文件的名称
    output_file = "./train.txt"
    
    # 从文件加载段落
    questions = load_segments_from_file(file_path)
    # 使用大模型提取人物对话
    chat_with_llm(questions, output_file)
