#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

# $example on$
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import *
# $example off$

def read_matrix(path, sc, spark):
    data = sc.textFile(path)

    def to_matrix_entry(s):
        s = s.split(" ")
        return MatrixEntry(int(s[0]), int(s[1]), float(s[2]))

    data = data.filter(lambda x: not x.startswith('%'))
    data = data.zipWithIndex().filter(lambda tup: tup[1] != 0).map(lambda x:x[0])

    print(data.take(5))

    data = data.map(to_matrix_entry)
    print(data.take(5))

    matrix = CoordinateMatrix(data)

    return matrix.toRowMatrix()


if __name__ == "__main__":
    spark = SparkSession.builder.master("yarn").config(conf=SparkConf()).getOrCreate()
    sc = spark.sparkContext

    mat = read_matrix(sys.argv[1], sc, spark)

    # Compute the top 5 singular values and corresponding singular vectors.
    decomp = mat.tallSkinnyQR(False)
    sc.stop()
    

