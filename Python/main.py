from listAllFiles import list_all_files, get_all_sub_folders
from longestSequence import longest_increasing_subsequence

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [11, 5, 2, 5, 3, 7, 101, 18]
    print(longest_increasing_subsequence(nums))

    # Getting all files from folders iteratively and adding in result file
    with open("all_files_listed.txt", 'w+') as file_object:
        url = 'https://gentoo.osuosl.org/distfiles/'
        html_data = list_all_files(url)
        endpoint_suffixes = get_all_sub_folders(html_data, file_object)
        for each_endpoint_suffix in endpoint_suffixes:
            new_url = url + each_endpoint_suffix
            get_all_sub_folders(list_all_files(new_url), file_object)
