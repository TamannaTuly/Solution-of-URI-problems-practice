# Read an integer value, which is the duration in seconds of a certain event in a factory, and inform
# it expressed in hours:minutes:seconds.
#
# Input
# The input file contains an integer N.
#
# Output
# Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.

duration = int(input())

hr = int(duration/3600)
min = int(duration/60)
sec = duration - (min*60)
min = min - (hr*60)

print(f'{hr}:{min}:{sec}')