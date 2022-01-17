def count_companies_in_readme():

    with open('README.md', 'r', encoding='utf-8') as f:
        all = f.readlines()

    table_start = '|Category|Company|Description|GitHub Stars|Alternative to|\n'
    idx = all.index(table_start)

    return len(all[idx + 2: -1])



if __name__ == "__main__":
    print(
        f"Found companies in README: {count_companies_in_readme()}"
    )