from ScrappingPackage.opendatasoftvisualisations import Opendatasoftvisualisations
from ScrappingPackage.opendatasoftscrapper import Opendatasoftscrapper
import pandas as pd
from tqdm import tqdm

if __name__ == '__main__':
    portails_references = pd.read_csv(
                            "mini_portails.csv",
                            sep=",",
                            dtype= {"url":str})
    
    for lien in tqdm(portails_references.loc[:,'lien']):
        ods_scrapper = Opendatasoftscrapper(url=lien)

        scrapping_results = ods_scrapper.get_all_results()

        fed_rate = scrapping_results.get("rate_federated_on_not_federated")

        # bar plot thèmes 
        ods_visualisations = Opendatasoftvisualisations(results = scrapping_results)
        bar_plot_themes_filename = "scrap:themes:"+lien.replace('/','') + '.pdf'
        ods_visualisations.bar_plot_themes(save = True, title = bar_plot_themes_filename,filename=bar_plot_themes_filename)


        # bar plot fed/not fed
        bar_plot_fed_filename = "scrap:fed:"+lien.replace('/','') + '.pdf'
        ods_visualisations.bar_plot_fed(save = True, title = "ratio : "+str(fed_rate) + " %",filename=bar_plot_fed_filename)