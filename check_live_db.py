import MySQLdb
import environ

# Load environment variables
env = environ.Env()
environ.Env.read_env()

def view_database():
    print("==================================================")
    print("      ♻️  AIVEN LIVE MYSQL DATABASE VIEWER ♻️      ")
    print("==================================================")
    print("Connecting to Aiven MySQL...")
    
    try:
        db = MySQLdb.connect(
            host=env('DB_HOST'),
            user=env('DB_USER'),
            passwd=env('DB_PASSWORD'),
            port=int(env('DB_PORT')),
            db=env('DB_NAME'),
            ssl_mode='REQUIRED'
        )
        cursor = db.cursor()
        print("Connected successfully! 🎉\n")
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    # Fetch and show all tables
    cursor.execute("SHOW TABLES")
    tables = [r[0] for r in cursor.fetchall()]
    
    print("Available Tables in Live Database:")
    for idx, table in enumerate(tables, 1):
        print(f"  [{idx}] {table}")
        
    print("\n==================================================")
    while True:
        choice = input("\nEnter table number (or name) to view data (or 'exit' to quit): ").strip()
        if choice.lower() == 'exit':
            break
            
        selected_table = None
        # Check if selection is an index number
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(tables):
                selected_table = tables[idx]
        elif choice in tables:
            selected_table = choice
            
        if not selected_table:
            print("❌ Invalid table name or index. Please try again.")
            continue
            
        # Get row count
        cursor.execute(f"SELECT COUNT(*) FROM `{selected_table}`")
        count = cursor.fetchone()[0]
        print(f"\n📊 Table: `{selected_table}` | Total Rows: {count}")
        
        # Get column names
        cursor.execute(f"DESCRIBE `{selected_table}`")
        columns = [col[0] for col in cursor.fetchall()]
        print(f"📋 Columns: {', '.join(columns)}")
        
        # Fetch first 5 rows
        cursor.execute(f"SELECT * FROM `{selected_table}` LIMIT 5")
        rows = cursor.fetchall()
        
        if not rows:
            print("ℹ️ This table is empty.")
        else:
            print("\n👇 First 5 Rows:")
            for r_idx, row in enumerate(rows, 1):
                row_dict = dict(zip(columns, row))
                print(f"\n--- Row {r_idx} ---")
                for col, val in row_dict.items():
                    print(f"  {col}: {val}")
        print("==================================================")
        
    db.close()
    print("Connection closed. Goodbye!")

if __name__ == '__main__':
    view_database()
