from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        n = len(queries)
        color_freq = defaultdict(int)  # Frequency of each color
        ball_color = {}  # Color of each ball
        res = []

        for i in range(n):
            ball, color = queries[i]

            # If the ball was already painted, remove its previous color
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_freq[prev_color] -= 1  # Reduce frequency
                if color_freq[prev_color] == 0:
                    del color_freq[prev_color]  # Remove if frequency becomes 0

            # Paint the ball with the new color
            ball_color[ball] = color
            color_freq[color] += 1

            # Add the number of distinct colors to the result
            res.append(len(color_freq))

        return res