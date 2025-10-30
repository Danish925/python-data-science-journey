# Python Data Science Journey - Notebooks

Hey there! This folder has all the Jupyter Notebooks for my `python-data-science-journey` project. I've sorted everything into folders based on the library or topic, so it should be easy to find what you're looking for.

## What's Inside?

1.  [**Pandas**](./pandas/)
2.  [**Matplotlib and Seaborn**](./matplotlib_and_seaborn/)
3.  [**Matplotlib and Seaborn Analysis (Saved Plots)**](./matplotlib_and_seaborn_analysis/)

---

## 1. Pandas

Here you'll find a bunch of notebooks that walk through how to use Pandas for data analysis. We start with the basics and then get into more advanced stuff like cleaning data and building pipelines. Most of it uses the Titanic dataset, which is a classic!

* [**01_pandas_basics.ipynb**](./pandas/01_pandas_basics.ipynb): Just getting started with Pandas? This is the place! It covers Series and DataFrames.
* [**02_titanic_loading_and_inspection.ipynb**](./pandas/02_titanic_loading_and_inspection.ipynb): Shows how to load the Titanic dataset and take a first look around with `.head()`, `.info()`, and `.describe()`.
* [**03_column_selection_and_filtering.ipynb**](./pandas/03_column_selection_and_filtering.ipynb): All about how to pick out the data you want using `.loc`, `.iloc`, and boolean filtering.
* [**04_missing_data_and_simple_filling.ipynb**](./pandas/04_missing_data_and_simple_filling.ipynb): Got missing data? This notebook covers how to find it (`.isnull()`) and fill it in with simple values (like the mean or median).
* [**05_groupby_deep_dive.ipynb**](./pandas/05_groupby_deep_dive.ipynb): A closer look at the super-useful `groupby` function for summarizing your data.
* [**06_pure_pandas_advanced_missing_data.ipynb**](./pandas/06_pure_pandas_advanced_missing_data.ipynb): More advanced ways to handle missing data using just Pandas.
* [**07_pure_pandas_datatype_optimization.ipynb**](./pandas/07_pure_pandas_datatype_optimization.ipynb): A neat trick to make your DataFrames use less memory by changing data types (like `object` to `category`).
* [**08_pure_pandas_string_processing.ipynb**](./pandas/08_pure_pandas_string_processing.ipynb): Tips for working with text data using the `.str` accessor.
* [**09_pure_pandas_outlier_detection.ipynb**](./pandas/09_pure_pandas_outlier_detection.ipynb): How to find and deal with those weird data points called outliers.
* [**10_complete_pandas_pipeline.ipynb**](./pandas/10_complete_pandas_pipeline.ipynb): Puts it all together! Shows how to build a full data-cleaning pipeline from start to finish.

---

## 2. Matplotlib and Seaborn

This section is all about making cool charts and graphs in Python. We'll start with the basics in Matplotlib and then explore all the awesome statistical plots you can make with Seaborn.

