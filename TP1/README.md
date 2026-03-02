# line 36
`.strip(".,!?")` only works for the start/end of a word
it fails if punctuation is in the middle, example: `"don't"` or `"U.S.A."`

# line 36
use `string.punctuation` bcz it's better than hardcoding marks manually

# line 39
btw, you can use `.get()` here to handle the dict lookup and the "else" in one line

# line 46
you can use a dict comprehension to normalize everything in one go
