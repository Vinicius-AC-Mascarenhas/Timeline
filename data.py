TITLE = "11/11 – EKKOS"

entries = [
	[False, "Shikisai", "Arranjo para fue + katsugi"],
	[False, "Discurso da Tikae"],
	[True,  "Rio no Kawa"],
	[False, "Águia", "Intro no fue"],
	[True,  "Emboscada"],
	[False, "Sapateado", "+ okedō"],
	[True,  "Liberdade"],
	[False, "Asuka ou Umi", "Arranjo para fue + katsugi"],
	[True,  "O Último Suspiro"]
	]

'''TITLE = "13/13 – EVENTO FICTÍCIO"
entries = [
	[False, "Shikisai", "Arranjo para fue + katsugi"],
	[False, "Discurso da Tikae"],
	[True,  "Rio no Kawa"],
	[False, "Águia", "Intro no fue"],
	[True,  "Emboscada"],
	[False, "Sapateado", "+ okedō"],
	[True,  "Liberdade"],
	[False, "Asuka", "Arranjo para fue + katsugi"],
	[True,  "O Último Suspiro"],
	[False, "Umi", "Arranjo para fue + katsugi"],
	[True,  "Kyōgaku"],
	[False, "Concerning Hobbits", "Fue"],
	[True,  "Miyuki"],
	[False, "WADAN", "Passagem deles"],
	[True,  "Matsuri"]
	]'''

songInstruments = {
	"Rio no Kawa"	   : ["fue", "1 shime", "", "2 nagadōs", "hira", "*2-KumiRio"],
	"Emboscada"	   : ["",    "2 shimes", "", "2 nagadōs", "hira"],
	"Liberdade"	   : ["fue", "*2-shimeA", "", "2 nagadōs", "hira"],
	"O Último Suspiro" : ["", "", "1 okedō", "1 nagadō", "hira", "*1-NiSusp", "*1-YonSusp"],
	"Kyōgaku"	   : ["", "", "[?] okedōs", "[?] nagadōs"],
	"Miyuki"	   : [""],
	"Matsuri"	   : [""]
}

specials = {
	"KumiRio"	   : ["kumi", "1 shime", "1 okedō"],
	"NiSusp"	   : ["nidai", "1 shime", "1 okedō"],
	"YonSusp"	   : ["yondai", "2 shimes", "1 okedō", "1 nagadō"],
	"shimeA"	   : ["shime", "base alta"]

}

#	A lista entries deve ser atualizada a cada planejamento de um novo evento,
#	sendo que o primeiro elemento de cada sublista diz se aquela sublista é um
#	número principal (música) ou de transição (passagem).
#
#	A lista songInstruments deve ser mantida entre eventos — a não ser que
#	haja uma mudança no layout de instrumentos de uma música.
#
#	1ª coluna: fue
#	2ª coluna: shime
#	3ª coluna: okedō
#	4ª coluna: nagadō
#	5ª coluna: hira ou oodaiko
#	6ª coluna: kumis diversos e outros
