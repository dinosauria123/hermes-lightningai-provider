# plugins/model-providers/lightningai/__init__.py
from providers import register_provider
from providers.base import ProviderProfile

lightningai = ProviderProfile(
    name="lightningai",
    aliases=("lightning", "lightning-ai", "lightningai"),
    display_name="Lightning AI",
    description="OpenAI-compatible gateway at lightning.ai, models fetched from /models",
    signup_url="https://lightning.ai",
    env_vars=("LIGHTNING_API_KEY", "LIGHTNING_AI_API_KEY", "LIGHTNING_BASE_URL"),
    base_url="https://lightning.ai/api/v1",
    auth_type="api_key",
    api_mode="chat_completions",
)

register_provider(lightningai)
