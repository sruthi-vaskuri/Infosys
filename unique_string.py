## Problem Statement

## Given a string S, find the length of the longest substring without repeating characters.

Input:
S = "ABDEFGABEF"
Output:
6
Explanation:
Longest substring is
"BDEFGA" and "DEFGAB".

## CODE

class Solution:
    def longestUniqueSubsttr(self, s):
        # code here
        character_index={}
        maxlen=0
        start=0
        for i in range(0,len(s)):
            if s[i] not in character_index:
                character_index[s[i]]=i
            elif character_index[s[i]]<start:
                character_index[s[i]]=i
            else:
                if maxlen<(i-start+1):
                    maxlen=i-start
                start=character_index[s[i]]+1
                character_index[s[i]]=i
        if maxlen<(i-start+1):
            maxlen=i-start+1
        return maxlen