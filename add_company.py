"""
This script adds company directly to the list
"""
# import yaml


def get_repo_from_url(url):
    """
    Given a url, return the repository name.

    :param url: the url of the repo
    :return: The repo name.
    """
    idx = url.find(".com/")
    return url[idx + len(".com/") :].strip("/")


def create_alternatives_md(names, links):
    """
    Create a markdown string of the form:

    [name1](link1), [name2](link2), ...

    :param names: A list of alternative names for the image
    :param links: A list of links to the alternative versions of the file
    :return: A string of the form:
    """
    return ", ".join(
        (f"""[{name.strip()}]({link.strip()})""" for name, link in zip(names, links))
    )


def create_shield_link(gh_link):
    return "https://img.shields.io/github/stars/{repo}?style=social".format(
        repo=get_repo_from_url(gh_link)
    ).strip()


def create_new_line(
    category, company_name, description, link, gh_link, alts_names, alts_links
):

    return "{}|{}|{}|{}|{}|\n".format(
        category.strip(),
        f"[{company_name.strip()}]({link.strip()})",
        description.strip(),
        f'<a href={gh_link.strip()}><img src="{create_shield_link(gh_link)}" width=150/></a>',
        create_alternatives_md(alts_names, alts_links),
    )


def add_new_company(
    category, company_name, description, link, gh_link, alts_names, alts_links
):

    with open("README.md", "r", encoding="utf-8") as f:
        all = f.readlines()

    table_start = "|Category|Company|Description|GitHub Stars|Alternative to|\n"
    table_end = "<!-- END STARTUP LIST -->\n"

    idx = all.index(table_start)
    idx_end = all.index(table_end)

    find_name = lambda x: x[x.index("[") + 1 : x.index("]")].strip()
    find_cat = lambda x: x[: x.index("|")].strip()

    categories = [(find_cat(x), find_name(x)) for x in all[idx + 2 : idx_end - 1]]

    search_tup = (category.strip(), company_name.strip())

    insert_idx = -1

    for i, tup in enumerate(reversed(categories)):
        if search_tup == tup:
            return "This entry already exists"
        elif search_tup > tup:
            print(search_tup, tup)
            insert_idx = len(categories) - i
            break

    all.insert(
        insert_idx + idx + 2,
        create_new_line(
            category, company_name, description, link, gh_link, alts_names, alts_links
        ),
    )

    # file_name = "_".join(company_name.split(" "))
    # with open(f"submissions/{file_name}.yaml", "w") as file:
    #     yaml.dump(
    #         dict(
    #             category=category,
    #             company_name=company_name,
    #             description=description,
    #             link=link,
    #             gh_link=gh_link,
    #             alts_names=alts_names,
    #             alts_links=alts_links,
    #         ),
    #         file,
    #         default_flow_style=False,
    #     )

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(all)

    return "ok, added!"


def add_company_from_command_line():
    count = 0
    args = dict()

    while True:
        if count == 0:
            args["company_name"] = input("Enter the company name.\n(e.g Metabase)\n: ")
            print("-" * 100)
            count += 1
        elif count == 1:
            args["category"] = input(
                "Enter category of the company. May be an existing or a new one.\n(e.g Business Intelligence)\n: "
            )
            print("-" * 100)
            count += 1
        elif count == 2:
            args["description"] = input(
                "Description of the company.\nKeep it short and simple (use one line)\n: "
            )
            print("-" * 100)
            count += 1
        elif count == 3:
            args["link"] = input(
                """Url to the company's website.\n(e.g https://www.metabase.com/)\n: """
            )
            print("-" * 100)
            count += 1
        elif count == 4:
            args["gh_link"] = input(
                """"Url of the product's github repo.\n(e.g https://github.com/metabase/metabase)\n: """
            )
            print("-" * 100)
            count += 1
        elif count == 5:
            args["alts_names"] = input(
                """Names of the company's well-known SaaS competitors.\n(e.g for Metabase: PowerBI, DataStudio, Tableau)\n: """
            ).split(",")
            print("-" * 100)
            count += 1
        elif count == 6:
            args["alts_links"] = input(
                "Links to the corresponding SaaS competitors.\n(e.g for Metabase: https://powerbi.microsoft.com/, https://datastudio.google.com/, https://www.tableau.com/)\n: "
            ).split(",")
            print("-" * 100)
            count += 1
        else:
            result = add_new_company(**args)
            print(result)
            break


if __name__ == "__main__":
    add_company_from_command_line()
