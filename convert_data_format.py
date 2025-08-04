import json

def convert_format(content_list):

    data_json = []
    for i in range(len(content_list) - 1):
        # 问答对的冒号可能是中文或英文
        if content_list[i].startswith('问') and content_list[i+1].startswith('答'):
            instruction = content_list[i].split('问', 1)[1].strip()[1:]
            output = content_list[i+1].split('答', 1)[1].strip()[1:]
            data_json.append({
                "instruction": instruction,
                "input": "",
                "output": output
            })
    return data_json



if __name__ == "__main__":
    # 定义文件路径
    file_path = ''
    # 输出目录
    output_file_path = ''

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    data_json = convert_format(content)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, ensure_ascii=False, indent=4)