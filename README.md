# Netflix Analysis & Dashboard Project

🔍 Overview:
This project is a data analysis and visualization dashboard based on Netflix's movie data. The goal was to explore trends, genres, popularity, 
and viewer sentiment across thousands of movies using Python for data preprocessing and Power BI for dashboard creation.

🎯 Objective: 
To gain actionable insights into Netflix's movie dataset by answering the following key questions:

Q1. What are the most popular movie genres?
Q2. Which movies received the highest and lowest popularity ratings?
Q3. What is the distribution of vote averages?
Q4. Which year saw the most movie releases on Netflix?

🛠️ Tools & Technologies:
Stack	Tools & Libraries
Data Prep:	Python, Pandas, NumPy, Matplotlib, Seaborn
Visualization:	Power BI (PBIX file), SQL (Power Query, optional)
IDE/Platform:	Jupyter Notebook, Power BI Desktop

📁 Files Included
File Name	Description:
>> netflix analysis project.py:-	Python script for cleaning, transforming, and exploring data/
link: https: //github.com/kimshix0x0/Netflix-analysis-project/blob/main/netflix%20analysis%20project.py
>> netflix dashboard.pbix:-	Interactive Power BI dashboard with slicers and KPIs.
link: https://github.com/kimshix0x0/Netflix-analysis-project/blob/main/Screenshot%202025-07-11%20161400.png 

📈 Dashboard Features (Power BI):
>> Genre Distribution: Count of movies by genre.
>> Vote Average Categories: Classified as popular, average, below avg, and not popular.
>> Popularity Highlights: Identify top/bottom movies based on popularity score.
>> Release Year Analysis: Histogram to identify the most active movie production years.
>> Filters and Slicers: Drill down into genres, years, or popularity dynamically.

🧹 Data Processing Steps (Python):
~ Removed irrelevant columns: Overview, Original_Language, Poster_Url.
~ Converted Release_Date into Year format for trend analysis.
~ Categorized Vote_Average into 4 meaningful labels using quartiles.
~ Handled missing values and duplicate rows.
~ Exploded multi-genre entries into one-genre-per-row format.
~ Converted Genre column to categorical type for optimal plotting.

📊 Insights Derived:
🎬 Most Frequent Genre: Drama (14%+ of total titles)
⭐ Highest Voted Genre: Drama again leads with 18.5% of movies receiving popular votes.
🚀 Top Movie by Popularity: Spider-Man: No Way Home – Genre: Action, Adventure, Sci-Fi.
📆 Top Production Year: 2020 had the highest number of movies released on Netflix.
🏁 How to Run This Project

Python Analysis:
> Install requirements: pandas, numpy, seaborn, matplotlib
> Run netflix analysis project.py in Jupyter or any Python IDE
> Power BI Dashboard
> Open netflix dashboard.pbix in Power BI Desktop
> Interact with filters and visuals to explore the insights




