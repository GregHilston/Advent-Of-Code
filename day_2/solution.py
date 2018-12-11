from datetime import datetime # to time how long execution took

startTime = datetime.now()

input_file_name = "input.txt"

with open(input_file_name) as handle:
    two_char_count = 0
    three_char_count = 0

    for line in handle:
        d = {}
        already_found_two_char = False
        already_found_three_char = False

        for char in line:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        print(d)

        for key, value in d.items():
            # print(f"value = {value}, already_found_two_char = {already_found_two_char} and already_found_three_char = {already_found_three_char}")
            if value == 2 and already_found_two_char == False:
                two_char_count += 1
                already_found_two_char = True
                # print(f"\tfound two pair {key}")
            elif value == 3 and already_found_three_char == False:
                three_char_count += 1
                already_found_three_char = True
                # print(f"\tfound three pair {key}")
        #break

print(f"checksum = {two_char_count * three_char_count}")
print(f"execution took {datetime.now() - startTime}")