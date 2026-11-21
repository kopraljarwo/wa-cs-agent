# WhatsApp AI Customer Service Agent

Autonomous customer support agent combining **LLM + pgvector RAG + Function Calling** over WhatsApp Cloud API.

## Architecture
- **API & Webhooks:** FastAPI
- **Agent Orchestration:** LangGraph (grounded RAG + strict tool calling)
- **Knowledge & Vector Store:** PostgreSQL + `pgvector`

## Next Tasks for Devin
1. Wire up `pgvector` retrieval pipeline for company FAQ & refund policy docs.
2. Connect LangGraph tool-calling nodes (`get_order_status`, `check_refund_eligibility`, `create_support_ticket`).
3. Add pytest suite for webhook verification and hallucination guardrails.
