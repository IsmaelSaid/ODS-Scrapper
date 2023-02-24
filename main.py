from ScrappingPackage.opendatasoftvisualisations import Opendatasoftvisualisations, Opendatasoftvisualisations_aggregated
from ScrappingPackage.opendatasoftscrapper import Opendatasoftscrapper
import pandas as pd
import argparse
from tqdm import tqdm

import ScrappingPackage.tools as t

parser = argparse.ArgumentParser()
parser.add_argument("-t","--bar_plot_themes",required=False,default=False)
parser.add_argument("-f","--bar_plot_fed_not_fed",required=False,default=False)
parser.add_argument("-mhs","--mhs_metric",required=False,default=False)
parser.add_argument('-r',"--ratio",required=False,default=False)
arguments = parser.parse_args()


bar_plot_themes = arguments.bar_plot_themes
bar_plot_fed_not_fed = arguments.bar_plot_fed_not_fed

compare_mhs_metric = arguments.mhs_metric
compare_ratio_metric = arguments.ratio

if __name__ == '__main__':
    portails_references = pd.read_csv(
                            "portails_reference_population.csv",
                            sep=",",
                            dtype= {"url":str})
    
    mhs_metrics = dict()
    ratio_metrics = dict()
    themes = dict()
    for _ , row in portails_references.iterrows():
        lien = row['lien']
        population = row['population']
        print("traitement "+lien)
        
        
        ods_scrapper = Opendatasoftscrapper(url=lien,estimated_population = population)

        # if there is no themes skip

        if(ods_scrapper.verify_themes_presence() == False):
            continue
        scrapping_results = ods_scrapper.get_all_results()
        
        fed_rate = scrapping_results.get("rate_federated_on_not_federated")
        mhs_metrics[lien] = scrapping_results["mhs_metric"]
        ratio_metrics[lien] = scrapping_results["rate_federated_on_not_federated"]
        themes[lien] = scrapping_results["themes"]

        if (bar_plot_themes):
            # bar plot thèmes 
            ods_visualisations = Opendatasoftvisualisations(results = scrapping_results)
            bar_plot_themes_filename = "scrap:themes:"+lien.replace('/','') + '.pdf'
            ods_visualisations.bar_plot_themes(save = True, title = bar_plot_themes_filename,filename=bar_plot_themes_filename)

        if (bar_plot_fed_not_fed):
            # bar plot fed/not fed
            bar_plot_fed_filename = "scrap:fed:"+lien.replace('/','') + '.pdf'
            ods_visualisations.bar_plot_fed(save = True, title = "ratio : "+str(fed_rate) + " %",filename=bar_plot_fed_filename)

        
    ods_agg_vis = Opendatasoftvisualisations_aggregated(mhs_metrics,ratio_metrics)
    if(compare_mhs_metric):
        bar_plot_mhs_metrics_filename = "metric:mhs"+'.pdf'
        bar_plot_mhs_metric_title = "Number of dataset per personn"
        ods_agg_vis.bar_plot_mhs_metrics(save= True,title=bar_plot_mhs_metric_title,filename=bar_plot_mhs_metrics_filename)
    
    if(compare_ratio_metric):
        bar_plot_ratio_metric_filename = "metric:ratio"+'.pdf'
        bar_plot_ratio_metric_title = "federated/unfederated"
        ods_agg_vis.bar_plot_ratio_metrics(save= True,title=bar_plot_ratio_metric_title,filename=bar_plot_ratio_metric_filename)