# Screenshots
AntennaPod might use screenshots on app stores, as well as website or other locations. This folder contains information about those.

## Creating screenshots
In the file `ScreenshotsDatabaseExport.db`, you can find a database export that is already prepared to take screenshots. It contains subscriptions where we already have the permission to use them for our promotion material.

The database export contains real podcasts but has some of the episodes removed that are not a good fit for screenshots or episodes where we are not allowed to use the artwork. The most recent episodes in the database that fill one screen can be used. Older or newer episodes might might not be allowed, so make sure to disable automatic feed updates before importing. Otherwise, the available episodes will change.

Please prefer using this database for promotion graphics. If you really need more episodes or more podcasts, please:

- Only take screenshots of child-friendly episode titles
- Do not take screenshots with episodes containing current politics
- Make sure that we are allowed to actually use the images and texts

## Translating screenshot titles
The translations are stored in `raw/LANGUAGE/texts.txt`. Each title is stored in one line. The line breaks are added manually (using `\n`) to ensure that they are added at a fitting position for promo graphics.

If the `raw/LANGUAGE` folder contains localized screenshots, those will be used. The folder can either contain no screenshots or all. If there are no screenshots, the generator script uses the English screenshots instead.

## Converting to framed screenshots
<img src="https://raw.githubusercontent.com/AntennaPod/Branding/master/Screenshots/raw/en-US/00.png" height="200" /> ► <img src="https://raw.githubusercontent.com/AntennaPod/AntennaPod/develop/app/src/main/play/listings/en-US/graphics/phone-screenshots/00.png" height="200" />

To convert the normal screenshots to framed ones, you can use the `generateScreenshots.py` tool.

System requirements:

- Linux
- Python
- ImageMagick needs to be installed
- The fonts mentioned in `generateScreenshots.py` need to be installed
