def consolidate_categories(data, lower_perc):
    """ Consolidate categories with frequencies in the lower percentile of categorical variables 

    Parameters
    __________
    data : pandas DataFrame or Series. 
        If data doesn't contain categorical variables, the function returns data unmodified.
    lower_perc: float
        Define the lowest frequency percentile that will be consolidated. Values must be between 0 and 1.
    """
    
    from pandas import DataFrame, Series
    
    dtypes_to_consolidate = ["object", "category"]
    
    if isinstance(data,DataFrame):
        
        for c in data.columns:
            
            if data[c].dtype in dtypes_to_consolidate:
                
                cum_freq = (data[c].value_counts() / len(data[c])).sort_values().cumsum().round(2)
                categories_to_consolidate = cum_freq[cum_freq <= lower_perc].index
                data[c].replace(categories_to_consolidate,'other',inplace=True)
    
    elif isinstance(data,Series):
        
        if data.dtype in dtypes_to_consolidate:
            
            cum_freq = (data.value_counts() / len(data)).sort_values().cumsum().round(2)
            categories_to_consolidate = cum_freq[cum_freq <= lower_perc].index
            data.replace(categories_to_consolidate,'other',inplace=True)
            
    else:
        
        raise TypeError("Input must be a pandas DataFrame or Series for parameter `data`")
    
    return data

def test_consolidate_categories():
    pass