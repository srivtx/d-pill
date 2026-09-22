#!/usr/bin/env python3
"""Contrast for two OKLCH colors.

Usage:
  python3 scripts/contrast.py text L C H L C H
  python3 scripts/contrast.py ui   L C H L C H

`text` requires 4.5:1. `ui` requires 3:1 (control edges, focus rings, marks).
Prints the ratio and exits 1 on a miss. Channels are clipped into gamut the
way a browser clips them, so the ratio matches the painted color.
"""

import math
import sys


def linear_srgb(L, C, H_deg):
    h = math.radians(H_deg)
    a = C * math.cos(h)
    b = C * math.sin(h)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bch = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(min(max(c, 0.0), 1.0) for c in (r, g, bch))


def luminance(rgb):
    r, g, b = rgb
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(c1, c2):
    y1, y2 = luminance(c1), luminance(c2)
    lighter, darker = max(y1, y2), min(y1, y2)
    return (lighter + 0.05) / (darker + 0.05)


def main(argv):
    if len(argv) != 8 or argv[1] not in ("text", "ui"):
        sys.stderr.write(__doc__)
        return 2
    kind = argv[1]
    nums = [float(x) for x in argv[2:]]
    a = linear_srgb(*nums[0:3])
    b = linear_srgb(*nums[3:6])
    value = ratio(a, b)
    floor = 4.5 if kind == "text" else 3.0
    verdict = "pass" if value >= floor else "fail"
    print(f"{value:.2f}  {kind} {verdict}  (floor {floor})")
    return 0 if value >= floor else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
