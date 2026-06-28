class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for word in strs:
            encoded_string.append(str(len(word)) + "#" + word)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # expect string to be in one giant string with a number 
        # followed by a break ('#') to indicate the end of the number
        # followed by the word

        # simply cannot split based on delimiter since the 
        # original word can have the delimiter char in the word
      
        decoded_str = []
        i = 0
        # 5#Hello5#World
        while i < len(s):
            print(f'{i}')
            offset = 0
            while s[i+offset] != '#':
                offset += 1
                
            length = int(s[i:i+offset])
            i += offset + 1
            decoded_str.append(s[i:i+length])
            i += length
        return decoded_str
            

            

            