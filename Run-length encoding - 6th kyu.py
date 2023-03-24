"""
Task
Your task is to write such a run-length encoding. For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct the original string by replicating the character sx ix times and concatening all those strings. Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.

Examples
As the article states, RLE is a very simple form of data compression. It's only suitable for runs of data, as one can see in the following example:

      It's very effective if the same data value occurs in many consecutive data elements:

      run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
      # => [[34,'a'], [3,'b']]
"""


def run_length_encoding(s):
    c, ans = 1, []
    for i in range(len(s)):
        try:
            if s[i] == s[i+1]:
                c += 1
            else:
                ans.append([c, s[i]])
                c = 1
        except IndexError:
            ans.append([c, s[i]])
            break
    return ans
