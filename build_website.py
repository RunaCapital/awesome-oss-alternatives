import yaml
import os


markdown_template = """
# {company_name}

**Category**: {category}

**Github**: [{gh_link}]({gh_link})

**Website**: [{link}]({link})

**Description**:
{description}

**Alternatives**: {alts}
"""

SPECIAL_MAPPING = {
    "ELT / ETL": "ETL",
    "Robotic Process Automation (RPA)": "Robotic Process Automation",
    "OPAL (Permit.io)": "OPAL",
}


appl = lambda x: SPECIAL_MAPPING[x] if x in SPECIAL_MAPPING else x


def get_all_companies():
    arr = []
    for filename in os.listdir("submissions"):
        if filename.endswith(".yaml"):
            with open(f"submissions/{filename}", "r", encoding="utf-8") as file:
                obj = yaml.load(file, yaml.Loader)
            obj["category"] = appl(obj["category"])
            obj["company_name"] = appl(obj["company_name"])
            arr.append(obj)
    return arr


def get_all_categories(arr):
    categories = set()
    for obj in arr:
        categories.add(obj["category"])
    return categories


def create_website_directories(categories):
    for category in categories:
        if not os.path.exists(f"website/docs/{category}"):
            os.mkdir(f"website/docs/{category}")


def generate_alternative_md(alts_names, alts_links):
    alt_md = ""
    for alt_link, alt_name in zip(alts_links, alts_names):
        alt_md += f"[{alt_name}]({alt_link}), "
    return alt_md.strip(", ")


def create_markdown_for_companies(companies):
    for company in companies:
        file_name = "-".join(company["company_name"].split(" "))
        with open(
            f"website/docs/{company['category']}/{file_name}.md", "w", encoding="utf-8"
        ) as file:
            file.write(
                markdown_template.format(
                    company_name=company["company_name"],
                    category=company["category"],
                    gh_link=company["gh_link"],
                    link=company["link"],
                    description=company["description"],
                    alts=generate_alternative_md(
                        company["alts_names"], company["alts_links"]
                    ),
                )
            )


if __name__ == "__main__":
    companies = get_all_companies()
    categories = get_all_categories(companies)
    # creating categories for the website in the docs folder
    create_website_directories(categories)
    # creating markdown files for the companies
    create_markdown_for_companies(companies)
