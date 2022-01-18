"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
def heart_rate(age):
    max_heart = 220 - age
    high_heart = max_heart * .85
    low_heart = max_heart * .65
    heart_rate_range = (f"{low_heart:.0f} and {high_heart:.0f}")
    return heart_rate_range


age = int(input("age "))
heart = heart_rate(age)

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {heart} beats per minute.")
