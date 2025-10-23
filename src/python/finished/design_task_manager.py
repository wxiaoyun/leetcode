import heapq
from typing import List

# https://leetcode.com/problems/design-task-manager/


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        task_to_user = {tid: uid for uid, tid, _ in tasks}
        self.task_to_user = task_to_user

        task_pq = [(-p, -tid) for _, tid, p in tasks]
        heapq.heapify(task_pq)
        self.task_pq = task_pq

        # Dict<task_id, priority>
        self.mutation = {tid: p for _, tid, p in tasks}
        return None

    def add(self, userId: int, taskId: int, priority: int) -> None:
        entry = (-priority, -taskId)
        heapq.heappush(self.task_pq, entry)
        self.task_to_user[taskId] = userId
        self.mutation[taskId] = priority
        return None

    def edit(self, taskId: int, newPriority: int) -> None:
        entry = (-newPriority, -taskId)
        heapq.heappush(self.task_pq, entry)
        self.mutation[taskId] = newPriority
        return None

    def rmv(self, taskId: int) -> None:
        if taskId in self.mutation:
            del self.mutation[taskId]
        if taskId in self.task_to_user:
            del self.task_to_user[taskId]
        return None

    def execTop(self) -> int:
        while self.task_pq:
            negative_priority, negative_tid = heapq.heappop(self.task_pq)
            priority, tid = -negative_priority, -negative_tid

            if tid not in self.mutation:
                continue

            actual_priority = self.mutation[tid]
            if priority != actual_priority:
                continue

            # priority is truthful
            uid = self.task_to_user[tid]
            self.rmv(tid)
            return uid

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
