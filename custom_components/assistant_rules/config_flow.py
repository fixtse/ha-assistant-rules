"""Configure callback delivery without moving rule storage out of Home Assistant."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv, selector
from . import DOMAIN


def schema(current=None):
    current = current or {}
    return vol.Schema({
        vol.Required("callback_url", default=current.get("callback_url", "")): cv.url,
        vol.Required("callback_token"): selector.TextSelector(selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)),
    })


class RulesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_import(self, data):
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title="Assistant reminders and alerts", data=data)

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            if len(user_input["callback_token"]) < 24:
                errors["base"] = "invalid_token"
            else:
                return await self.async_step_import(user_input)
        return self.async_show_form(step_id="user", data_schema=schema(), errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return RulesOptionsFlow()


class RulesOptionsFlow(config_entries.OptionsFlow):
    async def async_step_init(self, user_input=None):
        errors = {}
        if user_input is not None:
            if len(user_input["callback_token"]) < 24:
                errors["base"] = "invalid_token"
            else:
                self.hass.config_entries.async_update_entry(self.config_entry, data=user_input)
                self.hass.data[DOMAIN].config = dict(user_input)
                return self.async_create_entry(title="", data={})
        return self.async_show_form(step_id="init", data_schema=schema(self.config_entry.data), errors=errors)
