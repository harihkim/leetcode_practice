# length Of Longest Substring without repeated (duplicate) characters

#LeetCode Problem link : https://leetcode.com/problems/longest-substring-without-repeating-characters

def lengthOfLongestSubstring(word: str) -> int:
    length: int = 0
    maxlen= 0
    seq: str =""
    for i in word:
        if i in seq:
            if(length>maxlen):
                maxlen = length
            seq = seq + i
            seq = seq[seq.index(i)+1 : ] 
            length = len(seq)
        else:
            seq = seq + i
            length = length + 1
    if(length > maxlen):
        maxlen = length
    return maxlen

if __name__ == "__main__":
    print(lengthOfLongestSubstring(input("enter : ")))
