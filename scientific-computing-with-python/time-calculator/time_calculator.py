# My first solution

weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start, duration, weekday=None):
  start_is_post_meridian = False if start.find("PM") == -1 else True
  start_separator = start.find(":")
  start_hours = int(start[0:start_separator])
  start_hours = 0 if start_hours == 12 else start_hours
  start_hours = start_hours + 12 if start_is_post_meridian else start_hours
  start_minutes = int(start[start_separator+1:start_separator+3])

  duration_separator = duration.find(":")
  duration_hours = int(duration[0:duration_separator])
  duration_minutes = int(duration[duration_separator+1:duration_separator+3])

  total_minutes = start_minutes + duration_minutes
  extra_hours = int(total_minutes / 60)
  remaining_minutes = total_minutes if total_minutes < 60 else total_minutes % 60

  total_hours = start_hours + duration_hours + extra_hours
  remaining_hours = total_hours
  days = 0

  if total_hours > 23:
    days = int(total_hours / 24)
    remaining_hours = total_hours % 24

  meridian_text = "PM" if remaining_hours > 11 else "AM"
  minutes_text = f'0{remaining_minutes}' if remaining_minutes < 10 else remaining_minutes
  hours_text = remaining_hours - 12 if remaining_hours > 12 else remaining_hours
  if hours_text is 0:
    hours_text = '12'

  days_text = ''

  if days == 1:
    days_text = ' (next day)'

  if days > 1:
    days_text = f' ({days} days later)'

  weekday_text = ''
  if weekday:
    weekday = f'{weekday[0].upper()}{weekday[1:].lower()}'
    weekday_index = weekdays.index(weekday)
    days_forward = days % 7
    slot = weekday_index + days_forward
    if slot > 6:
      slot = slot - 7
    weekday_text = f', {weekdays[slot]}'

  new_time = f'{hours_text}:{minutes_text} {meridian_text}{weekday_text}{days_text}'
  return new_time
