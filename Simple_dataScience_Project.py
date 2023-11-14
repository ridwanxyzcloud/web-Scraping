import pandas as pd
import tabula

def task_0(df_input: pd.DataFrame) -> pd.DataFrame:
    """
    Confirm that you read the PDF and turned it into a dataframe.

    Parameters
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.

    Returns
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.
    """
    return df_input

def task_1(df_input: pd.DataFrame) -> tuple:
    """
    What's the shape of the dataframe?

    Parameters
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.

    Returns
    ---------------
    shape_of_dataframe (tuple)
        The rows and columns, tuple-format of your dataframe.
    """
    shape_of_dataframe = df_input.shape
    return shape_of_dataframe

def task_2(df_input: pd.DataFrame) -> float:
    """
    How many teams are in the dataset?

    Parameters
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.

    Returns
    ---------------
    number_of_teams (float)
        The unique count of teams that are present in the dataset.
    """
    number_of_teams = df_input['tm'].nunique()
    return number_of_teams

def task_3(df_input: pd.DataFrame) -> list:
    """
    What are the top 10 teams, sorted descendingly in total points?

    Parameters
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.

    Returns
    ---------------
    list_of_teams (list)
        The list of 10 teams ranked from top to bottom in total points scored.
    """
    list_of_teams = df_input.groupby('tm')['pts'].sum().sort_values(ascending=False).head(10).index.tolist()
    return list_of_teams

def task_4(df_input: pd.DataFrame) -> pd.DataFrame:
    """
    Excluding the players with assists = 0 and pts  = 0, calculate
    the ratio of TURNOVERS (to) per POINTS (pts), and return the 10 most effective 
    players and the top 10 least effective players, all in the SAME dataframe.

    Parameters
    ---------------
    df_input (pd.DataFrame)
        The dataframe you read from the PDFs.

    Returns
    ---------------
    most_and_least_effective_players (pd.DataFrame)
        A dataframe with 20 rows containing top 10 effective players, top 10
        least effective players.
    """
    # Exclude players with assists = 0 and pts = 0
    filtered_df = df_input[(df_input['ast'] != 0) & (df_input['pts'] != 0)]

    # Calculate the turnover-to-point ratio
    filtered_df['to_pts_ratio'] = filtered_df['tov'] / filtered_df['pts']

    # Get the top 10 most effective players and top 10 least effective players
    most_and_least_effective_players = (
        filtered_df.sort_values(by='to_pts_ratio').head(10)
        .append(filtered_df.sort_values(by='to_pts_ratio', ascending=False).head(10))
    )

    return most_and_least_effective_players
