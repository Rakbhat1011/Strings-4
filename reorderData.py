"""
Split each log into identifier and rest (the payload after the first space)
Classify: if rest[0].isdigit() - digit-log; else letter-log
Sort only letter-logs by key (rest, identifier); append digit-logs afterward unchanged
"""
"""
Time Complexity: O(n log n) for sorting the letter-logs (n = number of logs)
Space Complexity: O(n) to hold separated logs / sort keys
"""

from typing import List

class reorderData:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            id_, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append((rest, id_, log)) 

        letters.sort(key=lambda x: (x[0], x[1]))
        return [log for _, _, log in letters] + digits


if __name__ == "__main__":
    obj = reorderData()

    logs1 = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
    ]

    print(obj.reorderLogFiles(logs1))

    logs2 = [
        "a1 9 2 3 1",
        "g1 act car",
        "zo4 4 7",
        "ab1 off key dog",
        "a8 act zoo"
    ]

    print(obj.reorderLogFiles(logs2))
    print(obj.reorderLogFiles([]))  # []
    print(obj.reorderLogFiles(["let1 a", "dig1 1"]))  
