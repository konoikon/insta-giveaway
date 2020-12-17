# InstaGiveaway

This python package will help you win Instagram Giveaway competitions! It is really simple! Just log into your account, set up the posts you would like to compete for and that's it!

## How it works

```python
from instagiveaway import InstaGiveaway

ig = InstaGiveaway('<YOUR_USERNAME>', '<YOUR_PASSWORD>', ['<POST_ID_1>', '<POST_ID_2>', ...], ['<@ACCOUNT_TO_TAG_1>', ...])

ig.run(iterations=5, number_of_tags=2)
```

The above snippet will log into your account, and tag 2 people in 5 distinct comments in your given posts.
