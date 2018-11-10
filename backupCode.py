songInstrumentsBackup = {
	"Rio no Kawa"	   : ["fue", "1 shime", "", "2 nagadōs", "hira", "2 kumis"],
	"Emboscada"	   : ["",    "2 shimes", "", "2 nagadōs", "hira", ""],
	"Liberdade"	   : ["fue", "2 shimes altos", "", "2 nagadōs", "hira", ""],
	"O Último Suspiro" : ["", "", "1 okedō", "1 nagadō", "hira", "1 nidai + 1 yondai"]
}



def addEntryBackup (printInstruments, song, y, title, subtitle=""):
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
		myFont = ImageFont.truetype (MAIN_FONT, PRINT_INSTRUMENTS_FONT_SIZE)
		y = resetY
		title = resetTitle

		for i in range(0,6):#songInstruments[title]:
			x = PRINT_INSTRUMENTS_X[i]
			name = songInstruments[title][i]
			drawtxt.text((x,y), name, font=myFont, fill=TEXT_COLOUR)
			#instrumentWidth, instrumentHeight = myFont.getsize(i)
			#x += 1000 #instrumentWidth + PRINT_INSTRUMENTS_TAB_WIDTH

