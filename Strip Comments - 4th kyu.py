"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

"""



def strip_comments(strng, markers):
    """
    strng: type string
    markers: type list
    """
    lines = strng.split("\n") # split input string into lines
    for i in range(len(lines)):
        for marker in markers:
            index = lines[i].find(marker) # find index of first occurrence of marker
            if index != -1:
                lines[i] = lines[i][:index].rstrip() # remove everything after marker and strip trailing whitespace
                break # stop searching for other markers in this line
    return "\n".join(lines) # join lines back into a string with newline characters
