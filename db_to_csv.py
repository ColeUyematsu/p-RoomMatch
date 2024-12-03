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

# Path to the SQLite database
database_path = "./instance/database.db"

def delete_person_from_database(db_path, user_id):
    """
    Delete a person (entry) from the questionnaire_response table by user ID.

    Parameters:
        db_path (str): Path to the SQLite database file.
        user_id (int): ID of the user to be deleted.
    """
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        # SQL query to delete the user by ID
        query = "DELETE FROM questionnaire_response WHERE id = ?"
        cursor.execute(query, (user_id,))
        conn.commit()  # Save changes
        print(f"User with ID {user_id} has been deleted.")
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
    delete_person_from_database(database_path, 2)
    
    raw_data.to_csv("data.csv", index=False)