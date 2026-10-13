# lightningai Hermes plugin

Registers Lightning AI (`https://lightning.ai/api/v1`) as a Hermes model provider
(`--provider lightningai` / `lightning-ai` / `lightning`). Models are fetched
live from `/models`.

## Disclosure

- Registers one model provider at import and nothing else (no tools, hooks,
  commands or threads).
- Chat requests and the model-list probe go to `https://lightning.ai/api/v1`
  (or `LIGHTNING_BASE_URL`) through Hermes' own client with
  `LIGHTNING_API_KEY`, which Hermes reads. The plugin itself opens no connections,
  reads/writes no files and starts no processes.
- Env vars: `LIGHTNING_API_KEY` (also `LIGHTNING_AI_API_KEY`), optional
  `LIGHTNING_BASE_URL` to override the endpoint.
