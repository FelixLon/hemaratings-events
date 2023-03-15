## Hemaratings - Events downloader

#### Background
hemaratings.com is by their own description *".. an effort to collect results from as many HEMA tournaments as possible and present ratings generated based on those."*
Hema tournament organizers can submit their data to hemaratings, which calculates scores & ratings for the individual participants. 
The page https://hemaratings.com/events/ includes the listed events with details about their dates, number of participants (in which categories) etc.

#### Content
Sadly there is no API to retrieve the data. This Python script fetches the content from the aforementioned https://hemaratings.com/events/ , parses it with BeautifulSoup for the name, country, year and number of fights and fighters in the respective categories.
The data is loaded into Pandas dataframe, where it can be sorted and exported to an Excel file for better readability.
