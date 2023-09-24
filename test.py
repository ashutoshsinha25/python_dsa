
# import pandas as pd
# df = pd.DataFrame({'City\tState': ["Kolkata\tWest Bengal", "Chennai\tTamil Nadu", 
#                                    "Hyderabad\tTelengana", "Bangalore\tKarnataka" , 'None']})

# # print(list(df.columns)[0].split('\t'))

# # col1 = list(df.columns)[0].split('\t')[0]
# # col2 = list(df.columns)[0].split('\t')[1]

# # df_new = pd.DataFrame()
# # col = list(df.columns)[0]
# # df_new[col1] = df[col].apply(lambda x : x.split('\t')[0])
# # df_new[col2] = df[col].apply(lambda x : x.split('\t')[1])

# df_new = df['City\tState'].str.split('\t')

#  # Convert the values to a data frame
# df_new = pd.DataFrame(list(df_new.values))

# # print(df_new.head())

# print(df_new[df_new.isna()])

import pandas as pd

s = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'

print(pd.DataFrame(s.split(),columns=['Value'])['Value'].value_counts())