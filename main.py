import pyspark
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType, IntegerType

def main():
	# starts PySpark Session
	spark = pyspark.sql.SparkSession.builder.appName("Read .csv and write .parquet test").getOrCreate()

	# reads csv file into a dataframe
	input_df = spark.read.csv("data/meteorite_landings.csv", header=True, sep=",")
	input_df.printSchema()

	# casting columns to its right type
	input_df = input_df.withColumn("year", input_df["year"].cast(IntegerType()))
	input_df = input_df.withColumn("lat", input_df["lat"].cast(DoubleType()))
	input_df = input_df.withColumn("long", input_df["long"].cast(DoubleType()))

	# printing schema to check if the types are right
	input_df.printSchema()

	# filters only records of meteors that fell since 2000
	meteor_df = input_df.where((F.col("year") >= 2000) & (F.col("fall") == "Fell"))
	print("Amount of meteors that fell since 2000: {0}\n\n".format(meteor_df.count()))

	# filters meteors that fell in Brazil or close country (as we only have latitude and longitude positions, we look for a square area and it ends including a few other close countries)
	meteor_df = input_df.where((F.col("lat") >= -45) & (F.col("lat") <= 5) & (F.col("long") <= -35) & (F.col("long") >= -76))
	meteor_df.show()
	print("Amount of meteors that fell in Brazil or in a close country: {0}\n\n".format(meteor_df.count()))

	# writes the dataframe in disk as a parquet file
	meteor_df.write.parquet("brazilian_meteors.parquet")


if __name__ == "__main__":
	main()