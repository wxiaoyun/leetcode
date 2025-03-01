# https://leetcode.com/problems/my-calendar-ii


class MyCalendarTwo:

    def __init__(self):
        self.double_books = []
        self.books = []

    def book(self, startTime: int, endTime: int) -> bool:
        for db_s, db_e in self.double_books:
            if db_s < endTime and db_e > startTime:
                return False

        for s, e in self.books:
            if s < endTime and e > startTime:
                self.double_books.append((max(s, startTime), min(e, endTime)))

        self.books.append((startTime, endTime))
        return True


class MyCalendarTwo:

    def __init__(self):
        self.ovlp_0 = []
        self.ovlp_1 = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.ovlp_1:
            if s < end and start < e:
                return False  # any form of overlap is disallowed

        for s, e in self.ovlp_0:
            if s < end and start < e:
                # append the overlapping region
                self.ovlp_1.append((max(s, start), min(e, end)))
        self.ovlp_0.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
