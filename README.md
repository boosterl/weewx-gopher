# WeeWX Gopher

A skin for WeeWX which outputs [Gopher menu items](https://en.wikipedia.org/wiki/Gopher_(protocol)#Source_code_of_a_menu) which can be served by a [Gopher server](https://github.com/gophernicus/gophernicus).

```
                                                                                                                 Gopher Menu

       __          __    __          ____   __
       \ \        / /    \ \        / /\ \ / /
        \ \  /\  / /__  __\ \  /\  / /  \ V /
         \ \/  \/ / _ \/ _ \ \/  \/ /    > <
          \  /\  /  __/  __/\  /\  /    / . \
         __\/_ \/ \___|\___| \/  \/    /_/ \_\
        / ____|           | |
       | |  __  ___  _ __ | |__   ___ _ __
       | | |_ |/ _ \| '_ \| '_ \ / _ \ '__|
       | |__| | (_) | |_) | | | |  __/ |
        \_____|\___/| .__/|_| |_|\___|_|
                    | |
                    |_|

       Ghent, Belgium
       30/11/22 20:05:00

       Current Conditions

       Outside Temperature 0.2C
       Heat Index 0.2C
       Wind Chill 0.2C
       Dew Point -2.8C
       Outside Humidity 80%
       Barometer 1053.2 mbar (   N/A)
       Wind 0.0 m/s N (360)
       Rain Today 0.0 mm
       Rain Rate 0.0 mm/h
       UV Index 0.0
       Radiation 0 W/m
       Inside Temperature 17.2C
       Inside Humidity 30%

       Daily Statistics

       Outside Temperature Max 0.4C Min 0.1C
       Heat Index Max 0.4C Min 0.1C
       Wind Chill Max 0.4C Min 0.1C
       Dew Point Max -2.7C Min -3.0C
       Outside Humidity Max 80% Min 80%
       Barometer Max 1053.2 mbar Min 1053.2 mbar
       Max Wind
       0.0 m/s
       360
       Average Wind 0.0 m/s
       RMS Wind 0.0 m/s
       Vector Average 0.0 m/s
       Vector Direction 360
       Rain 0.0 mm
       Rain Rate 0.0 mm/h
       ET 0.0 mm
       UV Index 0.0
       Radiation Max 0 W/m Min 0 W/m
       Inside Temperature Max 17.2C Min 17.2C
       Inside Humidity Max 30% Min 30%

(FILE) Week
(FILE) Month
(FILE) Year
(FILE) About

       ___________________________________________________________________
                        Gophered by Gophernicus/3.1.1 on Debian/11 x86_64
```

## Installation

Clone the repo and run the installer:
```
wee_extension --install weewx-gopher
```

Restart weewx:
```
sudo systemctl restart weewx
```

To serve the Gopher menu items, [Gophernicus](https://github.com/gophernicus/gophernicus) can be used.

## Usage

To access the current weather coniditions, with for example `lynx`, just issue:
```
lynx gopher://$WEEWX_INSTANCE
```
