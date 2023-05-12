# https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx

def decrypt(word):
    # 97 - 122
    # a - z
    new_word = list(map(ord, word))
    for i in range(1, len(new_word)):
        j = new_word[i - 1] // 26

        while not (122 >= (new_word[i] + 26 * j) - new_word[i - 1] >= 97):
            j += 1
        new_word[i] = (new_word[i] + 26 * j)
    for i in range(len(word) - 1, 0, -1):
        new_word[i] -= new_word[i - 1]
    new_word[0] -= 1
    ans = ""
    for i in new_word:
        ans += chr(i)
    return ans


x = "bvqmjhgghjmqvbiqzjugthwmdv"
print(decrypt(x))