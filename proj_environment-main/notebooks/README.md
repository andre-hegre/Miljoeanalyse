## Mappestruktur og fremgangamåte


Vi har valgt å bruke jupyter notebooks for dette prosjektet for å gjøre analyser, plotting og datahåndtering på ulike måter. Ved å bruke jupyter notebooks var det lettere å kunne skrive koden på en mer forståelig måte, både for oss og for leseren, siden man kan forklare hva man gjør med markdown. 

Her er en forklaring av hver mappe og funksjonalitet: 


### Dataframes: 

Her omformer vi den rå dataen fra NILU og Frost til pandas dataframes og prøver å forstå dataen, og gjøre enkle filtreringer på den for å teste dataen ut litt. Vi lagrer de nye dataframes til nye json filer i folderen "data" og bruker pandasql til å gjøre enkle query filtreringer på dataframe. 


### Feilhåndtering:

Her skal vi både tilsette flere typer feil i datasettene, samt rette opp i disse feilene ved bruk av importerte funksjoner. Vi legger til feil i værdataen, og bruker nye funksjoner til å rette dette opp igjen, og rette opp eksisterende mangler i luftkvalitetsdataen. 


### Visualisering+prediktiv analyse:

Her bruker vi matplotlib og seaborn til å visualisere dataen på forskjellige vis med forskjellige grafer. Vi bruker begge datasettene og plotter de mot hverandre for å kunne se visuell sammenhengen mellom de. Deretter trener vi opp en regresjonsmodell for å predikere målinger basert på test data og evaluere hvor nøyaktig prediksjonen blir


### Dataanalyse


Her analyserer vi dataen og finner statistiske mål som gjennomsnitt, standardavvik og korrelasjon mellom datasettene. 

