# WS-EPHEMERAL-QBIT

This project aims to automate setting up an ephemeral matched port on windscribe's VPN service then setting a qBittorrent client's config to match. Once the setup is done it sleeps for next 6 days before renewal. This tool assumes you have a windscribe pro account and a qBittorrent client with accessible webui.

## Docker Compose Setup

```yaml
  ws-ephemeral-qbit:
    image: coordspace/ws-ephemeral-qbit:latest
    container_name: ws-ephemeral-qbit
    environment:
      - WS_USERNAME=
      - WS_PASSWORD=
      - QB_USERNAME=
      - QB_PASSWORD=
      - QB_PORT=8080
      - QB_HOST=http://localhost
      - WS_DEBUG=TRUE
    labels:
      - traefik.enable=false
    restart: "no"
```

Available tags for docker image:

| Tag    | Container type                                |
| ------ | --------------------------------------------- |
| latest | most recent changes straight from main branch |

## Privacy

In general, always go over the source for tools that use login credentials. Even better, compile the docker image yourself!

I assure you that nothing is being collected or logged. Your credentials are safe and set via environment variable only. Still If you have further questions or concerns, please open an issue here.

## License

[GPL3](LICENSE.md)
