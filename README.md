# ircawp2020

This is just a simple [Markov](https://en.wikipedia.org/wiki/Markov_chain) text toy. Use `ircawp-learn` to build a "brain" (just a big messy blob of json), and then `ircawp-phrase` to generate a sentence based on the contents of the brain.

This sort of thing goes in:

```
There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.

Many were increasingly of the opinion that they'd all made a big mistake in coming down from the trees in the first place. And some said that even the trees had been a bad move, and that no one should ever have left the oceans.

"My doctor says that I have a malformed public-duty gland and a natural deficiency in moral fibre," Ford muttered to himself, "and that I am therefore excused from saving Universes."

The ships hung in the sky in much the same way that bricks don't.

"You know," said Arthur, "it's at times like this, when I'm trapped in a Vogon airlock with a man from Betelgeuse, and about to die of asphyxiation in deep space that I really wish I'd listened to what my mother told me when I was young."

[...etc]
```

...and this sort of nonsense comes out...

```
Protect me when light with some way off.

It seemed to need to convert Fahrenheit to the dolphins because he had always assumed that I decided a man who most want to fill the sea, all the ingenuity of magic.

Shee, you stare at the huskies have left the water having a good time.

Eskimos had so much the only thing to know about in drifts, snow that people have speculated that any people miserable with.

"You know," said Arthur, "it's at the bowl of complete fools."
```

## Setup and sample usage

### Setup

The only real requirement is [jsonpickle](https://jsonpickle.github.io/), but feel free to use the `requirements.txt` file if you're feeling saucy.

### Generate a brain

You'll find some sample brains in the appropriately named directory, but if you want to rebuild them, let's build a brain out of some Hitchhiker's quotes:

`./ircawp-learn.py sample_input/hitch.txt > hitch-brain.json`

#### Two brains are better than one

If you have an existing brain you'd like to merge the new corpus into:

`./ircawp-learn.py sample_input/hitch.txt some-ol-brain.json > twobrainstogether.json`

### Emit some comedy

Now, just use:

`./ircawp-phrase.py hitch-brain.json`

...and out comes some "real woke shit that shatters through our warped looking glass". (Thanks, 1ndgfl0.)

## Notes

-   The 'brain' format is just an ugly, impossibly unoptimized json dump of a memory structure. It compresses pretty well, though.
-   I'll probably make a few tweaks to this to give a bit more coherency to the sentences being generated.
-   My ultimate goal is to feed this into a Slack bot. Not that you asked, but I figure it'd be nice to disclose my motivations.
-   Python is not my primary tongue, so forgive any relgious violations I may have committed against Guido's snake-language.

## "ircawp"?

Don't ask.

![](https://media.giphy.com/media/2Z6sjWggCaDXa/giphy.gif)

2020-02-15
