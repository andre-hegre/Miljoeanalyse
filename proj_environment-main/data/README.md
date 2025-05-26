## Her forklarer vi de forskjellige datafilene: 


### Frost_Observations.json

Dette er den uendrede dataen vi hentet fra Meterologisk Institutt API. Her finner man all innsamlet data ufiltrert


### df2_data.json

Her er filtrert og litt mer organisert data fra "Frost_Observations.json" filen omgjort til en dataframe. 


### df2_errors.json

Dette er filen der feilverdier er introdusert via funksjonene i notebooken "Hegre_branch"


### df2_fikset.json

Dette er filen der vi fikser opp feilverdiene som vi introduserte i df2_errors

### luftkvalitet_Kirkeveien_all_years.json

Dette er filen som inneholder innsamlet luftkvalitetsdata, uten endringer. 


### df1_data.json: 

Dette er en dataframe som inneholder luftkvalitetsdata på en ryddig måte. Denne fikk vi ved å utføre en pivot i dataframe fra filen "luftkvalitet_Kirkeveien_all_years.json" og filtrere den


### df1_fikset.json

Dette er samme dataframe som df1, men der vi har brukt teknikker for å kvitte oss med nullverdiene. 

