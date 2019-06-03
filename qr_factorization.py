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
import time

import pyspark
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

# $example on$
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import *
# $example off$

def read_matrix(path, sc, spark):
    print("Loading data...")
    t = time.time()

    data = sc.textFile(path)

    def to_matrix_entry(s):
        s = s.split(" ")
        return MatrixEntry(int(s[0]), int(s[1]), float(s[2]))

    data = data.filter(lambda x: not x.startswith('%'))
    data = data.zipWithIndex().filter(lambda tup: tup[1] != 0).map(lambda x:x[0])
    data = data.map(to_matrix_entry)
    data = data.repartition(20).cache()
    matrix = CoordinateMatrix(data)
    mat = matrix.toRowMatrix()

    print("Done in: %f s" % (time.time() - t))

    return mat


if __name__ == "__main__":
    conf = (pyspark.SparkConf()
            .setAppName("QR")
            .set("spark.hadoop.validateOutputSpecs", "false")
            .set("spark.executor.memory", "3g")
            .set("spark.driver.memory", "3g")
            .set("spark.driver.maxResultSize", "3g"))
    sc = pyspark.SparkContext(conf=conf)
    spark = pyspark.sql.SparkSession(sc)

    mat = read_matrix(sys.argv[1], sc, spark)

    print("Nbr workers", sc._conf.get('spark.executor.instances'))

    print("Compute QR")
    t = time.time()
    
    decomp = mat.tallSkinnyQR(False)

    print("QR computed in %f s" % (time.time() - t))
    sc.stop()
    

