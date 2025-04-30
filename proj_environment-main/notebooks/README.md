## Mappestruktur og fremgangamåte


Vi har valgt å bruke jupyter notebooks for dette prosjektet for å gjøre analyser, plotting og datahåndtering på ulike måter. Ved å bruke jupyter notebooks var det lettere å kunne skrive koden på en mer forståelig måte, både for oss og for leseren, siden man kan forklare hva man gjør med markdown. 

Her er en forklaring av hver mappe og funksjonalitet: 


### Dataframes: 

Her omformer vi den rå dataen fra NILU og Frost til pandas dataframes og prøver å forstå dataen, og gjøre enkle filtreringer på den for å teste dataen ut litt. Vi lagrer de nye dataframes til nye json filer i folderen "data" og bruker pandasql til å gjøre enkle query filtreringer på dataframe. 


### Error

Her tilfører vi feil og uregelmessigheter i dataen, slik at vi kan etterpå fikse på det igjen. Vi bruker funksjoner til å introdusere feil, uteliggere og manglende verdier til datasett. Vi lagrer nye filer med feilene til folderen "data"


### Funksjoner_data

Her fikser vi dataen vi endret på i "Error", og bruker metoder som "interpolate" til å fylle inn manglende verdier. Vi legger til de fikset filene under folderen "data".


### Visualisering

Her bruker vi matplotlib og seaborn til å visualisere dataen på forskjellige vis med forskjellige grafer. Vi bruker begge datasettene og plotter de mot hverandre for å kunne se visuelt sammenhengen mellom de. 


### Dataanalyse


Her analyserer vi dataen og finner statistiske mål som gjennomsnitt, standardavvik og korrelasjon mellom datasettene. 




Vurderingskriterier:

Hvilke spesifikke typer visualiseringer planlegger du å lage for å representere eksempelvis endringer i luftkvalitet og temperaturdata, og hvorfor valgte du disse?
Hvordan kan Matplotlib og Seaborn brukes til å forbedre forståelsen av de analyserte dataene, og hvilke funksjoner i disse bibliotekene vil være mest nyttige?
Hvordan vil du håndtere og visualisere manglende data i grafene dine for å sikre at de fortsatt er informative?
Kan du beskrive prosessen for å lage interaktive visualiseringer med Widgets, Plotly eller Bokeh, og hvilke fordeler dette kan gi i forhold til statiske visualiseringer?
Hvordan vil du evaluere effektiviteten av visualiseringene dine i å formidle de viktigste funnene fra dataanalysen til et bredere publikum?
