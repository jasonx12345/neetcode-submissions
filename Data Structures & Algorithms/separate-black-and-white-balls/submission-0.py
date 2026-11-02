class Solution:
    def minimumSteps(self, s: str) -> int:
        black_count = 0
        step = 0
        for ball in s:
            if ball == "1":
                black_count += 1
            else:
                step += black_count
        return step

    
