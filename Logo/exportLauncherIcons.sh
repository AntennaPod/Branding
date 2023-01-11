#!/bin/bash

function exportLauncherImage() {
    mkdir -p res/mipmap-mdpi
    mkdir -p res/mipmap-hdpi
    mkdir -p res/mipmap-xhdpi
    mkdir -p res/mipmap-xxhdpi
    mkdir -p res/mipmap-xxxhdpi
    inkscape --export-type="png" --export-width=48 --export-filename="res/mipmap-mdpi/$2" "$1"
    inkscape --export-type="png" --export-width=72 --export-filename="res/mipmap-hdpi/$2" "$1"
    inkscape --export-type="png" --export-width=96 --export-filename="res/mipmap-xhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=144 --export-filename="res/mipmap-xxhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=192 --export-filename="res/mipmap-xxxhdpi/$2" "$1"
    optipng res/**/**.png
}

exportLauncherImage logo-icon.svg ic_launcher.png

