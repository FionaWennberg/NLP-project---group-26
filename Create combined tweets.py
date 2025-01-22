
def create_combined_tweets(filenames_in, filename_out):
    with open(filename_out, mode='w', encoding='utf-8', newline='') as file_out:
        for filename_in in filenames_in:
            with open(filename_in, mode='r', encoding='utf-8', errors='ignore') as file_in:
                for line in file_in:
                    file_out.write(line)

    return "Files combined."

# Input and output file paths
filenames_in = [
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/JoeBidentweets_clean_P.csv',
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/Kamalatweets_clean_P.csv',
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/ossofftweets_clean_P.csv',
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/RepJeffriestweets_clean_P.csv',
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/RonWydentweets_clean_P.csv',
    'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/SenatorCantwelltweets_clean_P.csv']
filename_out = 'C:/Users/ingeb/OneDrive - Danmarks Tekniske Universitet/Semester 1/Intelligent Systems 2024/3-ugers kursus/Democrats/Democrattweets_combined_clean.csv'

# Process the raw files and generate the combined cleaned tweet list
result = create_combined_tweets(filenames_in, filename_out)
print(result)
