class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for e in emails:
            i, curr = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    curr += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i+1:]
            unique_emails.add((curr, domain))

        return len(unique_emails)

# Time -> O(no. of emails * average len of email)
# Space -> O(no. of unique emails)
        
