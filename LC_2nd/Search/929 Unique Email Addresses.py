'''
Created by Ming Li at 2019-02-22

Feature: 

Description: 

Contact: ming.li2@columbia.edu
'''
class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

if __name__ == '__main__':
    res = Solution()
    print(res)