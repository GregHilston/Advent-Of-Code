import time # for timing how long execution takes
import sys

start_time = time.time()

input_file_name = "../input.txt"
voltage = 0
voltages = {0: ""}

while True:
    for line in open(input_file_name):
        voltage += int(line)

        if voltage in voltages:
            print(f"first duplicate voltage: {voltage}")

            print("--- exeuction took %s seconds ---" % (time.time() - start_time))

            sys.exit(0)
        else:
            voltages[voltage] = ""