def sort_readme():

    with open("README.md", "r", encoding="utf-8") as f:
        all = f.readlines()

    table_start = "|Category|Company|Description|GitHub Stars|Alternative to|\n"
    table_end = "<!-- END STARTUP LIST -->\n"

    idx = all.index(table_start)
    idx_end = all.index(table_end)

    find_name = lambda x: x[x.index("[") + 1 : x.index("]")].strip()
    find_cat = lambda x: x[: x.index("|")].strip()

    pairs = [(find_cat(x), find_name(x)) for x in all[idx + 2 : idx_end - 1]]

    sorted_pairs = sorted(pairs)

    right_elements = [all[idx + 2 : -1][pairs.index(i)] for i in sorted_pairs]

    all[idx + 2 : idx_end - 1] = right_elements

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(all)


if __name__ == "__main__":
    sort_readme()
