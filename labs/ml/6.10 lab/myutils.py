import pandas as pd
def skew_calc(df):
    """
    Diagnoses skewness for every numeric column in a DataFrame and recommends a transformation based on the column's skewness and
    minimum value. Binary, encoded, and ID columns are excluded, since skewness isn't a meaningful for them.
    It returns a DataFrame with the following columns:
    Feature, Skewness, Degree, Direction, Recommended Transformation
    """
    # Your code here 
    results=[]

    numeric_columns=df.select_dtypes(include='number').columns

    for i in numeric_columns:
        skew=df[i].skew()

        if abs(skew)<0.5:
            deg='Approximately Symmetric'
        elif 0.5<=abs(skew)<=1:
            deg='Moderately Skewed'
        elif abs(skew)>1:
            deg='Highly Skewed'

        if abs(skew)<0.5:
            action='None needed'
        elif df[i].min()>0:
            action='Box-Cox or Yeo-Johnson'
        elif (df[i]>=0).all():
            action='log(x+1) or Yeo-Johnson'
        else:
            action='Yeo-Johnson'

        if skew>0:
            direction='Positive'
        elif skew<0:
            direction='Negative'
        else:
            direction='Symmetric'

        results.append({'Feature':i,
                       'Skewness':skew,
                       'Degree':deg,
                       'Direction':direction,
                       'Recommended Transformation':action})


    return pd.DataFrame(results)
