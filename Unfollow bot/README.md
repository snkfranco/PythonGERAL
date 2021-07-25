Insta Unfollower
===================

[![](https://images.microbadger.com/badges/version/tuxity/insta-unfollower.svg)](https://hub.docker.com/r/tuxity/insta-unfollower/)
![](https://images.microbadger.com/badges/image/tuxity/insta-unfollower.svg)

Script para instagram que permite que voce pare de seguir as pessoas em massa (MASSIVE UNFOLLOW)

## Instalação
### Com Docker
```
docker pull tuxity/insta-unfollower:latest
docker run -d -v $(pwd)/cache:/usr/src/insta-unfollower/cache --env INSTA_USERNAME=myusername --env INSTA_PASSWORD=mypassword tuxity/insta-unfollower:latest
```

### Sem Docker
```
INSTA_USERNAME=myusername INSTA_PASSWORD=mypassword python3 insta-unfollower.py
Ou
python3 insta-unfollower.py USERNAME PASSWORD
```

## RoadMap
- Username whitelist.
- Better flow for calculating time between requests to avoid ban.
- ~~Avoid re-log on instagram everytime when we run the script~~ done
- ~~Keep followers and following lists in cache to speedup execution~~ done
