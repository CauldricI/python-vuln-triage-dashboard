import pandas as pd, glob, os

def merge_sources(folder="data"):
    files = glob.glob(os.path.join(folder, "*.csv"))
    dfs = [pd.read_csv(f) for f in files]
    df = pd.concat(dfs, ignore_index=True)
    print(f"Merged {len(dfs)} files with {len(df)} total records")
    df.to_csv(os.path.join(folder, "merged_findings.csv"), index=False)

if __name__ == "__main__":
    merge_sources()
