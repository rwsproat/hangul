# This file is part of the Hangul Linotype distribution (https://github.com/rwsproat/hangul).
# Copyright (c) 2025 Richard Sproat.
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>.
from absl import app
from absl import flags
from collections import defaultdict
from load_data import load_data

import hangul_jamo


CUT = flags.DEFINE_enum(
  "cut",
  "horizontal",
  ["horizontal", "vertical"],
  "Which way to cut",
)

USE_OLD_SPELLING = flags.DEFINE_bool(
  "use_old_spelling",
  False,
  "Use the old spellings for initial emphatics",
)

BELOW = ["ㅜ", "ㅠ", "ㅛ", "ㅗ", "ㅡ"]
COMPOUND = ["ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]
DOUBLE_FINAL = {
  "ㅀ": "ㄹㅎ",
  "ㅄ": "ㅂㅅ",
  "ㄳ": "ㄱㅅ",
  "ㄵ": "ㄴㅈ",
  "ㄶ": "ㄴㅎ",
  "ㄺ": "ㄹㄱ",
  "ㄻ": "ㄹㅁ",
  "ㄼ": "ㄹㅂ",
  "ㄽ": "ㄹㅅ",
  "ㄾ": "ㄹㅌ",
  "ㄿ": "ㄹㅍ",
}

EMPHATIC = {
  "ㅃ": "ㅂ",
  "ㅉ": "ㅈ",
  "ㄸ": "ㄷ",
  "ㄲ": "ㄱ",
  "ㅆ": "ㅅ",
}

OLD_EMPHATIC = {
  "ㅃ": "ᄲ",
  "ㄸ": "ᄯ",
  "ㄲ": "ᄭ",
}

OLD_EMPHATIC_MAP = {
  "ᄲ": "ㅅㅂ",
  "ᄯ": "ㅅㄷ",
  "ᄭ": "ㅅㄱ",
}


def proc():
  syls = load_data()
  matrices = defaultdict(int)
  for syl in syls:
    cnt = syls[syl]
    ini, med, fin = hangul_jamo.decompose_syllable(syl)
    decomposition = []
    if CUT.value == "horizontal":
      if med in BELOW:
        decomposition.append(ini)
        decomposition.append(med)
      else:
        matrix = f"{ini}{med}"
        cmatrix = hangul_jamo.compose(matrix)
        if USE_OLD_SPELLING.value and ini in OLD_EMPHATIC:
          old_matrix = f"{OLD_EMPHATIC[ini]}{med}"
          decomposition.append(f"{cmatrix} ({matrix}/{old_matrix})")
        else:
          decomposition.append(f"{cmatrix} ({matrix})")
      if fin:
        decomposition.append(fin)
    else:

      def cut(char, direction):
        if direction == "left":
          direction = "◧"
        else:
          direction = "◨"
        return f"{direction[0]} ({char})"

      left_cut = []
      right_cut = []
      if med in BELOW:
        if USE_OLD_SPELLING.value and ini in OLD_EMPHATIC:
          ini = OLD_EMPHATIC[ini]
          ini = OLD_EMPHATIC_MAP[ini]
          left_cut.append(ini[0])
          right_cut.append(ini[1])
        elif ini in EMPHATIC:
          ini = EMPHATIC[ini]
          left_cut.append(ini)
          right_cut.append(ini)
        else:
          left_cut.append(cut(ini, "left"))
          right_cut.append(cut(ini, "right"))
        left_cut.append(cut(med, "left"))
        right_cut.append(cut(med, "right"))
      elif med in COMPOUND:
        left_cut.append(ini)
        left_cut.append(cut(med, "left"))
        right_cut.append(cut(med, "right"))
      else:
        left_cut.append(ini)
        right_cut.append(med)
      if fin in DOUBLE_FINAL:
        fin = DOUBLE_FINAL[fin]
        left_cut.append(fin[0])
        right_cut.append(fin[1])
      elif fin in EMPHATIC:
        fin = EMPHATIC[fin]
        left_cut.append(fin)
        right_cut.append(fin)
      elif fin:
        left_cut.append(cut(fin, "left"))
        right_cut.append(cut(fin, "right"))
      left_cut = " ".join(left_cut)
      right_cut = " ".join(right_cut)
      decomposition.append(left_cut)
      decomposition.append(right_cut)
    for matrix in decomposition:
      matrices[matrix] += cnt
    print(f"SYL:\t{syl}\t{decomposition}")

  tot = sum(matrices.values())

  for i, matrix in enumerate(
      sorted(
        matrices,
        key=lambda x: matrices[x],
        reverse=True,
      ),
  ):
    print(f"STATS:\t{i+1}\t{matrices[matrix]/tot:.08f}\t{matrix}")

  print(f"Total syllables:\t{len(syls)}")
  print(f"Total mats:     \t{len(matrices)}")


def main(unused_argv):
  try:
    proc()
  except BrokenPipeError:
    pass

if __name__ == "__main__":
  app.run(main)
