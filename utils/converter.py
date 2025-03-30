import json
import re

def convert_text_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<s>(.*?)</s>', re.DOTALL)
    blocks = pattern.findall(content)

    data = []
    for block in blocks:
        inst_match = re.search(r'\[INST\](.*?)\[/INST\]', block, re.DOTALL)
        if not inst_match:
            continue

        instruction = inst_match.group(1).strip()
        response = block[inst_match.end():].strip()
        
        data.append({
            "instruction": f"[INST]{instruction}[/INST]",
            "response": response
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')


convert_text_to_jsonl('data/psychoanalysis-micro.txt', 'data/psychoanalysis-micro.jsonl')