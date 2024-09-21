"""Task orchestration with async"""

from __future__ import annotations

import asyncio
import dataclasses
import datetime
import random
import time
import uuid
from enum import Enum


class TaskStatus(str, Enum):
    STARTED = "STARTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

    def __repr__(self) -> str:
        return self.value


@dataclasses.dataclass
class Task:
    task_id: str
    depends_on: list[Task] | None = None


task1 = Task(task_id="01")
task2 = Task(task_id="02", depends_on=[task1])
task3 = Task(task_id="03", depends_on=[task1])

tasks = [task1, task2, task3]


def run_task(task_id: str) -> str:
    """Simulates starting a run and getting an id back"""
    assert task_id
    run_id = str(uuid.uuid4())
    return run_id


def get_task_status(run_id: str) -> str:
    """Simulates querying an API to get task status"""
    assert run_id
    status = random.choices(
        [TaskStatus.RUNNING, TaskStatus.COMPLETED, TaskStatus.FAILED],
        [0.4, 0.4, 0.2],
        k=1,
    )[0]
    return status


async def run_task_and_poll(task, timeout=datetime.timedelta(minutes=1)):
    run_id = run_task(task.task_id)
    print(f"{datetime.datetime.now()}: Started task={task.task_id}, run_id={run_id}")
    deadline = time.time() + timeout.total_seconds()

    while time.time() < deadline:
        status = get_task_status(run_id=run_id)
        if status == TaskStatus.COMPLETED:
            return status
        elif status == TaskStatus.FAILED:
            raise Exception("Task failed!")
        await asyncio.sleep(1)
    raise TimeoutError


async def consumer(work_queue, result_queue):
    while True:
        task = await work_queue.get()
        try:
            result = await run_task_and_poll(task=task)
        except Exception as e:
            print(e)
            result = TaskStatus.FAILED
        work_queue.task_done()
        await result_queue.put((task.task_id, result))


async def run(max_concurrency: int = 3):
    work_queue = asyncio.Queue()
    result_queue = asyncio.Queue()
    consumers = [
        asyncio.create_task(consumer(work_queue, result_queue))
        for _ in range(max_concurrency)
    ]

    task_status = {task.task_id: None for task in tasks}
    starting_tasks = [task for task in tasks if task.depends_on is None]
    dependent_tasks = [task for task in tasks if task.depends_on is not None]

    if len(starting_tasks) == 0:
        if len(dependent_tasks) != 0:
            raise ValueError("Invalid task dag!")
        return

    for task in starting_tasks:
        await work_queue.put(task)
        task_status[task.task_id] = "STARTED"

    while True:
        if all(
            status in (TaskStatus.COMPLETED, TaskStatus.FAILED)
            for status in task_status.values()
        ):
            break

        task_id, result = await result_queue.get()
        task_status[task_id] = result

        for task in dependent_tasks:
            if task_status[task.task_id] is None:
                if all(
                    task_status[dep_task.task_id] == TaskStatus.COMPLETED
                    for dep_task in task.depends_on
                ):
                    await work_queue.put(task)
                    task_status[task.task_id] = TaskStatus.STARTED
                if any(
                    task_status[dep_task.task_id] == TaskStatus.FAILED
                    for dep_task in task.depends_on
                ):
                    task_status[task.task_id] = TaskStatus.FAILED

        print(task_status)

    for c in consumers:
        c.cancel()


def run_task_orchestration():
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(run())
    return results


if __name__ == "__main__":
    start = time.perf_counter()
    run_task_orchestration()
    end = time.perf_counter()
    print(f"Finished task orchestration in {end - start} seconds")
