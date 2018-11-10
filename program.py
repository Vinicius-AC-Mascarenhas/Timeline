from PIL import Image, ImageDraw, ImageFont
from math import floor
from data import *

#########################################################################
# Global variables
#########################################################################

XCENTER = 1600
dotList = []

SONG_TITLE_FONT_SIZE = 170
TRANSITION_FONT_SIZE = 140
TRANSITION_SUBTITLE_FONT_SIZE_FACTOR = 0.65

MAIN_FONT_NAME = "Arial"
MAIN_FONT_EXTENSION = ".ttf"
MAIN_FONT = MAIN_FONT_NAME + MAIN_FONT_EXTENSION
BOLD_FONT = MAIN_FONT_NAME + " Bold" + MAIN_FONT_EXTENSION

PRINT_INSTRUMENTS_STARTING_X = 4000
#PRINT_INSTRUMENTS_X = [3700, 4100, 5300, 6100, 7500] #when FONT_SIZE was 140
PRINT_INSTRUMENTS_X = [3600, 3900, 4800, 5400, 6100, 6500, 7000]
PRINT_INSTRUMENTS_FONT_SIZE = 120
PRINT_INSTRUMENTS_LEGEND_FONT_SIZE = 90
PRINT_INSTRUMENTS_TAB_WIDTH = 50

VERTICAL_SPACE_BETWEEN_DOTS = 3800 / len(entries)

#########################################################################
# Function definitions
#########################################################################

def formatEntry (x, y, title, subtitle, size, alignment, bold):
	fontString=MAIN_FONT
	if bold=="bold":
		fontString = BOLD_FONT

	myFont = ImageFont.truetype (fontString, size)
	titleWidth, titleHeight = myFont.getsize(title)
	subtitleX = x

	if alignment=="right":
		x = x - titleWidth
	elif alignment=="center":
		x = x - floor(titleWidth/2)

	drawtxt.text((x,y), title, font=myFont, fill=TEXT_COLOUR)

	subtitleHeight=0
	
	if subtitle!="":
		yOffset = 15
		myFont = ImageFont.truetype (MAIN_FONT, floor(size * TRANSITION_SUBTITLE_FONT_SIZE_FACTOR))
		subtitleWidth, subtitleHeight = myFont.getsize(subtitle)
		
		if alignment=="right":
			subtitleX = x - subtitleWidth + titleWidth
		elif alignment=="center":
			subtitleX = x - floor((subtitleWidth + titleWidth)/2)
		elif alignment=="left":
			subtitleX = x

		drawtxt.text((subtitleX,y+titleHeight+yOffset), subtitle, font=myFont, fill=TEXT_COLOUR)
	return titleHeight, subtitleHeight


def addEntry (printInstruments, song, y, title, subtitle=""):
	x = XCENTER
	resetY = y
	resetTitle = title
	xoffset = 200
	bold = False
	alignment = "right"
	size = TRANSITION_FONT_SIZE

	if song:
		bold = "bold"
		alignment = "left"
		x += xoffset
		size = SONG_TITLE_FONT_SIZE
		title = title.upper()
	else:
		x -= xoffset

	(titleHeight, subtitleHeight) = formatEntry (x, y, title, subtitle, size, alignment, bold)
	x = XCENTER
	#y += (titleHeight + subtitleHeight) * 0.6
	o = 50
	yCorrection = 80
	drawobj.ellipse(xy=[(x-o,y-o+yCorrection),(x+o,y+o+yCorrection)], fill=TEXT_COLOUR, outline=None)
	dotList.append((x,y+yCorrection,song))
	y += VERTICAL_SPACE_BETWEEN_DOTS 
	
	if printInstruments and song:
		title = resetTitle

		for i in range(0,len(songInstruments[title])):#songInstruments[title]:
			myFont = ImageFont.truetype (MAIN_FONT, PRINT_INSTRUMENTS_FONT_SIZE)
			x = PRINT_INSTRUMENTS_X[i]
			y = resetY
			name = songInstruments[title][i]
			if name!="":
				if name[0]=='*':
					numberStr = name[1]
					specialInstrument = specials[name[3:]]
					instrumentName = specialInstrument[0]
					if int(numberStr)>1:
						instrumentName = instrumentName + "s"

					line1 = numberStr + ' ' + instrumentName
					L1offset = 100
					y -= L1offset

					drawtxt.text((x,y), line1, font=myFont, fill=TEXT_COLOUR)
					nLines = len(specialInstrument)-1

					x += 50
					y += L1offset + 20
					myFont = ImageFont.truetype (MAIN_FONT, PRINT_INSTRUMENTS_LEGEND_FONT_SIZE)
					for j in range (0, nLines):
						drawtxt.text((x,y), '• '+specialInstrument[j+1], font=myFont, fill=TEXT_COLOUR)
						y += 100
					#print (line1 + str(nLines))
				else:
					drawtxt.text((x,y), name, font=myFont, fill=TEXT_COLOUR)
					#instrumentWidth, instrumentHeight = myFont.getsize(i)
					#x += 1000 #instrumentWidth + PRINT_INSTRUMENTS_TAB_WIDTH


