from pyspark import SparkContext
# $example on$
from pyspark.mllib.linalg import Vectors
from pyspark.mllib.linalg.distributed import RowMatrix
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVDExample")

    # $example on$
    rows = sc.parallelize([
        Vectors.dense(2.0, 0.0),
        Vectors.dense(4.0, 0.0,),
        Vectors.dense(2.0, 0.0),
        Vectors.dense(4.0, 0.0,),
        Vectors.dense(2.0, 0.0),
        Vectors.dense(4.0, 0.0,),
        Vectors.dense(2.0, 0.0),
        Vectors.dense(4.0, 0.0,),
    ])

    mat = RowMatrix(rows)

    # Compute the top 5 singular values and corresponding singular vectors.
    decomp = mat.tallSkinnyQR(False)

    print(f"Result: {decomp.R.toArray()}")
    sc.stop()
    
