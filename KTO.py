import json

def transform(content):
    n = len(content)
    dialogue_list = []
    dialogue = []
    for i in range(n - 2):
        if content[i].startswith("问") and content[i + 1].startswith("答") and content[i + 2].startswith("评价"):
            dialogue = {"messages": [], "label": None}
            dialogue["messages"].append({"content": content[i][2:], "role": "user"})
            dialogue["messages"].append({"content": content[i + 1][2:], "role": "assistant"})
            # print(content[i + 2])
            dialogue["label"] = True if content[i + 2][3:4] == "好" else False
            dialogue_list.append(dialogue)
            i += 3
    return dialogue_list

if __name__ == "__main__":
    # 定义文件路径
    file_path = 'C:\\Users\\11050\\Desktop\\虚假的人工智能\\赛博萧炎\\文档\\kto.txt'
    # 输出目录
    output_file_path = 'C:\\Users\\11050\\Desktop\\虚假的人工智能\\赛博萧炎\\文档\\kto.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    content = transform(content)

    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(content, json_file, ensure_ascii=False, indent=4)

