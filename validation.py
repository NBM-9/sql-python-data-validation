import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def validate_data(df):
    issues = {}

    issues['negative_amounts'] = df[df['amount'] < 0]
    issues['zero_amounts'] = df[df['amount'] == 0]
    issues['failed_transactions'] = df[df['status'] != 'completed']

    return issues

def main():
    df = load_data('data/transactions.csv')
    issues = validate_data(df)

    for issue, records in issues.items():
        print(f"\n{issue.upper()}")
        print(records)

if __name__ == "__main__":
    main()
