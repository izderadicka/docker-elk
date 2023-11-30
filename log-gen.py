#!/usr/bin/env python3

import datetime
import random
import argparse
import time

# Expected probabilities for each level
LEVELS=[("DEBUG", 10), ("INFO", 80), ("WARNING", 5), ("ERROR", 4), ("CRITICAL", 1)]
_total = sum([level[1] for level in LEVELS])
assert _total == 100, "Total probability should be 100% accros all levels"
_LEVELS = [level[0] for level in LEVELS]
_WEIGHTS = [level[1] for level in LEVELS]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='output_file')
    parser.add_argument('--max-lines', type=int, help='Maximum lines one run should generate')
    parser.add_argument('--frequency', type=float, help='Frequency of messages per second')
    return parser.parse_args()

# Open the file containing the words
with open('/usr/share/dict/words', 'r') as f:
    words = f.read().splitlines()

def random_level():
    return random.choices(population=_LEVELS, weights=_WEIGHTS, k=1)[0]

def random_message(min_length=5, max_length=10):
    length = random.randint(min_length, max_length)
    return ' '.join([random.choice(words) for _ in range(length)])

def main():
    args = parse_args()
    count = 0
    with open(args.file, 'at') as f:
        while args.max_lines is None or count < args.max_lines:
            message = f"{datetime.datetime.now(datetime.timezone.utc).isoformat()} {random_level()} {random_message()}\n"
            f.write(message)
            count += 1
            if args.frequency is not None:
                time.sleep(1 / args.frequency)
if __name__ == "__main__":
    main()