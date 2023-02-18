import seaborn as sns
import matplotlib.pyplot as plt


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
    