
# 🤖 DevLogs = Project Memory System

- **Date**: 2025-06-21
- **Time**: 21:51
- **Document Focus**: Guidelines for a devlog system for AI agent team handoffs

Development Status Report in the `./_DEV_LOG/` directory Preserve development context with team using AI memory assisted documentation to relay work between sessions with the agent human pair programming ~ metameta 

Session Report 
- Filename Format: `./_DEV_LOG/workinprogress/YYYY-MM-DD_HHMM_descriptive-title.md`
- Context: Current activities and AI generated moments to document:
  -  Real decisions, failures, rationale

Guidelines & Standards Report
- Filename Format: `./_DEV_LOG/guides-standards/GS_YYYY-MM-DD_HHMM_descriptive-title.md`
- Context:Project guidelines and standards for development 

DevOps & tooling Report 
- Filename Format: `./_DEV_LOG/devops-tools/DEVOPS_YYYY-MM-DD_HHMM_descriptive-title.md`
- Context: Tooling and infrastructure updates, decisions, and rationales

Handoff to next session Report
- Filename Format: `./_DEV_LOG/handoffs/HO_YYYY-MM-DD_HHMM_descriptive-title.md`
- Context: What to expect in the next session, what is ready, what is not, what is blocking

Issues & Blocking Items Report
- Filename Format: `./_DEV_LOG/issues/ISSUES_YYYY-MM-DD_HHMM_descriptive-title.md`
- Context: Blocking issues, what is holding up progress, and how to resolve
- Would like to develop an MCP workflow that runs in local development

Key Principles:
1. Real timestamps in filenames. Get the actual time with `touch file.tmp && ls -la file.tmp` 
2. Honest documentation - Include what failed, not just successes  
3. Context preservation - Why decisions were made, what was tried
4. Handoff clarity - Next session can continue without re-discovery

Project Overview:
- Chronicles journey using huggingface transformers and 
- Documents KnowTrails transcript search system evolution
- TurboRepo monorepo architecture
- Custom turborepo build, test, and deploy pipelines 
- FastAPI transcript service
- Discord bot integration
- Tracks "paraconsistent FE/BE alignment" philosophy  

- Serves as portfolio evidence of real problem-solving

Usage: Memory for several stakeholder and source of final project documentation being built with mkdocs in a separate repository as another collaboration project.

I would integrate it if i understood submodules in the context of the turbo monorepo.  seems like an anti-pattern if not handled properly.

The AIs task overall is to Read recent devlogs it is handed by filename, to understand current state, then create new ones documenting session work github issues and handoffs to new sessions. Sometimes handoff is needed as there is task creep and need issues created or moved to new token space.

---

Meta: This devlog documents the devlog system itself for future AI agent handoffs.
