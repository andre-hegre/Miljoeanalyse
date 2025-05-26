# Refleksjonsnotat

## Hva vi har lært
Gjennom prosjektet har vi lært mye om hele arbeidsflyten for analyse av miljødata – fra innsamling til prediktiv modellering. Vi startet med å sette opp et fungerende utviklingsmiljø med Python, VS Code, GitHub og Jupyter Notebook. Dette la grunnlaget for videre arbeid og ga oss en god struktur for samarbeid. Vi fikk innblikk i hvordan man henter inn data fra åpne kilder som Frost API, hvordan man renser og forbereder dataene for analyse, og hvordan man kan trekke ut innsikt fra dem. 

Vi lærte mye i praksis om versjonskontroll og å koordinere oppgaver mellom oss, slik at vi ikke gjorde endringer som skapte konflikt. 

## Nye ferdigheter
Vi har tilegnet oss flere nye ferdigheter, spesielt knyttet til databehandling i Python. Biblioteker som Pandas, NumPy og Matplotlib ble brukt til å analysere og visualisere data. Vi lærte oss å bruke list comprehensions, datarensing med Pandas, og hvordan vi kan bruke SQL-lignende spørringer i Pandas (via `sqldf`). I tillegg fikk vi trent på versjonskontroll i GitHub, og å jobbe med Jupyter Notebooks for dokumentasjon og kode. Å få til en regresjonsmodell var også noe nytt som vi får bruk til i fremtiden. 

## Utfordringer
En av de største utfordringene var datakvalitet og struktur i JSON-filene vi hentet fra API-et. Ofte måtte vi navigere komplekse datastrukturer for å hente ut observasjoner. Vi opplevde også utfordringer med manglende verdier, og brukte funksjoner som `fillna()` og `groupby().transform()` for å rydde i dataene. En annen utfordring var at ikke alle i gruppen fikk tilgang til samme datafiler samtidig, noe som forsinket analysen for enkelte.

## Samarbeid i gruppen
Samarbeidet i gruppen fungerte stort sett bra. Vi fordelte oppgaver etter interesse og styrker: noen jobbet mer med API og datainnhenting, andre med visualisering og analyse. Vi brukte GitHub for å dele kode og ha kontroll på versjoner. En forbedring kunne vært å ha en tydeligere kommunikasjonskanal for å sikre at alle hadde tilgang til samme filer til enhver tid.

## Vurdering av resultatene
Vi er ganske fornøyde generelt sett med resultatene. Vi fikk nyttig informasjon ved å analysere dataen, og visualiseringene viste sammenhengen mellom de to datasettene vi hentet fra. Regresjonsmodellen vår ble ikke veldig nøyaktig, men alikevel ble svingningene i både prediksjonen og målt data ganske sammenlignbare, bare at den virkelige dataen hadde større variasjon. 

## Forbedringsforslag
Neste gang kunne vi ha brukt mer tid på å sette opp felles datamodeller og testfunksjoner for å sikre konsistens. Vi kunne spesielt tatt i betraktning vindretning, for å undersøke om vi kunne se en forskjellig effekt vinden hadde avhengig av retningen. Dette valgte vi å se bort ifra, men ville vært noe å analysere for neste gang. 

## Videre utvikling
En naturlig videreføring av prosjektet kunne være å bruke mer avanserte modeller for prediksjon, som random forest eller nevrale nettverk. Vi kunne også ha koblet data fra flere kilder sammen, som luftkvalitet og trafikk, for å utforske bredere miljøpåvirkninger.

## Viktigste læringspunkter
Vi har lært hvordan man går fra rådata til innsikt. Vi har jobbet med ekte data, reelle problemer og fått se hvordan datavitenskap kan brukes til å skape forståelse for miljømessige forhold. Det tekniske og praktiske har gått hånd i hånd.

## Personlige refleksjoner
Prosjektet har vært motiverende fordi det kombinerer programmering med noe samfunnsnyttig. Erfaringene vi har gjort oss her vil være nyttige videre i studiet og arbeidslivet, spesielt innen dataanalyse, prosjektarbeid og samarbeid i team.


