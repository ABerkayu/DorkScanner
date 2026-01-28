# 🔍 DorkScanner - Automated Google Dorking Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Maintenance-Active-success)

**DorkScanner** is a lightweight Python tool designed to automate **Passive Reconnaissance** (OSINT) operations for penetration testers and security researchers. 

It leverages the power of Google Dorks to identify potential vulnerabilities, exposed files, and configuration errors on target systems without directly engaging with the server, helping you stay under the radar during the initial information gathering phase.

## 🚀 Key Features

* **Automated Dork Generation:** Instantly creates critical search queries (SQLi, Log files, Env configs, etc.) for any given domain.
* **Browser Integration:** Automatically opens search results in your default web browser using the `-o` flag.
* **Smart CLI Interface:** User-friendly command-line interface with colorized outputs for better readability.
* **No API Key Required:** Uses standard search queries, removing the need for paid API keys.

## 🛠️ Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ABerkayu/DorkScanner.git
    ```

2.  **Navigate to the Directory**
    ```bash
    cd DorkScanner
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

Run the script using Python. You must provide a target domain using the `-t` argument.

### 1. Basic Scan (Generate Links)
This mode will print the generated dork links to the terminal.
```bash
python3 scanner.py -t targetsite.com
