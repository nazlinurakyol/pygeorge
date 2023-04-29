def solution(text):
    words = text.split()
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

    for key, value in dict.items():
        print(key, value)
