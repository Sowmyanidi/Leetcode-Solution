class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes*6
        hour_angle = hour*30 + minutes*0.5
        angle = abs(minute_angle-hour_angle)
        return min(360-angle, angle)

sol = Solution()
print(sol.angleClock(3,30))


'''
The minute hand moves 6 degrees per minute (since 360 degrees / 60 minutes = 6 degrees per minute).
The hour hand moves 30 degrees per hour (since 360 degrees / 12 hours = 30 degrees per hour).
Additionally, the hour hand moves 0.5 degrees per minute (since 30 degrees / 60 minutes = 0.5 degrees per minute).
'''