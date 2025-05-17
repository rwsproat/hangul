# How many mats are needed for a Hangul Linotype/Intertype machine?

Statistics for estimating the number of matrices (mats) needed for a
Hangul Linotype machine as described in Section 3.6.4.2 of

Brian Roark, Richard Sproat and Suyoun Yoon. 2025. _Tools of the
Scribe: How writing systems, technology, and human factors interact to
affect the act of writing_. Cham: Springer Nature.

# Installation

pip3 install -r requirements.txt

# Running

`python3 estimate_mats.py --cut=[horizontal, vertical] (--use_old_spelling)`

This will print out a list of needed "cuts" to the Hangul syllable
composite in descending expected probability order, followed by the
total number of syllables, and an estimate of the number of Linotype
mats needed.

The main flag, `--cut`, controls whether one is intending to print
horizontally (as most modern Korean text is), in which case you would
need to cut the syllable blocks vertically in order to reduce the size
of the set to fit on a Linotype machine. Or vertically --- the
traditional writing direction --- in which case one cuts the syllable
blocks horizontally. The number of required mats is significantly
smaller if you cut the blocks horizontally, as opposed to vertically,
which is why Korean newspapers using a Linotype-style machine, such as
the [Shinhan Shinbun](https://en.wikipedia.org/wiki/Sinhan_Minbo) had to
be printed top to bottom.

This is illustrated in the following figure, which shows Two ways of
cutting the word 한글 _hangeul_ for a Linotype system. For horizontal
left-to-right text one would need to cut vertically, but this would
scarcely achieve any eduction in the number of needed type. On the
other hand, with the traditional top-to-bottom direction, one can cut
the syllable blocks horizontally, which can achieve a very large
reduction in the number of needed elements. The righthand column shows
how one can construct a new syllable out of the top element of 한 and
the bottom element of 글.

![Horizontal and vertical cuts of Hangul syllable blocks](https://github.com/rwsproat/hangul/blob/main/hangul_cuts.png)

The `--use_old_spelling` flag toggles whether or not to use the
spellings for emphatic consonants (such as "ᄲ" in place of modern
"ㅃ"), which were used prior to the various spelling reforms of the
early 20th century.

Syllable frequency data in syl-2-utf8.txt are from:

[http://nlp.kookmin.ac.kr/data/syldown.html](http://nlp.kookmin.ac.kr/data/syldown.html)





