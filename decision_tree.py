from __future__ import print_function

import os
import subprocess



import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz


real_state_data = pd.read_csv('dataframe_cont.csv')

index = real_state_data.index
columns = real_state_data.columns
values = real_state_data.values


#print("* prices:", real_state_data["SalePrice"].unique(), sep="\n")

def encode_target(df, target_column):
    """Add column to df with integers for the target.

    Args
    ----
    df -- pandas DataFrame.
    target_column -- column to map to int, producing
                     new Target column.

    Returns
    -------
    df_mod -- modified DataFrame.
    targets -- list of target names.
    """
    df_mod = df.copy()
    targets = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    df_mod["Target"] = df_mod[target_column].replace(map_to_int)

    return (df_mod, targets)


real_state_data2, targets = encode_target(real_state_data, "SalePrice")
# print("* real_state_data2.head()", real_state_data2[["Target", "SalePrice"]].head(), sep="\n", end="\n\n")
# print("* real_state_data2.tail()", real_state_data2[["Target", "SalePrice"]].tail(), sep="\n", end="\n\n")
# print("* targets", targets, sep="\n", end="\n")

features = list(real_state_data2.columns[:38])
# print("* features:", features, sep="\n")

y = real_state_data2["Target"]
X = real_state_data2[features]
dt = DecisionTreeClassifier(min_samples_split=20, random_state=99)
y_
dt.fit(X, y)


def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

        Args
        ----
        tree -- scikit-learn DecsisionTree.
        feature_names -- list of feature names.
        """
    with open("dt.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")


visualize_tree(dt, features)