def addAllEntries(y, printInstruments):
	x = XCENTER
	y0 = y
	dashLineWidth = 6000
	ystep = VERTICAL_SPACE_BETWEEN_DOTS
	for e in entries:
		if len(e) == 3:
			addEntry (printInstruments, e[0], y, e[1], e[2])
		else:
			addEntry (printInstruments, e[0], y, e[1])
		y += ystep
	drawobj.line([dotList[0][0], dotList[0][1], dotList[-1][0], dotList[-1][1]], fill=TEXT_COLOUR, width=25)

	yInterval = averageSongDotYInterval()

	for d in dotList:
		#print (str(d[0]) + ", " + str(d[1]) + " -- " + str(d[2]))
		endX = d[0]
		span = 100
		if d[2]: #if song==True
			endX += span
		else:
			endX -= span
		drawobj.line([d[0], d[1], endX, d[1]], fill=TEXT_COLOUR, width=25)
		if d[2]:
			x = d[0] + 2000
			y = d[1] - floor(yInterval/2)
			drawDashedLine (x, y, dashLineWidth)

	drawDashedLine (x, dotList[-1][1] + floor(yInterval/2), dashLineWidth)

def averageSongDotYInterval():
	listOfYValues = []
	listOfYIntervals = []
	for e in dotList:
		if e[2]:
			listOfYValues.append(e[1])
	for i in range (0, len(listOfYValues)-1):
		listOfYIntervals.append(listOfYValues[i+1]-listOfYValues[i])
	averageYInterval = sum(listOfYIntervals) / len(listOfYIntervals)
	return averageYInterval

def drawDashedLine (x, y, w):
	median = floor(255/2)
	grey = (median, median, median, median)
	stop = x + w
	width = 30
	space = 25
	#drawobj.line([x, y, x+w, y], fill=grey, width=2)
	while (x < stop):
		drawobj.line([x, y, x+width, y], fill=grey, width=2)
		x += width + space

def generatePage(img, txt, suffix):
	yposition = 300
	yincrement = 400
	formatEntry (XCENTER, yposition, TITLE, "", 250, "center", "bold")
	yposition += yincrement*2
	addAllEntries (yposition, True)
	if suffix=="":
		suffix = BACKGROUND_COLOUR
	elif suffix=="phone":
		basewidth = 300
		wpercent = (basewidth/float(txt.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		txt = txt.resize((basewidth,hsize), Image.ANTIALIAS)
	img.paste(txt,(0,0),txt)
	img.save("Timeline - " + suffix + ".png",'PNG')
		
#########################################################################
# A4, black background
#########################################################################

BACKGROUND_COLOUR = "black"
img = Image.open (BACKGROUND_COLOUR+"-bg.png")
txt = Image.new ('RGBA', img.size, (255,255,255,0))
TEXT_COLOUR="white"
drawtxt = ImageDraw.Draw (txt)
drawobj = ImageDraw.ImageDraw (img)
dotList = []
generatePage(img, txt, "black")

#########################################################################
# Phone screen, black background
#########################################################################

BACKGROUND_COLOUR = "black"
phone = img.crop((0,0,3600,5500))
phone.save("Timeline - phone.png",'PNG')

#########################################################################
# A4, white background
#########################################################################

BACKGROUND_COLOUR = "white"
img = Image.open (BACKGROUND_COLOUR+"-bg.png")
txt = Image.new ('RGBA', img.size, (255,255,255,0))
TEXT_COLOUR="black"
drawtxt = ImageDraw.Draw (txt)
drawobj = ImageDraw.ImageDraw (img)
dotList = []
generatePage(img, txt, "white")

