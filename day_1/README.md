## Part One

To make parsing easier, we can simply add every number together instead of having to check the sign and correctly subtract or add. This is because of the "commutative property of addition".

## Part Two

Originally, I stored the past voltages in a list and would check if the list contained a new voltage. After running and seeing that execution took forever, I remembered that a `contains` method on a list would take `O(n)` time, so I swapped my storage data structure to a dictionary (hash table) and improved lookup time to `O(1)`, which improved run time significantly.

Additionally, I originally did not understand that I had to look over the file multiple times.