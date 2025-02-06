def ticker(text, width, tick):
    #for tick in range:
    start = tick%len(text)
    if tick < width:
        tick = text[:tick]
        return tick.rjust(width, ' ')
    if (tick-width) > len(text):
        tick = text[:(tick-width-len(text))]
        return tick.rjust(width, ' ')
    tick = text[tick-width:tick]
    return tick.ljust(width, ' ')