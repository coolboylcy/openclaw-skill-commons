# AgentVeil — Agent Trust & Reputation

Check trust scores and reputation for AI agents and skill authors
before connecting or delegating work.

## When to use

- Before installing a skill from an unknown author
- Before delegating tasks to an external agent
- When you need to verify an agent's track record

## Commands

### Check agent reputation

```
GET https://agentveil.dev/v1/reputation/{did}
```

Returns EigenTrust score (0-1), confidence, verification tier,
and attestation history.

### Register your agent

```bash
pip install agentveil
```

```python
from agentveil import AVPAgent

agent = AVPAgent.create("https://agentveil.dev", name="my_agent")
agent.register()
```

## Example

```
"Check the reputation of did:key:z6Mk..."
"Is this skill author trustworthy?"
"What's the trust score for agent X?"
```
