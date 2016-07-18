from django.shortcuts import render
from django.http import HttpResponse

import numpy as np

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def bond(request,country="usa"):
	url="/image/bond_image/"+country+"/";
	print(url);
	return render(request, 'bond.html',{"urllink":url,"country":country.upper()});

def bond_image(request,country="usa"):
	import matplotlib.pyplot as plt
	plt.clf()
	from matplotlib.figure import Figure
	from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
	R2 = [('NLD', 0.89512616543538415), ('FRA', 0.86908405834376823), ('GBR', 0.86148700879268159), ('SWE', 0.86014814159835962), ('NOR', 0.85325866712475462), ('CHE', 0.84867905529912435), ('NZL', 0.82512650761648132), ('HKG', 0.73925452057686147), ('DEU', 0.6561290809129936), ('ITA', 0.65427492521633712), ('CAN', 0.63692864888176803), ('ESP', 0.6103589538493841), ('SGP', 0.58780824939573473), ('CHN', 0.51126614103436951), ('AUS', 0.50883761773673863), ('JPN', 0.4830427548868208), ('FIN', 0.47443446347495732), ('IND', 0.29225782761326713), ('GRC', 0.23275904793933522), ('THA', 0.17950619330139495), ('VNM', 0.17267825570136253), ('ZAF', 0.05551661953676057), ('ROU', 0.055303834109941108), ('IDN', 0.037015685749187677), ('MYS', 0.012566355143403651), ('PAK', 0.0066124223186581066), ('BEL', 0.0036450660960642978), ('PHL', 0.0033327688004854972), ('KOR', 0.0028494947039173768)]
	R2_CHN = [('SWE', 0.69034156897956422), ('GBR', 0.66437073502844668), ('ITA', 0.58167264894637727), ('VNM', 0.57489260109131624), ('IND', 0.547991605265576), ('JPN', 0.52176182613394362), ('SGP', 0.51470883462956474), ('USA', 0.51126614103436918), ('HKG', 0.4693675273724115), ('NOR', 0.42755539011670807), ('FIN', 0.32026774025983595), ('AUS', 0.20177766656269203), ('ESP', 0.11134057279529019), ('ZAF', 0.10896365742886405), ('THA', 0.10046719488856759), ('DEU', 0.059318391863647735), ('FRA', 0.05517279138730824), ('CHE', 0.049782043953704558), ('GRC', 0.032172120610898913), ('CAN', 0.028998025011100492), ('PAK', 0.028296023160579331), ('MYS', 0.026604882753869408), ('KOR', 0.018674712473603416), ('IDN', 0.01627033025868907), ('ROU', 0.0045868981894561234), ('NLD', 0.0030345938058611299), ('NZL', 0.0027912180911046081), ('PHL', 0.00085628920677072173), ('BEL', 0.00037619693022639122)]
	if country =="chn":
		R2=R2_CHN
	print(country)
	R2_value = [i[1] for i in R2]
	R2_lable = [i[0] for i in R2]

	n = len(R2)

	plt.subplot()

	index = np.arange(n)
	bar_width = 0.5

	rec = plt.bar(index,R2_value)
	plt.xticks(index + bar_width, R2_lable,rotation = 'vertical')
	plt.plot()
	canvas=FigureCanvas(plt.figure(1))
	response=HttpResponse(content_type="image/png")
	canvas.print_png(response);
	return response
	#return render(request, 'bond.html',{'rlist':R2list});

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

