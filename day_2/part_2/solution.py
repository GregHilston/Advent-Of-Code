import sys
from datetime import datetime # to time how long execution took

startTime = datetime.now()

input_file_name = "../input.txt"
_end = '*'

def hamming_distance(str1, str2):
    """From https://stackoverflow.com/questions/31007054/hamming-distance-between-two-binary-strings-not-working"""
    diff_count = 0

    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diff_count += 1
    
    return diff_count

def find_common_characters(str1, str2):
    common_characters = []

    for ch1, ch2 in zip(str1, str2):
        if ch1 == ch2:
            common_characters.append(ch1)

    return ''.join(str(x) for x in common_characters)

def look_for_other_word_one_hamming_distance_away(root, base_word, built_word):
    # print(f"root {root}")
    # print(f"base_word {base_word}")

    if isinstance(root, dict):
        for letter, d in root.items():
            # print(f"\tbuilt_word {built_word}")
            # print(f"\tletter {letter}")
            # print(f"\td {d}")

            look_for_other_word_one_hamming_distance_away(d, base_word, built_word + letter)
    else:
        built_word = built_word.strip(_end)
        # print("\tdone")
        # print(f"\tbuilt_word {built_word}")

        if hamming_distance(base_word, built_word) == 1:
            print(f"found two words one hamming distance away: {base_word} and {built_word}")
            
            common_characters = find_common_characters(base_word, built_word)
            print(f"common characters between two strings with hamming distance of 1 {common_characters}")

            sys.exit(0)

def construct_trie(words):
    root = dict()

    for word in words:
        current_dict = root
        
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end

        # print("start")
        look_for_other_word_one_hamming_distance_away(root, word, "")
    return root

with open(input_file_name) as file:
    ids = []
    
    for line in file:
        ids.append(line.strip('\n'))

    trie = construct_trie(ids)

    # print(trie)

print(f"execution took {datetime.now() - startTime}")