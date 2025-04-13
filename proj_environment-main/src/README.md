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


Den andre kilden vi valgte var data fra NILU

Vi hentet følgende data fra NILIU: 

- Daglig gjennomsnittlig 