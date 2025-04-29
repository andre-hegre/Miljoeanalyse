## Datakilder og forklaring

Vi har hentet data fra 2 forskjellige kilder, nemlig Meterologiske Instituttets "Frost" API tjeneste og gjennom nilu.no. Fra disse to kildene har vi henholdsvis hentet værdata og luftkvalitetdata. 

Frost er et tilbud fra Meterologisk Institutt som gir gratis tilgang til data fra mange forskjellige mulige værstasjoner og historisk data fra disse stasjonene. Vi hentet følgende værdata fra Frost: 

- Gjennomsnittlig vindstyrke per dag (mean(wind_speed P1D))
- Gjennomsnittlig luftfuktighet per dag (mean(relative_humidity P1D))
- Total mengde nedbør per dag (sum(precipitation_amount P1D))
- Gjennomsnittlig temperatur per dag (mean(air_temperature P1D))
- Vindretning hvert 10. minutt

kilde: https://frost.met.no/api.html


Meterologisk Institutt er en pålitelig kilde for norsk værdata, og har stasjoner over hele landet. Vi valgte å hente vår data fra en spesifikk værstasjon i Oslo, for å så videre sammenligne det med annen data. Dette var en god kilde, siden det var relativt lett å velge målestasjon, værdata og hvilken tidsperiode dataen var i. Siden alle målingene ble gjort på samme stasjon, kan vi også være mer sikre på at det ikke blir feil pga omgivelsene, som det kunne vært om data hadde blitt samlet fra forskjellige steder. 


Den andre kilden vi valgte var data fra NILU. NILU er et norsk klima og miljøforskningsinstitutt som har data på blant annet luftkvalitet. De er anerkjent som en pålitelig kilde, og samarbeider med europeiske institutt om miljørelatert forskning (https://nilu.no/prosjekter/). 

Vi hentet følgende data fra NILIU: 

- Daglig gjennomsnittlig NO2 konsentrasjon
- Daglig gjennomsnittlig PM10 (Partikler med <10 mikrometer diameter) konsentrasjon
- Daglig gjennomsnittlig NO konsentrasjon
- Daglig gjennomsnittlig NOx konsentrasjon (summen av NO og NO2)
- Daglig gjennomsnittlig PM2.5 (Partikler med <2.5 mikrometer diameter) konsentrasjon
- Daglig gjennomsnittlig CO konsentrasjon

kilde: https://api.nilu.no


### Datasamling og prosjekt

Dette prosjektet handler om å sammenligne værdata med data om luftkvalitet. Vi ville med andre ord analysere hvordan diverse værfenomen og målinger, som spesielt temperatur, vind, regn og luftfuktighet påvirker konsentrasjon av diverse partikler i luften. Vi valgte å analysere data for Norges største by, Oslo. Dette kan gi et innblikk i hvordan vær påvirker luftforurensing og andre luftpartikler i en by, og kan være viktig for å studere videre ting som klimaendringer, sammenligning med målinger ut på landet og planlegging av bygging av for eksempel fabrikker dersom vind ville hatt mye å si for forurensing til en by der vinden blåser mot. 

Vi valgte å hente data for 5 år, og rundt vår-sommermånedene (April-Juli). Vi valgte å unngå årstider med mye snøvær, siden det kunne påvirke datasettet og tilføre mye usikkerhet som vi ikke var i stand til å håndtere. Hvis for eksempel regn sterkt påvirker mengden partikler, vil snø kanskje ha en helt annen effekt, men som ikke er lett å skille fra ren "nedbør" data. Det ville vært mulig å hente data for flere år, men vi valgte en periode på 5 år, som vi mener er tilstrekkelig for å utføre analyser. 

Regn, vind, luftfuktighet og temperatur har effekter på konsentrasjoner av luftpartikler (UCAR,[Hentet 2021](https://scied.ucar.edu/learning-zone/air-quality/how-weather-affects-air-quality)). Vi valgte derfor data for nedbør, vind, temperatur og luftfuktighet fra Frost, og samtidig data for forskjellige partikkelkonsentrasjoner. 

Fra begge kildene var det mulig å få gjennomsnitt i løpet av én dag istedet for å manuelt ta det time for time. Dette gjorde det lettere å jobbe med, og lettere å sammenligne de to datasettene. 

Vi brukte requests modulen til å hente data, og lagret de som JSON filer i folderen "data".