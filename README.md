# AI Mentor — AI-Powered Personalized Learning Platform

A full-stack web application that helps self-learners follow personalized curriculum paths, powered by three AI engineering features. Built as a portfolio project demonstrating practical AI engineering depth — dynamic prompt engineering, retrieval-augmented generation built from scratch, and agentic reasoning for structured curriculum generation.

## What It Does

- **Follow a structured, AI-generated curriculum path** tailored to your goals and skill level
- **Chat with an AI mentor** for real-time, grounded guidance
- **Track learning progress** over time

## Core AI Features

### 1. Personalized Prompt Engine
Reads each user's skill level, goals, and learning style (captured during onboarding) and dynamically generates a unique system prompt per session — adapting tone, depth, and examples automatically as the user progresses.

### 2. RAG Pipeline (built from scratch, no LangChain)
Learning content from official docs and hand-written summaries is chunked, embedded using Gemini Embeddings, and stored in ChromaDB. User questions are answered using retrieved, trusted context rather than relying purely on the model's training data.

### 3. Agentic Curriculum Generator
Given a learning goal, the AI reasons through prerequisites, topic ordering, and realistic weekly time allocation, returning a structured JSON roadmap — validated with Pydantic and rendered as an interactive visual roadmap.

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React, Tailwind CSS, Framer Motion, Three.js |
| Backend | FastAPI (Python), async routes |
| Database | PostgreSQL, SQLAlchemy 2.0, Alembic migrations |
| Vector DB | ChromaDB |
| AI Provider | Google Gemini API (embeddings + generation) |
| Auth | JWT (stateless), bcrypt password hashing |
| Package Management | `uv` |

## Project Structure

ai-mentor/
├── backend/ # FastAPI application
└── frontend/ # React application (in progress)

## Current Status

🚧 **Actively in development.** Backend authentication (signup, login, JWT-protected routes) is complete. Currently building the Personalized Prompt Engine (Phase 3).

## Development Phases

- [x] Phase 2 — FastAPI Backend (auth, database, migrations)
- [ ] Phase 3 — AI Feature 1: Personalized Prompt Engine
- [ ] Phase 4 — AI Feature 2: RAG Pipeline
- [ ] Phase 5 — AI Feature 3: Agentic Curriculum Generator
- [ ] Phase 1 — Frontend (React + Tailwind + Framer Motion + Three.js)
- [ ] Phase 6 — Polish, Deploy, CI/CD

## Author

Built by [Naseef](https://github.com/Naseefnf) as a portfolio project for AI Engineer roles.