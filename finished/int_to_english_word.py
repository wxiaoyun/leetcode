# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_to_word = {
            0: None,
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_to_word = {
            0: None,
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty", 
            6: "Sixty",
            7: "Seventy", 
            8: "Eighty",
            9: "Ninety"
        }


        def to_words(num: int) -> str:
            assert num < 1000
            
            hundreds = ones_to_word[num // 100]

            num = num % 100
            if num < 20:
                words = [
                    hundreds + " Hundred" if hundreds else None,
                    ones_to_word[num]
                ]
                words = filter(lambda x: x is not None, words)
                return " ".join(list(words))
            
            tens = tens_to_word[num // 10]
            num = num % 10
            ones = ones_to_word[num // 1]

            words = [
                hundreds + " Hundred" if hundreds else None,
                tens, ones
            ]
            words = filter(lambda x: x is not None, words)
            return " ".join(list(words))
            
        billions = num // 1_000_000_000
        num = num % 1_000_000_000
        millions = num // 1_000_000
        num = num % 1_000_000
        thousands = num // 1_000
        num = num % 1_000
        ones = num // 1

        words = [
            to_words(billions) + " Billion" if billions else None,
            to_words(millions) + " Million" if millions else None,
            to_words(thousands) + " Thousand" if thousands else None,
            to_words(ones) if ones else None
        ]
        words = filter(lambda x: x is not None, words)
        return " ".join(list(words))