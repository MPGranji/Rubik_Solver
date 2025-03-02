def color_detect(h, s, v):
    if (h < 10 or h > 170) and s >= 100 and v >= 50:
        return 'red'
    elif 10 <= h < 25 and s >= 100 and v >= 50:
        return 'orange'
    elif 25 <= h < 40 and s >= 100 and v >= 50:
        return 'yellow'
    elif 40 <= h < 85 and s >= 100 and v >= 50:
        return 'green'
    elif 85 <= h < 130 and s >= 70 and v >= 50:
        return 'blue'
    return 'white'