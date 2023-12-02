#!/bin/bash

function exportAdaptiveLauncherImage() {
    mkdir -p res/mipmap-mdpi
    mkdir -p res/mipmap-hdpi
    mkdir -p res/mipmap-xhdpi
    mkdir -p res/mipmap-xxhdpi
    mkdir -p res/mipmap-xxxhdpi
    inkscape --export-type="png" --export-width=108 --export-filename="res/mipmap-mdpi/$2" "$1"
    inkscape --export-type="png" --export-width=192 --export-filename="res/mipmap-hdpi/$2" "$1"
    inkscape --export-type="png" --export-width=216 --export-filename="res/mipmap-xhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=324 --export-filename="res/mipmap-xxhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=432 --export-filename="res/mipmap-xxxhdpi/$2" "$1"
    optipng res/**/**.png
}

exportAdaptiveLauncherImage ic_dev_foreground.svg ic_launcher_foreground.png
exportAdaptiveLauncherImage ic_dev_background.svg ic_launcher_background.png

