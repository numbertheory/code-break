## CodeBreak

Standard code break game. This is more of a demonstration/code exercise
than anything useful, but it does work.

## Controls

When the game starts a secret code consisting of these colors is generated:

g = green

r = red

b = blue

p = purple

y = yellow

The code does not have to contain all the colors, and repeats of colors are
allowed. This is fully random, so `ppppp` is just as likely as `pgyrb`.

You are then given 12 guesses to guess what that secret code is. Submit
your guesses in one long string of five characters that only contain the
five colors (example below):

```
#1 Guess? gbgbg
```

### Hints

As you guess, the guess counter increases, and your guess history is displayed
(with the tokens in color) along with hints:

```
#2 Guess? yyyyy
      Guesses        |       Hint     
--------------------------------------
#1 █ | █ | █ | █ | █ |       C----
--------------------------------------
#2 █ | █ | █ | █ | █ |       -----
--------------------------------------
#3 █ | █ | █ | █ | █ |       CWW--
--------------------------------------
```

C = A token is in the correct position with the correct color

W = A token is in the wrong position, but with a correct color

The hints always display `C` tokens first, and then `W` tokens. The position
of the hints do not indicate the position of the correct token. In the example
above, the hint of `CWW` means that for guess #3, one token was in the correct
position and had the correct color, while two tokens were the correct colors,
but in the wrong position.

### Input validation

If your guess is invalid, it simply states that, and the turn counter does
not increase.

```
#3 Guess? gbgbgb
Invalid guess.
#3 Guess?
```

## Special commands

q = quit the game

c = cheat (display the answer, helpful for debugging)
