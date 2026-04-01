class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

            if len(s1) > len(s2):
                return False

            s1_count = [0] * 26
            window_count = [0] * 26

            # Count s1 characters
            for char in s1:
                s1_count[ord(char) - ord('a')] += 1

            # Track how many characters have matching counts
            matches = 0
            for i in range(26):
                if window_count[i] == s1_count[i]:
                    matches += 1

            # Single pass sliding window
            for right in range(len(s2)):
                # Add current character (right)
                idx = ord(s2[right]) - ord('a')
                window_count[idx] += 1

                # Update matches for this character
                if window_count[idx] == s1_count[idx]:
                    matches += 1
                elif window_count[idx] == s1_count[idx] + 1:
                    # Just exceeded the target count
                    matches -= 1

                # Remove character that falls out
                if right >= len(s1):
                    left_idx = ord(s2[right - len(s1)]) - ord('a')
                    window_count[left_idx] -= 1

                    # Update matches for left character
                    if window_count[left_idx] == s1_count[left_idx]:
                        matches += 1
                    elif window_count[left_idx] == s1_count[left_idx] - 1:
                        matches -= 1

                # Check if all 26 characters match
                if matches == 26:
                    return True

            return False

 