# Big Head

**Big Head** is a deployment of various home dashboard / monitoring tools, because it might be fun and cool.

All services are running via docker / docker-compose, across a variety of devices.

## Services

### Big Brain

**Big Brain** is the brains of the operation. Heh heh heh. Every piece of data will feed into the brain, and it'll also host all the crap for visualising it and what not.

### Big Nose

**Big Nose** is a minimal deployment of BalenaSense/sensor, intended to be hosted on a Raspberry Pi, running balenaOS, with a BME680 environment sensor doodad. It will take continual measurements, which it will feed into _Big Head_ via MQTT.
