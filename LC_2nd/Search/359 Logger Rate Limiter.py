'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 
https://leetcode.com/problems/logger-rate-limiter/
Contact: ming.li2@columbia.edu
'''


class Logger:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_time_dict = {}
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.message_time_dict:
            # check whether 10 seconds passed
            if timestamp - self.message_time_dict[message] >= 10:
                self.message_time_dict[message] = timestamp
                return True
            else:
                # self.message_time_dict[message] = timestamp
                return False
        else:
            # not in the self.message_time_dict:
            self.message_time_dict[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
if __name__ == '__main__':
    res = Solution()
    print(res)