#!/usr/bin/env python3

import vf_contour


arr = [[73, 636], [447, 685], [445, 1100], [1699, 1122], [1699, 133], [1110, 133], [1092, 846], [1103, 125], [478, 120], [449, 633]]

arr_reversed = arr[::-1]

print(vf_contour.get_quadrangle_vertices(arr_reversed, mode=1))
