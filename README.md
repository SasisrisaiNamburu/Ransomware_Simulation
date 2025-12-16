#### **Ransomware Simulation (Educational Only)**



This project demonstrates how ransomware works in a safe and controlled environment. It includes two Python scripts — an **encryptor** and a **decryptor** — that show how files can be encrypted and later restored using a secret key.



###### ⚠️ **Educational Use Only**

This project is meant for learning cybersecurity concepts. Please do **NOT** use it on any real system, network, or sensitive data.



##### **Features**



* Encrypts files inside a selected folder
* Generates a unique encryption key
* Creates a simple ransom note
* Decrypts the files using the same key
* Demonstrates real ransomware logic, but in a safe way



##### **How It Works**



1. ###### **Encryptor**



* Scans the 'test\_files' folder
* Encrypts each file using **Fernet** (AES-128 under the hood)
* Generates 'key.key'
* Writes a ransom note



**Run:**

*python encryptor.py*



###### 2\. **Decryptor**



* Reads 'key.key'
* Decrypts all '.encrypted' files
* Restores original content



**Run:**

*python decryptor.py*



##### **Requirements**



* Python 3.7 or above
* 'cryptography' library



*pip install cryptography*



##### **Learning Outcomes**



* How ransomware encrypts files
* How decryption works using a secret key
* Importance of backups and secure key management
* Safe malware analysis concepts



##### **Disclaimer**



This project is strictly for **educational and learning purposes.**

Please do **not** use it maliciously. The creator is not responsible for misuse.



###### **Author**



Sasisrisai Namburu

