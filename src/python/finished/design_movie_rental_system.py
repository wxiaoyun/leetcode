import heapq
from typing import List, Optional, Tuple

# https://leetcode.com/problems/design-movie-rental-system/


# TLE
class Shop:
    def __init__(self):
        self.movie_price = {}
        self.rented = set()
        self.rented_max_heap = []

    def add_movie(self, movie: int, price: int) -> None:
        self.movie_price[movie] = price
        return None

    def rent(self, movie: int) -> None:
        if movie in self.rented:
            return None

        self.rented.add(movie)

        price = self.get_movie_price(movie)
        assert price is not None

        heapq.heappush(self.rented_max_heap, (-price, movie))
        return None

    def drop(self, movie: int) -> None:
        if movie in self.rented:
            self.rented.remove(movie)

        return None

    def is_movie_rented(self, movie) -> bool:
        return movie in self.rented

    def get_movie_price(self, movie: int) -> Optional[int]:
        return self.movie_price.get(movie, None)

    def get_cheapest_rented_movies(self) -> List[Tuple[int, int]]:
        rented_movie_prices = set()

        while self.rented_max_heap and len(rented_movie_prices) < 5:
            neg_price, movie = heapq.heappop(self.rented_max_heap)
            if movie not in self.rented:
                continue

            rented_movie_prices.add((movie, -neg_price))

        for m, p in rented_movie_prices:
            heapq.heappush(self.rented_max_heap, (-p, m))

        return list(rented_movie_prices)


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        shops = [Shop() for _ in range(n)]

        for shop, movie, price in entries:
            shops[shop].add_movie(movie, price)

        self.shops = shops
        return None

    def search(self, movie: int) -> List[int]:
        pq = []

        for shop_id, shop in enumerate(self.shops):
            if shop.is_movie_rented(movie):
                continue

            price = shop.get_movie_price(movie)
            if price is None:
                continue

            entry = (-price, -shop_id)
            heapq.heappush(pq, entry)
            if len(pq) > 5:
                heapq.heappop(pq)

        result = []
        while pq:
            _, neg_shop_id = heapq.heappop(pq)
            result.append(-neg_shop_id)
        result.reverse()
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.shops[shop].rent(movie)
        return None

    def drop(self, shop: int, movie: int) -> None:
        self.shops[shop].drop(movie)
        return None

    def report(self) -> List[List[int]]:
        max_heap = []
        for shop_id, shop in enumerate(self.shops):
            movie_prices = shop.get_cheapest_rented_movies()

            for movie, price in movie_prices:
                entry = (-price, -shop_id, -movie)
                heapq.heappush(max_heap, entry)
                if len(max_heap) > 5:
                    heapq.heappop(max_heap)

        result = []
        while max_heap:
            _, neg_shop_id, neg_movie_id = heapq.heappop(max_heap)
            result.append((-neg_shop_id, -neg_movie_id))
        result.reverse()
        return result


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
