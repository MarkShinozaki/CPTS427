
# [Assignment 4 - Passwords](https://github.com/MarkShinozaki/CPTS427-CyberSecurityOfWireless-DistributedSystems/tree/Assignments/Homework%204)

#### [Assignment 4 Rubric](https://github.com/MarkShinozaki/CPTS427-CyberSecurityOfWireless-DistributedSystems/blob/Assignments/Homework%204/CptS427-HW4%20(1).pdf)

- This assignment focuses on analyzing different password files based on an imaginary specification for a password authentication scheme. You will need to understand the format of password files provided in the exercises.


### Key Points:

1. **Password File Requirements**:

    - Self-contained file
    - ASCII encoding
    - One line per user containing User ID, Group ID, Username, Email address, Password, Last authentication date, and Number of failed logins.

2. **Word List**:

    - MIT's list of 10,000 words is used to generate all password entries for this assignment.

3. **Salted Hashes**:

    - Understand the concept of adding a salt to a plaintext password to produce a unique ciphertext.
The password field in the file `Password.txt` is the output of the function `md5(password+salt)`.

4. **Tasks**:

- Analyze the Password.txt file to answer the following questions:
    - What is the salt that was added to each password?
    - Which user had the most failed logins, and how many failed logins did they have?
    - Which user has not logged in for the longest time?
- Ensure your program produces the same MD5 hashes as the unit tests provided.

### Simple and Brief Answers to the Questions:
1. **Salt Added to Each Password**:

    - The salt used in each password can be found by comparing the passwords in `Password.txt` with the wordlist provided in `wordList.txt` and identifying the specific word that, when combined with the password, produces the corresponding MD5 hash.

2. **User with the Most Failed Logins**:

    - Identify the user by searching the password file for the highest number of failed login attempts.

3. **User with the Longest Time Since Last Login**:

    - Look for the user with the oldest last authentication date in the password file.
