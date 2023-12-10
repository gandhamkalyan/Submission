import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    df = df.pivot_table(index='id_1', columns='id_2',values='car')
    df.fillna('0.0',inplace=True)


    return df


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    df['car_type'] = pd.cut(df['car'],bins=[-float('inf'), 15, 25, float('inf')],
                        labels=['low', 'medium', 'high'],right=False)
    
    car_type_counts = df['car_type'].value_counts().to_dict()

    return car_type_counts



    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_mean = df['bus'].mean()
    bus_index = df[df['bus'] > 2 * bus_mean].index.tolist()
    bus_index.sort()

    return bus_index

    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    route_avg_truck = df.groupby('route')['truck'].mean()
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    return selected_routes

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    modify_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)
    modify_matrix = modify_matrix.round(1)

    return modify_matrix

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'], errors='coerce')
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'], errors='coerce')

    # Check for missing timestamps
    invalid_timestamps = df['start_timestamp'].isnull() | df['end_timestamp'].isnull()
    df = df[~invalid_timestamps]
    
     # Reset  index before performing the join
    df = df.reset_index(drop=True)

    


    return pd.Series()
