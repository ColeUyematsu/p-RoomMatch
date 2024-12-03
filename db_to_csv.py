import sqlite3
import pandas as pd

# Database path
database_path = "./instance/database.db"

def fetch_latest_data(db_path):
    """
    Fetch the latest data from the questionnaire_response table.
    """
    conn = sqlite3.connect(db_path)
    try:
        query = "SELECT * FROM questionnaire_response"
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()
    return df

def save_to_database(processed_df, db_path):
    """
    Save the processed data back to the database in a new table.
    """
    conn = sqlite3.connect(db_path)
    try:
        # Save processed data to a new table
        processed_df.to_sql('ml_ready_data', conn, if_exists='replace', index=False)
    finally:
        conn.close()

if __name__ == "__main__":
    # Fetch the latest data into a DataFrame
    raw_data = fetch_latest_data(database_path)
    print("Raw Data Fetched:")
    print(raw_data.head())


    # Save the modified DataFrame back to the database
    save_to_database(raw_data, database_path)
    print("Modified data saved to the 'ml_ready_data' table.")
    
    raw_data.to_csv("data.csv", index=False)