* [**01_matplotlib_intro_and_line_plots.ipynb**](./matplotlib_and_seaborn/01_matplotlib_intro_and_line_plots.ipynb): A quick intro to Matplotlib and how to make your first line plots.
* [**02_matplotlib_univariate_histograms.ipynb**](./matplotlib_and_seaborn/02_matplotlib_univariate_histograms.ipynb): How to visualize the spread of a single variable using histograms.
* [**03_matplotlib_subplots_dashboard_basics.ipynb**](./matplotlib_and_seaborn/03_matplotlib_subplots_dashboard_basics.ipynb): Learn how to put multiple plots together in one figure, like a mini-dashboard.
* [**04_pandas_matplotlib_integration.ipynb**](./matplotlib_and_seaborn/04_pandas_matplotlib_integration.ipynb): Shows how to use the plotting functions built right into Pandas (which use Matplotlib behind the scenes).
* [**05_matplotlib_professional_styling.ipynb**](./matplotlib_and_seaborn/05_matplotlib_professional_styling.ipynb): Tips for making your plots look really sharp and professional.
* [**06_Seaborn_Introduction_and_Distribution_Plots.ipynb**](./matplotlib_and_seaborn/06_Seaborn_Introduction_and_Distribution_Plots.ipynb): An introduction to Seaborn, focusing on plots that show how your data is distributed.
* [**07_Seaborn_Univariate_Histograms_and_KDE.ipynb**](./matplotlib_and_seaborn/07_Seaborn_Univariate_Histograms_and_KDE.ipynb): More ways to plot a single variable, using histograms and Kernel Density Estimation (KDE) plots.
* [**08_Seaborn_Layouts_and_Figure_Styling.ipynb**](./matplotlib_and_seaborn/08_Seaborn_Layouts_and_Figure_Styling.ipynb): How to customize the look and feel of your Seaborn plots.
* [**09_Seaborn_and_Pandas_Integration.ipynb**](./matplotlib_and_seaborn/09_Seaborn_and_Pandas_Integration.ipynb): Shows how well Seaborn and Pandas work together. It's super smooth!
* [**10_Professional_Styling_and_Figure_Customization.ipynb**](./matplotlib_and_seaborn/10_Professional_Styling_and_Figure_Customization.ipynb): Even more advanced styling tricks for your Seaborn charts.
* [**11_Seaborn_Box_Plots\_&\_Violin_Plots.ipynb**](./matplotlib_and_seaborn/11_Seaborn_Box_Plots_&_Violin_Plots.ipynb): Using box plots and violin plots to see your data's distribution and find outliers.
* [**12_FacetGrid\_&\_Multi-Dimensional_Plots.ipynb**](./matplotlib_and_seaborn/12_FacetGrid_&_Multi-Dimensional_Plots.ipynb): A powerful tool called `FacetGrid` that lets you create a grid of plots based on different categories in your data.
* [**13_Seaborn_Correlation_Heatmaps.ipynb**](./matplotlib_and_seaborn/13_Seaborn_Correlation_Heatmaps.ipynb): How to use heatmaps to see which variables are correlated with each other.
* [**14_Seaborn_Heatmap_Customization.ipynb**](./matplotlib_and_seaborn/14_Seaborn_Heatmap_Customization.ipynb): Making your heatmaps look just right with custom colors and labels.
* [**15_Seaborn_pairplot_for_Multi-Dimensional_Analysis.ipynb**](./matplotlib_and_seaborn/15_Seaborn_pairplot_for_Multi-Dimensional_Analysis.ipynb): A fantastic plot (`pairplot`) that shows the relationships between every pair of features in your dataset.
* [**16_Seaborn_Regression_Plots_lmplot.ipynb**](./matplotlib_and_seaborn/16_Seaborn_Regression_Plots_lmplot.ipynb): How to plot linear regression lines on your scatter plots using `lmplot`.

---

## 3. Matplotlib and Seaborn Analysis (Saved Plots)

This folder holds the final images (`.png` files) created in the Matplotlib and Seaborn notebooks. It's a quick gallery of all the visualizations!

* [**part1_age_profile.png**](./matplotlib_and_seaborn_analysis/part1_age_profile.png)
* [**part2_age_analysis_dashboard.png**](./matplotlib_and_seaborn_analysis/part2_age_analysis_dashboard.png)
* [**part3_subplot_dashboard.png**](./matplotlib_and_seaborn_analysis/part3_subplot_dashboard.png)
* [**part4_pandas_integration.png**](./matplotlib_and_seaborn_analysis/part4_pandas_integration.png)
* [**part5_titanic_analysis_presentation.png**](./matplotlib_and_seaborn_analysis/part5_titanic_analysis_presentation.png)
* [**part6_seaborn_age_profile.png**](./matplotlib_and_seaborn_analysis/part6_seaborn_age_profile.png)
* [**part7_seaborn_age_dashboard.png**](./matplotlib_and_seaborn_analysis/part7_seaborn_age_dashboard.png)
* [**part8_seaborn_subplot_dashboard.png**](./matplotlib_and_seaborn_analysis/part8_seaborn_subplot_dashboard.png)
* [**part9_seaborn_dashboard.png**](./matplotlib_and_seaborn_analysis/part9_seaborn_dashboard.png)
* [**part10_seaborn_survival_report.png**](./matplotlib_and_seaborn_analysis/part10_seaborn_survival_report.png)
* [**part11_seaborn_box_violin_dashboard.png**](./matplotlib_and_seaborn_analysis/part11_seaborn_box_violin_dashboard.png)
* [**part12_seaborn_facetgrid_report.png**](./matplotlib_and_seaborn_analysis/part12_seaborn_facetgrid_report.png)
* [**part13_seaborn_correlation_dashboard.png**](./matplotlib_and_seaborn_analysis/part13_seaborn_correlation_dashboard.png)
* [**part14_seaborn_heatmap_report.png**](./matplotlib_and_seaborn_analysis/part14_seaborn_heatmap_report.png)
* [**part15_seaborn_pairplot_report.png**](./matplotlib_and_seaborn_analysis/part15_seaborn_pairplot_report.png)
* [**part16_seaborn_regression_dashboard.png**](./matplotlib_and_seaborn_analysis/part16_seaborn_regression_dashboard.png)
