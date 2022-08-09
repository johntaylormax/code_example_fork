# %%
from main import bdba

# %%
#convert list to dataframe
import pandas as pd
df = pd.DataFrame(bdba) #convert list to a dataframe
print(f'df dtype is {type(df)}') #confirm conversion
print(f'df shape is {df.shape}') #assess number of rows and columns
df.to_excel('bdba.xlsx', index=False) #create excel workbook to view data strings
df.head()


# %%
## Question 1:
## Find all versionless components (lib where version is null)
df_null = df[df['version'].isnull()]
df_null

# %%
## Question 2:
## Print a list of all unique vendor names
df.vendor.unique()

# %%
## Question 3:
## Find all components with vulns with cvss score > 8
## (Structure [vulns(list of dicts)]{'vuln'}('cvss')
df_vulns = df.copy()  #duplicate original df to work on it
df_vulns.insert(5, "cvss3_score", df_vulns['vulns'].apply(lambda x: x[0]['vuln']['cvss3_score'])) #grab the cvss3_score from the first vuln in the list
df_vulns['cvss3_score'] = df_vulns['cvss3_score'].astype(float) #convert to float because existing value is a string
df_vulns_high = df_vulns[df_vulns['cvss3_score'] > 8] #filter for cvss3_score > 8
df_vulns_high.head()


