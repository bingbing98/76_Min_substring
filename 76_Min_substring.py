class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 统计需要的字符数量，注意可能有的字符是重复的
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)  # 未满足的字符数量
        
        result = ''
        minlen = len(s)
        i = 0
        j = 0
        while j<len(s):         # 不断增大右边界
            if need[s[j]] > 0:  # 如果字符需求量大于0，那么此位置的字符是被需求的
                needCnt -= 1    # 未满足的字符数量-1
            need[s[j]] -= 1     # 字符需求量-1
            if needCnt == 0:    # 如果没有未满足的字符了，就缩小左边界，直到下一个被需求的字符
                while True:     
                    if need[s[i]] == 0: # 如果遇到了本被需要的字符，那么左边界就不能再右移了
                        need[s[i]] += 1 # 下一步此字符需求量+1
                        break
                    need[s[i]] += 1     # 左边界经过的字符需求量+1（有可能有连续相同的被需求的字符，这句不能去掉）
                    i += 1
                newlen = j-i            # 判断长短
                newresult = s[i:j+1]
                if newlen <= minlen:
                    minlen = newlen
                    result = newresult
                i += 1                  # 进行下一次搜寻
                needCnt += 1            # 左边界已经越过了本被需要的字符，所以未满足的字符数量+1
            # 以上过程是，先右移右边界，直到i-j之间包含所有被需求的字符，然后右移左边界，直到包含所需字符的最小长度
            # 然后再进行下一次搜寻，这时左边界已经越过了一个本被需要的字符
            j += 1              # 右边界右移
        return result
