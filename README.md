# WS-EPHEMERAL-QBIT

This project aims to automate requesting an ephemeral matched port from windscribe then update a qBittorrent client's config to match. Once the setup is done it sleeps for 6 days before requesting a new port. This tool assumes you have a windscribe pro account and a qBittorrent client with accessible webui.

## Docker Compose Setup

Environment variables:

| Variable      | Function                            | Default |
| ------------- | ----------------------------------- | ------- |
| WS_USERNAME   | Windscribe username                 |         |
| WS_PASSWORD   | Windscribe password                 |         |
| WS_TOTP_TOKEN | Windscribe 2FA Token                |         |
| QB_USERNAME   | qBittorrent WebUI username          |         |
| QB_PASSWORD   | qBittorrent WebUI password          |         |
| QB_PORT       | qBittorrent WebUI port              |         |
| QB_HOST       | qBittorrent WebUI URL (except port) |         |
| WS_DEBUG         | Enable debug logging             | False   |

Available tags for docker image:

| Tag    | Container type                                |
| ------ | --------------------------------------------- |
| latest | most recent changes straight from main branch |

## Privacy

In general, always go over the source for tools that use login credentials. Even better, compile the docker image yourself!

I assure you that nothing is being collected or logged. Your credentials are safe and set via environment variable only. Still If you have further questions or concerns, please open an issue here.

## License

[GPL3](LICENSE.md)
