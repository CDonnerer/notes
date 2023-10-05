"""Aync querying of API
"""
import time
import asyncio


class AsyncClient:
    async def post(self, item_id):
        await asyncio.sleep(0.1)
        return {"response": item_id}


def query_with_semaphore(item_ids, client, max_concurrent_requests=100):
    semaphore = asyncio.Semaphore(max_concurrent_requests)

    async def post_request(item_id):
        async with semaphore:
            response = await client.post(item_id)
            return response

    loop = asyncio.get_event_loop()
    group = asyncio.gather(*[post_request(item_id) for item_id in item_ids])
    results = loop.run_until_complete(group)

    return results


def query_with_loop_throttle(
    item_ids, client, requests_per_second=100, max_concurrent_requests=100
):
    semaphore = asyncio.Semaphore(max_concurrent_requests)

    async def post_request(client, item_id):
        async with semaphore:
            response = await client.post(item_id)
            return response

    async def post_many(item_ids):
        tasks = []

        for item_id in item_ids:
            task = asyncio.create_task(post_request(client, item_id))
            tasks.append(task)
            await asyncio.sleep(1 / requests_per_second)

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(post_many(item_ids))
    return results


def query_with_queues(
    item_ids, client, requests_per_second=100, max_concurrent_requests=100
):
    async def producer_fn(queue, item_ids):
        for item_id in item_ids:
            await queue.put(item_id)
            await asyncio.sleep(1 / requests_per_second)

    async def consumer(work_queue, result_queue):
        while True:
            item_id = await work_queue.get()
            result = await client.post(item_id)
            work_queue.task_done()
            await result_queue.put(result)

    async def run(item_ids):
        work_queue = asyncio.Queue()
        result_queue = asyncio.Queue()

        consumers = [
            asyncio.create_task(consumer(work_queue, result_queue))
            for _ in range(max_concurrent_requests)
        ]
        producer = asyncio.create_task(producer_fn(work_queue, item_ids))
        await producer

        await work_queue.join()

        for c in consumers:
            c.cancel()

        results = []
        while not result_queue.empty():
            result = await result_queue.get()
            results.append(result)
        return results

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(run(item_ids))
    return results


def main():
    item_ids = list(range(100))
    client = AsyncClient()

    start = time.perf_counter()
    res = query_with_semaphore(item_ids, client)
    end = time.perf_counter()
    print("Finished querying with semaphore in %s", end - start)

    start = time.perf_counter()
    res = query_with_loop_throttle(item_ids, client)
    end = time.perf_counter()
    print("Finished querying with loop throttle in %s", end - start)

    start = time.perf_counter()
    res = query_with_queues(item_ids, client)
    end = time.perf_counter()
    print("Finished querying with queues in %s", end - start)


if __name__ == "__main__":
    main()
