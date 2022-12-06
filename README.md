# WS-EPHEMERAL-QBIT 

This project aims to automate requesting an ephemeral matched port from Windscribe then update a qBittorrent client's config to match. Once the setup is done it sleeps for 6 days before requesting a new port. This tool assumes you have a Windscribe Pro account and a qBittorrent client with accessible webui.

<a href="https://hub.docker.com/r/coordspace/ws-ephemeral-qbit/builds"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Docker&logo=docker&message=latest image" /></a> <a href="https://github.com/users/CoordSpace/packages/container/package/ws-ephemeral-qbit"><img src="https://img.shields.io/static/v1?label=GHCR.io&message=latest image&style=for-the-badge" /></a> <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=for-the-badge)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

I assure you that nothing is being collected or logged. Any configuration credentials are stored solely on your device and used only when needed as part of authentication with Windscribe and your qBittorrent instance.

In general it's recommended to always go over the source for tools that use login credentials. After you've read through the source, feel free to compile the docker image yourself!

If you have further questions or concerns, please open an issue.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/Trigus42"><img src="https://avatars.githubusercontent.com/u/59501676?v=4?s=100" width="100px;" alt="Trigus42"/><br /><sub><b>Trigus42</b></sub></a><br /><a href="https://github.com/CoordSpace/ws-ephemeral-qbit/commits?author=Trigus42" title="Code">💻</a> <a href="https://github.com/CoordSpace/ws-ephemeral-qbit/commits?author=Trigus42" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

[GPL3](LICENSE.md)
