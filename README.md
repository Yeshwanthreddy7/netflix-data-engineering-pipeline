Dataset source:
https://www.kaggle.com/datasets/shivamb/netflix-shows

The original dataset is not included because of size constraints.git add README.md


Project/
│
├── Netflix_Dataset/
│   └── netflix_titles.csv
│
├── PySpark/
│   └── profiling.py
│
└── README.md

then you're ready to finish Day 1 and start Phase 2 tomorrow.

Step 1: Push the latest structure to GitHub

Run:

git add .
git commit -m "Added PySpark folder and project structure"
git push origin main

If Git says "nothing to commit", that's okay—your latest changes may already be tracked.

Step 2: Tomorrow's Goal — Data Profiling with PySpark

In profiling.py, you'll:

Load the Netflix dataset
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Netflix Data Profiling") \
    .getOrCreate()

df = spark.read.csv(
    "../Netflix_Dataset/netflix_titles.csv",
    header=True,
    inferSchema=True
)

df.show(5)
Check schema
df.printSchema()
Count records
print("Total Records:", df.count())
print("Total Columns:", len(df.columns))
Check missing values
from pyspark.sql.functions import col, isnan, when, count

df.select([
    count(
        when(col(c).isNull(), c)
    ).alias(c)
    for c in df.columns
]).show()
Check duplicates
print("Duplicate Records:",
      df.count() - df.dropDuplicates().count())
Basic statistics
df.describe().show()
End of Phase 2 Deliverable

By tomorrow evening, your GitHub should show:

PySpark/
│
├── profiling.py
├── data_cleaning.py
└── transformations.py

and profiling.py should generate:

Dataset shape
Schema report
Missing values report
Duplicate analysis
Basic statistics

This is the first real data engineering step and will give you solid content for both GitHub and your resume project. After that, Phase 3 will focus on data cleaning and transformation using PySpark.