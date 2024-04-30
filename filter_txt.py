from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import language_tool_python
import re

tool = language_tool_python.LanguageTool('en-US')


def remove_fuzzy_repeats(text, threshold=70):
    """
    Remove fuzzy repeated parts of the text.
    """
    lines = text.split('\n')
    result_lines = []
    for line in lines:
        # Process the current line only if it's not already present in the result_lines
        if not process.extractOne(line, result_lines, scorer=fuzz.partial_ratio, score_cutoff=threshold):
            result_lines.append(line)
    return '\n'.join(result_lines)


def correct_grammar(text, ignore_words):
    """
    Correct grammar and spelling mistakes in the text, excluding the ignored words.
    """
    tool = language_tool_python.LanguageTool('en-US')

    # Correct the text
    matches = tool.check(text)
    for word in ignore_words:
        matches = [match for match in matches if word.lower() not in match.context.lower()]

    return language_tool_python.utils.correct(text, matches)


def process_text_file(input_file_path, output_file_path, ignore_words):
    # Read the file
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except UnicodeDecodeError:
        with open(input_file_path, 'r', encoding='latin-1') as file:
            text = file.read()

    text = correct_grammar(text, ignore_words)
    text = remove_fuzzy_repeats(text)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)


input_file_path = 'Character Details.txt'
output_file_path = 'Character Details filtered.txt'
# later will move ignore words into another file
ignore_words = ['Liyue', 'Wangsheng', 'Mondstadt', 'Teyvat', 'Rex', 'Lapis', 'Abyss', 'Dvalin', 'Venti', 'Zhongli',
                'Hu Tao', 'Xiao', 'Childe', 'Diluc', 'Klee', 'Jean', 'Barbara', 'Lisa', 'Kaeya', 'Amber', 'Razor',
                'Bennett', 'Fischl', 'Sucrose', 'Xingqiu', 'Beidou', 'Ningguang', 'Noelle', 'Chongyun', 'Qiqi',
                'Keqing', 'Mona', 'Xiangling', 'Traveler', 'Albedo', 'Ganyu', 'Rosaria', 'Eula', 'Ayaka', 'Yoimiya',
                'Sayu', 'Kokomi', 'Sara', 'Raiden', 'Kujou', 'Kujou', 'Sara', 'Kamisato', 'Kamisato', 'Ayaka']

process_text_file(input_file_path, output_file_path, ignore_words)

