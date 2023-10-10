class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for k, word in enumerate(words) :
            s= ""
            for alpha in word :
                index = ord(alpha) - 97
                s += morse[index]
            result.append(s)

        print(result)

        return len(set(result))