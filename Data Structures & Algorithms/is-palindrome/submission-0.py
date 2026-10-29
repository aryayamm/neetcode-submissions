class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for i in s:
            if i.isalnum() == True:
                news += i
        news = news.lower()
        print(news)
        return news == news[::-1]