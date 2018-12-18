## AoC 2018 - Day 18 - NOTES

After some minutes we can see that the *resource value* repeats tehe next values:
[194110,196378,191475,192766,190365,184886,179850,181306,177210,175357,168168,170863,166464,170352,169024,173910,172200,178640,179968,185952,187844,194205,194271,198489,196098,199374,196992,199064]

After a short analysis we can see:
```
resource_value_position = (minute-5) % 28
```

Then we can see that at minute 1000000000 we have the 15th resource value:
```
169024
```