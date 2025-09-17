# https://leetcode.com/problems/design-a-food-rating-system/

from typing import List, Tuple
import heapq
from collections import defaultdict


class LazyPriorityQueue:
    def __init__(self, items: List[Tuple[int, str]]):
        self.mutation = {}
        heapq.heapify(items)
        self.items = items

    def mutate(self, food: str, new_rating: int):
        self.mutation[food] = -new_rating
        heapq.heappush(self.items, (-new_rating, food))
        return None

    def peek(self) -> str:
        while self.items:
            rating, food = self.items[0]

            if food not in self.mutation:
                return food

            if rating != self.mutation[food]:
                heapq.heappop(self.items)
                continue

            return food

        return ""


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        food_groupby_cuisines = defaultdict(list)

        for i in range(len(foods)):
            food_groupby_cuisines[cuisines[i]].append((-ratings[i], foods[i]))

        pq_groupby_cuisines = {}
        for cuisine, food_ratings in food_groupby_cuisines.items():
            lpq = LazyPriorityQueue(food_ratings)
            pq_groupby_cuisines[cuisine] = lpq

        self.pq_groupby_cuisines = pq_groupby_cuisines
        self.food_cuisine = {foods[i]: cuisines[i] for i in range(len(foods))}

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.pq_groupby_cuisines[cuisine].mutate(food, newRating)
        return None

    def highestRated(self, cuisine: str) -> str:
        return self.pq_groupby_cuisines[cuisine].peek()


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
