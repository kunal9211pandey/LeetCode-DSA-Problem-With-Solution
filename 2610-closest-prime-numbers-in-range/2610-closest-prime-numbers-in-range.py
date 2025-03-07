class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res = [-1, -1]
        is_prime = [True] * (right + 1)

        # for a given prime the next one will be the closest one
        last_prime, num = None, 2
        while num <= right:

            # if it's not prime, skip
            if is_prime[num]:
                if left <= num:
                    
                    # first prime encountered
                    if last_prime:
                        if res[0] == -1 or res[1] - res[0] > num - last_prime:
                            res = [last_prime, num]

                    last_prime = num
            
                # marked multiple as not primes
                multiplier = num
                while multiplier * num <= right:
                    is_prime[multiplier * num] = False
                    multiplier += 1

            # incremente prime
            num += 1
        
        return res             
                               
        