# custom_components/ultramsg/config_flow.py

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.components.persistent_notification import async_create

class UltraMSGConfigFlow(config_entries.ConfigFlow, domain='ultramsg'):
    """Handle the config flow for UltraMSG."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step of the config flow."""
        # Check if UltraMSG is already configured by verifying if the notify service exists
        is_configured = self.hass.data.get('ultramsg', {}).get('configured', False)

        if is_configured:
            message = "UltraMSG is already configured via `configuration.yaml`. No further action is needed."
        else:
            message = "UltraMSG is not yet configured in `configuration.yaml`. Please add the necessary configuration."

        # Create a persistent notification with the message
        async_create(
            self.hass,
            message,
            title="UltraMSG Configuration",
            notification_id="ultramsg_config_flow"
        )

        # Abort the flow with a fixed reason key to avoid errors
        return self.async_abort(reason=message)

    @callback
    def async_get_options_flow(self):
        """No options flow."""
        return None
