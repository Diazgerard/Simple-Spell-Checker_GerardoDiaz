def levenshtein_distance(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    
                    dp[i][j - 1],    
                    dp[i - 1][j - 1] 
                )
    return dp[-1][-1]


def load_dictionary(path):
    with open(path, "r") as f:
        return [word.strip() for word in f.readlines()]


def suggest(word, dictionary, n=3):
    distances = [(w, levenshtein_distance(word, w)) for w in dictionary]
    distances.sort(key=lambda x: x[1])
    return [w for w, _ in distances[:n]]