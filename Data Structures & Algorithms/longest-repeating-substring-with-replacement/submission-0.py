class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # You are given a string s consisting of only uppercase english characters and an integer k. 

        # You can choose up to k chars and replace them with any other uppercase English character.

        # return the length of the longest substring which contains only one distinct character.

        character_occurences = defaultdict(int)

        most_occurences = 0

        result = 0

        L = 0
        R = 1

        while R <= len(s):
            character = s[R - 1]

            character_occurences[character] += 1

            most_occurences = max(most_occurences, character_occurences[character])

            while R - L - most_occurences > k:
                last_character = s[L]

                character_occurences[last_character] -= 1

                L += 1

            result = max(result, R - L)

            R += 1

        return result
