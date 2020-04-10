# 2920 음계
if __name__ == "__main__":
    sounds = list(map(int, input().split()))
    ascending = sorted(sounds)
    descending = list(reversed(sorted(sounds)))
    if sounds == ascending:
        print("ascending")
    elif sounds == descending:
        print("descending")
    else:
        print("mixed")