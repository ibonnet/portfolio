# Data Journalist at POLITICO
This folder contains the files for the <b>"Web Producer: Data Visualization"</b> and <b>"Data Journalist"</b> positions at <a href="https://www.politico.eu/"><i>POLITICO Europe</i></a>.

Based on the website's chart, I will be using the following color palette and fonts when available:
<li><b>Color palette:</b> <i>#E198A6</i> for the most important information and <i>#CDC1C3</i> for the secondary information</li>

<br>
  <img src="https://github.com/ibonnet/portfolio/blob/main/politico/colorpalette.png?raw=true" height="170">

<li><b>Font:</b> <i>'proxima-nova', sans-serif;</i> <i>font-family: 'Roboto',Arial,sans-serif</i></li>

## Exercise 1
This exercise uses data from a new <a href="https://transparency.eu/mep-lobby-brief/">Transparency International EU</a> analysis with MEP declarations since the beginning of this mandate, which is available <a href="https://github.com/ibonnet/portfolio/tree/main/politico/ex1">here</a>.</li>
<p>I first researched previous work from POLITICO about the Qatargate to follow the chart style and find inspiration. For this exercise, I used <a href="https://www.politico.eu/article/meps-rush-declare-junkets-qatargate-analysis-transparency-international-corruption/">Wilhelmine Preussen's article and Arnau Busquets Guàrdia's charts</a> <b>"MEPs rush to declare junkets amid Qatargate, analysis shows"</b> published on Feb. 15, 2023 as guidance.

### Late declarations per political group
I used a <b>stacked bar chart</b> to show the percentage of late declarations per political group. The three groups with the highest percentage of late submissions are left political-parties, with the Progressive Alliance of Socialists and Democrats submitting 60% of the submissions late to the MEP.

  <li><b>Dataset:</b> I created <a href="https://github.com/ibonnet/portfolio/blob/main/politico/ex1/LateDeclarationsCOUNT.csv">a new excel sheet where I grouped the MEP political parties.</a></li>
  <li><b>Used tool:</b> I used Excel for the dataset, then exported the document as a .csv file. I used the <a href="https://d3-graph-gallery.com/"><b>d3.js Graph Gallery</b></a> to build the bar chart.</li>
  <li><b>Interactivity:</b> The bar chart can be accessed <a href="https://ibonnet.github.io/portfolio/tree/main/politico/ex1">here</a>.</li>
  <li><b>Documentation:</b> All files used for this exercise are available <a href="https://github.com/ibonnet/portfolio/edit/main/politico/">here</a>.</li>
  
<br>
  <img src="https://github.com/ibonnet/portfolio/blob/main/politico/ex1/LateDeclarationsScreenshot.png?raw=true" height="350">

<i>Note: I added a quick tooltip for interactivity. If given more time, I would make it more aesthetically pleasing and fixed the percentage to only a two decimals.</i>

### Number of declarations submitted in different time periods
I extracted all unique values from the dataset, creating <a href="https://github.com/ibonnet/portfolio/blob/ef349863108375e77fcded302d6f60c82a3b2a0d/politico/ex1/SubmissionDate.json">a new array</a> with the number of declarations submitted each day since 2019.
  
  With <a href="https://app.datawrapper.de/"><b>Datawrapper</b></a>, I created this <b>bar chart</b> which you can visualize <a href="https://datawrapper.dwcdn.net/smsND/1/">here</a>.
  
  <br>
  <img src="https://github.com/ibonnet/portfolio/blob/main/politico/ex1/NumberofDeclarationsSubmitted.gif" height="200">

### Late declarations per MEP
  With <a href="https://app.datawrapper.de/"><b>Datawrapper</b></a>, I created this <b>Range Plot</b> to see the declaration period for each MEP, which shows significant delays for specific members who submitted their declarations almost four years after their trips.

<br>
  <img src="https://github.com/ibonnet/portfolio/blob/main/politico/ex1/LateDeclarationsPerMEP.gif?raw=true" height="350">

## Exercise 2
For this exercise, I used <a href="https://www.politico.eu/article/ombudsman-criticizes-eu-commission-on-revolving-doors/">Lily Bayer's article</a> <b>"Ombudsman criticizes European Commission on ‘revolving doors’"</b> published on May 18, 2022 for inspiration.
<p>Two pie charts could effectively visualize the top three concerns and the breakdown of inquiries handled by the Ombudsman's office in 2021.

### Top concerns about the EU institutions
This pie chart shows the percentage breakdown of the top three concerns in the inquiries closed by the Ombudsman in 2021:
<li><b>Transparency and accountability</b> (29%)</li>
<li><b>Culture of service</b> (26%)</li>
<li><b>Proper use of discretionary powers (18%)</b></li>
<br>A pie chart is a suitable choice to show the proportions of different categories and work well as images that don't have interactivity due to the fact that they are straightforward and accessible to the audience.


<br>
  <img src="https://github.com/ibonnet/portfolio/blob/1933e93589cd7435970674df292649dd64976e87/politico/ex2/TopConcerns.png" height="400">


### Breakdown of inquiries handled by the Ombudsman's office in 2021
This pie chart shows the breakdown of inquiries handled by the Ombudsman's office in 2021:
<li><b>Advice through the Interactive Guide on the Ombudsman's website</b> (83%)</li>
<li><b>Remaining requests for information</b> (6%)</li>
<li><b>Handled as complaints</b> (11%)</li>
<br>This chart can also be easily visualized using a pie chart and photographed for the newsletter.



<br>
  <img src="" height="400">
  
## Exercise 3
For this exercise, I used <a href="https://www.politico.eu/article/critical-raw-materials-act-europe-guide/">Antonia Zimmermann and Sarah Anne Aarup's article</a> <b>"The critical raw materials you need to know"</b> published on March 9, 2023 for inspiration.

<p>The editor's request is very general, which gives room for creativity and different types of charts and visualizations. This is why I would first look at the data available and suggest multiple ideas to discuss with the editor. For instance:

<li>Top critical raw materials by production or import/export</li>
<li>Trends in critical raw materials production or use</li>
<li>Comparison of the EU's critical raw materials strategy to those of other countries/regions</li>
<li>Impact of the critical raw materials strategy on EU industries or economies</li>

<p>After I have clarified the specific insights to highlight with the editor, I can then choose a suitable chart type and tool for the task. For example, if the focus is on production and import/export of critical raw materials, a stacked bar chart or a line chart could be used to show the trends over time. If the focus is on comparing the EU's strategy to those of other countries, a radar chart or a bubble chart could be used to visualize the similarities and differences.

<p>I personally like to work on <b>d3.js</b> and <b>Illustrator</b>, which is why I would prioritize those tools to create the charts. If there are any issues or questions during the process, I would communicate them with the editor to ensure that the final chart meets their expectations.

## Coding exercises

### Exercise A
### Exercise B
### Exercise C
### Bonus
