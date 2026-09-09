# Psychology Agents

Multi-agent AI system exploring how personality traits shape behavior in LLM-driven agents, grounded in psychological theory.

## Overview

This project simulates agents with distinct psychological profiles to study how personality-level traits influence decision-making, communication style, and interaction patterns. The flagship agent, **Marcus**, is modeled with narcissistic personality traits — used as a test case for observing how self-focused, validation-seeking behavior emerges and persists across conversational turns.

Marcus is a genuine agent, not just a persona-driven chatbot: he perceives input, autonomously decides whether to respond directly or invoke a tool, can chain multiple tool calls in a single turn without re-prompting, and retains conversational memory across turns.

## Agent Capabilities

- **Multi-tool decision-making** — Marcus chooses between `rate_idea` and `roast_username` based on context, without being told which to use
- **Autonomous multi-step execution** — given a compound request (e.g. "rate these three ideas"), Marcus independently calls the relevant tool multiple times in sequence, then synthesizes a final response
- **Conversation memory** — Marcus retains and correctly recalls information shared earlier in the conversation
- **Structured tool calls** — tool arguments are generated and parsed as structured JSON, not free text

## Tech

- **Groq API** — running on `openai/gpt-oss-120b` for fast inference
- Python-based agent architecture using function-calling / tool-use

## Status

Functional — Marcus runs with multi-tool selection, autonomous multi-step tool calling, and persistent conversation memory. Next steps include expanding to additional personality archetypes and building out structured evaluation for behavioral consistency.

## Background

Built by someone with a psychology background (BSc, Singhania University) moving into applied AI/robotics — this project is a first step in connecting behavioral science to embodied and agentic AI systems.
