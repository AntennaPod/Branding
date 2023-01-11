#!/bin/bash

function exportNotificationIcon() {
    mkdir -p res/drawable-mdpi
    mkdir -p res/drawable-hdpi
    mkdir -p res/drawable-xhdpi
    mkdir -p res/drawable-xxhdpi
    mkdir -p res/drawable-xxxhdpi

    inkscape --export-type="png" --export-width=24 --export-filename="res/drawable-mdpi/$2" "$1"
    inkscape --export-type="png" --export-width=36 --export-filename="res/drawable-hdpi/$2" "$1"
    inkscape --export-type="png" --export-width=48 --export-filename="res/drawable-xhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=72 --export-filename="res/drawable-xxhdpi/$2" "$1"
    inkscape --export-type="png" --export-width=96 --export-filename="res/drawable-xxxhdpi/$2" "$1"
    optipng res/**/**.png
}

exportNotificationIcon system_icon_white.svg ic_notification.png
exportNotificationIcon system_icon_white_news.svg ic_notification_new.png

