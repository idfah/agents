---
name: multi-agent-ideation
description: Use independent subagents to generate, score and synthesize ideas
  for a problem.  Use only when the user explicitly asks to "perform
  multi-agent ideation," "use multiple agents to ideate," or uses a close
  phrase that clearly requests multi-agent ideation.  Do not use for ordinary
  brainstorming or requests for ideas.
---

# Multi-Agent Ideation

Generate and evaluate novel ideas without changing the target.

## Establish The Brief

- Infer the topic from the request and current discussion.  Ask essential
  clarifying questions when a task-complete brief cannot be formed.
- Create a compact, solution-neutral brief containing the objective, relevant
  facts, constraints, success criteria, artifacts and exclusions.
- Include prior decisions that constrain the task, but omit unrelated context
  and preliminary solutions that could anchor the agents.
- Permit read-only inspection and safe research.  Do not modify files or
  implement any proposal during ideation.

## Select Independent Agents

Launch subagents with the Agent tool, passing the role name as `subagent_type`.
Launch all subagents in a single message so they run concurrently.

Use these custom agents for the default roles:
- Machine Learning Scientist: `ml_scientist`
- Algorithms Expert: `algorithms_expert`
- Mathematician: `mathematician`
- Researcher: `researcher`

If the caller names a roster, use it instead of the defaults.  If the caller
asks to add or also include roles, extend the default roster.  Use a matching
custom agent when available and `general-purpose` only when necessary.

Subagents do not inherit the conversation.  Give each the same explicit core
brief plus its role-specific perspective.  Tell each agent to work
independently, not delegate and not consult other agents.

## Collect Scored Proposals

Ask every subagent for exactly five distinct proposals, ordered by decreasing
score and limited to 1,000 words total.  Include this YAML-like structure in
each prompt:

```yaml
- title: A concise name
  score: An integer from 1 to 10
  proposal: What to do
  rationale: Why it may work
  caveats: Material assumptions, limitations or risks
```

Use 10 for an exceptionally strong proposal, 5 for a plausible proposal with
substantial concerns and 1 for a proposal that is not recommended.  Do not
force a particular score distribution.

## Synthesize The Results

After all agents respond, collate their proposals without generating a
separate proposal set.  Merge semantically equivalent or usefully
complementary ideas.  Exercise judgment based on:

- independent commonality across agents
- contributing scores without mechanically averaging them
- strength of the rationales and material caveats
- whether a distinctive minority proposal deserves preservation

Return 3-5 leading candidates ordered by the top-level agent's judgment.  For
each candidate, describe the idea, rationale and caveats, and report the
independent support count and contributing score range when useful.

Summarize what coalesced, where agents disagreed and which ideas remained
distinct.  Treat scattered conclusions as evidence that the task may be
ambiguous, broad or in need of refinement or experimentation.  Do not
manufacture consensus.

Return the report in the response and write it to a file only when explicitly
requested.  If the caller also requested planning or implementation, print the
report before beginning that separately authorized task.
