# Assistant event-driven reminders and alerts

[![Open in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=fixtse&repository=ha-assistant-rules&category=integration)
[![Set up integration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=assistant_rules)

HACS preparation is complete, but this repository is currently private. [HACS does
not support private repositories](https://www.hacs.dev/docs/faq/private_repositories/),
so the HACS button cannot download this repository until its owner makes it public.
GitHub login or a personal access token does not remove this HACS limitation.
Until then, use an authenticated GitHub download and the manual installation below.

When the repository is public:

1. With HACS already installed, select **Open in HACS**, choose your Home Assistant instance, and add the custom repository as an **Integration**.
2. Download the integration in HACS, then restart Home Assistant.
3. Select **Set up integration** above, or open Settings → Devices & services → Add integration.
4. To upgrade an existing installation, keep its existing domain and private HA storage; HACS replaces only the component files. Review release notes before updating.

If the HACS button is unavailable, add `https://github.com/fixtse/ha-assistant-rules`
in HACS → ⋮ → Custom repositories, category **Integration**. This also requires
a public repository. The repository uses `custom_components/assistant_rules`,
with its HACS metadata at the repository root. Releases use the manifest's version.


![Integration icon](custom_components/assistant_rules/brand/icon.png)

Home Assistant owns reminder/timer deadlines and sensor/weather subscriptions, with one-shot callbacks to Zero.

Private repository: https://github.com/fixtse/ha-assistant-rules. Install `custom_components/assistant_rules` into the same path under your HA config directory, then restart HA and add the integration in Settings → Devices & services. Local icons require Home Assistant 2026.3 or newer. Private repositories require authenticated GitHub access to download updates.

Configure manages callback URL and private token (at least 24 characters) for future events. Existing rules and deadlines stay in HA storage. Rule state is managed through Zero's existing reminder/alert tools. Uncertain callback delivery is never automatically replayed. There is no separate assistant prompt in this component.

Existing YAML configuration imports once into a config entry. UI configuration then takes precedence; remove YAML after migration. Preserve existing `.storage` files and integration domains when upgrading. Back up your private config before deployment.

Development: open this repository in an isolated Codespace. Run `python3 -B -m unittest discover -s tests` and `python3 -m compileall -q custom_components`. The parent assistant repository also verifies both real HA config/options flows and protocol compatibility. Source changes must be synchronized with its tested snapshot in `integrations/home_assistant/`. Never run an installer against a live instance as a test.
