# Coding bonus: French Presidential Election Map
This repository contains the code and data used to create a map illustrating the results of the second round of the French presidential election in 2017 and 2022 by municipality.

## Data Sources
The data used in this map was obtained from the following sources:

<li>Election results data: <a href="https://www.interieur.gouv.fr/Elections/Les-resultats/Presidentielles/elecresult__presidentielle-2017/(path)/presidentielle-2017/FE.html">French Ministry of the Interior</a></li>
<li>Municipality shapefile: <a href="https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#communes">French National Geographic Institute (IGN)</a></li>

## Files
The repository contains the following files:

<li><a href="election_results_2017.csv">election_results_2017.csv</a>: CSV file containing the election results data for the second round of the 2017 presidential election by municipality.</li>
<li><a href="election_results_2022.csv">election_results_2022.csv</a>: CSV file containing the election results data for the second round of the 2022 presidential election by municipality.</li>
<li><a href="municipalities_shapefile.shp">municipalities_shapefile.shp</a>: Shapefile containing the municipalities of France.</li>
<li><a href="create_map.py">create_map.py</a>: Python script that imports the election results data and the municipality shapefile, joins them based on the municipality code (code INSEE), and creates a map illustrating the results of the two elections.</li>
<li><a href="map.png">map.png</a>: PNG file of the final map.</li>

## License
The code in this repository is licensed under the MIT License. You may use this code for any purpose.

Please note that the data obtained from the French Ministry of the Interior and the IGN may be subject to various legal and ethical considerations, including copyright and data privacy laws. It is your responsibility to ensure that you have the appropriate permissions to use and distribute the data. The authors of this repository disclaim any liability for the use or misuse of the data obtained through this repository.
