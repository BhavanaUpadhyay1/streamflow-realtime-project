# test_env.py
import pandas as pd
import kafka
import pyspark
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
import snowflake.connector

print("✅ Libraries imported successfully!")

# --- Pandas Test ---
df = pd.DataFrame({"product": ["Laptop", "Phone"], "price": [800, 500]})
print("\n📊 Pandas DataFrame:")
print(df)

# --- Spark + Delta Test ---
builder = (
    SparkSession.builder.appName("RealtimeTest")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

spark_df = spark.createDataFrame(df)
print("\n⚡ Spark DataFrame:")
spark_df.show()

# --- Snowflake Connector Test (Dry Run) ---
try:
    print("\n❄️ Snowflake Connector available:", snowflake.connector.__version__)
except Exception as e:
    print("Snowflake check failed:", e)

print("\n🎉 Environment setup looks good!")


▶️ Run the test

Inside your activated realtime_env, run:
python test_env.py

''' You should see:

A small Pandas table

A Spark DataFrame (same data)

Snowflake connector version '''
