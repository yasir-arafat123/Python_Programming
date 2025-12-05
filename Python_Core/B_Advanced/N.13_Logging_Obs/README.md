# Logging, Configuration & Observability

Goal: Teach structured logging, configuration patterns, and intro observability concepts (metrics, trace correlation hints).

## Subtopics
1. 01_logging_Basics
2. 02_Handlers_Formatters_Filters
3. 03_Structured_Logging_JSON
4. 04_Log_Rotation_Performance
5. 05_Tracing_Context_Correlation
6. 06_Metrics_counters_timers
7. 07_Monitoring_Integration

## Learning Outcomes
- Configure logging robustly (dictConfig, basicConfig comparisons).
- Emit structured JSON logs with contextual enrichment.
- Explain log levels and performance trade-offs.
- Sketch how metrics & traces complement logs.

## Exercises
- Create a dictConfig with rotating file handler + console.
- Add request-id correlation through contextvars.
- Benchmark overhead of debug vs info logging in a loop.
