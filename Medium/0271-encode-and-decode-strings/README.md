# 271. Encode and Decode Strings

**Difficulty:** Medium  
**Tags:** Array, String, Design  
**Link:** https://leetcode.com/problems/encode-and-decode-strings/

## Solutions

| Language | File |
|----------|------|
| Python | [solution.py](solution.py) |

## Notes

LeetCode Premium — solved and verified off-platform, not submitted to the LeetCode judge.
Length-prefix encoding (`<len>#<payload>`): the reader takes the length before reading
the payload, so a `#` or digits inside the string can never be mistaken for a delimiter.
