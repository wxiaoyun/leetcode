from typing import List

# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)
        rec_ing = {}
        for i, r in enumerate(recipes):
            rec_ing[r] = ingredients[i]

        dp = {}
        def can_create(recipe: str) -> bool:
            if recipe in dp:
                return dp[recipe]
            
            dp[recipe] = False
            for ingr in rec_ing[recipe]:
                if ingr in sup:
                    continue
                
                if ingr in rec_ing and can_create(ingr):
                    continue
                
                return False
                
            dp[recipe] = True
            return True
        
        res = []
        for r in recipes:
            if can_create(r):
                res.append(r)
        return res
