import re

from copy import out_path


def read_txt_file(file_path):
    # 读取txt文件内容并返回
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 '{file_path}'")
        return None
    except Exception as e:
        print(f"错误：读取文件时发生异常 - {e}")
        return None


def find_character_positions(text, characters):
    all_names = []
    name_to_canonical = {}

    for canonical, aliases in characters.items():
        for name in [canonical] + aliases:
            all_names.append(name)
            name_to_canonical[name] = canonical

    # 按名称长度排序，避免子串优先匹配
    all_names_sorted = sorted(all_names, key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(name) for name in all_names_sorted))
    result = []
    for match in pattern.finditer(text):
        matched_name = match.group(0)
        canonical_name = name_to_canonical[matched_name]
        result.append({
            "canonical_name": canonical_name,
            "matched_name": matched_name,
            "start": match.start(),
            "end": match.end(),
        })
    return result

def split_context(characters, content):

    content = content.replace('\n', '').replace(' ', '').replace('\t', '').replace('　　', '')
    characters = {
        "萧薰儿": ["熏儿", "薰儿"]
    }
    matches = find_character_positions(content, characters)
    # 按10000长度作为切割长度
    # 若是两个名字出现的位置过远，舍弃则中间这段，两个名字分别作为新的段落
    length = 10000
    last_pos = matches[0]['start']
    paragraphs = []
    i = 1
    for i, match in enumerate(matches):
        end_pos = match['end']
        if match['end'] - last_pos < length:
            continue
        if match['end'] - last_pos > 2 * length:
            if matches[i - 1]['end'] == last_pos:
                last_pos = match['end']
                continue
            else:
                end_pos = matches[i - 1]['end']
                flag = 1
        text = content[content.rfind('。', 0, last_pos) + 1:content.find('。', end_pos) + 1]
        paragraphs.append(f'《段落》{str(i)}\n' + text)
        i += 1
        last_pos = end_pos
        # 如果两个词间距过大，需要更新一下last_pos
        if flag:
            last_pos = match['end']
            flag = 0
        return paragraphs

if __name__ == "__main__":

    file_path = ""  # 替换为实际文件路径
    out_path = "" # 替换为实际文件路径
    # 找需要提取的角色名，格式如下"官方名字":["别名","常见含错别字的名字"]，如
    # characters = {
    #     "萧薰儿": ["熏儿", "薰儿"],
    #     "萧炎":["小炎子"，“炎帝”]
    # }
    # 字典类型
    characters = {
         "萧薰儿": ["熏儿", "薰儿"]
    }
    content = read_txt_file(file_path)
    paragraphs = split_context(characters, content)
    with open(out_path, 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph + '\n\n')




