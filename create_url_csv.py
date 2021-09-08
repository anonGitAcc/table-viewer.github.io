import pandas as pd
# copy the template

base_url = "https://anongitacc.github.io/table-viewer.github.io/batch_pages/batch{}/"


url_list = []
for i in range(4,55):
    url_list.append(base_url.format(str(i)))


df = pd.DataFrame()
df["table_url"] = url_list
df.to_csv("annotation_urls_explanation_collection_wikipedia_external_v2.csv", index = False)