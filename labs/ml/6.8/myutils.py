import pandas as pd
def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    # Your code here
    results = []
    for i in df.select_dtypes(include='number').columns:
        skew = df[i].skew()
        if -0.5 < skew < 0.5:
            degree = 'approximately symmetric'
        elif -1 < skew < 1:
            degree = 'moderately skewed'
        else:
            degree = 'highly skewed'

        if skew > 0:
            direction = 'positive'
        elif skew < 0:
            direction = 'negative'
        else:
            direction = 'Symmetric'

        if -0.5 < skew < 0.5:
            transform = 'None needed'
        elif df[i].min() == 0:
            transform = 'log plus one or yeo-johnson'
        elif df[i].min() < 0:
            transform = 'yeo-johnson'
        else:
            transform = 'box-cox or yeo-johnson'

        results.append({
            'Feature': i,
            'Skewness': skew,
            'Degree': degree,
            'Direction': direction,
            'Recommended Transformation': transform})

    return pd.DataFrame(results)
