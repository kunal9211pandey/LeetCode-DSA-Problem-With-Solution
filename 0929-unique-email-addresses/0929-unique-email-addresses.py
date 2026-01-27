class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split('@')

            # remove part after '+'
            local = local.split('+')[0]

            # remove dots
            local = local.replace('.', '')

            unique.add(local + '@' + domain)

        return len(unique)
