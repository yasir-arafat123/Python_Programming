# Concurrency, Parallelism & Async

Aim: Provide a mental model for threads, processes, async IO, and choosing the right approach under the GIL constraints.

## Subtopics
1. 01_Threads_GIL_Concepts
2. 02_threading_Locks_Events
3. 03_Queues_Producer_Consumer
4. 04_multiprocessing_Pools
5. 05_AsyncIO_Event_Loop
6. 06_Async_Tasks_Cancellation
7. 07_Async_Streams_async_generators
8. 08_Concurrency_Patterns
9. 09_Performance_Comparison
10. 10_ThirdParty_async_http

## Learning Outcomes
- Differentiate concurrency vs parallelism.
- Explain GIL impact and when CPU-bound needs multiprocessing.
- Write basic threading + queue pipeline and async equivalent.
- Handle cancellation and timeouts correctly.

## Exercises
- Convert a blocking IO loop to asyncio.
- Implement a safe producer/consumer with graceful shutdown.
- Benchmark thread pool vs process pool for CPU vs IO tasks.
