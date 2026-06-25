
"""
import matplotlib.pyplot as plt
x = [2010,2015,2020,2025] # x cord
y = [100,200,250,300] # y cord.
 
#
# **Markers**
 
# |character      |  |  |description |
# |-------------|  -------------------------------|
# |'.'       | | |point marker|
# |','       | | |pixel marker|
# |'o'       | | |circle marker|
# |'v'       | | |triangle_down marker|
# |'^'       | | |triangle_up marker|
# |'<'       | | |triangle_left marker|
# |'>'       | | |triangle_right marker|
# |'1'       | | |tri_down marker|
# |'2'       | | |tri_up marker|
# |'3'       | | |tri_left marker|
# |'4'       | | |tri_right marker|
# |'8'       | | |octagon marker|
# |'s'       | | |square marker|
# |'p'       | | |pentagon marker|
# |'P'       | | |plus (filled) marker|
# |'*'       | | |star marker|
# |'h'       | | |hexagon1 marker|
# |'H'       | | |hexagon2 marker|
# |'+'       | | |plus marker|
# |'x'       | | |x marker|
# |'X'       | | |x (filled) marker|
# |'D'       | | |diamond marker|
# |'d'       | | |thin_diamond marker|
# |'|'       | | |vline marker|
# |'_'       | | |hline marker|
 
# **Line Styles**
 
# |character      |  |  |  |description |
# |-------------|   -------------------------------|
# |'-'       | | | |solid line style|
# |'--'      | | | |dashed line style|
# |'-.'      | | | |dash-dot line style|
# |':'       | | | |dotted line style|
 
# Example format strings:
 
#     'b'    # blue markers with default shape
#     'or'   # red circles
#     '-g'   # green solid line
#     '--'   # dashed line with default color
#     '^k:'  # black triangle_up markers connected by a dotted line
# **Colors**
 
# |character      |  |  |  |color |
# |-------------|   -------------------------------|
# |'b'       | | | |blue|
# |'g'       | | | |green|
# |'r'       | | | |red|
# |'c'       | | | |cyan|
# |'m'       | | | |magenta|
# |'y'       | | | |yellow|
# |'k'       | | | |black|
# |'w'       | | | |white|
# graph size
plt.figure(figsize=(6,2)) # width or height
plt.plot(x,y,color="y",marker='*',linestyle=":",linewidth=4,markersize=14,)
plt.show()😂
"""

#window + "." press karne se emojy add kar skte hai


#https://matplotlib.org/stable/users/explain/colors/index.html

#https://matplotlib.org/stable/users/explain/colors/index.html

import matplotlib.pylab as plt
x=[2010,2015,2020,2025] #x code
y=[100,200,250,300] #y code
plt.plot(x,y,color='green',marker='*',linestyle='dashed',linewidth=2,markersize=10)
plt.title("sales report")
plt.xlabel("Year")
plt.ylabel("sales")
plt.show()