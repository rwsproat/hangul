# Hangul Linotype 

Statistics for estimating the number of mats needed for a Hangul
Linotype machine as described in Section 3.6.4.2 of

Brian Roark, Richard Sproat and Suyoun Yoon. 2025. Tools of the
Scribe: How writing systems, technology, and human factors interact to
affect the act of writing. Springer Nature.

First install requirements:

pip3 install -r requirements.txt

Then run

python3 fill_matrix --cut=[horizontal, vertical] (--use_old_spelling)

This will print out a list of needed "cuts" to the Hangul syllable
composite in descending expected probability order, followed by the
total number of syllables, and an estimate of the number of Linotype
mats needed.  The number of required mats is significantly smaller if
you cut the blocks horizontally, as opposed to vertically, which is
why Linotype-style Korean newspapers had to be printed top to
bottom. The --use_old_spelling flag toggles whether or not to use the
spellings for emphatic consonants (such as "ᄲ" in place of
modern "ㅃ"), which were used prior to the various spelling reforms of
the early 20th century.

Syllable frequency data in syl-2-utf8.txt are from:

http://nlp.kookmin.ac.kr/data/syldown.html



