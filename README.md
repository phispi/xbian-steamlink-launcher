# Steamlink Launcher for Xbian Kodi

Plugin for [Xbian](https://xbian.org/) [Kodi](https://kodi.tv/) to launch [Steamlink](https://steamcommunity.com/app/353380/discussions/6/2806204039992195182/).

## Requirements

* Xbian already installed.

* [ssh](https://xbian.org/faq/#)(What is the default login/password? and How do I change the SSH port?) access to your xbian installation.

* Install [steamlink](https://steamcommunity.com/app/353380/discussions/0/1743353164093954254) debian package with:

  ```shell
  sudo apt-get update
  sudo apt-get install -y steamlink
  ```

## Plugin installation

* Log into ssh on your Kodi installation.

* Download the [zip](https://github.com/bigbrozer/kodi-steamlink-launcher/releases) of the launcher and install it via Kodi (*Extension → Install from Zip file*). You must **allow untrusted sources** in system settings prior to this.

## Want to contribute ?

Submit your contributions through [pull requests](https://help.github.com/articles/about-pull-requests/).

## Acknowledgement

```plain
Steam Copyright 2003-2018 Valve Corp. All rights reserved. Use of Steam Link software is subject to the Steam Subscriber Agreement, https://store.steampowered.com/subscriber_agreement/.
```

## Inspiration

* [bigbrozer/](https://gitlab.com/bigbrozer/kodi-steamlink-launcher) - generic kodi-steamlink-launcher package/scripts
* [grimlokason/osmc-steamlink](https://gitlab.com/grimlokason/osmc-steamlink) - scripting logic
* [swetoast/steamlink-launcher](https://github.com/swetoast/steamlink-launcher) - original script resources

## License

Steamlink Launcher for Kodi is licensed under GPLv2, see `LICENSE.txt`.
