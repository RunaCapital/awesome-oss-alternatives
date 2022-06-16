"""
This script create yamls from README
"""

import yaml


def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        all = f.readlines()

        table_start = "|Category|Company|Description|GitHub Stars|Alternative to|\n"
        table_end = "<!-- END STARTUP LIST -->\n"

        idx = all.index(table_start)
        idx_end = all.index(table_end)
    return all[idx + 2 : idx_end - 1]


def parse_line(line: str):
    arr = line.split("|")
    category = arr[0]
    name = arr[1].split("]")[0][1:]
    website = arr[1].split("]")[1][1:-1]
    description = arr[2]
    github = arr[3].split(">")[0].split("href=")[1]
    alts = list(map(lambda x: x.strip().split("]")[0][1:], arr[4].split(",")))
    alts_links = list(map(lambda x: x.strip().split("](")[1][:-1], arr[4].split(",")))
    return dict(
        category=category,
        company_name=name,
        link=website,
        description=description,
        gh_link=github,
        alts_names=alts,
        alts_links=alts_links,
    )


if __name__ == "__main__":
    arr = read_readme()
    for line in arr:
        obj = parse_line(line)
        file_name = "_".join(obj["company_name"].split(" "))
        with open(f"submissions/{file_name}.yaml", "w") as file:
            yaml.dump(obj, file, default_flow_style=False)
