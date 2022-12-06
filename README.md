# WS-EPHEMERAL-QBIT

This project aims to automate requesting an ephemeral matched port from WindScribe then update a qBittorrent client's config to match. Once the setup is done it sleeps for 6 days before requesting a new port. This tool assumes you have a WindScribe Pro account and a qBittorrent client with accessible webui.

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
| DEBUG         | Enable debug logging                | False   |

Available tags for docker image:

| Tag    | Container type                                |
| ------ | --------------------------------------------- |
| latest | most recent changes straight from main branch |

## Privacy

I assure you that nothing is being collected or logged. Any configuration credentials are stored solely on your device and used only when needed as part of authentication with WindScribe and your qBittorrent instance.

In general it's recommended to always go over the source for tools that use login credentials. After you've read through the source, feel free to compile the docker image yourself!

If you have further questions or concerns, please open an issue.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

[GPL3](LICENSE.md)
