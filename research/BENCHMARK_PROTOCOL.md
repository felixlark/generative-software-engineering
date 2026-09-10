# Benchmark protocol

## Goal

Compare software-agent organizations and GSE variants without changing the task underneath the comparison.

## Experimental controls

Hold constant where possible:

- task input and acceptance criteria;
- repository baseline;
- model and reasoning configuration;
- tool and permission access;
- dependency and network environment;
- evaluation rubric.

Compare configurations such as a single end-to-end GSE, a dynamically delegated GSE, and a fixed-role pipeline when the research question requires it.

## Required measurements

Record:

- final functional quality and acceptance evidence;
- regressions or escaped defects;
- total input/output/cached tokens across all agents when available;
- tool calls and external compute cost when available;
- wall-clock time;
- number and size of handoffs;
- rework, conflicts, abandoned branches, and retries;
- context-loss recovery success;
- resulting code/process complexity.

Do not report a precise total cost when participant telemetry is incomplete. Keep cached-input accounting distinct from uncached input according to the runtime's metric semantics.

## Task set

Include both tasks that are naturally single-owner and tasks with genuine parallel or specialist work. A benchmark containing only highly parallel tasks biases the result toward multi-agent structures.

## Evidence bundle

For every run preserve task ID, baseline, configuration, outcome contract, delegation decisions, candidate identity, validation commands/interactions, final evaluator result, and known limitations.
