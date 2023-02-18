# Open data soft scrapper
This python package gives some basic tools to easily collect information on open data soft portals (SaaS): 
- Number of federated or non-federated data
- Themes 
- Data producers


## Installation

You'll need these librairies.
- Pandas:
```
pip install pandas
```

- Requests 
```
pip install requests
```

- Seaborn & Matplotlib 
```
pip install matplotlib
pip install seaborn
```

- tqdm (optional)
```
pip install tqdm
```


## Scrappe your own portal 
``` main.py
from ScrappingPackage.opendatasoftscrapper import Opendatasoftscrapper
url = "https://data.regionreunion.com"
ods_scrapper = Opendatasoftscrapper(lien =  lien)
results = ods_scrapper.get_all_results()
```

The method `get_all_results()` returns a dict that holds the extracted information. 

You can use ```bar_plot_fed()``` from ```Opendatasoftvisualisations``` class to make plots out of these results and save theme.


```
from ScrappingPackage.opendatasoftvisualisations import Opendatasoftvisualisations
ods_vis = Opendatasoftvisualisations(results)
ods_vis.bar_plot_fed(save = True, title = "bar plot 1" )
ods_vis.bar_plot_themes(save = True,title = "bar plot 2")
```

## Quick test
If you want to test the program immediately, you can run :
```python3 main.py```

## Output

<div>
<p align="center">
  <img src="/plot%20exemple/barplot1.png" />
</p>
<p align="center">
  <img src="/plot%20exemple/barplot2.png" />
</p>

</div>