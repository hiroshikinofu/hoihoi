market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
def switch_lights(stoplight):
    for key in stoplight.keys():
        if stooplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] =='yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
switch_lights(market_2nd)
assert 'red' in stoplight.values(), '赤信号がない！ ' + str(stoplight)
