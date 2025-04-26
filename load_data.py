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
from collections import defaultdict

def load_data():
  indata = False
  syls = defaultdict(int)
  with open("syl-2-utf8.txt") as s:
    for line in s:
      if line.startswith("===="):
        indata = True
      elif indata:
        line = line.strip().split()
        syl = line[0].strip()
        if len(syl) == 1:
          cnt = int(line[1].strip())
          syls[syl] = cnt
  return syls
