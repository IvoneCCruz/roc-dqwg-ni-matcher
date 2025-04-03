# Databricks notebook source
# MAGIC %pip install xlsxwriter openpyxl

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd

df = spark.sql("select 1 as id, 'jonas' as name, '123564' as phone").toPandas()
writer = pd.ExcelWriter('/Volumes/sandbox/icc/icc/output_data/test.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.close()


