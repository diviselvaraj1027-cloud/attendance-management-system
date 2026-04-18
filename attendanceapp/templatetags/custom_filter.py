from django import template

register = template.Library()

@register.filter
def to_hours_minutes(decimal_hours):
    if decimal_hours == 'N/A':
        return 'N/A'
    try:
        hours = int(decimal_hours)
        minutes = round((decimal_hours - hours) * 60)
        return f"{hours}h {minutes}m"
    except:
        return decimal_hours