text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."

import re
def generate_sentence(text: str) -> str:
    pattern = '[A-Z]\w+'
    res2 = re.findall(pattern, text)

    new_str = " ".join(res2).lower() + '.'

    new_string = re.sub(r'^\w', new_str[:1].upper(), new_str)
    return new_string

print(generate_sentence(text))