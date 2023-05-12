def list_turning(x: object) -> object:
    """

    :param x:
    :return:
    """
    z = ["none"] * len(x)
    for i in range(len(x)):
        z[i] = x[i]
    return z


def position(x):
    y = 100
    for i in range(len(x)):
        if x[i] == "1":
            y = i
    return y


# -------------------------------------------------------------------
fi = input()
sec = input()
th = input()
fo = input()
fif = input()
# -------------------------------------------------------------------
fil = list_turning(fi)
secl = list_turning(sec)
thl = list_turning(th)
fol = list_turning(fo)
fifl = list_turning(fif)
# -------------------------------------------------------------------
filp = position(fil)
seclp = position(secl)
thlp = position(thl)
folp = position(fol)
fiflp = position(fifl)
# -------------------------------------------------------------------
turns = 0
if filp == 0 or filp == 8:
    turns = 2
elif filp == 2 or filp == 6:
    turns = 1
elif filp == 4:
    turns = 0
if seclp == 0 or seclp == 8:
    turns = 2
elif seclp == 2 or seclp == 6:
    turns = 1
elif seclp == 4:
    turns = 0
if thlp == 0 or thlp == 8:
    turns = 2
elif thlp == 2 or thlp == 6:
    turns = 1
elif thlp == 4:
    turns = 0
if folp == 0 or folp == 8:
    turns = 2
elif folp == 2 or folp == 6:
    turns = 1
elif folp == 4:
    turns = 0
if fiflp == 0 or fiflp == 8:
    turns = 2
elif fiflp == 2 or fiflp == 6:
    turns = 1
elif fiflp == 4:
    turns = 0
# -------------------------------------------------------------------
if filp != 100 or fiflp != 100:
    turns += 2
elif seclp != 100 or folp != 100:
    turns += 1
# -------------------------------------------------------------------
print(turns)
