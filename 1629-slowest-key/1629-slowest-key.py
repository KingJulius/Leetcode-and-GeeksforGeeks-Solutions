class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        k, t = keysPressed[0], releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            curr_time = releaseTimes[i]-releaseTimes[i-1]
            if (curr_time > t) or (curr_time == t and keysPressed[i] > k):
                t = curr_time
                k = keysPressed[i]
        return k