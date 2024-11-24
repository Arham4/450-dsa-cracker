def minFlips(self, S):␍
    first_version_flips = 0␍
    character_expected = "0"␍
    for i in range(len(S)):␍
        if S[i] != character_expected:␍
            first_version_flips += 1␍
        character_expected = "1" if character_expected == "0" else "0"␍
    second_version_flips = 0␍
    character_expected = "1"␍
    for i in range(len(S)):␍
        if S[i] != character_expected:␍
            second_version_flips += 1␍
        character_expected = "1" if character_expected == "0" else "0"␍
    return min(first_version_flips, second_version_flips)
