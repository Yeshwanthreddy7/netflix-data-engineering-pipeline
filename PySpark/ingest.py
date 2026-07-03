from pyspark.sql import SparkSession

def main():
    # Create Spark Session
    spark = (
        SparkSession.builder
        .appName("Netflix Data Engineering Pipeline")
        .getOrCreate()
    )

    # Read Dataset
    df = spark.read.csv(
        "../Netflix_Dataset/netflix_titles.csv",
        header=True,
        inferSchema=True
    )

    print("\n===== First 5 Rows =====")
    df.show(5, truncate=False)

    print("\n===== Dataset Schema =====")
    df.printSchema()

    print(f"\nTotal Rows    : {df.count()}")
    print(f"Total Columns : {len(df.columns)}")

    spark.stop()


if __name__ == "__main__":
    main()