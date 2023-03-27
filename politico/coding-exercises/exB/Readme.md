# Coding exercise B: Russia trade

This repository contains the coding exercise to visualize EU imports of select products, by share of imports from each country, including other EU countries.


## Data Source
The data used in this map was obtained from <a href="https://ec.europa.eu/eurostat/databrowser/view/DS-057380/default/table?lang=en&category=ext_go.ext_go_detail">Eurostat</a> which can be downloaded <a href="https://www.politico.eu/wp-content/uploads/2023/03/07/Russia-trade-exercise-data.zip">here</a>.

## Data Preparation
<li>Ensure that all country names are in their corresponding ISO-2 country codes.</li>
<li>Identify the top 9 trade partners for each country, based on the highest imports in the period covered by the dataset.</li>
<li>Calculate the share of imports from top 9 trade partners, Russia, and all other countries.</li>
<li>If a country imports the product from fewer than 9 partners, do not include the “Others” column.</li>

## Code
