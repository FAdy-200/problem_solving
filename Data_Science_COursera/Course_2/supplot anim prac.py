import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
from matplotlib import rcParams

rcParams['animation.convert_path'] = r'C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\convert.exe'
rcParams['animation.ffmpeg_path'] = r'C:\Program Files\ffmpeg\bin\ffmpeg.exe'
fig, ((a1, a2), (a3, a4)) = plt.subplots(2, 2, sharex="all")
n = 900
nor = np.random.normal(4, 1, n)
uni = np.random.uniform(0, 8, n)
gam = np.random.gamma(2, 1, n)
ch = np.random.exponential(1, n)


def update(c):
    if c == n:
        a.event_source.stop()
    plt.cla()
    b = np.arange(0, 8, 0.5)
    a1.hist(nor[:c+100],
            bins=b
            , color="#396AB1")
    a1.title.set_text("Normal")
    a2.hist(uni[:c+100], bins=b, color="#396AB1")
    a2.title.set_text("Uniform")
    a3.hist(gam[:c+100], bins=b, color="#396AB1")
    a3.title.set_text("gamma")
    a4.hist(ch[:c+100], bins=b, color="#396AB1")
    a4.title.set_text("expo")
    plt.suptitle(t="n = {}".format(c+100))


# Writer = an.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

a = an.FuncAnimation(fig, update, interval=10)
# a.save("D:\My study\PYCHARM PR\Data_Science_COursera\Course_2\meme1.gif", writer="imagemagick")

plt.show()


