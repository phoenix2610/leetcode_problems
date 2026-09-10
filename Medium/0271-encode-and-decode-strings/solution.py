def encode(strs):
    parts = []
    for s in strs:
        parts.append(f"{len(s)}#{s}")
    return "".join(parts)

def decode(s):
    result = []
    i = 0

    while i < len(s):
        j = i

        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        start = j + 1
        end = start + length
        result.append(s[start:end])
        i = end

    return result
