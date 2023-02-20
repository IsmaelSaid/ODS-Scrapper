import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Opendatasoftvisualisations:
    """
    this class holds a set of methods for visualisations of . 
    """
    def __init__(self,results : dict):
        self.results = results


    def bar_plot_themes(self, save : bool = False, title : str = "bar_plot_themes.pdf",filename : str = "barplot_themes.pdf"):

        # let's make a simple bar plot.

        themes = self.results.get("nb_dataset_per_theme_df")
        type_dataset = self.results.get("nb_federated_and_not_federated_df")
        rate = self.results.get("rate_federated_on_not_federated")
        
        # feel and look
        sns.set_style("whitegrid")

        # create the plot
        fig, ax = plt.subplots()
        ax = sns.barplot(data=themes,x="name",y="count",palette=sns.color_palette('crest',1))


        ax.set_title(title)
        
        # rotate labels because they are to long
        plt.xticks(
            rotation = 60,
            horizontalalignment = "right"
        )

        # save the plot somewhere
        if(save):
            fig.savefig(filename,format ="pdf",bbox_inches = "tight")

    def bar_plot_fed(self, save : bool = False,title:str = "bar_plot_fed.pdf", filename : str = "barplot_fedreated.pdf"):

        #  retrieval of results
        themes = self.results.get("nb_dataset_per_theme_df")
        type_dataset = self.results.get("nb_federated_and_not_federated_df")
        rate = self.results.get("rate_federated_on_not_federated")
        
        # feel and look
        sns.set_style("whitegrid")

        fig, ax = plt.subplots()
        ax = sns.barplot(data=type_dataset,x="type_dataset",ax = ax,y="nb_dataset",palette=sns.color_palette('crest',1))
        
        plt.title(title)
        
        
        # save the plot somewhere
        if(save):
            plt.savefig(filename,format = "pdf",bbox_inches = "tight")
    
class Opendatasoftvisualisations_aggregated:
    def __init__(self, mhs_metrics : dict, ratio_metrics : dict):
        self.mhs_metrics = mhs_metrics
        self.ratio_metrics = ratio_metrics


    def bar_plot_mhs_metrics(self, save : bool = False,title:str = "bar_plot_mhs_metric",filename = "bar_plot_mhs_metrics.pdf"):
         #  retrieval of results

        mhs_metrics_df = pd.DataFrame({
            "portails" : list(self.mhs_metrics.keys()),
            "nb_dataset/personn" : list(self.mhs_metrics.values())
        })
        
        # feel and look
        sns.set_style("whitegrid")

        fig, ax = plt.subplots()
        ax = sns.barplot(data=mhs_metrics_df,y="portails",ax = ax,x="nb_dataset/personn",palette=sns.color_palette('crest',1))
        
        plt.title(title)
        plt.xticks(
            rotation = 90
        )

        # save the plot somewhere
        if(save):
            plt.savefig(filename,format = "pdf",bbox_inches = "tight")

    def bar_plot_ratio_metrics(self, save : bool = False,title:str = "bar_plot_ratio_metric",filename = "bar_plot_ratio_metrics.pdf"):
            #  retrieval of results

        mhs_metrics_df = pd.DataFrame({
            "portails" : list(self.ratio_metrics.keys()),
            "fed/unfed" : list(self.ratio_metrics.values())
        })
        
        # feel and look
        sns.set_style("whitegrid")

        fig, ax = plt.subplots()
        ax = sns.barplot(data=mhs_metrics_df,y="portails",ax = ax,x="fed/unfed",palette=sns.color_palette('crest',1))
        
        plt.title(title)
        plt.xticks(
            rotation = 90
        )
        # save the plot somewhere
        if(save):
            plt.savefig(filename,format = "pdf",bbox_inches = "tight")