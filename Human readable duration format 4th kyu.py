"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
    """
    
    
def format_duration(seconds):
    if seconds == 0: return "now"
    
    year, seconds = divmod(seconds, 31536000)
    day, seconds = divmod(seconds, 86400)
    hour, seconds = divmod(seconds, 3600)
    minute, seconds = divmod(seconds, 60)
    
    ans = []
    if year:
        ans.append(f"{year} year{'s' if year > 1 else ''}")
    if day:
        ans.append(f"{day} day{'s' if day > 1 else ''}")
    if hour:
        ans.append(f"{hour} hour{'s' if hour > 1 else ''}")
    if minute:
        ans.append(f"{minute} minute{'s' if minute > 1 else ''}")
    if seconds:
        ans.append(f"{seconds} second{'s' if seconds > 1 else ''}")
        
    return ans[0] if len(ans) == 1 else ", ".join(ans[:-1]) + " and " + ans[-1]
