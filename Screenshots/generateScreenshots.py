#!/bin/python
import os
from pathlib import Path

def generateText(text, font):
    print(text)
    os.system("convert -size 1698x750 xc:none -gravity Center -pointsize 130 -fill '#167df0' -font " + font + ' -annotate 0 "' + text + '" /tmp/text.png')

def generateTabletText(text, font):
    print(text)
    os.system("convert -size 1730x350 xc:none -gravity Center -pointsize 80 -fill '#167df0' -font " + font + ' -annotate 0 "' + text + '" /tmp/text.png')

def simplePhone(text, backgroundFile, screenshotFile, outputFile, font):
    generateText(text, font)
    os.system('convert templates/' + backgroundFile
        + ' templates/phone.png -geometry +0+0 -composite '
        + screenshotFile + ' -geometry +306+992 -composite '
        + '/tmp/text.png -geometry +0+0 -composite '
        + outputFile)

def simpleTablet(text, screenshotFile, outputFile, font):
    generateTabletText(text, font)
    os.system('convert ' + screenshotFile + ' -resize 1285 "/tmp/resized-image.png"')
    os.system('convert templates/tablet.png '
        + '/tmp/resized-image.png -geometry +224+459 -composite '
        + '/tmp/text.png -geometry +0+0 -composite '
        + outputFile)

def twoPhones(text, rawScreenshotsPath, outputFile, font):
    generateText(text, font)
    os.system('convert templates/background2.png '
        + 'templates/twophones-a.png -geometry +0+10 -composite '
        + rawScreenshotsPath + '/03a.png -geometry +119+992 -composite '
        + 'templates/twophones-b.png -geometry +0+0 -composite '
        + rawScreenshotsPath + '/03b.png -geometry +479+1540 -composite '
        + '/tmp/text.png -geometry +0+0 -composite '
        + outputFile)

def generateScreenshots(language, font):
    Path('output/' + language).mkdir(parents=True, exist_ok=True)
    with open('raw/' + language + '/texts.txt') as textDefinitions:
        texts = textDefinitions.readlines()
    rawScreenshotsPath = 'raw/' + language
    outputPath = 'output/' + language
    
    if not Path(rawScreenshotsPath + '/00.png').is_file():
        rawScreenshotsPath = 'raw/en-US'

    simplePhone(texts[0], 'background1.png', rawScreenshotsPath + '/00.png', outputPath + '/00.png', font)
    twoPhones(texts[3],                      rawScreenshotsPath,             outputPath + '/01.png', font)
    simplePhone(texts[1], 'background1.png', rawScreenshotsPath + '/01.png', outputPath + '/02.png', font)
    simplePhone(texts[2], 'background2.png', rawScreenshotsPath + '/02.png', outputPath + '/03.png', font)
    simplePhone(texts[4], 'background1.png', rawScreenshotsPath + '/04.png', outputPath + '/04.png', font)
    simplePhone(texts[5], 'background2.png', rawScreenshotsPath + '/05.png', outputPath + '/05.png', font)
    if len(texts) == 7:
        simpleTablet(texts[6], rawScreenshotsPath + '/tablet.png', outputPath + '/tablet.png', font)
    os.system('mogrify -resize 1120 "' + outputPath + '/0*.png"')

generateScreenshots('de-DE', 'Sarabun-Bold')
generateScreenshots('en-US', 'Sarabun-Bold')
generateScreenshots('fr-FR', 'Sarabun-Bold')
generateScreenshots('he-IL', 'Arimo-Bold')
generateScreenshots('nl-NL', 'Sarabun-Bold')
generateScreenshots('it-IT', 'Sarabun-Bold')
generateScreenshots('es-ES', 'Sarabun-Bold')
