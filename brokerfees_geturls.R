library(openxlsx)
library(dplyr)
library(tidyverse)

library(openxlsx)
library(dplyr)
library(tidyverse)

# Load or define the 'filtered_data' dataframe here

# Regular expression to match rows containing "pad" in the URL
search_word <- "pad"

# Use grepl() to create a logical vector indicating rows that match the pattern
matching_indices <- grepl(search_word, hotpads_urls$URL, ignore.case = TRUE)

# Filter out rows that don't contain the search word in the URL
filtered_data <- hotpads_urls[matching_indices, , drop = FALSE]

# Eliminate rows with the word "zillow" in the URL
filtered_data <- filtered_data[!grepl("zillow|hotpads", filtered_data$URL, ignore.case = TRUE), ]


# # Find URLS with "hotpads.com" or "zillow" in the URL
# search_words2 <- c("hotpads.com", "zillow")
# 
# # Filter out rows with "hotpads.com" or "zillow" somewhere in the URL
# filtered_data <- filtered_data[grepl(paste(search_words2, collapse = "|"), filtered_data$URL, ignore.case = TRUE), ]

# Print the filtered dataframe
print(filtered_data)

#write to CSV
write.csv(filtered_data, "/Users/marin/Dropbox/My Mac (MacBook-Air.local)/Desktop/filtered_urls.csv", row.names = FALSE)

