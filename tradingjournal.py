import csv

print("--- Trade & Performance Journal ---")
print("Loading trade data...\n")

total_pnl = 0.0
winning_trades = 0
total_trades = 0

try:
    with open("trades.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            trade_id = row['trade_id']
            asset = row['asset']
            trade_type = row['type']
            pnl = float(row['pnl']) # Convert string to float for math
            
            # Accumulate metrics
            total_pnl += pnl
            total_trades += 1
            if pnl > 0:
                winning_trades += 1
            
            print(f"Trade ID: {trade_id} | Asset: {asset} | Type: {trade_type} | PnL: ${pnl:.2f}")

        # Calculate win rate percentage
        win_rate = (winning_trades / total_trades) * 100 if total_trades > 0 else 0

        # Print final performance summary report
        print("\n" + "="*35)
        print("📊 PERFORMANCE SUMMARY REPORT")
        print("="*35)
        print(f"Total Trades : {total_trades}")
        print(f"Winning Trades: {winning_trades}")
        print(f"Win Rate     : {win_rate:.1f}%")
        print(f"Net PnL      : ${total_pnl:.2f}")
        print("="*35)

except FileNotFoundError:
    print("Error: trades.csv file not found.")