import re

with open('/Users/arcsinx/code/websites/xmarva.github.io/_posts/2025-04-17-building-a-transformer.md', 'r+', encoding='utf-8') as file:
    content = file.read()

    updated_content = re.sub(r'(?<!\$)\$(?!\$)', '$$', content)

    file.seek(0)
    file.write(updated_content)
    file.truncate()

print("Complete!")