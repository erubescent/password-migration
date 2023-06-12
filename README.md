# Password Migration Script 😈

[![License](https://img.shields.io/github/license/erubescent/password-migration?style=plastic)](/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/erubescent/password-migration?color=red&style=plastic)](https://github.com/erubescent/password-migration/commits/main)

This script is designed to simplify the process of transferring passwords from a text file to a password manager. It allows for easy navigation through individual website data sets, ensuring a smooth and organized migration experience.

## Requirements

- Python 3.x
- No additional external dependencies

## How does it work? 🤔

1. Store your passwords in a text file. By default, the script assumes the file is named `passwords.txt` and located in the same directory.

2. Each website's password information should be separated by a unique identifier. By default, the identifier is set to `-+=`, but you can modify it in the script if needed.

3. Clone the repository and run the script using Python:
`python password_migration.py`

4. The script will display the information for the first set of text before the first identifier in the text file.

5. Use the following commands to navigate:
- Press `N` to move to the next data set.
- Press `B` to go back to the previous data set.
- Press `Q` to quit the script.

> As you navigate through the data set, manually transfer the information to your password manager.

> Once you reach the end or choose to quit, the script will terminate.

**Note:** Take appropriate precautions to securely handle and store your passwords during the migration process.

## Why you might need this 💁‍♀️
Picture yourself relying on your notes app, such as iCloud, to store all your passwords, only to find it increasingly burdensome to manually update the note each time you add new passwords. The resulting disarray of website names, passwords, and recovery codes makes it arduous to manage effectively, putting your valuable data at risk. In this scenario, you're seeking a streamlined solution to effortlessly organize and seamlessly transfer all your password information from the notes app to a password manager, ensuring efficient and secure management of your credentials.

## Preparing your data

1. **Export your passwords**: Export your password information from the notes app to a text file. Ensure that the exported file contains all the website names, passwords, and any additional recovery codes you want to transfer.

2. **Format the `passwords.txt` file**: Open the exported text file and format it with each website's information separated by a unique identifier of your choice. Here's an example structure using the default identifier:

```text
Website/URL (1)
Username    (1)
Email       (1)
Password    (1)

-+=

Website/URL (2)
Username    (2)
Email       (2)
Password    (2)

-+=

Website/URL (3)
Username    (3)
Email       (3)
Password    (3)
```

## Customization

- If your password file has a different name or location, modify the `file_path` variable
- To change the identifier used to separate data sets, modify the `identifier` variable

## License

This script is released under the [MIT License](LICENSE).

## Support

For any questions or concerns, please [open an issue](https://github.com/erubescent/password-migration/issues). 🔥🔥🔥
