def GetStripURL(url):
    slug = url.rstrip("/").split("/")[-1].split("-")

    result = []

    for i in range(len(slug)):
        result.append(slug[i])

    return result

def GetBaseURL(url):
    parts = url.split("/")
    return parts[0] + "//" + parts[2] + "/"

def GetCombinationFromStrip(strip, base_url):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            slug = "-".join(path)
            result.append(base_url.rstrip("/") + "/" + slug + "/")
            return

        for i in range(len(remaining)):
            backtrack(
                path + [remaining[i]],
                remaining[:i] + remaining[i+1:]
            )

    backtrack([], strip)

    return result